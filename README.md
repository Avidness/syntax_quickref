# Syntax Quick Ref and Automated Tester

This project provides implementations of the Breadth-First Search (BFS) algorithm in **Python**, **TypeScript**, and **JavaScript**. Each language version reads a graph structure from a JSON input file, performs BFS traversal, and writes the result to a JSON output file.

## Project Structure
```arduino
syntax_quickref/ 
├── src/ 
│ └── LANGUAGE_NAME/ 
|   ├── Dockerfile
│   ├── TEST_NAME.py 
│   └── run_tests.sh 
|    ...
├── tests/ 
│ └─── TEST_NAME/ 
|   ├── test_input.json
|   └── expected_output.json 
|      ...
├── results/ 
├── docker-compose.yml
├── READEME.md
└── test_runner.py
```

## Quick Start

To set up and run the project, you only need to run:

```bash
python test_runner.py
```

### Running test_runner.py will automatically:

* Build and start Docker containers for each implementation (Python, JavaScript, TypeScript).
* Install required dependencies.
* Execute each language’s BFS implementation.
* Compare the output to the expected result and display the test results.
* The output JSON files for each language will be saved in the results/ directory.

## Project Requirements

* Python 3.x
* Docker and Docker Compose

## Example Input and Output

Your input JSON file (located in tests/bfs/test_input.json) should look like this:

```json
{
    "graph": {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    },
    "start_node": "A"
}
```
An expected output for this input in tests/bfs/expected_output.json:

```json
{
    "bfs_order": ["A", "B", "C", "D", "E", "F"]
}
```

Each implementation reads the input file, performs BFS starting from the start_node, and writes an output JSON file with the BFS traversal order.

## Extending the Project

### Adding a New Language Implementation

To add support for a new language:

1. Create a new directory for the language in `src/` (e.g., `src/ruby/`).
2. Add the BFS Implementation:
    * Write the BFS logic in the new language. Your code should read the JSON input and output files.
3. Create a `run_tests.sh` Script in the new language directory:
    * The script should execute the BFS code and save the output to `results/<language>_bfs_output.json`.
4. Update `docker-compose.yml`:
    * Add a service configuration for the new language in Docker Compose.

After adding the files, run `python test_runner.py` to include the new language in the test process.

### Adding a New Test

To add a new test:

1. Create a Subdirectory in `tests/` for the test (e.g., `tests/dfs/`).
2. Add Input and Expected Output Files:
    * `test_input.json`: Defines the input for the new test.
    * `expected_output.json`: Defines the expected BFS (or other traversal) output for the test.
3. Update `test_runner.py`:
    * Include the new test in the tests list within `test_runner.py`.
Running `python test_runner.py` will now also execute the new test case across all language implementations.

## License
This project is licensed under the MIT License.
