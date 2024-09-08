import itertools
from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt
import mlflow
import mlflow.pyfunc
import numpy as np
import pandas as pd
import typer
import yaml
from config import MlflowMetaParameters
from joblib import dump
from loguru import logger
from matplotlib.figure import Figure
from mlflow.models.signature import infer_signature
from model import SentimentDetector
from scipy.sparse.csr import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split

np.random.seed(1234)
app = typer.Typer()


def prepare_data(
    df: pd.DataFrame, test_size: float
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(
        df, test_size=test_size, stratify=df["sentiment"], random_state=1234
    )
    return train_df, test_df


def make_features(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> Tuple[csr_matrix, csr_matrix]:
    vectorizer = TfidfVectorizer(stop_words="english")
    train_inputs = vectorizer.fit_transform(train_df["review"])
    dump(vectorizer, "vectorizer.joblib")
    test_inputs = vectorizer.transform(test_df["review"])
    return train_inputs, test_inputs


def train(train_inputs, train_outputs: np.ndarray, **model_kwargs) -> BaseEstimator:
    model = LogisticRegression(**model_kwargs)
    model.fit(train_inputs, train_outputs)
    return model


def evaluate(
    model: BaseEstimator,
    test_inputs: csr_matrix,
    test_outputs: np.ndarray,
    class_names: List[str],
) -> Tuple[float, Figure]:
    predicted_test_outputs = model.predict(test_inputs)
    figure = draw_confusion_matrix(test_outputs, predicted_test_outputs, class_names)
    return f1_score(test_outputs, predicted_test_outputs), figure


def draw_confusion_matrix(
    true_labels: np.ndarray, predicted_labels: np.ndarray, class_names: List[str]
) -> Figure:
    labels = list(range(len(class_names)))
    conf_mat = confusion_matrix(true_labels, predicted_labels, labels=labels)

    plt.imshow(conf_mat, interpolation="nearest", cmap=plt.cm.Purples)
    plt.colorbar()

    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=90, fontsize=20)
    plt.yticks(tick_marks, class_names, fontsize=20)

    fmt = "d"
    thresh = conf_mat.max() / 2.0
    for i, j in itertools.product(range(conf_mat.shape[0]), range(conf_mat.shape[1])):
        plt.text(
            j,
            i,
            format(conf_mat[i, j], fmt),
            horizontalalignment="center",
            color="white" if conf_mat[i, j] > thresh else "black",
            fontsize=20,
        )

    plt.title("Confusion matrix")
    plt.ylabel("Actual label", fontsize=20)
    plt.xlabel("Predicted label", fontsize=20)
    plt.tight_layout()
    return plt.gcf()


@app.command()
def main(penalty: str = "l2", C: float = 1.0, solver: str = "lbfgs"):
    path_to_dataset = (
        Path(__file__).resolve().parents[1] / "dataset_training" / "imdb-dataset.csv"
    )
    path_to_conda_yaml = Path(__file__).resolve().parent / "conda.yaml"
    path_versioning_model = Path(__file__).resolve().parent / "version.yml"

    df = pd.read_csv(path_to_dataset)
    df["label"] = pd.factorize(df["sentiment"])[0]
    params = {"penalty": penalty, "C": C, "solver": solver, "test_size": 0.3}
    train_df, test_df = prepare_data(df, test_size=params["test_size"])

    mlflow.set_tracking_uri(MlflowMetaParameters.TRACKING_URI)
    mlflow.set_experiment(MlflowMetaParameters.EXPERIMENT_NAME)

    with mlflow.start_run():
        train_inputs, test_inputs = make_features(train_df, test_df)
        model = train(
            train_inputs, train_df["label"].values, penalty=penalty, C=C, solver=solver
        )
        dump(model, "model.joblib")

        f1_score, figure = evaluate(
            model,
            test_inputs,
            test_df["label"].values,
            df["sentiment"].unique().tolist(),
        )
        logger.info("F1 score: ", f1_score)

        for parameter in params:
            mlflow.log_param(parameter, params[parameter])
        mlflow.log_metric("f1_score", f1_score)
        mlflow.log_figure(figure, "figure.png")

        signature = infer_signature(test_inputs.toarray(), model.predict(test_inputs))
        sentiment_detector = SentimentDetector()
        artifacts = {"vectorizer": "./vectorizer.joblib", "model": "model.joblib"}
        mlflow.pyfunc.log_model(
            artifact_path="model",
            conda_env=str(path_to_conda_yaml),
            python_model=sentiment_detector,
            artifacts=artifacts,
            registered_model_name=MlflowMetaParameters.REGISTRY_NAME,
            signature=signature,
        )

    with path_versioning_model.open("r") as yaml_data_versionning:
        versionng_yaml = yaml.safe_load(yaml_data_versionning)

    versionng_yaml["version"] += 1

    with path_versioning_model.open("w") as yaml_data_versionning:
        versionng_yaml = yaml.safe_dump(
            versionng_yaml, yaml_data_versionning, indent=4, default_flow_style=False
        )


if __name__ == "__main__":
    app()
