import typing as t
from pathlib import Path

import numpy as np
import pandas as pd
from loguru import logger
from pydantic import BaseModel, Field
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Receiver : Contient l'état des données et le contexte d'exécution
# et utilise Pydantic pour la validation des données
class DataState(BaseModel):
    data: t.Optional[pd.DataFrame] = Field(default=None, description="Données brutes")
    X_train: t.Optional[np.ndarray] = Field(
        default=None, description="Caractéristiques d'entraînement"
    )
    X_test: t.Optional[np.ndarray] = Field(
        default=None, description="Caractéristiques de test"
    )
    y_train: t.Optional[np.ndarray] = Field(
        default=None, description="Cibles d'entraînement"
    )
    y_test: t.Optional[np.ndarray] = Field(default=None, description="Cibles de test")
    model: t.Optional[t.Any] = Field(default=None, description="Modèle entraîné")
    accuracy: t.Optional[float] = Field(default=None, description="Précision du modèle")

    class Config:
        arbitrary_types_allowed = True


# Command : Interface abstraite pour toutes les commandes
class DataProcessingCommand(t.Protocol):
    def execute(self, state: DataState) -> DataState: ...


# Concrete Command : Implémentation spécifique pour charger les données
class LoadDataCommand:
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self, state: DataState) -> DataState:
        state.data = pd.read_csv(self.file_path)
        logger.info("Données chargées")
        return state


# Concrete Command : Implémentation spécifique pour diviser les données
class SplitDataCommand:
    def execute(self, state: DataState) -> DataState:
        X = state.data.drop("target", axis=1)
        y = state.data["target"]
        state.X_train, state.X_test, state.y_train, state.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        logger.info("Données divisées en ensembles d'entraînement et de test")
        return state


# Concrete Command : Implémentation spécifique pour normaliser les données
class ScaleDataCommand:
    def execute(self, state: DataState) -> DataState:
        scaler = StandardScaler()
        state.X_train = scaler.fit_transform(state.X_train)
        state.X_test = scaler.transform(state.X_test)
        logger.info("Données normalisées")
        return state


# Concrete Command : Implémentation spécifique pour entraîner le modèle
class TrainModelCommand:
    def execute(self, state: DataState) -> DataState:
        state.model = RandomForestClassifier(n_estimators=100, random_state=42)
        state.model.fit(state.X_train, state.y_train)
        logger.info("Modèle entraîné")
        return state


# Concrete Command : Implémentation spécifique pour évaluer le modèle
class EvaluateModelCommand:
    def execute(self, state: DataState) -> DataState:
        y_pred = state.model.predict(state.X_test)
        state.accuracy = accuracy_score(state.y_test, y_pred)
        logger.info(f"Modèle évalué, précision: {state.accuracy}")
        return state


# Invoker : Gère la séquence d'exécution des commandes
class DataPipeline:
    def __init__(self):
        self.commands = []
        self.state = DataState()

    def add_command(self, command: DataProcessingCommand) -> None:
        self.commands.append(command)

    def run(self) -> DataState:
        for command in self.commands:
            self.state = command.execute(self.state)
        return self.state


FILE_TO_PROCESS = Path(__file__).resolve() / "data.csv"

# Utilisation : Configuration et exécution du pipeline
pipeline = DataPipeline()

pipeline.add_command(LoadDataCommand(FILE_TO_PROCESS))
pipeline.add_command(SplitDataCommand())
pipeline.add_command(ScaleDataCommand())
pipeline.add_command(TrainModelCommand())
pipeline.add_command(EvaluateModelCommand())

final_state = pipeline.run()

logger.info(f"Précision finale: {final_state.accuracy}")
