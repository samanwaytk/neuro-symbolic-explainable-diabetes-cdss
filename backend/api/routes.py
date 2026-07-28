from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api.schemas import (
    PatientRequest,
    PatientResponse,
)

from backend.services.hybrid_engine import hybrid_prediction

from backend.database.database import get_db
from backend.database.crud import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
)

router = APIRouter()


@router.post("/predict")
def predict(
    patient: PatientRequest,
    db: Session = Depends(get_db)
):

    result = hybrid_prediction(patient.model_dump())

    patient_record = {
        **result["patient_data"],

        "ml_prediction": result["ml_prediction"],
        "probability": result["probability"],
        "rule_risk": result["rule_risk"],
        "final_decision": result["final_decision"]
    }

    create_patient(db, patient_record)

    return result

@router.get(
    "/patients",
    response_model=list[PatientResponse]
)
def read_patients(db: Session = Depends(get_db)):
    return get_all_patients(db)
@router.get(
    "/patients/{patient_id}",
    response_model=PatientResponse
)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return get_patient_by_id(db, patient_id)