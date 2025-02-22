import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        
        # Ensure extracted text is valid
        if len(text.strip()) == 0:
            return "ERROR: No readable text found. Ensure it's a nutrition label."

        return text.strip()

    except Exception as e:
        return f"ERROR: Failed to process image. {str(e)}"
