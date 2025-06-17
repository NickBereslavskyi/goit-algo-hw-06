import networkx as nx
from collections import deque

# Create the same graph as Task 1
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G"])
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

# DFS (Depth-First Search)
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))

dfs_paths = list(dfs(G, "A", "G"))
print("DFS paths from A to G:", dfs_paths)

# BFS (Breadth-First Search)
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))

bfs_paths = list(bfs(G, "A", "G"))
print("BFS paths from A to G:", bfs_paths)