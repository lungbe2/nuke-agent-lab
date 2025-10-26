import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Pick a model (flash = faster, pro = more powerful)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Send a simple test prompt
response = model.generate_content("Say hello from Gemini!")

# Print the AI's reply
print(response.text)
