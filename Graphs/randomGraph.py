import random


# Random graph generator
class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)
            node.add_edge(self)

    def __repr__(self):
        return f"Node({self.id})"

    @property
    def degree(self) -> int:
        return len(self.edges)



# Random graph generator
def generate_random_graph() -> list:
    graph = [
        Node(i) for i in range(10)
    ]
    # Adding random edges
    for _ in range(30):
        node1 = random.choice(graph)
        node2 = random.choice(graph)
        if node1 != node2:
            node1.add_edge(node2)

    return graph


# Random undirected graph generator
def generate_random_undirected_graph(num_nodes: int, num_edges: int) -> list:
    graph = [Node(i) for i in range(num_nodes)]
    edges = set()
    while len(edges) < num_edges:
            node1 = random.choice(graph)
            node2 = random.choice(graph)
            if node1 != node2 and (node1, node2) not in edges and (node2, node1) not in edges:
                node1.add_edge(node2)
                edges.add((node1, node2))

    return graph
