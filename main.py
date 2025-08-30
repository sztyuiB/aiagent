import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"

if len(sys.argv) > 1:
    user_prompt = sys.argv[1]
else:
    sys.exit("Error: prompt was not provided")

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

response = client.models.generate_content(model=model, contents=messages)

print(response.text)

if "--verbose" in sys.argv:
    print("User prompt: " + str(user_prompt))
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))