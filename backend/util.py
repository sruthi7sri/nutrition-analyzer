import re
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Path where your fine-tuned model is saved
MODEL_PATH = "distilbert_food_classifier"

# Load the tokenizer and model once when the module is imported
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()  # Set model to evaluation mode

def clean_text(text: str) -> str:
    """
    Cleans the input text using the same preprocessing as training:
      - Converts to lowercase
      - Removes digits
      - Removes punctuation
      - Trims whitespace
    """
    text = text.strip().lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text

def predict_nutrition(extracted_text: str) -> dict:
    """
    Cleans and tokenizes the extracted OCR text, then performs inference using the pre-trained model.
    
    Args:
        extracted_text (str): The raw OCR output.
    
    Returns:
        dict: Contains the cleaned text and the model's prediction.
    """
    # Clean the text using the same function as in training
    cleaned = clean_text(extracted_text)
    
    # Tokenize with the same parameters as during training
    inputs = tokenizer(
        cleaned,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )
    
    # Run inference without gradient calculation
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
    
    # Map numeric prediction to label (must match your training label mapping)
    label_mapping = {0: "healthy", 1: "moderately_healthy", 2: "unhealthy"}
    prediction = label_mapping.get(predicted_class_id, "unknown")
    
    return {"cleaned_text": cleaned, "prediction": prediction}
