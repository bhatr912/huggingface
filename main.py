# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import load_model

app = FastAPI()
model = load_model()

class RequestModel(BaseModel):
    text: str

@app.post("/predict/")
def predict(request: RequestModel):
    text = request.text
    prediction = model(text)
    return {"prediction": prediction}
