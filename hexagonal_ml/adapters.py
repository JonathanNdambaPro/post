import pickle

from ports import LoanModel


class LoanPredictor(LoanModel):
    def __init__(self, model_path):
        with open(model_path, "rb") as model_file:
            self.model = pickle.load(model_file)

    def predict(self, features):
        return self.model.predict([features])[0]
