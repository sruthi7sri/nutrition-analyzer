import json
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def process_ocr_response(extracted_text: str) -> dict:
    """
    Processes text extracted by the teammate, ensures proper formatting, and returns structured JSON.
    """
    try:
        # Ensure text is valid
        cleaned_text = clean_text(extracted_text)
        if not cleaned_text:
            return {"error": "No readable text found. Ensure it's a nutrition label."}

        # Format the cleaned text into a structured JSON format
        structured_data = format_as_json(cleaned_text)

        logging.info(f"OCR Output Processed: {json.dumps(structured_data, indent=2)}")
        return structured_data

    except Exception as e:
        logging.error(f"Error processing OCR response: {str(e)}")
        return {"error": f"Error processing OCR response: {str(e)}"}

def clean_text(text: str) -> str:
    """
    Cleans the extracted text by removing unnecessary whitespace, special characters, and noise.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
    return text if text else None

def format_as_json(text: str) -> dict:
    """
    Formats cleaned text into a structured JSON format.
    """
    return {"processed_text": text}

# Example Usage (remove/comment out in production)
if __name__ == "__main__":
    # Simulated extracted text from your teammate
    extracted_text = "Calories: 200 kcal\nSugar: 10g\nSodium: 300mg"
    
    response = process_ocr_response(extracted_text)
    print(json.dumps(response, indent=2))
