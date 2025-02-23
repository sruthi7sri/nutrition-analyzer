from PIL import Image, ImageOps
import pytesseract

def extract_text_from_image(image_path: str) -> str:
    """
    Opens an image from the given path, preprocesses it by converting to grayscale
    and then to a black-and-white image, and extracts text using pytesseract.
    
    Args:
        image_path (str): The file path of the image.
        
    Returns:
        str: The extracted text from the image.
    """
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to grayscale
    gray_img = ImageOps.grayscale(img)
    
    # Convert to black and white (binary)
    bw_img = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    
    # (Optional) Save the preprocessed image for verification (you may comment this out)
    # bw_img.save(image_path)  # Consider saving to a different filename to avoid overwriting
    
    # Define custom pytesseract configuration
    custom_config = r'--oem 3 --psm 6'
    
    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(bw_img, config=custom_config)
    
    return extracted_text
