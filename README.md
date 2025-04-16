# llm-evals-python-example

This project demonstrates how to use [OpenAI's evals library](https://github.com/openai/evals) to test large language models (LLMs) on simple math problems.

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

## Running the Simple Math Eval

Run the main script:
```bash
python main.py
```

This will evaluate your chosen LLM (default: `gpt-3.5-turbo`) on basic arithmetic questions defined in `evals/simple_math.yaml`.

## Files
- `main.py`: Script to run the eval
- `evals/simple_math.yaml`: Config file with math questions/answers
- `requirements.txt`: Python dependencies

You can modify `evals/simple_math.yaml` to add more questions or change the model in `main.py`.
