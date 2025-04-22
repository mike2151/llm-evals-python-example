from dataclasses import dataclass
import json
from typing import Any, List, Literal
from openai.types.responses.response_output_item import ResponseOutputItem

from openai import OpenAI
client = OpenAI()


@dataclass
class PromptToEvaluate:
    prompt: str
    expected_answer: str


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

prompts_to_evaluate: list[PromptToEvaluate] = [
    PromptToEvaluate(prompt="What is 2+2?", expected_answer="4"),
    PromptToEvaluate(prompt="What is 27/3?", expected_answer="9"),
    PromptToEvaluate(prompt="What is (9) * (2+3)?", expected_answer="45")
]


def get_equation_result(equation: str) -> Any:
    return eval(equation)


for prompt_to_evaluate in prompts_to_evaluate:
    prompt = prompt_to_evaluate.prompt
    expected_answer = prompt_to_evaluate.expected_answer
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
    # response contains a function which then needs to be evaled
    tool_call: ResponseOutputItem = response.output[0]
    args = json.loads(tool_call.arguments)
    function_name = tool_call.name

    # In this case, will be "get_equation_result"
    final_function = eval(function_name)
    output_from_function = final_function(**args)

    test_case_result: Literal['Passed',
                              'Failed'] = "Passed" if int(output_from_function) == int(expected_answer) else "Failed"
    test_case_output = f"Output: {output_from_function}. Expected Result: {expected_answer}" if test_case_result == "Failed" else ""
    print(f"Prompt: {prompt}. Result: {test_case_result}", test_case_output)
