﻿# goit-algo-hw-06

## Task 1

We modeled a real-world city transportation network using the `networkx` library.  
The graph consists of 7 nodes representing stations and 8 edges representing direct connections.

- Number of nodes: 7
- Number of edges: 8
- Degree of nodes:

| Node | Degree |
|------|--------|
| A    | 2      |
| B    | 2      |
| C    | 3      |
| D    | 3      |
| E    | 2      |
| F    | 3      |
| G    | 1      |

The graph was visualized using `matplotlib`.

## Task 2

We implemented both DFS (Depth-First Search) and BFS (Breadth-First Search) algorithms to search for paths from node A to node G.

- DFS returned all possible paths it could find (depending on traversal order).
- BFS returned the shortest path in terms of the number of edges.

**Difference explanation:**
- BFS always finds the shortest path in terms of number of steps because it explores neighbors level-by-level.
- DFS may find longer paths as it explores one branch deeply before backtracking.

## Task 3: Dijkstra's Algorithm (Manual Implementation)

To find the shortest path in a **weighted graph**, we implemented **Dijkstra’s algorithm manually**, without using NetworkX built-in functions.

### Features of the Implementation:

- Used a priority queue (`heapq`) to select the node with the smallest tentative distance.
- Tracked distances and previous nodes.
- Reconstructed the shortest path manually from the `previous` dictionary.

### Result:

- **Shortest path from A to G**:  
  `['A', 'C', 'D', 'F', 'G']`
- **Total travel time**:  
  `10` (sum of weights along the shortest path)

### Why manual implementation?

Although built-in algorithms are reliable and efficient, writing the algorithm from scratch helped understand:

- How the shortest paths are calculated step-by-step
- The importance of using a priority queue to optimize performance
- Path reconstruction logic via backtracking from destination

---

## Technologies used

- Python 3
- networkx
- matplotlib
