# run_eval.py
import subprocess
import os
import sys

# You can find all available models here: https://platform.openai.com/docs/models
MODEL_TO_EVALUATE = "gpt-3.5-turbo" 

EVAL_YAML_PATH = "evals/simple_math.yaml"

# --- Check for API Key ---
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set it before running the script:")
    print("  export OPENAI_API_KEY='your-api-key'")
    sys.exit(1)

# --- Check for evals library ---
try:
    import evals
except ImportError:
    print("Error: evals library not installed.")
    print("Please install it by running:")
    print("  pip install -r requirements.txt")
    sys.exit(1)

EVAL_NAME = "simple_math"

RELATIVE_EVAL_YAML_PATH = "evals/simple_math.yaml"
# Get the directory where this script (run_eval.py) is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the absolute path to the YAML file
ABSOLUTE_EVAL_YAML_PATH = os.path.join(SCRIPT_DIR, RELATIVE_EVAL_YAML_PATH)

# --- Construct the Command ---
# The basic command is: python3 -m evals.cli.oaieval <model_name> <eval_yaml_path_or_name>
command = [
    sys.executable,         # Path to the current Python interpreter (e.g., /path/to/venv/bin/python)
    "-m",                   
    "evals.cli.oaieval",    # The module path for the oaeval tool
    MODEL_TO_EVALUATE,      
    EVAL_NAME,
    "--registry_path",
    ABSOLUTE_EVAL_YAML_PATH          
]

# You can add optional arguments here, for example:
# command.extend(["--record_path", "output/eval_results.jsonl"]) # Save detailed logs
# command.extend(["--max_samples", "2"]) # Limit the number of samples to run (for testing)

print(f"\nRunning evaluation command:")
print(f"  {' '.join(command)}\n")


# --- Execute the Command ---
try:
    # Run the command and capture output in real-time
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

    # Print output line by line as it comes
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

    # Wait for the process to complete and get the return code
    rc = process.poll()

    if rc == 0:
        print("\nEvaluation completed successfully.")
    else:
        print(f"\nEvaluation failed with return code {rc}.")

    print(f"\nDetailed logs and results are often saved in /tmp/evallogs/")
    print("(Check the output above for the exact path if a --record_path was used or generated)")

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)