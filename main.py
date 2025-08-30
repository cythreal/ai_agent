import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info

def main():
    parser = argparse.ArgumentParser(description="AI Agent Helpdesk")
    parser.add_argument(
    "User Prompt",
    help="Provided User Prompt"
    )
    parser.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Enable verbose output",
    )
    args = parser.parse_args()
    verb_check(args.verbose)

def verb_check(verbose=False):
    load_dotenv(dotenv_path="apikey.env")

    args = sys.argv[1]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)
    )

    if verbose:
        print("User prompt:", args)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        
    print("---------------------------")
    print("Reply:")
    print(response.text)


if __name__ == "__main__":
    main()

