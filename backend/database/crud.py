from sqlalchemy.orm import Session

from backend.database.models import Patient


def create_patient(db: Session, patient_data: dict):

    patient = Patient(**patient_data)

    db.add(patient)

    db.commit()

    db.refresh(patient)

    return patient

def get_all_patients(db: Session):
    return db.query(Patient).all()


def get_patient_by_id(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()


