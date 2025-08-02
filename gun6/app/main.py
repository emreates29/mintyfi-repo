import pickle
from fastapi import FastAPI
from app.schema import PredictRequest, PredictResponse
import joblib

app = FastAPI()

model = None
vectorizer = None

@app.on_event("startup")
def load_model():
    global model, vectorizer
    model = joblib.load("en_iyi_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    features = vectorizer.transform([request.text])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max()
    return PredictResponse(label=prediction, probability=float(probability))
