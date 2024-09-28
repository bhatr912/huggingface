# model.py (Download and save model)
from transformers import pipeline

def load_model():
    # Download a small model from Hugging Face
    return pipeline("fill-mask", model="distilbert-base-uncased")
