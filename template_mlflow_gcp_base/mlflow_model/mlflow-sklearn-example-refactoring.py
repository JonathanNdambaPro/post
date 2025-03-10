import itertools
from enum import StrEnum
from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
import typer
from joblib import dump
from loguru import logger
from matplotlib.figure import Figure
from mlflow.models.signature import infer_signature
from scipy.sparse.csr import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split

np.random.seed(1234)
app = typer.Typer()


class ChoicePenality(StrEnum):
    l1 = "l1"
    l2 = "l2"
    elasticnet = "elasticnet"
    none = "none"


class ChoiceSolver(StrEnum):
    newton_cg = "newton_cg"
    lbfgs = "lbfgs"
    liblinear = "liblinear"
    sag = "sag"
    saga = "saga"


class MlflowMetaParameters(StrEnum):
    EXPERIMENT_NAME = "mlflow-models-sklearn"
    TRACKING_URI = "http://127.0.0.1:8080"  # "http://mlflow-tracking-server:5000"


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
def main(
    penalty: ChoicePenality = ChoicePenality.l2,
    C: float = 1.0,
    solver: ChoiceSolver = ChoiceSolver.lbfgs,
):
    path_to_dataset = (
        Path(__file__).resolve().parents[1] / "dataset_training" / "imdb-dataset.csv"
    )
    df = pd.read_csv(path_to_dataset)

    df["label"] = pd.factorize(df["sentiment"])[0]

    params = {"penalty": penalty, "C": C, "solver": solver, "test_size": 0.3}
    train_df, test_df = prepare_data(df, test_size=params["test_size"])

    train_inputs, test_inputs = make_features(train_df, test_df)
    model = train(
        train_inputs, train_df["label"].values, penalty=penalty, C=C, solver=solver
    )
    mlflow.set_tracking_uri(MlflowMetaParameters.TRACKING_URI)
    mlflow.set_experiment(MlflowMetaParameters.EXPERIMENT_NAME)

    with mlflow.start_run():
        f1_score, figure = evaluate(
            model,
            test_inputs,
            test_df["label"].values,
            df["sentiment"].unique().tolist(),
        )
        logger.info(f"F1 score: {f1_score}")

        for parameter in params:
            mlflow.log_param(parameter, params[parameter])
        mlflow.log_metric("f1_score", f1_score)
        mlflow.log_figure(figure, "figure.png")

        signature = infer_signature(
            test_inputs.toarray(), model.predict(test_inputs)
        )  # La signature défini les schémas de l'entrée sortie
        mlflow.sklearn.log_model(model, "model", signature=signature)


if __name__ == "__main__":
    app()
