import logging
import re
import string
import unicodedata
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

# --- Configuration ---
logging.basicConfig(level=logging.INFO)
app = FastAPI()

# --- Models ---
class CourseRequest(BaseModel):
    course_name: str = "Default Course"
    course_duration: str = "Default Duration"
    course_level: str = "Default Level"

def save_to_file(filename, response):
    file = open(filename, "w", encoding='utf-8')
    try:
        file.write(response)
        file.close()
        return True
    except Exception as e:
        logging.error(f"Error writing to file {filename}: {e}", exc_info=True)
        return False

# --- Gemini API Client Setup ---
def initialize_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY", "AIzaSyAjnQ2bFxRIauzEI17YV1MnIvmS8lnI_j0")
    if "YOUR_API_KEY" in api_key:
        logging.warning("Using a placeholder API key. Set the GEMINI_API_KEY environment variable.")
    
    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        logging.error(f"Failed to initialize Gemini client: {e}", exc_info=True)
        return None

client = initialize_gemini_client()

# --- Helper Functions ---
def sanitize_filename(filename):
    """Removes or replaces characters illegal in most file systems."""
    try:
        filename = str(filename)
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        sanitized = ''.join(c for c in filename if c in valid_chars)
        sanitized = sanitized.replace(' ', '_')
        sanitized = sanitized.strip('._ ')
        sanitized = sanitized[:100]  # Limit length
        return sanitized or "default_filename"
    except Exception as e:
        logging.error(f"Error sanitizing filename '{filename}': {e}")
        return "default_filename_error"

def gen_text_from_gemini(prompt_list):
    """Generates text using the Gemini API and returns the text content."""
    if not client:
        logging.error("Gemini client not initialized.")
        return None

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_list
        )
        if response and response.candidates:
            text_content = response.candidates[0].content.parts[0].text
            logging.info("Successfully generated content via Gemini.")
            return text_content
        else:
            logging.warning(f"Gemini response missing expected content for prompt: {prompt_list}")
            return None
    except Exception as e:
        logging.error(f"Error during Gemini API call: {e}", exc_info=True)
        return None

def save_to_file(filename, content):
    """Save content to a file with error handling."""
    try:
        with open(filename, "w", encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Content saved successfully to {filename}")
        return True
    except IOError as e:
        logging.error(f"Failed to write to file '{filename}': {e}", exc_info=True)
        return False

# --- Course Generation Functions ---
def generate_course_structure(course_name, course_duration, course_level):
    """Generate course structure using Gemini."""
    prompt = [f"generate a one on one course structure for a course on {course_name} "
              f"for {course_duration} of time and {course_level} level "
              f"(do not include markdown or any styling elements)"
              f"(make the course interactive by adding in tests, quizzes, and projects)"]
    return gen_text_from_gemini(prompt)

def generate_course_content(structure):
    """Generate detailed course content based on structure."""
    prompt = [f"generate detailed one on one course content for the following course structure: {structure}"]
    return gen_text_from_gemini(prompt)

def generate_course_plan(content, course_duration):
    """Generate slide-by-slide course plan."""
    prompt = [f"Based on the following course content and plan, create a one on one course for duration of {course_duration}."
              f"create a slide plan outlining topics, activities for each indevisual slide "
              f"(like tests, quizzes, projects) return a line of instructions for each indevisual slide "
              f"(you must start directly with describing the slides, and must not add any formating on your own, "
              f"the only formattiong required is each slide info stored each in indivisual line.) : \n {content}"]
    return gen_text_from_gemini(prompt)


# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Course Generation API is running."}

@app.get("/health")
def health_check():
    return {"status": "healthy", "gemini_client_initialized": client is not None}

@app.post("/generate")
async def generate(item: CourseRequest):
    course_name = item.course_name
    course_duration = item.course_duration
    course_level = item.course_level
    safe_course_name = sanitize_filename(course_name)
    
    # Generate structure
    logging.info(f"Generating structure for: {safe_course_name}")
    structure = generate_course_structure(course_name, course_duration, course_level)
    if not structure:
        raise HTTPException(status_code=500, detail="Failed to generate course structure.")

    # Generate content
    logging.info(f"Generating content for: {safe_course_name}")
    content = generate_course_content(structure)
    if not content:
        raise HTTPException(status_code=500, detail="Failed to generate course content.")

    # Save content
    file_name_content = f"{safe_course_name}_content.txt"
    if not save_to_file(file_name_content, content):
        raise HTTPException(status_code=500, detail="Failed to save course content file.")

    # Generate plan
    logging.info(f"Generating plan for: {safe_course_name}")
    plan = generate_course_plan(content, course_duration)
    if not plan:
        raise HTTPException(status_code=500, detail="Failed to generate course plan.")

    # Save plan
    file_name_plan = f"{safe_course_name}_plan.txt"
    if not save_to_file(file_name_plan, plan):
        raise HTTPException(status_code=500, detail="Failed to save course plan file.")

    lines=file_name_plan.splitlines()
    logging.info("File read successfully")

    for line_no , line in enumerate(lines):
        logging.info(f"Processing line {line_no + 1}: {line.strip()}")
        
        line = line.strip()
        if line:
            # Remove any leading/trailing whitespace and newlines
            slide_content = line.strip()
            logging.info(f"Generating content for slide {line_no + 1}")
            # Prepare the prompt for Gemini API
            prompt = f"make a html program for a slide for a course on AI with content , only return the html program , and no pre or post text .({slide_content})"
            response = gen_text_from_gemini(prompt)
            logging.info(f"Response received for slide {line_no + 1}: {response}")
            if response:
                logging.info(f"Content generated for slide {line_no + 1}")
                # Remove markdown code blocks if they exist in the response
                if response.startswith("```") and response.endswith("```"):
                    # If it's specifically HTML with language marker
                    if response.startswith("```html"):
                        response = response[7:-3].strip()
                    # General case for any code blocks
                    else:
                        response = response[3:-3].strip()
                logging.info(f"Response cleaned for slide {line_no + 1}")

                # Save the response to a file
                filename = f"./slides/slide_{line_no + 1}.html"
                logging.info(f"Saving content to {filename}")
                if save_to_file(filename, response):
                    logging.info(f"Content saved successfully to {filename}")
                else:
                    logging.error(f"Failed to save content for slide {line_no + 1}")
                
            else:
                print(f"Failed to generate content for prompt: {prompt}")

    return {
        "message": f"Successfully generated content and plan for {course_name}.",
        "content_file": file_name_content,
        "plan_file": file_name_plan,
    }

# --- To run the server: uvicorn main:app --reload ---
