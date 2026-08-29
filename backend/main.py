from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router


app = FastAPI(
    title="Neuro-Symbolic XAI CDSS",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API routes
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Neuro-Symbolic XAI CDSS API is Running"
    }