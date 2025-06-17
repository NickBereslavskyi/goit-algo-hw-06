import networkx as nx
import matplotlib.pyplot as plt

# Task 1: Create and Analyze the Graph

# Create the graph (city transportation network)
G = nx.Graph()

# Add nodes
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G"])

# Add edges (connections between stations)
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "F"),
    ("F", "G")
]
G.add_edges_from(edges)

# Visualize the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1000, font_size=15)
plt.title("City Transportation Network (Unweighted)")
plt.show()

# Analyze the graph
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Degrees:", dict(G.degree()))