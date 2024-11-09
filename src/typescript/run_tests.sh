#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

APP_DIR="/app"
TESTS_DIR="/tests"
RESULTS_DIR="/results"

mkdir -p "$RESULTS_DIR"

run_test() {
    test_name="$1"
    script="$2"
    input_file="$TESTS_DIR/$test_name/test_input.json"
    output_file="$RESULTS_DIR/typescript_${test_name}_output.json"

    # Compile TypeScript files
    npm run build

    # Run the compiled JavaScript test
    node "dist/$script" "$input_file" "$output_file"
}

cd "$APP_DIR"

# Run the BFS test
run_test "bfs" "bfs.js"

echo "TypeScript BFS test completed."
