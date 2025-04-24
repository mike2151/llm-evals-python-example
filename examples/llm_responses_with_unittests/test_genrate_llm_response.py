import unittest
import pytest

from .generate_llm_response import GenerateLLMResponse


class TestGenerateLLMResponse(unittest.TestCase):
    @pytest.mark.timeout(10)
    def test_simple_math_equation(self) -> None:
        prompt = "What is 2+2"
        llm_class = GenerateLLMResponse(prompt)
        llm_response = llm_class.generate_response()
        llm_numeric_return = int(llm_response)
        self.assertEqual(llm_numeric_return, 4)

    @pytest.mark.timeout(10)
    def test_pendas(self) -> None:
        prompt = "What is ((2+2) * 4) / 2?"
        llm_class = GenerateLLMResponse(prompt)
        llm_response = llm_class.generate_response()
        llm_numeric_return = int(llm_response)
        self.assertEqual(llm_numeric_return, 8)

    @pytest.mark.timeout(10)
    def test_square_root(self) -> None:
        prompt = "What is the square root of 16?"
        llm_class = GenerateLLMResponse(prompt)
        llm_response = llm_class.generate_response()
        llm_numeric_return = int(llm_response)
        self.assertEqual(llm_numeric_return, 4)
