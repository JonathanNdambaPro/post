from pydantic import BaseModel, Field


class LoanApplication(BaseModel):
    age: int = Field(..., gt=17, description="Age must be at least 18 years old")
    income: float = Field(..., gt=0, description="Income must be positive")
    credit_score: int = Field(
        ..., ge=300, le=850, description="Credit score must be between 300 and 850"
    )
    loan_amount: float = Field(..., gt=0, description="Loan amount must be positive")
