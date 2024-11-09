import * as fs from 'fs';

class Queue<T> {
    private items: T[] = [];

    enqueue(item: T): void {
        this.items.push(item);
    }

    dequeue(): T | undefined {
        return this.items.shift();
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }
}

class Graph {
    private adjList: { [key: string]: string[] } = {};

    addEdge(src: string, dest: string): void {
        if (!this.adjList[src]) {
            this.adjList[src] = [];
        }
        this.adjList[src].push(dest);
    }

    bfs(startNode: string): string[] {
        const queue = new Queue<string>();
        const visited = new Set<string>();
        const bfsOrder: string[] = [];

        queue.enqueue(startNode);
        visited.add(startNode);

        while (!queue.isEmpty()) {
            const node = queue.dequeue()!;
            bfsOrder.push(node);

            if (this.adjList[node]) {
                for (const neighbor of this.adjList[node]) {
                    if (!visited.has(neighbor)) {
                        visited.add(neighbor);
                        queue.enqueue(neighbor);
                    }
                }
            }
        }

        return bfsOrder;
    }

    static readGraphFromFile(filePath: string): { graphInstance: Graph, startNode: string } {
        const data = fs.readFileSync(filePath, 'utf8');
        const { graph, start_node: startNode } = JSON.parse(data);
        const graphInstance = new Graph();

        for (const src in graph) {
            for (const dest of graph[src]) {
                graphInstance.addEdge(src, dest);
            }
        }

        return { graphInstance, startNode };
    }

    static writeBFSOrderToFile(filePath: string, bfsOrder: string[]): void {
        const outputData = { bfs_order: bfsOrder };
        fs.writeFileSync(filePath, JSON.stringify(outputData, null, 4), 'utf8');
    }
}

// Main function to perform BFS using the Graph class
function main() {
    if (process.argv.length !== 4) {
        console.error("Usage: ts-node bfs.ts <input_file> <output_file>");
        process.exit(1);
    }

    const inputFilePath = process.argv[2];
    const outputFilePath = process.argv[3];

    // Read graph and start node from input file
    const { graphInstance, startNode } = Graph.readGraphFromFile(inputFilePath);

    // Perform BFS
    const bfsOrder = graphInstance.bfs(startNode);

    // Write the BFS traversal order to the output file
    Graph.writeBFSOrderToFile(outputFilePath, bfsOrder);

    console.log("BFS traversal completed.");
}

// Run the main function
main();
