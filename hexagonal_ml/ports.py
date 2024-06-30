from abc import ABC, abstractmethod


class LoanModel(ABC):
    @abstractmethod
    def predict(self, features):
        pass
