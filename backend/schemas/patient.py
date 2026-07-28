from pydantic import BaseModel

class PatientData(BaseModel):
    age: int
    bmi: float
    blood_glucose_level: int