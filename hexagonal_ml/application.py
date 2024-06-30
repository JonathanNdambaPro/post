from domain import LoanApplication
from ports import LoanModel


class LoanPredictionService:
    def __init__(self, loan_model: LoanModel):
        self.loan_model = loan_model

    def predict_loan_approval(self, application: LoanApplication):
        features = [
            application.age,
            application.income,
            application.credit_score,
            application.loan_amount,
        ]
        return self.loan_model.predict(features)
