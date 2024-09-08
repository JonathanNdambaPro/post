from pathlib import Path

import mlflow
import mlflow.pyfunc
import pandas as pd
import yaml
from config import MlflowMetaParameters
from loguru import logger

mlflow.set_tracking_uri(MlflowMetaParameters.TRACKING_URI)
mlflow.set_experiment(MlflowMetaParameters.EXPERIMENT_NAME)

model_name = MlflowMetaParameters.REGISTRY_NAME
model_version = 1

path_versioning_model = Path(__file__).resolve().parent / "version.yml"

with path_versioning_model.open("r") as yaml_data_versionning:
    versionng_yaml = yaml.safe_load(yaml_data_versionning)

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{versionng_yaml["version"]}")

df = pd.DataFrame({"review": ["Hi! How are you?"]})
predictions = model.predict(df)

logger.info(predictions)
