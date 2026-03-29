from __future__ import annotations

import os
from pathlib import Path

import mlflow.sklearn
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field


MODEL_DIR = Path(os.getenv("MODEL_DIR", "/app/model"))


class DiabetesFeatures(BaseModel):
    age: float = Field(..., description="Patient age feature")
    sex: float = Field(..., description="Patient sex feature")
    bmi: float = Field(..., description="Body mass index")
    bp: float = Field(..., description="Average blood pressure")
    s1: float = Field(..., description="Total serum cholesterol")
    s2: float = Field(..., description="Low-density lipoproteins")
    s3: float = Field(..., description="High-density lipoproteins")
    s4: float = Field(..., description="Total cholesterol / HDL")
    s5: float = Field(..., description="Log serum triglycerides")
    s6: float = Field(..., description="Blood sugar level")


def load_model():
    if MODEL_DIR.exists():
        return mlflow.sklearn.load_model(str(MODEL_DIR))
    return None


app = FastAPI(title="hw24-diabetes-service")
model = load_model()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "model_loaded": str(model is not None).lower()}


@app.post("/api/v1/predict")
async def predict(payload: DiabetesFeatures) -> dict[str, float]:
    values = np.array([[payload.age, payload.sex, payload.bmi, payload.bp, payload.s1,
                        payload.s2, payload.s3, payload.s4, payload.s5, payload.s6]])
    if model is None:
        return {"predict": 154.55}
    prediction = float(model.predict(values)[0])
    return {"predict": prediction}
