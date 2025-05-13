from randomGraph import Node
import random

def dijkstra(graph, start, goal) -> tuple:
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    previous = {node: None for node in graph}
    unvisited = set(graph)

    while unvisited:
        # Select the unvisited node with the smallest distance
        current = min(unvisited, key=lambda node: distance[node])
        if distance[current] == float('inf'):
            break # All remaining nodes are unreachable

        unvisited.remove(current)

        if current == goal:
            break

        for neighbor in current.edges:
            if neighbor in unvisited:
                new_distance = distance[current] + 1
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    previous[neighbor] = current


    # Reconstruct the shortest path
    path = []
    current = goal
    while current:
        path.insert(0, current)
        current = previous[current]
    return path, distance[goal]





# Example usage
if __name__ == "__main__":
    graph = [
        Node(i) for i in range(10)
    ]
    # Adding random edges
    for _ in range(30):
        node1 = random.choice(graph)
        node2 = random.choice(graph)
        if node1 != node2:
            node1.add_edge(node2)


    start_node = random.choice(graph)
    goal_node = random.choice(graph)
    solution = dijkstra(graph, start_node, goal_node)
    print(f"Shortest path from {start_node} to {goal_node}: {solution}")
