import os
from dotenv import load_dotenv

# Load environment variables from .env file
def get_api_key():
    load_dotenv()
    return os.environ.get("GEMINI_API_KEY")
