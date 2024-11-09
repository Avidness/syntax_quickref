# Use the official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy the JavaScript source code
COPY . .

# Install dependencies if any (for example, Jest for testing if needed)
RUN npm install

# Ensure run_tests.sh is executable
RUN chmod +x /app/run_tests.sh

# Run the tests
CMD ["./run_tests.sh"]
