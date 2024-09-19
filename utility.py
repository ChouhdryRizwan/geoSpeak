import os
import json
import google.generativeai as gen_ai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Google Gemini-Pro AI model
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)

model = gen_ai.GenerativeModel('gemini-1.5-flash')

# Function to load languages from a JSON file
def load_languages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        languages = json.load(file)
    return languages

# Function to generate the translation using Gemini
def generate_translation(source_text, target_language):
    full_prompt = f"Translate the following '{source_text}' into {target_language}. Keep concise to the length of the prompt, don't add any characters that are not required, and keep the response contextual."
    response = model.generate_content(full_prompt)
    return response.text
