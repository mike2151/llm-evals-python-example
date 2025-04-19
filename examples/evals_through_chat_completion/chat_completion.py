import json
from openai import OpenAI
import os
import sys

api_key: str | None = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set it before running the script:")
    print("  export OPENAI_API_KEY='your-api-key'")
    sys.exit(1)

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_equation_result",
            "description": "Get the answer to a math equation",
            "parameters": {
                "type": "object",
                "properties": {
                    "equation": {
                        "type": "string",
                        "description": "The math equation to solve, e.g. 2+2",
                    },
                },
                "required": ["equation"],
            },
        }
    }
]
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provides answers as numbers only when appropriate."
    },
    {
        "role": "user",
        "content": "What is 2+2?"
    }
]
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = completion.choices[0].message
# Check if the message has tool calls
if message.tool_calls:
    # Get the function call
    function_call = message.tool_calls[0]
    function_name = function_call.function.name

    # Parse the arguments
    function_args = json.loads(function_call.function.arguments)

    # If it's our equation function, evaluate it
    if function_name == "get_equation_result":
        equation = function_args.get("equation")
        result = eval(equation)
        print("Ran prompt for equation", equation, "Result:", result)
