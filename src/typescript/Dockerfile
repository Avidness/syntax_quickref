# Use the official Node.js image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy the TypeScript source code
COPY . .

# Install TypeScript globally
RUN npm install -g typescript

# Compile all TypeScript files
RUN tsc bfs.ts
#RUN tsc dfs.ts
#RUN tsc loops.ts
#RUN tsc array_mod.ts

# Ensure run_tests.sh is executable
RUN chmod +x /app/run_tests.sh

# Run the tests
CMD ["./run_tests.sh"]
