import randomGraph
from Dijkstra import dijkstra

def getDiameter(graph) -> int:
    # Calcualte paths from all nodes to all other nodes
    max_distance = 0
    for node in graph:
        for other_node in graph:
            if node != other_node:
                _, distance = dijkstra(graph, node, other_node)
                if distance > max_distance:
                    max_distance = distance

    return max_distance

if __name__ == "__main__":
    # Example usage
    graph = randomGraph.generate_random_graph()
    diameter = getDiameter(graph)
    print(f"Diameter of the graph: {diameter}")
