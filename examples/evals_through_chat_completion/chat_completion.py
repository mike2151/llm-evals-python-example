from openai import OpenAI
import os   
import sys

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set it before running the script:")
    print("  export OPENAI_API_KEY='your-api-key'")
    sys.exit(1)

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "What is 2+2?"
        }
    ]
)

print(completion.choices[0].message.content)



