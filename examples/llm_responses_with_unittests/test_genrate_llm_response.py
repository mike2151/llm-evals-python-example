import unittest

from .generate_llm_response import GenerateLLMResponse


class TestGenerateLLMResponse(unittest.TestCase):
    def test_simple_math_equation(self) -> None:
        prompt = "What is 2+2"
        llm_class = GenerateLLMResponse(prompt)
        llm_response = llm_class.generate_response()
        llm_numeric_return = int(llm_response)
        self.assertEqual(llm_numeric_return, 4)
