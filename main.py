from core.config import get_api_key
from core.gemini_client import GeminiClient
from utils.prompt_utils import parse_prompt
from utils.output_utils import display_response

def main():
    api_key = get_api_key()
    client = GeminiClient(api_key)

    print("Welcome to Project Artemis! Type your prompt and press Enter.")
    print("Type 'exit' or 'quit' to end the session.")
    print("Add '--verbose' to the end of your prompt for detailed output.\n")

    while True:
        raw_prompt = input("Prompt: ")
        if raw_prompt.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        prompt, verbose_flag = parse_prompt(raw_prompt)
        response = client.generate_content(prompt)
        display_response(response, prompt, verbose_flag)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
