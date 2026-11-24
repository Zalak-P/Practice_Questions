# Graphs

V = vertices; E = edges; R and C = grid dimensions; α = inverse Ackermann function. Recursive alternatives can exceed Python recursion limits or Java stack depth on long paths; use the iterative alternative where supplied.

Video series and approaches follwed - https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

## Basic Grid — Explore One Connected Component at a Time

### 1. ★ Number of Islands — 200

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

**Input/Output**

```text
Input: grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["1","0","0","0"]
]
Output: 3
```

```python
class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 2. ★ Flood Fill — 733

[LeetCode/GFG Link](https://leetcode.com/problems/flood-fill/)

Recolor the 4-connected component containing (sr, sc) in a nonempty image. Updates the image in place.

**Input/Output**

```text
Input: image = [
    [1,1,0,0],
    [1,0,0,1],
    [1,1,0,1],
    [0,0,0,1]
]
sr = 0, sc = 0, color = 2

Output: [
    [2,2,0,0],
    [2,0,0,1],
    [2,2,0,1],
    [0,0,0,1]
]
```

```python
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        # Return early if the original color equals the new color, to prevent endless revisits.
        if original_color == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 3. Number of Distinct Islands (G-16)

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-distinct-islands/)

**Input/Output**

```text
Input: grid = [
    [1,1,0,0],
    [1,0,0,0],
    [0,0,1,1],
    [0,0,1,0]
]
Output: 1
```

```python

```

## Multi-source BFS — Expand Level by Level

### 4. ★ Rotting Oranges — 994

[LeetCode/GFG Link](https://leetcode.com/problems/rotting-oranges/)

Each minute, rotten oranges infect fresh oranges up, down, left, and right. Return the minimum minutes to rot all oranges, or -1 if impossible.

- 0 = empty
- 1 = fresh
- 2 = rotten

**Input/Output**

```text
Input: grid = [
    [2,1,1,0],
    [1,1,0,0],
    [0,1,1,1],
    [0,0,0,1]
]
Output: 6
```

```python
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        minutes = 0
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1

                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                     if 0 <= nr< rows and 0 <=nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1

        return minutes
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the BFS queue.

### 5. ★ 01 Matrix — 542

[LeetCode/GFG Link](https://leetcode.com/problems/01-matrix/)

Find each cell’s distance to its nearest 0 using multi-source BFS. The nonempty binary matrix contains at least one 0.

**Input/Output**

```text
Input: mat = [
    [0,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,0]
]

Output: [
    [0,1,2,3],
    [1,2,3,2],
    [2,3,2,1],
    [3,2,1,0]
]
```

```python
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        answer_matrix = [[-1] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    answer_matrix[r][c] = 0
                    queue.append((r, c))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr< rows and 0 <=nc < cols and answer_matrix[nr][nc] == -1:
                    answer_matrix[nr][nc] = answer_matrix[r][c] + 1
                    queue.append((nr, nc))

        return answer_matrix

```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C), including the distance matrix and BFS queue.

## Boundary Exploration

### 6. ★ Surrounded Regions — 130

[LeetCode/GFG Link](https://leetcode.com/problems/surrounded-regions/)

Flip enclosed 'O' regions to 'X' in place. First preserve all 'O' cells connected to the boundary of the nonempty board.

**Input/Output**

```text
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","O","X","X"]]
Output: board becomes [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]; no return value
```

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 2: Flip remaining 'O' to 'X', 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS recursion stack.

### 7. Number of Enclaves (G-15)

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-enclaves/)

**Input/Output**

```text
Input: grid = [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]
]
Output: 3
```

```python

```

## Grid Shortest Path — BFS with Queue and Distance

### 8. Shortest Distance in a Binary Maze (G-36)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1)

**Input/Output**

```text
Input: mat = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [0,0,0,1]
]
src = [0,0], dest = [3,3]
Output: 6
```

```python

```

## BFS / DFS — adj Traversal

### 9. ★ BFS Traversal of a adj

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-adj/1)

BFS visits nodes level by level, using a queue. Mark each node visited when adding it to the queue to prevent duplicates.

**Input/Output**

```text
Input: adj = [[1,2],[0,3,4],[0,5],[1],[1],[2]]
Output: [0,1,2,3,4,5]
```

```python
class Solution:
    def bfs(self, adj):
        if not adj:
            return []

        visited = {0}
        queue = deque([0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 10. ★ DFS Traversal of a adj

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-adj/1)

DFS explores one branch as deeply as possible before backtracking. Start from vertex 0 and follow adjacency-list order.

**Input/Output**

```text
Input: adj = [[1,2],[0,3,4],[0,5],[1],[1],[2]]
Output: [0,1,3,4,2,5]
```

```python
class Solution:
    def dfs(self, adj):
        visited = set()
        result = []

        def traverse(node):
            visited.add(node)
            result.append(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    traverse(neighbor)

        if adj:
            traverse(0)

        return result
```

**Time Space Complexity**

- **Time:**
- Each vertex is visited at most once: O(V).
- Each visited vertex scans its adjacency list. Across the adj, that is E entries for a directed adj, or 2E for an undirected adj so ~ O(E).
- Assuming average O(1) set operations, total time is O(V + E).
- The neighbor loop scans only its node’s neighbors.
- **Space:**
- Visited can contain V vertices: O(V).
- A adj can produce V active recursive calls: O(V).
- result can contain V vertices: O(V) output space.
- Auxiliary space is O(V). Including the output, it remains O(V).

### 11. ★ Number of Provinces — 547

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-provinces/)

Given an adjacency matrix isConnected, count the groups of directly or indirectly connected cities.

**Input/Output**

```text
Input: isConnected = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,1]
]
Output: 2
```

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        answer = 0
        n = len(isConnected)

        for i in range(n):
            if i not in visited:
                answer += 1
                queue = deque([i])
                visited.add(i)

                while queue:
                    node = queue.popleft()

                    for neighbor in range(n):
                        if isConnected[node][neighbor] == 1 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

        return answer
```

**Time Space Complexity**

- **Time:** O(n² × α(n))
- **Space:** O(n) auxiliary for DSU; the input matrix is excluded.

## Cycle Detection — Parent Tracking / DFS Recursion Stack / State Tracking

### 12. ★ Detect Cycle in an Undirected adj — BFS and DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-adj/1)

Detect a cycle in any component of an undirected adj. Input edges use vertices 0 through V − 1; edge IDs distinguish parallel edges. Mark vertices when scheduling them. Ignore only the edge used to enter the current vertex; another edge to a seen vertex proves a cycle. Both BFS and DFS are included.

The rule is: process a node only when it has no incoming edges left.

Indegree means the number of incoming edges to a node. In Course Schedule, it represents how many prerequisites remain.

**Input/Output**

```text
Input:
V = 5
edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]
adj = [[1,2],[0,2,3],[1,0],[1,4],[3]]
Output: true
```

**BFS**

```python
class Solution:
    def isCycle(self, adj):
        visited = set()

        for start in range(len(adj)):
            if start in visited:
                continue
            visited.add(start)
            queue = deque([(start, -1)])

            while queue:
                node, parent = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True
        return False
```

```python
def has_cycle_undirected(vertices, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in adj[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for v in range(vertices):
        if v not in visited:
            if dfs(v, -1):
                return True

    return False
```

### 13. ★ Detect Cycle in a Directed adj — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-adj/1)

Detect a directed cycle using DFS states: 0 = unvisited, 1 = active, 2 = completed. An edge to an active node proves a cycle. Explicit stack frames avoid recursion depth limits.

**Input/Output**

```text
Input: V = 5, edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]
Output: true
```

```python
def has_cycle_directed(vertices, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    visited = set()
    rec_stack = set()  # Tracks nodes in the current recursion path

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in adj[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for v in range(vertices):
        if v not in visited:
            if dfs(v):
                return True

    return False
```

## Bipartite adj — Two-color BFS / DFS

A bipartite adj is a adj whose nodes have 2 different colors, or you can assign 2 diff colors to the adjcent nodes.
Thus dividing the adj in 2 groups where no edges are interconnected within same group.

Observations:- 10
|

- Linear adjs with no cycles are always Bipartite, 1 -> 2-> 4 -> 5
  \
   7 - 9
- Any adj with even cycle **length** is also bipartite.

### 14. ★ Is adj Bipartite? — 785

[LeetCode/GFG Link](https://leetcode.com/problems/is-adj-bipartite/)

Check whether an undirected adjacency-list adj can be colored with two colors. Covers disconnected components.

**Input/Output**

```text
Input: adj = [[1,3],[0,2],[1,3],[0,2]]
Output: true
```

1. **Two-Coloring Test:** Try to color every vertex using any two colors (e.g., Red and Blue) so that no two adjecent connected vertices share the same color. If you can do it, it is bipartite. (BFS Approach)

```python
class Solution:
    def isBipartite(self, adj):
        color_array = [-1] * len(adj)

        for i in range(len(adj)):
            if color_array[i] != -1:
                continue

            color_array[i] = 0
            queue = deque([i])

            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if color_array[neighbor] == -1:
                        color_array[neighbor] = 1 - color_array[node]
                        queue.append(neighbor)
                    elif color_array[neighbor] == color_array[node]:
                        return False

        return True
```

2. **Odd Cycle Check:** If the adj contains a loop (cycle) with an odd number of edges/vertices, it is not bipartite. (DFS Approach)

```python
class Solution:
    def isBipartite(self, adj):
        color_array = [-1] * len(adj)

        def dfs(node, current_color):
            color_array[node] = current_color

            for neighbor in adj[node]:
                if color_array[neighbor] == -1:
                    if not dfs(neighbor, 1 - current_color):
                        return False
                elif color_array[neighbor] == current_color:
                    return False

            return True

        for node in range(len(adj)):
            if color_array[node] == -1 and not dfs(node, 0):
                return False

        return True
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list; includes recursion stack for DFS.

## Directed adj — DFS State Tracking

[LeetCode/GFG Link](https://leetcode.com/problems/find-eventual-safe-states/)

Use three states:

- 0: Unvisited.
- 1: Previously visited is not enough—the node must still be active in the current path.
- 2: Completed—all outgoing neighbors explored.

### 15. Detect cycle in directed adj

**Input/Output**

```text
Input: adj = [[1],[2,3],[0],[4],[]]
Output: true
```

```python
class Solution:
    def isCyclic(self, adj):
        state = [0] * len(adj)

        def dfs(node):
            state[node] = 1
            for neighbor in adj[node]:
                if state[neighbor] == 1:
                    return True
                if state[neighbor] == 0 and dfs(neighbor):
                    return True
            state[node] = 2
            return False

        for node in range(len(adj)):
            if state[node] == 0 and dfs(node):
                return True
        return False
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V)

### 16. Find eventual safe states

**Input/Output**

```text
Input: adj = [[1],[2,3],[1],[4],[]]
Output: [3,4]
```

```python

```

## Kahn’s Algorithm — Indegree / Outdegree

Topological sort is a linear ordering of vertices in DAG. It is used for every directed edge u->v, u appears before v.
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

### 17. ★ Detect Cycle in a Directed adj

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-adj/1)

Kahn’s algorithm is a BFS-based way to put the nodes of a directed adj in dependency order, called a topological order.

The rule is: process a node only when it has no incoming edges left.

Indegree means the number of incoming edges to a node. In Course Schedule, it represents how many prerequisites remain.

**Input/Output**

```text
Input: adj = [[1],[2,3],[0],[4],[]]
Output: true
```

```python

class Solution:
    def isCyclic(self, adj):
        indegree = [0] * len(adj)

        for node in range(len(adj)):
            for neighbor in adj[node]:
                indegree[neighbor] += 1

        # queue containing all nodes whose indegree is 0
        queue = deque()
        for node in range(len(adj)):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            processed += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return processed != len(adj)
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E)

### 18. ★ Find Eventual Safe States — 802

[LeetCode/GFG Link](https://leetcode.com/problems/find-eventual-safe-states/)

Return sorted vertices whose every path eventually terminates. Start with terminal vertices and remove edges in the reversed adj.

**Input/Output**

```text
Input: adj = [[1],[2,3],[1],[4],[]]
Output: [3,4]
```

```python
class Solution:
    def eventualSafeNodes(self, adj):
        n = len(adj)
        reverse = [[] for _ in range(n)]
        outdegree = [0] * n

        for node in range(n):
            outdegree[node] = len(adj[node])
            for neighbor in adj[node]:
                reverse[neighbor].append(node)

        queue = deque(node for node in range(n) if outdegree[node] == 0)
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True

            for previous in reverse[node]:
                outdegree[previous] -= 1
                if outdegree[previous] == 0:
                    queue.append(previous)

        return [node for node in range(n) if safe[node]]
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the reversed adj.

### 19. ★ Topological Sort — Kahn’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

Return a valid ordering of vertices in a directed acyclic adj given V and edges. Returns an empty array/list if a cycle exists.

**Input/Output**

```text
Input: V = 5, edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
Output: [0,1,2,3,4] (one valid order)
```

```python
class Solution:
    def topoSort(self, V, edges):
        n = V
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        indegree = [0] * n

        for neighbors in adj:
            for v in neighbors:
                indegree[v] += 1

        queue = deque(u for u in range(n) if indegree[u] == 0)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == n else []
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 19. ★ Course Schedule — 207

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule/)

Determine whether all courses can be completed. Each prerequisite pair is [course, prerequisite].

**Input/Output**

```text
Input: numCourses = 5, prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3]]
Output: true
```

```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1

        # queue containing all nodes whose indegree is 0
        queue = deque(u for u in range(numCourses) if indegree[u] == 0)
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 20. ★ Course Schedule II — 210

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule-ii/)

Return a valid course order, or an empty array/list when a cycle makes completion impossible.

**Input/Output**

```text
Input: numCourses = 5, prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3]]
Output: [0,1,2,3,4] (one valid order)
```

```python

class Solution:
    def findOrder(self, numCourses, prerequisites):
        n = numCourses
        adj = [[] for _ in range(n)]
        for u, v in prerequisites:
            adj[u].append(v)

        indegree = [0] * n
        for neighbors in adj:
            for v in neighbors:
                indegree[v] += 1

        queue = deque(u for u in range(n) if indegree[u] == 0)
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == n else []
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 21. ★ Alien Dictionary — 269

[LeetCode/GFG Link](https://leetcode.com/problems/alien-dictionary/)

Infer any valid ordering of the lowercase letters appearing in sorted alien words. Return an empty string for a cycle or invalid prefix order. LeetCode 269 is Premium. The workbook method is named findOrder.

**Input/Output**

```text
Input: words = ["wrt","wrf","er","ett", rftt]
Output: "zacb" (one valid order; z before c and a before b)
```

```python

class Solution:
    def findOrder(self, words):
        adj = {ch: set() for word in words for ch in word}   # adj = { "w": set(), "r": set(), "t": set(), "f": set(), "e": set()}

        degree = dict.fromkeys(adj, 0)

        for curr, next in zip(words, words[1:]): # this lets compare each word with next word.
            for ch1, ch2 in zip(curr, next):
                if ch1 != ch2:
                    if ch2 not in adj[ch1]:
                        adj[ch1].add(ch2)   # adj = { "w": {"e"}, "r":{"t"}, "t":{"f"}, "f": set(), "e": {"r"} }
                        degree[ch2] += 1  # indegree = { "w": 0, "r": 1, "t": 1, "f": 1, "e": 1}
                    break
            else:
                if len(curr) > len(next):
                    return ''

        queue = deque(ch for ch in adj if degree[ch] == 0)  # queue = deque(["w"])
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)

            for nxt in adj[ch]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    queue.append(nxt)

        return ''.join(order) if len(order) == len(adj) else ''
```

**Time Space Complexity**

- **Time:** O(S + A + E), where S is total input characters, A distinct letters, and E distinct ordering constraints.
- **Space:** O(A + E), excluding input word storage.

## DAG Shortest Path — Topological Order and Edge Relaxation

### 22. ★ Shortest Path in a Directed Acyclic adj

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-adj/1)

Find distances from vertex 0 in a nonempty DAG with edges [u, v, weight]. Relax edges in topological order; unreachable vertices return −1.

**Input/Output**

```text
Input: V = 4, edges = [[0,1,2],[0,2,5],[1,2,-1]]
Output: [0,2,1,-1]
```

```python

class Solution:
    def shortestPath(self, V, edges):
        n = V
        adj = [[] for _ in range(V)]
        degree = [0] * n

        for u, v, w in edges:
            adj[u].append((v, w))
            degree[v] += 1

        queue = deque(u for u in range(n) if degree[u] == 0)
        dist = [float('inf')] * n
        dist[0] = 0

        while queue:
            node = queue.popleft()

            for v, w in adj[node]:
                if dist[node] != float('inf'):
                    dist[v] = min(dist[v], dist[node] + w)

                degree[v] -= 1

                if degree[v] == 0:
                    queue.append(v)

        return [-1 if d == float('inf') else d for d in dist]
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## Shortest Path BFS — Explicit Graph

### 23. ★ Shortest Path in an Undirected Graph with Unit Weights

[LeetCode/GFG Link](https://www.geeksforgeeks.org/dsa/shortest-path-in-undirected-adj-having-unit-distance/)

Find distances from src in an undirected, unweighted graph with V vertices. Return −1 for unreachable vertices.

**Input/Output**

```text
Input: V = 6, edges = [[0,1],[1,2], [2,3], [4,5]], src = 0
Output: [0,1,2,3]
```

```python

class Solution:
    def shortestPath(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [-1] * V
        dist[src] = 0
        queue = deque([src])

        while queue:
            node = queue.popleft()

            for v in adj[node]:
                if dist[v] == -1:
                    dist[v] = dist[node] + 1
                    queue.append(v)

        return dist
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## Shortest Path BFS — Generate the Next States

### 24. ★ Word Ladder — 127

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

**Input/Output**

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

```python
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        remaining = set(wordList)
        if endWord not in remaining:
            return 0

        remaining.discard(beginWord)
        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in ascii_lowercase:
                    candidate = word[:i] + ch + word[i + 1:]

                    if candidate in remaining:
                        remaining.remove(candidate)
                        queue.append((candidate, length + 1))
        return 0
```

**Time Space Complexity**

- **Time:** O((N + 1) × 26 × L²), including string construction/hashing; N = dictionary size.
- **Space:** O((N + 1) × L), for dictionary/queue strings of length L; N = dictionary size.

### 25. Minimum Multiplications to Reach End (G-39)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1)

```text
Input: arr = [2, 3, 5, 7, 11], start = 3, end = 2310
Output: 4
```

```python

queue = deque([start])
visited = {start}
steps = 0


```

## All Shortest Sequences — BFS and Backtracking

### 26. Word Ladder II (G-30, G-31)

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder-ii/)

```text
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Output:
[
    ["hit", "hot", "dot", "dog", "cog"],
    ["hit", "hot", "lot", "log", "cog"]
]
```

```python
from collections import deque, defaultdict
from string import ascii_lowercase

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return []

        queue = deque([beginWord])
        distance = {beginWord: 0}
        parents = defaultdict(list)

        while queue and endWord not in distance:
            for _ in range(len(queue)):
                word = queue.popleft()


```

## Dijkstra’s Algorithm

### 27. ★ Dijkstra’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1)

Find minimum distances from src to every vertex in an undirected graph with nonnegative edge weights. Edges are [u, v, weight]; unreachable vertices return −1.

**Input/Output**

```text
Input: V = 5, edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[3,4,3]], src = 0
Output: [0,3,1,4,7]
```

```python
from heapq import heappop, heappush

class Solution:
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]

        for u, v, weight in edges:
            adj[u].append((v, weight))
            adj[v].append((u, weight))

        distance = [float('inf')] * V
        distance[src] = 0
        heap = [(0, src)]

        while heap:
            cost, u = heappop(heap)

            if cost != distance[u]:
                continue

            for v, weight in adj[u]:
                new_cost = cost + weight
                if new_cost < distance[v]:
                    distance[v] = new_cost
                    heappush(heap, (new_cost, v))

        return [-1 if cost == float('inf') else cost for cost in distance]

```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2)) with a heap that can retain outdated entries.
- **Space:** O(V + E), including the adjacency list and heap with outdated entries.

### 28. Print Shortest Path in a Weighted Undirected adj (G-35)

Return the sequence path of vertices from source to destination (total number of nodes)

```text
Input: V = 5, edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1], [4,3,3], [3,5,1]], src = 1, dest = 5
Output: [1,4,3,5]
```

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-adj/1)

```python
from heapq import heappop, heappush

class Solution:
    def shortestPath(self, V, edges, source, destination):
        adj = [[] for _ in range(V+1)]

        for u, v, weight in edges:
            adj[u].append((v, weight))
            adj[v].append((u, weight))

        distance = [float('inf')] * (V+1)
        parent = [-1] * (V + 1)
        distance[src] = 0
        heap = [(0, src)]

        while heap:
            cost, u = heappop(heap)

            if cost != distance[u]:
                continue

            for v, weight in adj[u]:
                new_cost = cost + weight
                if new_cost < distance[v]:
                    distance[v] = new_cost
                    parent[v] = u
                    heappush(heap, (new_cost, v))

        if distance[dest] == float("inf"):
            return [-1]

        path = []
        node = dest

        while node != -1:
            path.append(node)
            node = parent[node]

        return path[::-1]
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E)

### 29. ★ Path With Minimum Effort — 1631

[LeetCode/GFG Link](https://leetcode.com/problems/path-with-minimum-effort/)

Minimize the largest absolute height difference along a 4-directional path from top-left to bottom-right in a nonempty grid.

**Input/Output**

```text
Input: heights = [
    [1,2,2,2],
    [3,8,2,2],
    [5,3,5,2],
    [5,5,5,5]
]
Output: 2
```

```python
from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while heap:
            cost, r, c = heappop(heap)

            if cost != effort[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return cost

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_cost = max(cost, abs(heights[nr][nc] - heights[r][c]))

                    if new_cost < effort[nr][nc]:
                        effort[nr][nc] = new_cost
                        heappush(heap, (new_cost, nr, nc))

        return 0
```

**Time Space Complexity**

- **Time:** O(rows x cols x log(rows x cols))
- **Space:** O(rows x cols) for distances and the heap (a grid has O(R × C) edges).

### 30. Number of Ways to Arrive at Destination (G-40)

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)

Count the shortest paths from node 0 to node n - 1 in an undirected weighted graph. Return the count modulo 10⁹ + 7. All road weights are positive.

```text
Input:
n = 4
roads = [[0,1,1], [0,2,1], [1,3,1], [2,3,1], [0,3,2]]

Output: 3
0 → 1 → 3
0 → 2 → 3
0 → 3
```

```python
from heapq import heappush, heappop

class Solution:
    def countPaths(self, n, roads):
        mod = 10**9 + 7
        adj = [[] for _ in range(n)]

        for u, v, weight in roads:
            adj[u].append((v, weight))
            adj[v].append((u, weight))

        distance = [float("inf")] * n
        ways = [0] * n
        distance[0] = 0
        ways[0] = 1
        heap = [(0, 0)]

        while heap:
            cost, u = heappop(heap)

            if cost != distance[u]:
                continue

            for v, weight in adj[u]:
                new_cost = cost + weight

                if new_cost < distance[v]:
                    distance[v] = new_cost
                    ways[v] = ways[u]
                    heappush(heap, (new_cost, v))
                elif new_cost == distance[v]:
                    ways[v] = (ways[v] + ways[u]) % mod

        return ways[n - 1]
```

## Bellman–Ford — Repeated Edge Relaxation

### 31. ★ Bellman–Ford Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1)

Find shortest distances from src to every vertex in a directed weighted graph. Negative weights allowed. Return [-1] for a reachable negative cycle; use 100000000 for unreachable vertices (GFG convention).

**Input/Output**

```text
Input: V = 5, edges = [[0,1,4],[0,2,5],[1,2,-2],[2,3,3],[3,4,1]], src = 0
Output: [0,4,2,5,6]
```

```python
class Solution:
    def bellmanFord(self, V, edges, src):
        inf = float('inf')
        dist = [inf] * V
        dist[src] = 0

        for _ in range(V - 1):
            changed = False
            for u, v, w in edges:
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if changed == False:
                break

        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                return [-1]

        return [100000000 if d == inf else d for d in dist]
```

**Time Space Complexity**

- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 32. ★ Cheapest Flights Within K Stops — 787

[LeetCode/GFG Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest route from src to dst using at most k stops (k + 1 edges). Each relaxation round reads only the previous round’s distances.

**Input/Output**

```text
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,3,100],[0,3,500],[1,3,350]], src = 0, dest = 3, k = 1
Output: 450
```

```python
class Solution:
    def findCheapestPrice(self, n, flights, src, dest, k):
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            next_dist = dist.copy()

            for u, v, price in flights:
                next_dist[v] = min(next_dist[v], dist[u] + price)

            dist = next_dist
        return -1 if dist[dst] == float('inf') else dist[dest]
```

**Time Space Complexity**

- **Time:** O((k + 1) × (V + E))
- **Space:** O(V) for two distance arrays.

## Floyd–Warshall — All-pairs Shortest Paths

### 33. ★ Floyd–Warshall Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1)

Find all-pairs shortest paths in place. Input matrix has 0 on its diagonal and 100000000 for no edge; negative weights are allowed, but no negative cycles. Finite distances have absolute value below 100000000.

**Input/Output**

```text
Input: dist = [
    [0,4,5,100000000,100000000],
    [100000000,0,-2,100000000,100000000],
    [100000000,100000000,0,3,100000000],
    [100000000,100000000,100000000,0,1],
    [100000000,100000000,100000000,100000000,0]
]

Output: dist becomes [
    [0,4,2,5,6],
    [100000000,0,-2,1,2],
    [100000000,100000000,0,3,4],
    [100000000,100000000,100000000,0,1],
    [100000000,100000000,100000000,100000000,0]
]
No return value.
```

```python
class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        inf = 100000000

        for k in range(n):
            for i in range(n):
                if dist[i][k] == inf:
                    continue

                for j in range(n):
                    if dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**Time Space Complexity**

- **Time:** O(V³)
- **Space:** O(1) auxiliary; the O(V²) input distance matrix is updated in place.

### 34. ★ Find the City With the Smallest Number of Neighbors at a Threshold Distance — 1334

[LeetCode/GFG Link](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

You are given cities connected by **weighted roads** and a distance threshold.
For each city, count how many other cities it can reach with a shortest-path distance less than or equal to the threshold.
Return the city with the smallest count. If cities tie, return the one with the largest city number.

**Input/Output**

```text
Input: n = 5, edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[3,4,3]], distanceThreshold = 3
Output: 4
```

```python
class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, weight in edges:
            dist[u][v] = dist[v][u] = min(dist[u][v], weight)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        answer, best = -1, n

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= best:
                best = count
                answer = i

        return answer
```

**Time Space Complexity**

- **Time:** O(n³ + E)
- **Space:** O(n²).

## Minimum Spanning Tree — Grow a Tree Using a Min-heap

**MST:**
We can draw multiple Spanning Trees from a graph. Spanning Tree means - A tree in which we have N nodes and N-1 edges, and all nodes are reachable from each other. Total sum of all the edges have to be the least from all the spanning trees. That is called MST.

### 35. ★ Prim’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

This algo is used to find MST in a graph using heap. A total minium weight is returned of MST. We can also return edges/tree of MST.

**Input/Output**

```text
Input: V = 5, edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[3,4,3]]
Output: 7
MST edges: 0–2, 2–1, 1–3, 3–4
```

```python
from heapq import heappop, heappush

class Solution:
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        used = [False] * V
        heap = [(0, 0)]
        total = 0

        while heap:
            weight, u = heappop(heap)
            if used[u]:
                continue

            used[u] = True
            total += weight

            for v, w in adj[u]:
                if not used[v]:
                    heappush(heap, (w, v))

        return total
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

## DSU / Union Find — Basic Operations

Disjoint Set will work in constant time. Ex. node belong to any component or not etc. Instead of using DFS/BFS and exploring all the nodes-depth/nodes-levels.

Used for Dynamic Graphs (which changes a lot)

Two functionalites of Disjoint Sets:

1. Finding Parent()
2. Union() [rank, size] - will connect the edges

### 36. ★ Implement DSU — Path Compression and Union by Rank and Size

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1)

**Input/Output**

```text
Input: DSU(4); union(0,1); union(1,2); union(0,2); find(0) == find(2); find(0) == find(3)
Output: true; true; false; true; false (initialization has no output)
```

1. Union by rank - rank array and parent array.

- Find ultimate parent of u and v, -> pu, pv
- Find ultimate rank of pu and pv
- Connect smaller rank to larger rank always

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True
```

2. Union by Size - size array and parent array.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]

        return True
```

```python
dsu = DSU(5)

print(dsu.union(0, 1))           # True
print(dsu.union(1, 2))           # True
print(dsu.find(0) == dsu.find(2))  # True
print(dsu.find(0) == dsu.find(4))  # False
print(dsu.union(0, 2))           # False: already connected
```

**Time Space Complexity**

- **Time:** O(n) initialization; O(α(n)) amortized per find/union, where α is the inverse Ackermann function.
- **Space:** O(n) for parent and size arrays.
- With path compression, rank is a height bound, not necessarily the tree’s current height.

### 37. ★ Find Minimum Spanning Tree using DSU (Kruskal’s Algorithm)

1. Sort all edges according to weight
2. DSU Data structure

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1)

Find the MST weight of a connected undirected adj with edges [u, v, weight]. Process edges by weight and merge different components.

**Input/Output**

```text
V = 4
adj = [
    [[1, 1], [2, 3]],
    [[0, 1], [2, 2], [3, 5]],
    [[0, 3], [1, 2], [3, 4]],
    [[1, 5], [2, 4]]
]

Output: 7
MST edges: 0–1, 1–2, 2–3
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True


class Solution:
    def spanningTree(self, V, adj):
        edges = []
        #O(V+E)
        for u in range(V):
            for v, weight in adj[u]:
                if u < v:
                    edges.append((weight, u, v))
        # V log V
        edges.sort()
        dsu = DSU(V)
        total_weight = 0
        # V x 4 x alpha x 2
        for weight, u, v in edges:
            if dsu.union(u, v):
                total_weight += weight

        return total_weight
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2) + E × α(V))
- **Space:** O(V + E), including DSU and the sorted edge copy.
- Why u < v? An undirected edge appears in both nodes’ lists. This keeps only one copy.

### 38. ★ DSU - Number of Provinces — 547

```text
Input: isConnected = [
    [1,1,0,0,0],
    [1,1,1,0,0],
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]
Output: 2
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True


class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        dsu = DSU(n)
        provinces = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if dsu.union(i, j):
                        provinces -= 1

        return provinces
```

```text
Initially, {0}, {1}, {2}, {3}, {4} are 5 provinces. Merging connected cities leaves {0,1,2} and {3,4}: 2 provinces.

Why j = i + 1 onward? The matrix is symmetric, so we check each city pair once and skip self-connections.

Time: O(n² × α(n))
Space: O(n)
```

## DSU — Count Components and Redundant Connections

### 39. ★ Minimum of Number of Operations to Make Network Connected — 1319

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Given n computers and undirected connections, you can move an existing cable to connect two disconnected computers. Return the minimum moves needed to connect the entire network, or -1 if impossible.

You need at least n - 1 cables. If enough cables exist, the answer is number of components − 1.

**Input/Output**

```text
Input: n = 5, connections = [[0,1],[0,2],[1,2],[1,3],[2,3]]
Output: 1
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True


class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        dsu = DSU(n)
        components = n

        for u, v in connections:
            if dsu.union(u, v):
                components -= 1

        return components - 1
```

**Time Space Complexity**

- **Time:** O(V + E × α(V))
- **Space:** O(V) for DSU.

## DSU — Merge Entities through Shared Identifiers

### 40. ★ Accounts Merge — 721

[LeetCode/GFG Link](https://leetcode.com/problems/accounts-merge/)

Each account contains a name followed by email addresses. Merge accounts sharing an email, and sort the emails in each merged account. Matching names alone do not mean accounts belong together.

**Input/Output**

```text
Input:
accounts = [
    ["John", "a@mail.com", "b@mail.com"],
    ["John", "b@mail.com", "c@mail.com"],
    ["Mary", "m@mail.com"],
    ["John", "x@mail.com"]
]

Output:
[
    ["John", "a@mail.com", "b@mail.com", "c@mail.com"],
    ["Mary", "m@mail.com"],
    ["John", "x@mail.com"]
]
```

```python
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True


class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU(len(accounts))
        email_owner = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_owner:
                    dsu.union(i, email_owner[email])
                else:
                    email_owner[email] = i

        groups = defaultdict(list)

        for email, owner in email_owner.items():
            root = dsu.find(owner)
            groups[root].append(email)

        result = []

        for root, emails in groups.items():
            result.append([accounts[root][0]] + sorted(emails))

        return result
```

**Time Space Complexity**

```text
Time: O(N + M × α(N) + U log U)
Space: O(N + M + U)

N = accounts, M = email occurrences, U = unique emails. These bounds treat email string operations as constant cost.
```

## DSU on Grids — Merge Neighboring Land

### 41. Number of Islands II — Online Queries (G-51)

Initially, an n × m grid contains only water (0). Each query [r, c] turns that cell into land (1). Return the number of islands after each query.
Land cells connect horizontally or vertically. Adding land to an existing land cell makes no change.

```text
Input:
n = 3
m = 3
operators = [[0,0],[0,2],[2,2],[0,1]]
Output: [1,2,3,2]
```

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands-ii/)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True


class Solution:
    def numOfIslands(self, n, m, operators):
        dsu = DSU(n * m)
        land = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        result = []

        for r, c in operators:
            if land[r][c]:
                result.append(islands)
                continue

            land[r][c] = True
            islands += 1
            node = r * m + c

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and land[nr][nc]:
                    neighbor = nr * m + nc

                    if dsu.union(node, neighbor):
                        islands -= 1

            result.append(islands)

        return result
```

**Time Complexity:** O(n × m + Q × α(n × m))
**Space Complexity:** O(n × m) auxiliary space, plus O(Q) for the output.
Q is the number of queries; α is the inverse Ackermann function, which is nearly constant.

### 42. Making a Large Island (G-52)

[LeetCode/GFG Link](https://leetcode.com/problems/making-a-large-island/)

Given an n × n grid of 0s and 1s, change at most one 0 into 1. Return the largest possible island area. Connections are only up, down, left, and right.

```text
grid = [
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
output: 7
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n * n)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        dsu.union(r * n + c, nr * n + nc)

        answer = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    answer = max(answer, dsu.size[dsu.find(r * n + c)])
                    continue

                roots = set()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        roots.add(dsu.find(nr * n + nc))

                area = 1
                for root in roots:
                    area += dsu.size[root]

                answer = max(answer, area)

        return answer
```

### 43. ★ Most Stones Removed with Same Row or Column — 947

[LeetCode/GFG Link](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

You are given stone positions as [row, column].
You can remove a stone if another stone still on the board shares its row or its column.
Return the maximum number of stones you can remove.

**Input/Output**

```text
Input: stones = [[0, 0], [0, 1], [1, 0], [2, 2]]
Output: 2
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]

        return True

class Solution:
    def removeStones(self, stones):
        n = len(stones)
        dsu = DSU(n)
        row_owner = {}
        col_owner = {}
        components = n

        for i, (row, col) in enumerate(stones):
            if row in row_owner:
                if dsu.union(i, row_owner[row]):
                    components -= 1
            else:
                row_owner[row] = i

            if col in col_owner:
                if dsu.union(i, col_owner[col]):
                    components -= 1
            else:
                col_owner[col] = i

        return n - components
```

**Time Space Complexity**

- **Time:** O(n × α(n)) expected, where n = stones; hash-map operations are expected O(1).
- **Space:** O(n).

## Advanced DFS — Finishing Order and Reversed adj

### 44. ★ Strongly connected components (Kosaraju’s Algorithm)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

In a directed graph, a strongly connected component (SCC) is a group of vertices where every vertex can reach every other vertex in that group.

Return the number of strongly connected components.

**Input/Output**

```text
Input: adj = [
    [1],       # 0 → 1
    [2],       # 1 → 2
    [0, 3],    # 2 → 0, 2 → 3
    [4],       # 3 → 4
    [3]        # 4 → 3
]
Output: 2
```

The components are {0, 1, 2} and {3, 4}. The first group can reach the second through 2 → 3, but the second cannot reach the first.

Kosaraju’s algorithm has three steps:
1. Run DFS and record each vertex after finishing all its neighbors.
2. Reverse every edge.
3. Process vertices in reverse finishing order on the reversed graph. Each new DFS identifies one SCC.

```python
class Solution:
    def kosaraju(self, adj):
        n = len(adj)
        visited = [False] * n
        order = []

        def dfs(node):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

            order.append(node)

        for node in range(n):
            if not visited[node]:
                dfs(node)

        reverse = [[] for _ in range(n)]

        for node in range(n):
            for neighbor in adj[node]:
                reverse[neighbor].append(node)

        visited = [False] * n

        def reverse_dfs(node):
            visited[node] = True

            for neighbor in reverse[node]:
                if not visited[neighbor]:
                    reverse_dfs(neighbor)

        components = 0

        while order:
            node = order.pop()

            if not visited[node]:
                components += 1
                reverse_dfs(node)

        return components
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including both adjacency lists.

## Advanced DFS — Discovery Times and Low-link Values

### 45. ★ Critical Connections in a Network — 1192

[LeetCode/GFG Link](https://leetcode.com/problems/critical-connections-in-a-network/)

Given n servers and undirected connections, return all critical connections, also called bridges.
A connection is critical if removing it disconnects the network.

**Input/Output**

```text
n = 4, connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
Output: [[1,3]] (edge endpoints may be reversed)
```

Code — DFS with discovery times and low-link values
- discovery[node]: When DFS first visits this node.
- low[node]: The earliest discovery time reachable from its DFS subtree using tree edges and at most one back edge.
- An edge from a DFS parent node to its child neighbor is a bridge when low[neighbor] > discovery[node].

```python
class Solution:
    def criticalConnections(self, n, connections):
        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        discovery = [-1] * n
        low = [-1] * n
        bridges = []
        timer = 0

        def dfs(node, parent):
            nonlocal timer

            discovery[node] = low[node] = timer
            timer += 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if discovery[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])

                    if low[neighbor] > discovery[node]:
                        bridges.append([node, neighbor])
                else:
                    low[node] = min(low[node], discovery[neighbor])

        for node in range(n):
            if discovery[node] == -1:
                dfs(node, -1)
        return bridges

```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 46. Articulation Points in a adj (G-56)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/articulation-point-1/1)

Given an undirected graph, return all articulation points.
An articulation point is a vertex whose removal, along with its incident edges, increases the number of connected components.
Return the vertices in ascending order, or [-1] if none exist.

```text
adj = [
    [1, 2],
    [0, 2, 3],
    [0, 1],
    [1, 4],
    [3]
]
[1, 3]
```

```python
class Solution:
    def articulationPoints(self, V, adj):
        discovery = [-1] * V
        low = [-1] * V
        marked = [False] * V
        timer = 0

        def dfs(node, parent):
            nonlocal timer

            discovery[node] = low[node] = timer
            timer += 1
            children = 0

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if discovery[neighbor] == -1:
                    children += 1
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])

                    if parent != -1 and low[neighbor] >= discovery[node]:
                        marked[node] = True
                else:
                    low[node] = min(low[node], discovery[neighbor])

            if parent == -1 and children > 1:
                marked[node] = True

        for node in range(V):
            if discovery[node] == -1:
                dfs(node, -1)

        result = [node for node in range(V) if marked[node]]
        return result if result else [-1]
        
```

## Additional Problems — Not in the Agreed List

### 46. ★ Find if Path Exists in adj — 1971

[LeetCode/GFG Link](https://leetcode.com/problems/find-if-path-exists-in-graph/)

**Input/Output**

```text
Input: n = 6, edges = [[0,1],[0,2],[1,3],[2,3],[4,5]], source = 0, destination = 5
Output: false
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 47. ★ Clone adj — 133

[LeetCode/GFG Link](https://leetcode.com/problems/clone-graph/)

**Input/Output**

```text
Input: adj = [[2,3],[1,3],[1,2,4],[3,5],[4]]
Output: A deep copy with adj = [[2,3],[1,3],[1,2,4],[3,5],[4]], sharing no nodes with the input
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 48. ★ Keys and Rooms — 841

[LeetCode/GFG Link](https://leetcode.com/problems/keys-and-rooms/)

**Input/Output**

```text
Input: rooms = [[1,2],[2,3],[3],[4],[]]
Output: true
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 49. ★ Number of Connected Components in an Undirected adj — 323

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

**Input/Output**

```text
Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5]]
Output: 3
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 50. ★ Shortest Bridge — 934

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-bridge/)

**Input/Output**

```text
Input: grid = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,1]
]
Output: 5
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 51. ★ Max Area of Island — 695

[LeetCode/GFG Link](https://leetcode.com/problems/max-area-of-island/)

**Input/Output**

```text
Input: grid = [
    [1,1,0,0],
    [1,1,0,1],
    [0,1,0,1],
    [0,0,0,1]
]
Output: 5
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 52. ★ Pacific Atlantic Water Flow — 417

[LeetCode/GFG Link](https://leetcode.com/problems/pacific-atlantic-water-flow/)

**Input/Output**

```text
Input: heights = [
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6],
    [4,5,6,7]
]
Output: [[0,3],[1,3],[2,3],[3,0],[3,1],[3,2],[3,3]] (any order)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 53. ★ Possible Bipartition — 886

[LeetCode/GFG Link](https://leetcode.com/problems/possible-bipartition/)

**Input/Output**

```text
Input: n = 6, dislikes = [[1,2],[1,4],[3,2],[3,6],[5,4]]
Output: true
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 54. ★ Topological Sort — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

**Input/Output**

```text
Input: V = 5, edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
Output: [0,2,1,3,4] (one valid order)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 55. ★ Find All Possible Recipes from Given Supplies — 2115

[LeetCode/GFG Link](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)

**Input/Output**

```text
Input:
recipes = ["bread","toast","sandwich","burger","meal"]
ingredients = [["flour"],["bread"],["toast","cheese"],["bread","patty"],["sandwich","burger"]]
supplies = ["flour","cheese","patty"]

Output: ["bread","toast","sandwich","burger","meal"] (any order)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 56. ★ Shortest Path in Binary Matrix — 1091

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

**Input/Output**

```text
Input: grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
Output: 4
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 57. ★ Open the Lock — 752

[LeetCode/GFG Link](https://leetcode.com/problems/open-the-lock/)

**Input/Output**

```text
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 58. ★ Snakes and Ladders — 909

[LeetCode/GFG Link](https://leetcode.com/problems/snakes-and-ladders/)

**Input/Output**

```text
Input: board = [
    [-1,-1,-1,-1],
    [-1,-1,-1,-1],
    [-1,-1,-1,-1],
    [-1,-1,-1,-1]
]
Output: 3
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 59. ★ Network Delay Time — 743

[LeetCode/GFG Link](https://leetcode.com/problems/network-delay-time/)

**Input/Output**

```text
Input: times = [[1,2,4],[1,3,1],[3,2,2],[2,4,1],[4,5,3]], n = 5, k = 1
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 60. ★ Negative Cycle Detection

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1)

**Input/Output**

```text
Input: V = 5, edges = [[0,1,2],[1,2,3],[2,0,1],[3,4,-2],[4,3,1]]
Output: 1
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 61. ★ Redundant Connection — 684

[LeetCode/GFG Link](https://leetcode.com/problems/redundant-connection/)

**Input/Output**

```text
Input: edges = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: [1,5]
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 62. ★ Min Cost to Connect All Points — 1584

[LeetCode/GFG Link](https://leetcode.com/problems/min-cost-to-connect-all-points/)

**Input/Output**

```text
Input: points = [[0,0],[1,0],[2,0],[3,0],[4,0]]
Output: 4
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 63. ★ Evaluate Division — 399

[LeetCode/GFG Link](https://leetcode.com/problems/evaluate-division/)

**Input/Output**

```text
Input:
equations = [["a","b"],["b","c"],["c","d"],["d","e"],["e","f"]]
values = [2.0,3.0,4.0,5.0,6.0]
queries = [["a","f"],["f","a"],["b","d"],["a","a"],["x","x"]]

Output: [720.0,0.001388888888888889,12.0,1.0,-1.0]
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 64. ★ All Paths From Source to Target — 797

[LeetCode/GFG Link](https://leetcode.com/problems/all-paths-from-source-to-target/)

**Input/Output**

```text
Input: adj = [[1,2],[3],[3,4],[4],[]]
Output: [[0,1,3,4],[0,2,3,4],[0,2,4]] (any order)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 65. ★ Longest Increasing Path in a Matrix — 329

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

**Input/Output**

```text
Input: matrix = [
    [1,2,3,4],
    [8,7,6,5],
    [9,10,11,12],
    [16,15,14,13]
]
Output: 16
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**
