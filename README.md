# ATS Resume Expert

## Overview
ATS Resume Expert is a Streamlit-based web application designed to analyze resumes against job descriptions. Using Google Gemini AI, the app provides insights on how well a resume matches a given job, suggests improvements, and offers a percentage-based ATS match score.

## Features
- **Resume Analysis:** Reviews the resume against the job description and provides a detailed evaluation.
- **Skill Improvement Suggestions:** Offers recommendations to enhance skills and increase job relevance.
- **ATS Percentage Match:** Computes the percentage of match between the resume and job description while identifying missing keywords.
- **PDF Resume Processing:** Extracts and processes the first page of a PDF resume.

## Technologies Used
- **Streamlit**: Web application framework for UI.
- **Google Gemini AI**: Used for resume analysis and evaluation.
- **PyMuPDF (Fitz)**: Extracts content from PDF files.
- **pdf2image**: Converts PDF to images.
- **PIL (Pillow)**: Handles image processing.
- **dotenv**: Manages environment variables securely.

## Installation
### Prerequisites
Ensure you have Python 3.10+ installed and a virtual environment set up.

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd ats-resume-expert
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following line, replacing `YOUR_API_KEY` with your actual Google API Key:
     ```sh
     GOOGLE_API_KEY=YOUR_API_KEY
     ```

## Usage
1. Run the application:
   ```sh
   streamlit run app.py
   ```
2. Open the web interface and:
   - Enter a job description.
   - Upload a resume in PDF format.
   - Click on one of the following buttons:
     - **"Tell Me About the Resume"**: Provides an evaluation of how well the resume fits the job description.
     - **"How Can I Improve My Skills"**: Suggests skill enhancements.
     - **"Percentage Match"**: Returns a compatibility percentage along with missing keywords.

## File Structure
```
ats-resume-expert/
│── app.py  # Main Streamlit application
│── requirements.txt  # Required Python dependencies
│── .env  # Environment variables (not included in repo)
│── README.md  # Documentation
```

## Known Issues & Future Improvements
- Improve text extraction for multi-page resumes.
- Enhance keyword matching algorithm for ATS percentage calculation.
- Add support for multiple AI models.



