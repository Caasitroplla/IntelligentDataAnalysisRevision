import randomGraph
import Dijkstra
import numpy as np
from typing import Dict, Any, List


def degreeCentrlity(graph: List[Any]):
    # Node with the most connections
    degree_centrality: Dict[Any, int] = {}
    for node in graph:
        degree_centrality[node] = int(node.degree)

    # Find the node with the maximum degree
    max_node = max(degree_centrality, key=lambda node: degree_centrality[node])
    return degree_centrality, max_node


def closenessCentrality(graph):
    # This measures which node is closest to all other nodes in the graph.
    sum_of_distances = {}
    for node in graph:
        for other_node in graph:
            if node != other_node:
                path, distance = Dijkstra.dijkstra(graph, node, other_node)
                if node not in sum_of_distances:
                    sum_of_distances[node] = 0
                sum_of_distances[node] += distance

    # Find the node with the minimum sum of distances
    min_node = min(sum_of_distances, key=lambda node: sum_of_distances[node])
    return min_node, sum_of_distances[min_node]


def betweennessCentrality(graph):
    # Most paths that go through a node
    betweenness_centrality = {}
    for node in graph:
        for other_node in graph:
            if node != other_node:
                path, distance = Dijkstra.dijkstra(graph, node, other_node)
                if path:
                    for n in path:
                        if n not in betweenness_centrality:
                            betweenness_centrality[n] = 0
                        if n != node and n != other_node:
                            betweenness_centrality[n] += 1

    # Find the node with the maximum betweenness
    max_node = max(betweenness_centrality, key=lambda node: betweenness_centrality[node])
    return betweenness_centrality, max_node



def eigenvectorCentrality(graph):
    # Turn graph into a matrix
    matrix = np.zeros((len(graph), len(graph)))
    for i, node in enumerate(graph):
        for j, other_node in enumerate(graph):
            if node in other_node.edges:
                matrix[i][j] = 1

    # Calculate the eigenvector centrality
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    idx = np.argmax(eigenvalues)

    centrality_vector = np.abs(eigenvectors[:, idx])

    centrality_vector = centrality_vector / np.sum(centrality_vector)

    # Find most central and return
    most_central = np.argmax(centrality_vector)
    return centrality_vector, most_central




if __name__ == "__main__":
    graph = randomGraph.generate_random_graph()

    res = closenessCentrality(graph)

    print(f"Node with the highest closeness centrality: {res[0]} with a score of {res[1]}")

    res = eigenvectorCentrality(graph)

    print(f"Node with the highest eigenvector centrality: {res[1]} with a score of {res[0][res[1]]}")

    res = degreeCentrlity(graph)

    print(f"Node with the highest degree centrality: {res[1]} with a score of {res[0][res[1]]}")

    res = betweennessCentrality(graph)

    print(f"Node with the highest betweenness centrality: {res[1]} with a score of {res[0][res[1]]}")
