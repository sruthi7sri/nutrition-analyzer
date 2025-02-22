import re

def analyze_text(extracted_text: str):
    """
    Checks for high sugar and sodium content in the extracted text.
    Returns warnings if excessive amounts are found.
    """
    warnings = []

    # Regular expressions to extract nutrient values
    sugar_match = re.search(r"(\d+(\.\d+)?)\s*(g|mg)?\s*sugar", extracted_text, re.IGNORECASE)
    sodium_match = re.search(r"(\d+(\.\d+)?)\s*(g|mg)?\s*sodium", extracted_text, re.IGNORECASE)

    # Check sugar content
    if sugar_match:
        sugar_value = float(sugar_match.group(1))
        if sugar_value > 10:  # Assuming 10g+ is high
            warnings.append(f"⚠️ High Sugar: {sugar_value}g")

    # Check sodium content
    if sodium_match:
        sodium_value = float(sodium_match.group(1))
        if sodium_value > 200:  # Assuming 200mg+ is high
            warnings.append(f"⚠️ High Sodium: {sodium_value}mg")

    if not warnings:
        warnings.append("✅ No significant health warnings detected.")

    return warnings
