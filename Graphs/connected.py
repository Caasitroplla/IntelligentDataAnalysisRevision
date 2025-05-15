from typing import Any
import random

class Node:
    def __init__(self, value: Any):
        self.value = value
        self._edges = []

    def add_edge(self, node: "Node"):
        if node not in self._edges:
            self._edges.append(node)

    @property
    def edges(self) -> list["Node"]:
        return self._edges


def depth_first_search(node: Node, visited: set[Node]):
    """
    Perform a depth-first search on the graph.
    """
    visited.add(node)
    for neighbor in node.edges:
        if neighbor not in visited:
            depth_first_search(neighbor, visited)

def is_connected(graph: list["Node"]) -> bool:
    """
    Check if the graph is connected.
    """
    visited = set()
    depth_first_search(graph[0], visited)
    return len(visited) == len(graph)

# Generate a random graph with the specified size.
if __name__ == "__main__":
    # Example usage
    graph = [Node(i) for i in range(100)]
    for i in range(100):
        for j in range(i + 1, 100):
            if random.choice([True, False]):
                graph[i].add_edge(graph[j])
                graph[j].add_edge(graph[i])

    print("Graph is connected:", is_connected(graph))

    # Add 1 node that is not connected
    disconnected_node = Node(100)
    graph.append(disconnected_node)
    print("Graph is connected after adding a disconnected node:", is_connected(graph))
