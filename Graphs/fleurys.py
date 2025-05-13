import random
import randomGraph

def fleurys(graph):
    # Check is it has either 0 or 2 odd vertices
    odd_vertices = [node for node in graph if node.degree % 2 == 1]

    # Set start node
    if len(odd_vertices) == 0:
        current_node = graph[0]
    else:
        current_node = odd_vertices[0]

    # Follow edges one at a time
    path = []
    while True:
        # Check if current node has edges
        if not current_node.edges:
            break

        # Evaluate all possible next edges
        for edge in current_node.edges:
            # Check if edge not a bridge
            if edge not in path:
                path.append(edge)
                current_node = edge
                break

        else:
            # If all edges are bridges, choose one at random
            edge = random.choice(current_node.edges)
            path.append(edge)
            current_node = edge
            break

    return path

# Example usage
if __name__ == "__main__":
    graph = randomGraph.generate_random_undirected_graph(10, 20)
    path = fleurys(graph)
    print(f"Eulerian path: {path}")
