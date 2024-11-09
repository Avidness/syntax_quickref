import json
import sys
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = []
        self.adj_list[src].append(dest)

    def bfs(self, start_node):
        queue = deque([start_node])
        visited = set([start_node])
        bfs_order = []

        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_order

    @staticmethod
    def read_graph_from_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            graph_data = data["graph"]
            start_node = data["start_node"]

            graph = Graph()
            for src, neighbors in graph_data.items():
                for dest in neighbors:
                    graph.add_edge(src, dest)

            return graph, start_node

    @staticmethod
    def write_bfs_order_to_file(file_path, bfs_order):
        output_data = {"bfs_order": bfs_order}
        with open(file_path, 'w') as file:
            json.dump(output_data, file, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: python bfs.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read graph and start node from input file
    graph, start_node = Graph.read_graph_from_file(input_file)

    # Perform BFS
    bfs_order = graph.bfs(start_node)

    # Write the BFS traversal order to the output file
    Graph.write_bfs_order_to_file(output_file, bfs_order)

    print("BFS traversal completed.")

if __name__ == "__main__":
    main()
