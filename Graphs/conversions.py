from typing import Any
import random

class Node:
    def __init__(self, value: Any):
        self.value = value
        self._edges = []

    def add_edge(self, node: "Node", weight: float = 1):
        if node not in self._edges:
            self._edges.append((node, weight))

    @property
    def edges(self) -> list["Node"]:
        return self._edges

    def __iter__(self):
        return iter(self._edges)

    def __str__(self) -> str:
        formatted_edges = []
        for edge in self._edges:
            edge_id = edge[0].value
            weight = edge[1]
            formatted_edges.append(f"{edge_id} (weight: {weight})")
        return f"Node {self.value} with edges: {formatted_edges}"


def class_to_matrix(graph: list["Node"]) -> list[list[float]]:
    """
    Convert a graph represented as a list of nodes to an adjacency matrix.
    """
    size = len(graph)
    matrix = [[float("inf")] * size for _ in range(size)]

    for i, node in enumerate(graph):
        for destination, weight in node.edges:
            j = graph.index(destination)
            matrix[i][j] = weight

    return matrix


def matrix_to_class(matrix: list[list[float]]) -> list["Node"]:
    """
    Convert an adjacency matrix back to a graph represented as a list of nodes.
    """
    size = len(matrix)
    nodes = [Node(i) for i in range(size)]

    for i in range(size):
        for j in range(size):
            if matrix[i][j] != float("inf") and i != j:
                nodes[i].add_edge(nodes[j], matrix[i][j])

    return nodes


def random_graph(size: int, weighted=False, directed=True) -> list["Node"]:
    """
    Generate a random graph with the specified number of nodes.
    """
    nodes = [Node(i) for i in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            if random.choice([True, False]):
                if not directed:
                    weight = random.randint(1, 9) if weighted else 1
                    nodes[i].add_edge(nodes[j], weight)
                    nodes[j].add_edge(nodes[i], weight)
                else:
                    weight = random.randint(1, 9) if weighted else 1
                    nodes[i].add_edge(nodes[j], weight)
                    nodes[j].add_edge(nodes[i], weight)

    return nodes


if __name__ == "__main__":
    # Example usage
    graph = random_graph(5, weighted=True)
    print("Original graph:")
    for node in graph:
        print(node)

    matrix = class_to_matrix(graph)
    print("\nAdjacency matrix:")

    for row in matrix:
        print(row)

    converted_graph = matrix_to_class(matrix)
    print("\nConverted graph:")

    for node in converted_graph:
        print(node)
