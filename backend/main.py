from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(
    title="Neuro-Symbolic XAI CDSS",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Neuro-Symbolic XAI CDSS API is Running"
    }