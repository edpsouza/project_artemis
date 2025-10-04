from google import genai
from google.genai import types

class GeminiClient:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate_content(self, prompt):
        # Prepare the messages for the model
        messages = [
            types.Content(role="user", parts=[types.Part(text=prompt)]),
        ]

        # Generate content using the Gemini model
        response = self.client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )

        return response
