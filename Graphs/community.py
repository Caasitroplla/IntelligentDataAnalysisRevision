import randomGraph
from centrality import betweennessCentrality
from copy import deepcopy

# Function to evaluate modularity of a graph given community assignments
def modularity(graph, communities) -> float:
    m = sum(node.degree for node in graph) / 2
    Q = 0.0
    for node in graph:
        for neighbor in node.edges:
            if communities[node] == communities[neighbor]:
                Q += 1 - (node.degree * neighbor.degree) / (2 * m)
    return Q / (2 * m) if m > 0 else 0


# Louvain method for community detection
def louvain(graph):
    # Step 1: Assign each node to its own community
    communities = {node: i for i, node in enumerate(graph)}
    node_to_comm = {node: i for i, node in enumerate(graph)}
    current_modularity = modularity(graph, communities)
    improvement = True

    while improvement:
        improvement, communities, current_modularity = move_nodes_to_best_communities(graph, communities, current_modularity)
        if improvement:
            graph, communities, current_modularity, node_to_comm = aggregate_communities(graph, communities, node_to_comm)

    # Return final communities as a mapping from original node to community id
    return node_to_comm

def move_nodes_to_best_communities(graph, communities, current_modularity):
    improvement = False
    for node in graph:
        node_community = communities[node]
        best_community = node_community
        best_gain = 0
        for neighbor in node.edges:
            target_community = communities[neighbor]
            if target_community == node_community:
                continue
            # Move node to neighbor's community
            communities[node] = target_community
            new_modularity = modularity(graph, communities)
            gain = new_modularity - current_modularity
            if gain > best_gain:
                best_gain = gain
                best_community = target_community
            # Restore
            communities[node] = node_community
        # Move node to the best community if gain is positive
        if best_community != node_community and best_gain > 0:
            communities[node] = best_community
            current_modularity += best_gain
            improvement = True
    return improvement, communities, current_modularity

def aggregate_communities(graph, communities, node_to_comm):
    # Aggregate communities into super-nodes
    comm_to_nodes = {}
    for node, comm in communities.items():
        comm_to_nodes.setdefault(comm, []).append(node)
    # Build new nodes (super-nodes)
    new_nodes = []
    comm_map = {}
    for new_comm_id, (comm, nodes) in enumerate(comm_to_nodes.items()):
        super_node = SuperNode(nodes)
        new_nodes.append(super_node)
        for node in nodes:
            comm_map[node] = super_node
            # Update all original nodes in this supernode to new_comm_id
            if hasattr(node, 'nodes'):
                for orig_node in node.nodes:
                    node_to_comm[orig_node] = new_comm_id
            else:
                node_to_comm[node] = new_comm_id
    # Add edges between super-nodes
    for super_node in new_nodes:
        super_node.edges = []
    for node in graph:
        for neighbor in node.edges:
            if comm_map[node] != comm_map[neighbor]:
                if comm_map[neighbor] not in comm_map[node].edges:
                    comm_map[node].edges.append(comm_map[neighbor])
    # Prepare for next iteration
    graph = new_nodes
    communities = {node: i for i, node in enumerate(graph)}
    current_modularity = modularity(graph, communities)
    return graph, communities, current_modularity, node_to_comm


# Helper class for super-nodes (aggregated communities)
class SuperNode:
    def __init__(self, nodes):
        self.nodes = nodes  # List of original nodes
        self.edges = []

    @property
    def degree(self):
        return sum(node.degree for node in self.nodes)

    def __repr__(self):
        return f"SuperNode({[node.id for node in self.nodes]})"


def edges(graph):
    edges = 0
    for node in graph:
        edges += len(node.edges)

    return edges // 2  # Each edge is counted twice in an undirected graph


# Girvan-Newman method for community detection
def girvanNewman(graph):
    dendrogram_components = []
    working_graph = deepcopy(graph)
    max_iterations = 1000  # safeguard

    for _ in range(max_iterations):
        if edges(working_graph) < 1:
            break

        # Calculate betweenness centrality
        centrality = betweennessCentrality(working_graph)[0]
        # Find the edge with the highest betweenness
        max_node = max(centrality, key=lambda node: centrality[node])
        if not max_node.edges:
            break
        # Remove one edge with highest betweenness
        neighbor = max_node.edges[0]
        max_node.edges.remove(neighbor)
        neighbor.edges.remove(max_node)

        # Check for connected components
        components = get_connected_components(working_graph)
        if len(components) > 1:
            dendrogram_components = components
            break

    return dendrogram_components

def get_connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = []
            queue = [node]
            while queue:
                current = queue.pop()
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    queue.extend([n for n in current.edges if n not in visited])
            components.append(component)
    return components


if __name__ == "__main__":
    graph = randomGraph.generate_random_undirected_graph(10, 20)
    # Modularity of standard graph (all nodes in their own community)
    print("Modularity of the graph (each node its own community):", modularity(graph, {node: i for i, node in enumerate(graph)}))

    # Example usage
    print("Louvain method for community detection:")
    res = louvain(graph)
    for node, community in res.items():
        print(f"Node {node.id} is in community {community}")

    print("Girvan-Newman method for community detection:")
    res = girvanNewman(graph)
    for i, component in enumerate(res):
        print(f"Component {i}: {[node.id for node in component]}")
