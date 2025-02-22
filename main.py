from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """Upload an image and save it to the server."""
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename, "message": "File uploaded successfully!"}
