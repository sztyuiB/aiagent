import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

system_prompt = '''
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
'''
available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file])

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"

if len(sys.argv) > 1:
    user_prompt = sys.argv[1]
else:
    sys.exit("Error: prompt was not provided")

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

response = client.models.generate_content(
    model=model,
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

if len(response.function_calls) > 0:
    if "--verbose" in sys.argv:
        actual_call = call_function(response.function_calls[0], verbose=True)
        try:
            print(f"-> {actual_call.parts[0].function_response.response}")
        except Exception as E:
            print(f"Fatal error: {E}")
    #print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
else:
    print(response.text)

if "--verbose" in sys.argv:
    print("User prompt: " + str(user_prompt))
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
