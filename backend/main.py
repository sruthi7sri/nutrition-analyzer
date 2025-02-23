from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import logging
from ocr import extract_text_from_image  # Your OCR extraction function
from util import predict_nutrition      # Import the function from util.py
from allergies import check_allergies_extended
from text_summary import summarize_nutrition, generate_daily_intake_recommendation
# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or list your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Allowed image file extensions
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

def validate_image(filename: str) -> bool:
    ext = filename.split(".")[-1].lower()
    return ext in ALLOWED_EXTENSIONS

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), allergy: str = Form(...)):
    try:
        # Validate file type
        if not validate_image(file.filename):
            raise HTTPException(status_code=400, detail="Invalid file type. Allowed: JPG, JPEG, PNG")
        
        # Save the uploaded file
        file_path = UPLOAD_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logging.info(f"File {file.filename} saved successfully.")

        # Extract text from the saved image using OCR
        extracted_text = extract_text_from_image(str(file_path))
        if not extracted_text:
            raise HTTPException(status_code=500, detail="OCR processing failed. Ensure the image is clear.")
        
        logging.info("OCR extraction complete.")

        # Summarize the nutrition label text
        nutrition_summary = summarize_nutrition(extracted_text)
        logging.info("Nutrition summarization complete.")

        # Generate daily intake recommendations (dynamic or static based on your summary.py logic)
        daily_intake_recommendation = generate_daily_intake_recommendation(nutrition_summary)
        logging.info("Daily intake recommendation generated.")

        user_allergies = []
        if allergy and allergy.lower() != "none":
            user_allergies.append(allergy)

        # Check for allergens in the extracted text using the extended allergy function.
        allergy_warning = check_allergies_extended(extracted_text, user_allergies)

        # Use the utility function to clean text and run model inference
        result = predict_nutrition(extracted_text)
        
        response = {
            "message": "File processed successfully!",
            "filename": file.filename,
            "allergy": allergy,
            "extracted_text": extracted_text,
            "model_prediction": result["prediction"],
            "nutrition_summary": nutrition_summary,
            "daily_intake_recommendation": daily_intake_recommendation,
            "allergy_warning": allergy_warning,
        }
        return JSONResponse(content=response)

    except Exception as e:
        logging.error(f"Error processing file {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Nutrition Analyzer API is Running!"}
