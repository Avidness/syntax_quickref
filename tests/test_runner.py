import json
import subprocess
import os

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def run_test(language, test_name):
    result_file = f"results/{language}_{test_name}_output.json"
    input_file = f"tests/{test_name}/test_input.json"
    expected_file = f"tests/{test_name}/expected_output.json"
    
    # Run the docker-compose service
    service_name = f"{language}_tests"
    print(f"Running {test_name} test for {language}...")
    subprocess.run(["docker-compose", "run", "--rm", service_name])
    
    # Load expected output and result
    expected_output = load_json(expected_file)
    actual_output = load_json(result_file)
    
    # Compare results
    passed = expected_output == actual_output
    print(f"{language} - {test_name} Test {'PASSED' if passed else 'FAILED'}")
    return passed

def main():
    languages = ["javascript", "python", "typescript"]#, "java", "c", "python", "typescript"]
    tests = ["bfs"]#, "dfs", "loops", "array_modifications"]

    summary = {}
    
    for test in tests:
        summary[test] = {}
        for language in languages:
            print(f"Running {test} test for {language}...")
            passed = run_test(language, test)
            summary[test][language] = "PASSED" if passed else "FAILED"

    print("\nTest Summary:")
    print(json.dumps(summary, indent=4))

if __name__ == "__main__":
    main()
