# Nutrition Analyzer

## Inspiration
Many consumers struggle to decipher nutrition labels, making it difficult to make informed dietary choices. Misleading claims, hidden ingredients, and a lack of personalized guidance often lead to unhealthy eating habits. The **Nutrition Analyzer** was created to simplify nutritional awareness using AI and provide users with personalized health insights effortlessly.

## What It Does
The **Nutrition Analyzer** is a smart web application that allows users to:
- Upload an image of a nutrition label to extract key details using AI.
- Input dietary preferences and allergies for personalized analysis.
- Get an instant health classification—healthy, moderately healthy, or unhealthy.
- Receive detailed nutritional summaries, including calories, macronutrients, and ingredients.
- Get allergy warnings based on user input.
- View daily intake recommendations for better dietary decisions.

## Technology Stack

| Task | Technology |
|-------------------------------|--------------------------------------------------|
| **Extract text from image** | Python (FastAPI), PyTesseract, Image Preprocessing (TBD) |
| **Convert extracted text into structured JSON** | T5 Base (Summarization), DistilBERT (Classification) |
| **Score food based on FDA/WHO guidelines** | Python (AST API, Pandas), OpenFoodFacts Dataset |
| **Build user interface for image upload & results** | HTML, CSS, JavaScript |
| **Connect frontend to backend via API calls** | Flask/FastAPI (Backend), Fetch/Axios (Frontend) |
| **Host and manage backend** | GitHub |

## How We Built It
- **Image Processing & AI:** Used machine learning models (such as DistilBERT) to extract text from nutrition labels and analyze them.
- **Web Application:** Frontend built using HTML, CSS, with backend powered by JavaScript and FastAPT.
- **Health Classification Algorithm:** Implemented a system to categorize food items based on extracted nutritional data.
- **Database Integration:** Utilized a dataset of nutritional information to enhance analysis and provide comparisons.

## Challenges We Ran Into
- **Accurate Text Extraction:** Handling low-quality prints, complex fonts, and blurry images for OCR-based extraction.
- **Classification Complexity:** Defining precise thresholds for health categorization required extensive data validation.
- **Personalization Handling:** Balancing custom dietary preferences with accurate health assessments.
- **Real-Time Processing:** Ensuring fast and accurate analysis without lag.

## Accomplishments
- Successfully implemented AI-based nutrition analysis from images.
- Developed a personalized dietary insights feature tailored to users' health needs.
- Built an interactive and user-friendly web application.
- Implemented real-time health classification for quick and accessible nutrition evaluation.
- Created a foundation for future AI-driven food recommendations.

## What We Learned
- The importance of AI in simplifying complex health data for users.
- How OCR and image recognition can be optimized for better text extraction.
- The challenges of balancing personalization with accurate nutritional analysis.
- The significance of real-time data processing for an intuitive user experience.
- How expanding the database can enhance AI-driven insights for better decision-making.

## Future Enhancements
- **Healthier Alternatives:** Recommend alternative food options if a product is unhealthy.
- **Expanded Database:** Improve AI accuracy with a larger dataset.
- **Mobile Application:** Extend functionality to mobile platforms.

## Setup Instructions
### Clone the Repository
```bash
git clone https://github.com/sruthi7sri/nutrition-analyzer.git
cd nutrition-analyzer
