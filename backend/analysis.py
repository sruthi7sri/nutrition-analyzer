import re
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define threshold values for warnings
THRESHOLDS = {
    "sugar": 10,   # grams (considered high if above this)
    "sodium": 200, # mg (considered high if above this)
    "calories": 500, # kcal (considered high if above this)
}

def analyze_text(extracted_text: str) -> dict:
    """
    Extracts key nutrition values and provides warnings based on predefined thresholds.
    """
    # Initialize result dictionary
    nutrition_info = {
        "sugar": extract_nutrient(extracted_text, r"(\d+(\.\d+)?)\s*(g|mg)?\s*sugar"),
        "sodium": extract_nutrient(extracted_text, r"(\d+(\.\d+)?)\s*(g|mg)?\s*sodium"),
        "calories": extract_nutrient(extracted_text, r"(\d+(\.\d+)?)\s*(kcal|calories)"),
    }

    # Generate warnings based on threshold values
    warnings = generate_warnings(nutrition_info)

    # Logging extracted values
    logging.info(f"Extracted Nutrition Info: {json.dumps(nutrition_info, indent=2)}")
    logging.info(f"Warnings: {warnings}")

    # Return structured response
    return {
        "nutrition_values": nutrition_info,
        "warnings": warnings
    }

def extract_nutrient(text: str, pattern: str):
    """
    Extracts a numeric nutrient value from text using regex.
    Returns 'N/A' if the value is not found.
    """
    match = re.search(pattern, text, re.IGNORECASE)
    return float(match.group(1)) if match else "N/A"

def generate_warnings(nutrition_info: dict):
    """
    Generates warnings if values exceed predefined thresholds.
    """
    warnings = []
    for nutrient, value in nutrition_info.items():
        if value != "N/A" and value > THRESHOLDS[nutrient]:
            warnings.append(f"High {nutrient.capitalize()}: {value}")

    if not warnings:
        warnings.append("No significant health warnings detected.")

    return warnings

# Example Usage (Remove in Production)
if __name__ == "__main__":
    # Simulated extracted text from OCR
    extracted_text = "Calories: 600 kcal\nSugar: 12g\nSodium: 250mg"
    
    response = analyze_text(extracted_text)
    print(json.dumps(response, indent=2))
