# Graphs — Python

V = vertices; E = edges; R and C = grid dimensions; α = inverse Ackermann function. Recursive alternatives can exceed Python recursion limits or Java stack depth on long paths; use the iterative alternative where supplied.

Video series and approaches follwed - https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

## BFS and connected components

### 1. ★ BFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

BFS visits nodes level by level, using a queue. Mark each node visited when adding it to the queue to prevent duplicates.

**Input/Output**

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,2,3]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 2. ★ Find if Path Exists in Graph — 1971

[LeetCode/GFG Link](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Check whether source can reach destination in an undirected graph with vertices 0 through n − 1.

**Input/Output**

```text
Input: n = 3, edges = [[0,1],[1,2]], source = 0, destination = 2
Output: true
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 3. ★ Clone Graph — 133

[LeetCode/GFG Link](https://leetcode.com/problems/clone-graph/)

Given a node in a connected undirected graph, return a deep copy of the graph. Every cloned node must be a new object with the same value and corresponding cloned neighbors.

**Input/Output**

```text
Input: Adjacency list: [[2],[1]] (node values are 1 and 2)
Output: A new graph with adjacency list [[2],[1]], sharing no nodes with the input
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V) auxiliary for the map and queue, plus O(V + E) for the cloned output graph.

### 4. ★ Keys and Rooms — 841

[LeetCode/GFG Link](https://leetcode.com/problems/keys-and-rooms/)

Visit room 0 and follow its keys to other rooms. Return whether every room can be reached. Use iterative DFS; each room is processed once.

**Input/Output**

```text
Input: rooms = [[1],[2],[3],[]]
Output: true
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input; E is the total number of keys.

### 5. ★ Number of Connected Components in an Undirected Graph — 323

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Count connected components, including isolated vertices, in an undirected graph.

**Input/Output**

```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 6. ★ Number of Provinces — 547

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-provinces/)

Count connected groups in a symmetric n × n adjacency matrix. Scan each undirected connection once and merge its components.

**Input/Output**

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(n² × α(n))
- **Space:** O(n) auxiliary for DSU; the input matrix is excluded.

### 7. ★ Rotting Oranges — 994

[LeetCode/GFG Link](https://leetcode.com/problems/rotting-oranges/)

Spread rot from all rotten oranges simultaneously in a nonempty grid. Return minutes until all fresh oranges rot, or −1. Updates the grid.

**Input/Output**

```text
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the BFS queue.

### 8. ★ 01 Matrix — 542

[LeetCode/GFG Link](https://leetcode.com/problems/01-matrix/)

Find each cell’s distance to its nearest 0 using multi-source BFS. The nonempty binary matrix contains at least one 0.

**Input/Output**

```text
Input: mat = [[0,1,1],[1,1,1]]
Output: [[0,1,2],[1,2,3]]
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C), including the distance matrix and BFS queue.

### 9. ★ Shortest Bridge — 934

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-bridge/)

Given exactly two 4-connected islands, return the fewest water cells to flip to connect them. Mark one island, then expand it by BFS. Updates the grid.

**Input/Output**

```text
Input: grid = [[0,1],[1,0]]
Output: 1
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack and BFS queue.

### 10. ★ DFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

DFS explores one branch as deeply as possible before backtracking. Start from vertex 0 and follow adjacency-list order.

**Input/Output**

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,3,2]
```

**Code**


**Time Space Complexity**

- **Time:**
- Each vertex is visited at most once: O(V).
- Each visited vertex scans its adjacency list. Across the graph, that is E entries for a directed graph, or 2E for an undirected graph so ~ O(E).
- Assuming average O(1) set operations, total time is O(V + E).
- The neighbor loop scans only its node’s neighbors.
- **Space:**
- Visited can contain V vertices: O(V).
- A graph can produce V active recursive calls: O(V).
- result can contain V vertices: O(V) output space.
- Auxiliary space is O(V). Including the output, it remains O(V).

## Grid traversal

### 11. ★ Number of Islands — 200

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

**Input/Output**

```text
Input: grid = [["1","1","0"],["0","0","1"]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 12. ★ Flood Fill — 733

[LeetCode/GFG Link](https://leetcode.com/problems/flood-fill/)

Recolor the 4-connected component containing (sr, sc) in a nonempty image. Updates the image in place.

**Input/Output**

```text
Input: image = [[1,1],[1,0]], sr = 0, sc = 0, color = 2
Output: [[2,2],[2,0]]
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 13. ★ Max Area of Island — 695

[LeetCode/GFG Link](https://leetcode.com/problems/max-area-of-island/)

Return the largest 4-connected area of 1s in a nonempty binary grid. Visited land is changed to 0.

**Input/Output**

```text
Input: grid = [[1,1,0],[1,0,1]]
Output: 3
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 14. ★ Surrounded Regions — 130

[LeetCode/GFG Link](https://leetcode.com/problems/surrounded-regions/)

Flip enclosed 'O' regions to 'X' in place. First preserve all 'O' cells connected to the boundary of the nonempty board.

**Input/Output**

```text
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","O","X","X"]]
Output: board becomes [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]; no return value
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS recursion stack.

### 15. ★ Pacific Atlantic Water Flow — 417

[LeetCode/GFG Link](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Find cells from which water reaches both oceans. Search backward from ocean boundaries to equal or higher cells in the nonempty height grid.

**Input/Output**

```text
Input: heights = [[1,2],[4,3]]
Output: [[0,1],[1,0],[1,1]] (any order)
```

**Code**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C)

## Cycle detection

### 16. ★ Detect Cycle in an Undirected Graph — BFS and DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

Detect a cycle in any component of an undirected graph. Input edges use vertices 0 through V − 1; edge IDs distinguish parallel edges. Mark vertices when scheduling them. Ignore only the edge used to enter the current vertex; another edge to a seen vertex proves a cycle. Both BFS and DFS are included.

The rule is: process a node only when it has no incoming edges left.

Indegree means the number of incoming edges to a node. In Course Schedule, it represents how many prerequisites remain.

**Input/Output**

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

**Code**

**BFS**



### 17. ★ Detect Cycle in a Directed Graph — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using DFS states: 0 = unvisited, 1 = active, 2 = completed. An edge to an active node proves a cycle. Explicit stack frames avoid recursion depth limits.

**Input/Output**

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V)

## Kahn’s Algorithm

### 18. ★ Detect Cycle in a Directed Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Kahn’s algorithm is a BFS-based way to put the nodes of a directed graph in dependency order, called a topological order.

The rule is: process a node only when it has no incoming edges left.

Indegree means the number of incoming edges to a node. In Course Schedule, it represents how many prerequisites remain.

**Input/Output**

```text
Input: edges = [[0,1],[1,2],[2,0]]
Output: true
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E)

### 19. ★ Course Schedule — 207

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule/)

Determine whether all courses can be completed. Each prerequisite pair is [course, prerequisite].

**Input/Output**

```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 20. ★ Find Eventual Safe States — 802

[LeetCode/GFG Link](https://leetcode.com/problems/find-eventual-safe-states/)

Return sorted vertices whose every path eventually terminates. Start with terminal vertices and remove edges in the reversed graph.

**Input/Output**

```text
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the reversed graph.

## Bipartite graphs

A bipartite graph is a graph whose nodes have 2 different colors, or you can assign 2 diff colors to the adjcent nodes.
Thus dividing the graph in 2 groups where no edges are interconnected within same group.

                                                                     6 - 8
Observations:-                                                      /     \
- Linear graphs with no cycles are always Bipartite, 1 -> 2-> 4 -> 5      10
                                                                    \
                                                                     7 - 9
- Any graph with even cycle **length** is also bipartite.


### 21. ★ Is Graph Bipartite? — 785

[LeetCode/GFG Link](https://leetcode.com/problems/is-graph-bipartite/)

Check whether an undirected adjacency-list graph can be colored with two colors. Covers disconnected components.

**Input/Output**

```text
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
```

**Code**

1. **Two-Coloring Test:** Try to color every vertex using any two colors (e.g., Red and Blue) so that no two adjecent connected vertices share the same color. If you can do it, it is bipartite. (BFS Approach)


2. **Odd Cycle Check:** If the graph contains a loop (cycle) with an odd number of edges/vertices, it is not bipartite. (DFS Approach)


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list; includes recursion stack for DFS.


### 22. ★ Possible Bipartition — 886

[LeetCode/GFG Link](https://leetcode.com/problems/possible-bipartition/)

Split people labeled 1 through n into two groups so every disliked pair is separated. Build an undirected graph and two-color it.

**Input/Output**

```text
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## Topological sorting

Topological sort is used when tasks have dependencies and you need a valid order to complete them.
For example, suppose you’re building an application:
| Task | Must happen first |
|---|---|
| `0`: Create database | Nothing |
| `1`: Build API | Create database |
| `2`: Prepare test data | Create database |
| `3`: Run integration tests | Build API and prepare test data |
The dependency edges are:
0 → 1
0 → 2
1 → 3
2 → 3

Topological sort gives a valid execution order:
Create database → Build API → Prepare test data → Run integration tests

### 23. ★ Topological Sort — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,2,1,3] (one valid order)
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E)

### 24. ★ Topological Sort — Kahn’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

Return a valid ordering of vertices in a directed acyclic graph given V and edges. Returns an empty array/list if a cycle exists.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,1,2,3] (one valid order)
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 25. ★ Course Schedule II — 210

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule-ii/)

Return a valid course order, or an empty array/list when a cycle makes completion impossible.

**Input/Output**

```text
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] (one valid order)
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 26. ★ Alien Dictionary — 269

[LeetCode/GFG Link](https://leetcode.com/problems/alien-dictionary/)

Infer any valid ordering of the lowercase letters appearing in sorted alien words. Return an empty string for a cycle or invalid prefix order. LeetCode 269 is Premium. The workbook method is named findOrder.

**Input/Output**

```text
Input: words = ["za","zb","ca","cb"]
Output: "zacb" (one valid order; z before c and a before b)
```

**Code**


**Time Space Complexity**

- **Time:** O(S + A + E), where S is total input characters, A distinct letters, and E distinct ordering constraints.
- **Space:** O(A + E), excluding input word storage.

### 27. ★ Find All Possible Recipes from Given Supplies — 2115

[LeetCode/GFG Link](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)

Process supplies as available nodes. Each ingredient unlocks dependent recipes by reducing their remaining ingredient count. Enqueue a recipe when all its ingredients are available; cyclic or missing dependencies remain unresolved. Supplies are unlimited.

**Input/Output**

```text
Input: recipes = ["tea","combo"], ingredients = [["water","leaf"],["tea","bread"]], supplies = ["water","leaf","bread"]
Output: ["tea","combo"]
```

**Code**


**Time Space Complexity**

- **Time:** O(N + I + S) expected hash-table operations; N = recipes, I = ingredient occurrences, S = supplies. String hashing additionally depends on string lengths.
- **Space:** O(N + I + S).

## Unweighted shortest paths and state-based BFS

### 28. ★ Shortest Path in an Undirected Graph with Unit Weights

[LeetCode/GFG Link](https://www.geeksforgeeks.org/dsa/shortest-path-in-undirected-graph-having-unit-distance/)

Find distances from src in an undirected, unweighted graph with V vertices. Return −1 for unreachable vertices.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[1,2]], src = 0
Output: [0,1,2,-1]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 29. ★ Shortest Path in Binary Matrix — 1091

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

Find the shortest 8-directional path of 0s from top-left to bottom-right in an n × n grid. Count visited cells; return −1 if impossible. Updates the grid.

**Input/Output**

```text
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n²) for the BFS queue.

### 30. ★ Word Ladder — 127

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

**Input/Output**

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

**Code**


**Time Space Complexity**

- **Time:** O((N + 1) × 26 × L²), including string construction/hashing; N = dictionary size.
- **Space:** O((N + 1) × L), for dictionary/queue strings of length L; N = dictionary size.

### 31. ★ Open the Lock — 752

[LeetCode/GFG Link](https://leetcode.com/problems/open-the-lock/)

Find the minimum wheel turns from 0000 to target while avoiding deadends; return −1 if impossible. Each state has four decimal digits.

**Input/Output**

```text
Input: deadends = [], target = "0009"
Output: 1
```

**Code**


**Time Space Complexity**

- **Time:** O(D + 10⁴ × 8) for four fixed digits; D = number of deadends.
- **Space:** O(D + 10⁴) for fixed four-digit states; D = deadends.

### 32. ★ Snakes and Ladders — 909

[LeetCode/GFG Link](https://leetcode.com/problems/snakes-and-ladders/)

Use BFS over square numbers to find the minimum dice rolls from 1 to n². Convert each square to its boustrophedon board coordinate. Follow at most one snake or ladder per roll; return −1 if the target is unreachable.

**Input/Output**

```text
Input: board = [[-1,-1],[-1,-1]]
Output: 1
```

**Code**


**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n²).

## Weighted shortest paths

### 33. ★ Dijkstra’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1)

Find shortest distances from src in an undirected graph with nonnegative edge weights. Edges are [u, v, weight]; unreachable vertices return −1.

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,9]], src = 0
Output: [0,4,6]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E log(E + 2)) with a heap that can retain outdated entries.
- **Space:** O(V + E), including the adjacency list and heap with outdated entries.

### 34. ★ Network Delay Time — 743

[LeetCode/GFG Link](https://leetcode.com/problems/network-delay-time/)

Find when all nodes receive a signal from k, or −1 if some cannot. Directed edges times use labels 1 through n and nonnegative travel times.

**Input/Output**

```text
Input: times = [[1,2,2],[2,3,1]], n = 3, k = 1
Output: 3
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 35. ★ Path With Minimum Effort — 1631

[LeetCode/GFG Link](https://leetcode.com/problems/path-with-minimum-effort/)

Minimize the largest absolute height difference along a 4-directional path from top-left to bottom-right in a nonempty grid.

**Input/Output**

```text
Input: heights = [[1,3],[2,4]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(RC log(RC + 1))
- **Space:** O(R × C) for distances and the heap (a grid has O(R × C) edges).

### 36. ★ Cheapest Flights Within K Stops — 787

[LeetCode/GFG Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest route from src to dst using at most k stops (k + 1 edges). Each relaxation round reads only the previous round’s distances.

**Input/Output**

```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
```

**Code**


**Time Space Complexity**

- **Time:** O((k + 1) × (V + E))
- **Space:** O(V) for two distance arrays.

### 37. ★ Bellman–Ford Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1)

Find distances from src in a directed graph with negative weights allowed. Return [-1] for a reachable negative cycle; use 100000000 for unreachable vertices (GFG convention).

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,-2],[0,2,5]], src = 0
Output: [0,4,2]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 38. ★ Negative Cycle Detection

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1)

Detect a negative-weight cycle anywhere in a directed graph, including disconnected components. Initialize every distance to zero, equivalent to a super-source. An improvement on the Vth Bellman–Ford pass proves a negative cycle. Return 1 if found, otherwise 0.

**Input/Output**

```text
Input: V = 4, edges = [[0,1,2],[2,3,-2],[3,2,1]]
Output: 1 (negative cycle is disconnected from vertex 0)
```

**Code**


**Time Space Complexity**

- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 39. ★ Floyd–Warshall Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1)

Find all-pairs shortest paths in place. Input matrix has 0 on its diagonal and 100000000 for no edge; negative weights are allowed, but no negative cycles. Finite distances have absolute value below 100000000.

**Input/Output**

```text
Input: dist = [[0,3,100000000],[100000000,0,2],[100000000,100000000,0]]
Output: dist becomes [[0,3,5],[100000000,0,2],[100000000,100000000,0]]; no return value
```

**Code**


**Time Space Complexity**

- **Time:** O(V³)
- **Space:** O(1) auxiliary; the O(V²) input distance matrix is updated in place.

### 40. ★ Find the City With the Smallest Number of Neighbors at a Threshold Distance — 1334

[LeetCode/GFG Link](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

Use Floyd–Warshall for all-pairs shortest distances in an undirected weighted graph. Count other cities within distanceThreshold. On equal counts, choose the city with the larger index.

**Input/Output**

```text
Input: n = 4, edges = [[0,1,2],[1,2,2],[2,3,2]], distanceThreshold = 2
Output: 3
```

**Code**


**Time Space Complexity**

- **Time:** O(n³ + E)
- **Space:** O(n²).

### 41. ★ Shortest Path in a Directed Acyclic Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1)

Find distances from vertex 0 in a nonempty DAG with edges [u, v, weight]. Relax edges in topological order; unreachable vertices return −1.

**Input/Output**

```text
Input: V = 4, edges = [[0,1,2],[0,2,5],[1,2,-1]]
Output: [0,2,1,-1]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## Disjoint Set Union — Union-Find

### 42. ★ Implement DSU — Path Compression and Union by Size

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1)

Maintain disjoint sets for elements 0 through n − 1 using path compression and union by size. union returns whether two different components were merged.

**Input/Output**

```text
Input: DSU(4); union(0,1); union(1,2); union(0,2); find(0) == find(2); find(0) == find(3)
Output: true; true; false; true; false (initialization has no output)
```

**Code**


**Time Space Complexity**

- **Time:** O(n) initialization; O(α(n)) amortized per find/union, where α is the inverse Ackermann function.
- **Space:** O(n) for parent and size arrays.

### 43. ★ Redundant Connection — 684

[LeetCode/GFG Link](https://leetcode.com/problems/redundant-connection/)

An undirected tree on labels 1 through n has one extra edge. Return the edge that creates a cycle when edges are processed in input order.

**Input/Output**

```text
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Code**


**Time Space Complexity**

- **Time:** O(n × α(n))
- **Space:** O(n) for DSU.

### 44. ★ Number of Operations to Make Network Connected — 1319

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Return the fewest cable moves to connect all n computers, or −1 if there are fewer than n − 1 cables.

**Input/Output**

```text
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E × α(V))
- **Space:** O(V) for DSU.

### 45. ★ Accounts Merge — 721

[LeetCode/GFG Link](https://leetcode.com/problems/accounts-merge/)

Merge accounts sharing an email and sort each merged email list. Each account has a name and at least one email; shared-email accounts have the same name.

**Input/Output**

```text
Input: accounts = [["Mira","a@x.com","b@x.com"],["Mira","b@x.com","c@x.com"],["Noah","n@x.com"]]
Output: [["Mira","a@x.com","b@x.com","c@x.com"],["Noah","n@x.com"]] (account groups may appear in any order)
```

**Code**


**Time Space Complexity**

- **Time:** O(A + M × (L + α(A)) + U log(U + 1) × L), where A = accounts, M = email occurrences, U = unique emails, L = maximum email length.
- **Space:** O(A + M + U × L), including temporary email lists and output; sorting can also use linear temporary storage.

### 46. ★ Most Stones Removed with Same Row or Column — 947

[LeetCode/GFG Link](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

Model stones as nodes. Union stones sharing a row or column, using a representative map for each coordinate. Each connected component must keep one stone; return the number of stones minus the number of components.

**Input/Output**

```text
Input: stones = [[0,0],[0,1],[1,1],[3,4]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(n × α(n)) expected, where n = stones; hash-map operations are expected O(1).
- **Space:** O(n).

## 10. Minimum spanning tree

### 47. ★ Kruskal’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1)

Find the MST weight of a connected undirected graph with edges [u, v, weight]. Process edges by weight and merge different components.

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,7]]
Output: 6
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E log(E + 2) + E × α(V))
- **Space:** O(V + E), including DSU and the sorted edge copy.

### 48. ★ Prim’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

Find the MST weight of an undirected connected graph with V ≥ 1 and edges [u, v, weight]. Add the cheapest edge reaching an unused vertex.

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,7]]
Output: 6
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 49. ★ Min Cost to Connect All Points — 1584

[LeetCode/GFG Link](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Connect all points with minimum total Manhattan distance. Use dense Prim without building all pairwise edges.

**Input/Output**

```text
Input: points = [[0,0],[2,0],[2,2]]
Output: 4
```

**Code**


**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n), excluding input points.

## 11. Strongly connected components and connectivity

### 50. ★ Kosaraju’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

Count strongly connected components in a directed graph given V and edges. Record DFS finish order, then traverse the reversed graph in reverse finish order.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[1,0],[1,2],[2,3],[3,2]]
Output: 2
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including both adjacency lists.

### 51. ★ Critical Connections in a Network — 1192

[LeetCode/GFG Link](https://leetcode.com/problems/critical-connections-in-a-network/)

Find bridges: edges whose removal increases the number of connected components. Iterative DFS tracks discovery times and the lowest reachable ancestor; edge IDs handle parallel edges.

**Input/Output**

```text
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]] (edge endpoints may be reversed)
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 12. Other important graph patterns

### 52. ★ Evaluate Division — 399

[LeetCode/GFG Link](https://leetcode.com/problems/evaluate-division/)

For a / b = value, store edges a → b with value and b → a with its reciprocal. For each query, DFS multiplies edge weights along a path. Unknown or disconnected variables return −1.0; a known variable divided by itself returns 1.0. Equations are consistent.

**Input/Output**

```text
Input: equations = [["x","y"],["y","z"]], values = [4.0,2.0], queries = [["x","z"],["z","x"],["u","u"]]
Output: [8.0,0.125,-1.0]
```

**Code**


**Time Space Complexity**

- **Time:** O(V + E + Q(V + E)) expected map/set operations; Q = queries. Variable-name hashing additionally depends on string length.
- **Space:** O(V + E) auxiliary, plus O(Q) output.

### 53. ★ All Paths From Source to Target — 797

[LeetCode/GFG Link](https://leetcode.com/problems/all-paths-from-source-to-target/)

Given a DAG adjacency list, enumerate every path from node 0 to node n − 1. Use DFS/backtracking: append a neighbor before exploring and remove it afterward. A global visited set would incorrectly discard distinct paths.

**Input/Output**

```text
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]] (any order)
```

**Code**


**Time Space Complexity**

- **Time:** O(V × 2^V) worst case, including path copies; the number of paths can be exponential.
- **Space:** O(V) auxiliary for the path and recursion, plus O(V × 2^V) worst-case output.

### 54. ★ Longest Increasing Path in a Matrix — 329

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

Strictly increasing edges form a DAG. DFS memoizes the longest path starting at each cell, so each cell is solved once. The alternative topological-layer solution avoids recursion depth limits on long paths.

**Input/Output**

```text
Input: matrix = [[3,4],[2,5]]
Output: 4
```

**Code**

**DFS + memoization**


**Topological layers — avoids recursion**


**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C).
