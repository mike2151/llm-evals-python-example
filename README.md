# llm-evals-python-example

This project demonstrates how to use [OpenAI's evals library](https://github.com/openai/evals) to test large language models (LLMs) in different scenarios

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your OpenAI API key:**
   Set your API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=your-api-key-here
   ```
## Examples
See the `examples` folder for examples on running evals

1. [Evals through chat completion](examples/evals_through_chat_completion/chat_completion.py)

2. [Evals through OpenAI Evals library](examples/evals_library/main.py)

