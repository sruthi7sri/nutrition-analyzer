from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import os
import logging
from ocr import extract_text_from_image  # Ensure your teammate's function is imported
from analysis import analyze_text  # Import the analysis function

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Allowed image file types
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

# Function to Validate Image
def validate_image(filename: str):
    ext = filename.split(".")[-1].lower()
    return ext in ALLOWED_EXTENSIONS

# API: Upload Image & Analyze Nutrition
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), allergy: str = Form(...)):
    try:
        # Validate file type
        if not validate_image(file.filename):
            logging.warning(f"Invalid file type uploaded: {file.filename}")
            raise HTTPException(status_code=400, detail="Invalid file type. Allowed: JPG, JPEG, PNG")

        # Save file to uploads directory
        file_path = UPLOAD_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logging.info(f"File {file.filename} saved successfully.")

        # Send to OCR for text extraction
        extracted_text = extract_text_from_image(str(file_path))

        # Handle cases where OCR fails
        if "error" in extracted_text or not extracted_text:
            logging.error(f"OCR failed for file: {file.filename}")
            raise HTTPException(status_code=500, detail="OCR processing failed. Ensure the image is clear.")

        # Analyze text for warnings
        analysis_result = analyze_text(extracted_text)

        response = {
            "message": "File uploaded successfully!",
            "filename": file.filename,
            "allergy": allergy,
            "extracted_text": extracted_text,
            "health_warnings": analysis_result["warnings"]
        }

        logging.info(f"Processing complete for file: {file.filename}")
        return JSONResponse(content=response)

    except Exception as e:
        logging.error(f"Error processing file {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Health Check Endpoint
@app.get("/")
async def root():
    return {"message": "Nutrition Analyzer API is Running!"}
