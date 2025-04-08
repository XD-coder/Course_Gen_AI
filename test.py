import logging
import os # Added for environment variable access
from google import genai # Assuming genai is installed

# --- Configuration --
# !!! Load API Key Securely (e.g., from environment variable) !!!
# Replace with your actual key loading method
api_key = os.getenv("GEMINI_API_KEY") # Fallback or direct key

if api_key == "YOUR_API_KEY_HERE":
    logging.warning("Using a placeholder API key. Set the GEMINI_API_KEY environment variable.")
logging.basicConfig(level=logging.INFO)
logging.info("Initializing Gemini client...")
# --- Gemini API Client Setup ---
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    logging.error(f"Failed to initialize Gemini client: {e}", exc_info=True)
    # Depending on your application, you might want to exit or handle this differently
    client = None # Ensure client is None if initialization fails


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
        logging.error(f"Error during Gemini API call for prompt {prompt_list}: {e}", exc_info=True)
        return None


def save_to_file(filename, response):
    file = open(filename, "w", encoding='utf-8')
    try:
        file.write(response)
        file.close()
        return True
    except Exception as e:
        logging.error(f"Error writing to file {filename}: {e}", exc_info=True)
        return False

#start of function
def genHTML(filename, course_name):
    logging.info("Reading AI_plan.txt")
    file = open("AI_plan.txt", "r", encoding='utf-8')
    lines = file.readlines()
    file.close()
    logging.info("File read successfully")

    for line_no , line in enumerate(lines):
        logging.info(f"Processing line {line_no + 1}: {line.strip()}")
        
        line = line.strip()
        if line:
            slide_content = line.strip()
            logging.info(f"Generating content for slide {line_no + 1}")
            prompt = f"make a html program for a slide for a course on {course_name} with content , only return the html program , and no pre or post text .({slide_content})"
            response = gen_text_from_gemini(prompt)
            logging.info(f"Response received for slide {line_no + 1}: {response}")
            if response:
                logging.info(f"Content generated for slide {line_no + 1}")
                # Remove markdown code blocks if they exist in the response
                if response.startswith("```") and response.endswith("```"):
                    # If it's specifically HTML with language marker
                    if response.startswith("```html"):
                        response = response[7:-3].strip()
                    else:
                        response = response[3:-3].strip()
                logging.info(f"Response cleaned for slide {line_no + 1}")

                #save the response to a file
                os.makedirs(f"./{course_name}/slides", exist_ok=True)
                filename = f"./{course_name}/slides/slide_{line_no + 1}.html"
                logging.info(f"Saving content to {filename}")
                if save_to_file(filename, response):
                    logging.info(f"Content saved successfully to {filename}")
                else:
                    logging.error(f"Failed to save content for slide {line_no + 1}")
                
            else:
                print(f"Failed to generate content for prompt: {prompt}")



if __name__ == "__main__":
    # Example usage
    genHTML("AI_plan.txt")