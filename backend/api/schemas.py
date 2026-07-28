from pydantic import BaseModel


class PatientRequest(BaseModel):
    patient_name: str

    gender: int
    age: float
    hypertension: int
    heart_disease: int
    smoking_history: int

    bmi: float
    HbA1c_level: float
    blood_glucose_level: int

from datetime import datetime

class PatientResponse(BaseModel):

    id: int

    patient_name: str

    age: float

    probability: float

    final_decision: str

    created_at: datetime

    model_config = {
        "from_attributes": True
    }