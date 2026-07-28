import joblib

MODEL_PATH = "models/diabetes_model.pkl"
GENDER_ENCODER_PATH = "models/gender_encoder.pkl"
SMOKING_ENCODER_PATH = "models/smoking_encoder.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def load_gender_encoder():
    return joblib.load(GENDER_ENCODER_PATH)


def load_smoking_encoder():
    return joblib.load(SMOKING_ENCODER_PATH)