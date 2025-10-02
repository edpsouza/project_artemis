import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Check if the prompt argument is provided, if not exit with non-zero status code
    if len(sys.argv) < 2:
        print("Error: Prompt argument is required.")
        sys.exit(1)

    # Get the user prompt from command line arguments
    user_prompt = sys.argv[1]
    # Check if the verbose flag is provided
    verbose_flag = "--verbose" in sys.argv[2:]

    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Prepare the messages for the model
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Generate content using the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # Checks verbose flag, and if present print aditional information
    if verbose_flag:
        print(f"User prompt: {user_prompt}\n")
        print(response.text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    # If not verbose, just print the response text
    else:
        print(response.text)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
