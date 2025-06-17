import networkx as nx
import matplotlib.pyplot as plt

# Create weighted graph
WG = nx.Graph()

# Add weighted edges
weighted_edges = [
    ("A", "B", 5),
    ("A", "C", 3),
    ("B", "D", 4),
    ("C", "D", 2),
    ("C", "E", 6),
    ("D", "F", 3),
    ("E", "F", 1),
    ("F", "G", 2)
]
WG.add_weighted_edges_from(weighted_edges)

# Visualize weighted graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color="lightgreen", node_size=1000, font_size=15)
labels = nx.get_edge_attributes(WG, 'weight')
nx.draw_networkx_edge_labels(WG, pos, edge_labels=labels)
plt.title("City Transportation Network (Weighted)")
plt.show()

# Find shortest path with Dijkstra
path = nx.dijkstra_path(WG, source="A", target="G")
length = nx.dijkstra_path_length(WG, source="A", target="G")
print("Dijkstra shortest path from A to G:", path)
print("Total travel time:", length)