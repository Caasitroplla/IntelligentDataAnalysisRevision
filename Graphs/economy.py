import randomGraph
import Dijkstra

def getEdges(graph):
    edges = 0
    for node in graph:
        edges += len(node.edges)
    return edges

def getEfficiency(graph):
    # Calculate the global efficiency of the graph
    a = 1 / (len(graph) * (len(graph) - 1))
    b = 0
    for node in graph:
        for other_node in graph:
            if node != other_node:
                _, distance = Dijkstra.dijkstra(graph, node, other_node)
                if distance != float('inf'):
                    b += 1 / distance

    efficiency = a * b
    return efficiency

def economy(graph):
    # Define the minimum cost keeping all nodes connected
    min_cost = len(graph) - 1
    cost = getEdges(graph)
    normalised_cost = cost / min_cost

    # Calculate the global efficiency
    efficiency = getEfficiency(graph)

    # Calculate the ideal efficiency, ideal - every node is connected to every other node
    min_efficiency = 1 / (len(graph) - 1)
    normalised_efficiency = efficiency / min_efficiency

    return normalised_cost, normalised_efficiency


if __name__ == "__main__":
    graph = randomGraph.generate_random_graph()
    cost, efficiency = economy(graph)
    print(f"Normalised cost: {cost}")
    print(f"Normalised efficiency: {efficiency}")
