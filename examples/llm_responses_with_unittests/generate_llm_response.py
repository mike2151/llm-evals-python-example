import json
from typing import Any, List, Literal
from openai.types.responses.response_output_item import ResponseOutputItem

from openai import OpenAI
client = OpenAI()


def get_equation_result(equation: str) -> Any:
    return eval(equation)


class GenerateLLMResponse():
    tools: Any = [{
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

    def __init__(self, prompt: str) -> None:
        self.prompt: str = prompt

    def generate_response(self) -> str:
        response = client.responses.create(
            model="gpt-3.5-turbo",
            input=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides answers as numbers only when appropriate."
                },
                {
                    "role": "user",
                    "content": self.prompt
                }
            ],
            tools=self.tools
        )
        # response contains a function which then needs to be evaled
        tool_call: ResponseOutputItem = response.output[0]
        args = json.loads(tool_call.arguments)
        function_name = tool_call.name

        # In this case, will be "get_equation_result"
        final_function = eval(function_name)
        output_from_function = final_function(**args)
        return output_from_function
