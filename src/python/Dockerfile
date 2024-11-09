# Use the official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy the Python source code
COPY . .

# Install dependencies if needed (e.g., pytest)
RUN pip install -r requirements.txt || true

# Ensure run_tests.sh is executable
RUN chmod +x /app/run_tests.sh

# Run the tests
CMD ["./run_tests.sh"]
