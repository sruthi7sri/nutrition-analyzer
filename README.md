# Nutrition Analyzer

An AI-powered web application that analyzes nutrition labels to provide personalized health insights and assist users in making informed food choices.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Workflow](#project-workflow)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

## Overview
Many consumers struggle to understand nutrition labels due to hidden ingredients and misleading claims. The **Nutrition Analyzer** simplifies this process by leveraging **machine learning and AI** to extract, summarize, and classify nutrition data. Users can upload an image of a nutrition label, specify dietary preferences (e.g., allergies), and receive health insights based on the extracted information.

## Features
- **Image Recognition of Nutrition Labels:** AI-based text extraction from uploaded images.
- **User-Specified Dietary Concerns:** Customizable preferences based on dietary restrictions and health goals.
- **Health Assessment:** Classifies products as *healthy, moderately healthy, or unhealthy*.
- **Comprehensive Nutritional Summaries:** Provides detailed insights into calories, macronutrients, ingredients, and more.
- **Allergy Warnings:** Detects allergens based on user inputs.
- **Text Summarization:** Generates a concise summary of the extracted text.
- **Daily Intake Recommendations:** Offers dietary guidance based on extracted data.

## Project Workflow
The **Nutrition Analyzer** follows a structured five-step process:

### 1. UI Interaction
- Users upload an image of a nutrition label and select dietary concerns.
- The UI calls an API with the image and allergy data.

### 2. Text Extraction
- The backend processes the image and extracts text using **OCR (PyTesseract)**.

### 3. Text Summarization & Classification
- Extracted text is summarized using a text summarization model.
- A classification model categorizes the nutrition data.

### 4. JSON Creation
- The extracted and processed data is formatted into a structured JSON response.

### 5. API Response & UI Display
- The UI receives the processed JSON and displays the final results to the user.

## Technology Stack
- **Frontend:** React.js, HTML, CSS
- **Backend:** Flask (Python)
- **OCR:** PyTesseract
- **Text Summarization:** DistilBERT
- **Classification Model:** Machine Learning-based health categorization
- **Database:** MongoDB / Firebase (if applicable)
- **Deployment:** Docker, AWS/GCP/Azure

## Setup Instructions
To set up the project locally:

### 1. Clone the repository:
```bash
git clone https://github.com/sruthi7sri/nutrition-analyzer.git
cd nutrition-analyzer


