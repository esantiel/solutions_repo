import networkx as nx

def calculate_equivalent_resistance(G, start_node, end_node):
    """
    Calculate the equivalent resistance between start_node and end_node in graph G.
    G: NetworkX graph with edges having 'resistance' attribute.
    Returns: Equivalent resistance (float).
    """
    # Make a copy to avoid modifying the original graph
    G = G.copy()

    # Continue simplifying until only start_node and end_node remain with one edge
    while len(G.nodes) > 2 or (len(G.nodes) == 2 and len(G.edges) > 1):
        # 1. Series reduction: Find nodes with degree 2
        series_reduced = False
        for node in list(G.nodes):
            if node in [start_node, end_node]:
                continue
            if G.degree(node) == 2:
                neighbors = list(G.neighbors(node))
                u, v = neighbors
                # Get resistances
                r1 = G[u][node]['resistance']
                r2 = G[node][v]['resistance']
                # Add new edge with combined resistance
                G.add_edge(u, v, resistance=r1 + r2)
                # Remove the intermediate node
                G.remove_node(node)
                series_reduced = True
                break

        if series_reduced:
            continue

        # 2. Parallel reduction: Find pairs of nodes with multiple edges
        parallel_reduced = False
        for u, v in G.edges():
            if G.number_of_edges(u, v) > 1:
                # Get all edges between u and v
                edges = G.get_edge_data(u, v)
                resistances = [data['resistance'] for data in edges.values()]
                # Calculate equivalent resistance for parallel
                inv_r_eq = sum(1/r for r in resistances)
                r_eq = 1 / inv_r_eq
                # Remove all edges between u and v
                G.remove_edges_from([(u, v)] * len(resistances))
                # Add single edge with equivalent resistance
                G.add_edge(u, v, resistance=r_eq)
                parallel_reduced = True
                break

        if not (series_reduced or parallel_reduced):
            raise ValueError("Graph cannot be reduced further; possible complex configuration not handled.")

    # Final check: Should have one edge between start_node and end_node
    if len(G.edges) != 1 or not G.has_edge(start_node, end_node):
        raise ValueError("Reduction failed: Expected one edge between start and end nodes.")
    
    return G[start_node][end_node]['resistance']

# Test cases
def create_test_graphs():
    # Test 1: Simple Series (R1 = 2Ω, R2 = 3Ω)
    G1 = nx.MultiGraph()
    G1.add_edge(0, 1, resistance=2)
    G1.add_edge(1, 2, resistance=3)
    print("Test 1: Simple Series (2Ω + 3Ω)")
    print("Expected: 5Ω")
    print("Calculated:", calculate_equivalent_resistance(G1, 0, 2))

    # Test 2: Simple Parallel (R1 = 2Ω, R2 = 2Ω)
    G2 = nx.MultiGraph()
    G2.add_edge(0, 1, resistance=2)
    G2.add_edge(0, 1, resistance=2)
    print("\nTest 2: Simple Parallel (2Ω || 2Ω)")
    print("Expected: 1Ω")
    print("Calculated:", calculate_equivalent_resistance(G2, 0, 1))

    # Test 3: Nested Configuration (Series of two parallel pairs)
    # (R1 = 2Ω || R2 = 2Ω) in series with (R3 = 4Ω || R4 = 4Ω)
    G3 = nx.MultiGraph()
    G3.add_edge(0, 1, resistance=2)  # R1
    G3.add_edge(0, 1, resistance=2)  # R2
    G3.add_edge(1, 2, resistance=4)  # R3
    G3.add_edge(1, 2, resistance=4)  # R4
    print("\nTest 3: Nested (2Ω || 2Ω) + (4Ω || 4Ω)")
    print("Expected: 1Ω + 2Ω = 3Ω")
    print("Calculated:", calculate_equivalent_resistance(G3, 0, 2))

# Run tests
if __name__ == "__main__":
    create_test_graphs()