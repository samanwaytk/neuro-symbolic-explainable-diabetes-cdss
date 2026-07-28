from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from backend.database.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String, nullable=True)

    gender = Column(Integer)
    age = Column(Float)

    hypertension = Column(Integer)
    heart_disease = Column(Integer)

    smoking_history = Column(Integer)

    bmi = Column(Float)

    HbA1c_level = Column(Float)

    blood_glucose_level = Column(Integer)

    ml_prediction = Column(Integer)

    probability = Column(Float)

    rule_risk = Column(String)

    final_decision = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)