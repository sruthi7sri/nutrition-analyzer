from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import os
from ocr import extract_text_from_image  # Ensure your teammate's function is imported
from analysis import analyze_text  # Import the analysis function

app = FastAPI()

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Allowed image file types
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

# 🛠️ Function to Validate Image
def validate_image(filename: str):
    ext = filename.split(".")[-1].lower()
    return ext in ALLOWED_EXTENSIONS

# ✅ API: Upload Image & Allergy Info
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), allergy: str = Form(...)):
    # Validate file type
    if not validate_image(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type. Allowed: JPG, JPEG, PNG")

    # Save file to uploads directory
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Send to OCR for text extraction
    extracted_text = extract_text_from_image(str(file_path))

    # Analyze text for warnings
    warnings = analyze_text(extracted_text)

    return JSONResponse(content={
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "allergy": allergy,
        "extracted_text": extracted_text,
        "health_warnings": warnings
    })

# ✅ Health Check Endpoint
@app.get("/")
async def root():
    return {"message": "Nutrition Analyzer API is Running!"}
