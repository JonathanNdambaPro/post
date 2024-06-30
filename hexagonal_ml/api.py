from adapters import LoanPredictor
from application import LoanPredictionService
from domain import LoanApplication
from fastapi import Depends, FastAPI

app = FastAPI()


def get_loan_service() -> LoanPredictionService:
    model_path = "model.pkl"
    predictor = LoanPredictor(model_path)
    return LoanPredictionService(predictor)


@app.post("/predict-loan/", response_model=dict)
def predict_loan(
    loan_request: LoanApplication,
    service: LoanPredictionService = Depends(get_loan_service),
):
    approval = service.predict_loan_approval(loan_request)
    return {"approval": approval}
