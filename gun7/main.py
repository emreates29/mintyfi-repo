import joblib
from fastapi import FastAPI, Depends, Request
from app.schema import PredictRequest, PredictResponse
from contextlib import asynccontextmanager

class Resources:
    def __init__(self):
        self.model = joblib.load("en_iyi_model.pkl")
        self.vectorizer = joblib.load("vectorizer.pkl")

def get_resources(request: Request):
    return request.app.state.resources

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.resources = Resources()
    yield
    # cleanup

app = FastAPI(lifespan=lifespan)

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest, resources: Resources = Depends(get_resources)):
    features = resources.vectorizer.transform([request.text])
    prediction = resources.model.predict(features)[0]
    probability = resources.model.predict_proba(features)[0].max()
    return PredictResponse(label=prediction, probability=float(probability))
