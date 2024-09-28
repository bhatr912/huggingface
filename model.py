# model.py (Download and save model)
from transformers import pipeline

def load_model():
    # Download a small model from Hugging Face
    return pipeline("fill-mask", model="distilbert-base-uncased")

##https://chatgpt.com/share/66f798bf-b928-800e-a79b-74a2ae11ed46