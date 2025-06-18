import matplotlib.pyplot as plt
import networkx as nx
import heapq

# 1. Створюємо зважений граф
WG = nx.Graph()

# Ваги представляють час подорожі
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

# 2. Візуалізація
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color="lightgreen", node_size=1000, font_size=15)
labels = nx.get_edge_attributes(WG, 'weight')
nx.draw_networkx_edge_labels(WG, pos, edge_labels=labels)
plt.title("City Transportation Network (Weighted)")
plt.show()


# 3. Реалізація алгоритму Дейкстри вручну 
def dijkstra(graph, start):
    # Ініціалізація відстаней: безкінечність до всіх, окрім стартової
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    # Ініціалізація попередників для побудови шляху
    previous = {node: None for node in graph.nodes}

    # Пріоритетна черга: (відстань, вузол)
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Якщо знайшли коротший шлях до сусідів
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous


# 4. Вивід найкоротшого шляху від A до G
def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]
    if path[0] == start:
        return path
    else:
        return []

# Виконання
start_node = "A"
end_node = "G"
distances, previous = dijkstra(WG, start_node)
path = reconstruct_path(previous, start_node, end_node)

print(f"Shortest path from {start_node} to {end_node}:", path)
print("Total travel time:", distances[end_node])
