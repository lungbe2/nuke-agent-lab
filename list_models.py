import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("AIzaSyCcqUTs5nKSdugnpII7ldF4F5K1ydWye24"))

# List all models available to your key
for m in genai.list_models():
    print(m.name, m.supported_generation_methods)