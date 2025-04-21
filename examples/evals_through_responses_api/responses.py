import json
from openai.types.responses.response_output_item import ResponseOutputItem


from openai import OpenAI
client = OpenAI()

tools = [{
    "type": "function",
    "name": "get_equation_result",
    "description": "Get the answer to a math equation",
    "parameters": {
        "type": "object",
        "properties": {
            "equation": {
                "type": "string",
                "description": "The math equation to solve, e.g. 2+2"
            }
        },
        "required": [
            "equation"
        ],
        "additionalProperties": False
    }
}]

prompt: str = "What is 2+2?"


response = client.responses.create(
    model="gpt-3.5-turbo",
    input=[
        {
            "role": "system",
            "content": "You are a helpful assistant that provides answers as numbers only when appropriate."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    tools=tools
)


def get_equation_result(equation):
    return eval(equation)


# response contains a function which then needs to be evaled
tool_call: ResponseOutputItem = response.output[0]
args = json.loads(tool_call.arguments)
function_name = tool_call.name

# In this case, will be "get_equation_result"
final_function = eval(function_name)
output_from_function = final_function(**args)

print(output_from_function)
