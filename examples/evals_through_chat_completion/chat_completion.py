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

print(completion)


# client = OpenAI()

# # structured output to make sure that the response is a number
# completion: ChatCompletion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant that provides answers as numbers only when appropriate."
#         },
#         {
#             "role": "user",
#             "content": "What is 2+2?"
#         }
#     ],
#     response_format={"type": "text"}
# )

# print(completion.choices[0].message.content)
