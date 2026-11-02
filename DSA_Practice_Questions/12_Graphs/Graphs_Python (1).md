# Graphs — Python

V = vertices; E = edges; R and C = grid dimensions; α = inverse Ackermann function. 

## 1. BFS, DFS, and connected components

### 1. BFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

Visit vertices reachable from vertex 0 in breadth-first order. Input: adjacency list; an empty graph returns an empty list.

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,2,3]
```

```python
from collections import deque

class Solution:
    def bfs(self, adj):
        if not adj:
            return []

        seen = {0}
        queue = deque([0])
        order = []
        
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        return order
```
- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 2. DFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

Visit vertices reachable from vertex 0 in depth-first order, following adjacency-list order. Use explicit stack frames.

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,3,2]
```

```python
class Solution:
    def dfs(self, adj):
        if not adj:
            return []
        seen = {0}
        order = [0]
        stack = [(0, iter(adj[0]))]
        while stack:
            u, neighbors = stack[-1]
            v = next(neighbors, None)
            if v is None:
                stack.pop()
            elif v not in seen:
                seen.add(v)
                order.append(v)
                stack.append((v, iter(adj[v])))
        return order
```
- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 3. Find if Path Exists in Graph — 1971

[LeetCode/GFG Link](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Check whether source can reach destination in an undirected graph with vertices 0 through n − 1.

```text
Input: n = 3, edges = [[0,1],[1,2]], source = 0, destination = 2
Output: true
```

```python
class Solution:
    def validPath(self, n, edges, source, destination):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = {source}
        stack = [source]
        while stack:
            u = stack.pop()
            if u == destination:
                return True
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return False
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 4. Number of Connected Components in an Undirected Graph — 323

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Count connected components, including isolated vertices, in an undirected graph. LeetCode 323 is Premium.

```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

```python
class Solution:
    def countComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = set()
        count = 0
        for start in range(n):
            if start in seen:
                continue
            count += 1
            seen.add(start)
            stack = [start]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
        return count
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 5. Clone Graph — 133

[LeetCode/GFG Link](https://leetcode.com/problems/clone-graph/)

Deep-copy the connected component reachable from node. The Node definition is included; use the judge-provided definition on LeetCode.

```text
Input: Adjacency list: [[2],[1]] (node values are 1 and 2)
Output: A new graph with adjacency list [[2],[1]], sharing no nodes with the input
```

```python
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        copies = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            u = queue.popleft()
            for v in u.neighbors:
                if v not in copies:
                    copies[v] = Node(v.val)
                    queue.append(v)
                copies[u].neighbors.append(copies[v])
        return copies[node]
```
- **Time:** O(V + E)
- **Space:** O(V) auxiliary for the map and queue, plus O(V + E) for the cloned output graph.

### 6. Keys and Rooms — 841

[LeetCode/GFG Link](https://leetcode.com/problems/keys-and-rooms/)

Visit room 0 and follow its keys to other rooms. Return whether every room can be reached. Use iterative DFS; each room is processed once.

```text
Input: rooms = [[1],[2],[3],[]]
Output: true
```

```python
class Solution:
    def canVisitAllRooms(self, rooms):
        seen = {0}
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key)
        return len(seen) == len(rooms)
```
- **Time:** O(V + E)
- **Space:** O(V), excluding the input; E is the total number of keys.

### 7. Number of Provinces — 547

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-provinces/)

Count connected groups in a symmetric n × n adjacency matrix. Scan each undirected connection once and merge its components.

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        dsu = DSU(n)
        count = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and dsu.union(i, j):
                    count -= 1
        return count
```
- **Time:** O(n² × α(n))
- **Space:** O(n) auxiliary for DSU; the input matrix is excluded.

## 2. Grid traversal

### 8. Number of Islands — 200

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

```text
Input: grid = [["1","1","0"],["0","0","1"]]
Output: 2
```

```python
class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue
                count += 1
                grid[r][c] = '0'
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            stack.append((nx, ny))
        return count
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 9. Flood Fill — 733

[LeetCode/GFG Link](https://leetcode.com/problems/flood-fill/)

Recolor the 4-connected component containing (sr, sc) in a nonempty image. Updates the image in place.

```text
Input: image = [[1,1],[1,0]], sr = 0, sc = 0, color = 2
Output: [[2,2],[2,0]]
```

```python
class Solution:
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if old == color:
            return image
        rows, cols = len(image), len(image[0])
        image[sr][sc] = color
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and image[x][y] == old:
                    image[x][y] = color
                    stack.append((x, y))
        return image
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 10. Max Area of Island — 695

[LeetCode/GFG Link](https://leetcode.com/problems/max-area-of-island/)

Return the largest 4-connected area of 1s in a nonempty binary grid. Visited land is changed to 0.

```text
Input: grid = [[1,1,0],[1,0,1]]
Output: 3
```

```python
class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                grid[r][c] = 0
                stack = [(r, c)]
                area = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                best = max(best, area)
        return best
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 11. Surrounded Regions — 130

[LeetCode/GFG Link](https://leetcode.com/problems/surrounded-regions/)

Flip enclosed 'O' regions to 'X' in place. First preserve all 'O' cells connected to the boundary of the nonempty board.

```text
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","O","X","X"]]
Output: board becomes [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]; no return value
```

```python
from collections import deque

class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    board[r][c] = '#'
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'O':
                    board[x][y] = '#'
                    queue.append((x, y))
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 'O' if board[r][c] == '#' else 'X'
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the BFS queue.

### 12. Pacific Atlantic Water Flow — 417

[LeetCode/GFG Link](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Find cells from which water reaches both oceans. Search backward from ocean boundaries to equal or higher cells in the nonempty height grid.

```text
Input: heights = [[1,2],[4,3]]
Output: [[0,1],[1,0],[1,1]] (any order)
```

```python
from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        def reach(starts):
            seen = set(starts)
            queue = deque(seen)
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = r + dr, c + dc
                    if (0 <= x < rows and 0 <= y < cols and (x, y) not in seen
                            and heights[x][y] >= heights[r][c]):
                        seen.add((x, y))
                        queue.append((x, y))
            return seen
        pacific = reach([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
        atlantic = reach([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)])
        return [[r, c] for r in range(rows) for c in range(cols)
                if (r, c) in pacific and (r, c) in atlantic]
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the two reachable sets/arrays and BFS queues.

## 3. Multi-source BFS

### 13. Rotting Oranges — 994

[LeetCode/GFG Link](https://leetcode.com/problems/rotting-oranges/)

Spread rot from all rotten oranges simultaneously in a nonempty grid. Return minutes until all fresh oranges rot, or −1. Updates the grid.

```text
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = r + dr, c + dc
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        queue.append((x, y))
            minutes += 1
        return minutes if fresh == 0 else -1
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the BFS queue.

### 14. 01 Matrix — 542

[LeetCode/GFG Link](https://leetcode.com/problems/01-matrix/)

Find each cell’s distance to its nearest 0 using multi-source BFS. The nonempty binary matrix contains at least one 0.

```text
Input: mat = [[0,1,1],[1,1,1]]
Output: [[0,1,2],[1,2,3]]
```

```python
from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and dist[x][y] == -1:
                    dist[x][y] = dist[r][c] + 1
                    queue.append((x, y))
        return dist
```
- **Time:** O(R × C)
- **Space:** O(R × C), including the distance matrix and BFS queue.

### 15. Shortest Bridge — 934

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-bridge/)

Given exactly two 4-connected islands, return the fewest water cells to flip to connect them. Mark one island, then expand it by BFS. Updates the grid.

```text
Input: grid = [[0,1],[1,0]]
Output: 1
```

```python
from collections import deque

class Solution:
    def shortestBridge(self, grid):
        rows, cols = len(grid), len(grid[0])
        start = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        stack = [start]
        queue = deque([start])
        grid[start[0]][start[1]] = 2
        while stack:
            r, c = stack.pop()
            for dr, dc in dirs:
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    stack.append((x, y))
                    queue.append((x, y))
        flips = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    x, y = r + dr, c + dc
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] != 2:
                        if grid[x][y] == 1:
                            return flips
                        grid[x][y] = 2
                        queue.append((x, y))
            flips += 1
        return -1
```
- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack and BFS queue.

## 4. Cycle detection

### 16. Detect Cycle in an Undirected Graph — BFS and DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

Detect a cycle in any component of an undirected graph. Input edges use vertices 0 through V − 1; edge IDs distinguish parallel edges. Mark vertices when scheduling them. Ignore only the edge used to enter the current vertex; another edge to a seen vertex proves a cycle. Both BFS and DFS are included.

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

**BFS**

```python
from collections import deque

class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        for eid, (u, v) in enumerate(edges):
            adj[u].append((v, eid))
            adj[v].append((u, eid))
        seen = set()
        for start in range(V):
            if start in seen:
                continue
            seen.add(start)
            queue = deque([(start, -1)])
            while queue:
                u, parent_edge = queue.popleft()
                for v, eid in adj[u]:
                    if eid == parent_edge:
                        continue
                    if v in seen:
                        return True
                    seen.add(v)
                    queue.append((v, eid))
        return False
```

**DFS — explicit stack**

```python
class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        for eid, (u, v) in enumerate(edges):
            adj[u].append((v, eid))
            adj[v].append((u, eid))
        seen = set()
        for start in range(V):
            if start in seen:
                continue
            seen.add(start)
            stack = [(start, -1)]
            while stack:
                u, parent_edge = stack.pop()
                for v, eid in adj[u]:
                    if eid == parent_edge:
                        continue
                    if v in seen:
                        return True
                    seen.add(v)
                    stack.append((v, eid))
        return False
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list; O(V) traversal storage for either variant.

### 17. Detect Cycle in a Directed Graph — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using DFS states: 0 = unvisited, 1 = active, 2 = completed. An edge to an active node proves a cycle. Explicit stack frames avoid recursion depth limits.

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

```python
class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        state = [0] * V
        for start in range(V):
            if state[start] != 0:
                continue
            state[start] = 1
            stack = [(start, iter(adj[start]))]
            while stack:
                u, neighbors = stack[-1]
                v = next(neighbors, None)
                if v is None:
                    state[u] = 2
                    stack.pop()
                elif state[v] == 1:
                    return True
                elif state[v] == 0:
                    state[v] = 1
                    stack.append((v, iter(adj[v])))
        return False
```
- **Time:** O(V + E)
- **Space:** O(V + E)

### 18. Detect Cycle in a Directed Graph — Kahn’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using Kahn’s algorithm: a cycle exists if not all vertices can be removed. Input: V and directed edges.

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

```python
from collections import deque

class Solution:
    def isCyclic(self, V, edges):
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
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return len(order) != n
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 19. Course Schedule — 207

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule/)

Determine whether all courses can be completed. Each prerequisite pair is [course, prerequisite].

```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
```

```python
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        n = numCourses
        adj = [[] for _ in range(n)]
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
        indegree = [0] * n
        for neighbors in adj:
            for v in neighbors:
                indegree[v] += 1
        queue = deque(u for u in range(n) if indegree[u] == 0)
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return len(order) == n
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 20. Find Eventual Safe States — 802

[LeetCode/GFG Link](https://leetcode.com/problems/find-eventual-safe-states/)

Return sorted vertices whose every path eventually terminates. Start with terminal vertices and remove edges in the reversed graph.

```text
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
```

```python
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        reverse = [[] for _ in range(n)]
        degree = [len(neighbors) for neighbors in graph]
        for u in range(n):
            for v in graph[u]:
                reverse[v].append(u)
        queue = deque(u for u in range(n) if degree[u] == 0)
        while queue:
            u = queue.popleft()
            for v in reverse[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)
        return [u for u in range(n) if degree[u] == 0]
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the reversed graph.

## 5. Bipartite graphs

### 21. Is Graph Bipartite? — 785

[LeetCode/GFG Link](https://leetcode.com/problems/is-graph-bipartite/)

Check whether an undirected adjacency-list graph can be colored with two colors so adjacent vertices differ. Covers disconnected components.

```text
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
```

**BFS**

```python
from collections import deque

class Solution:
    def isBipartite(self, graph):
        color = [-1] * len(graph)
        for start in range(len(graph)):
            if color[start] != -1:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
```

**DFS — recursive**

```python
class Solution:
    def isBipartite(self, graph):
        color = [-1] * len(graph)
        def dfs(node, current_color):
            color[node] = current_color
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - current_color):
                        return False
                elif color[neighbor] == current_color:
                    return False
            return True
        for node in range(len(graph)):
            if color[node] == -1 and not dfs(node, 0):
                return False
        return True
```
- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list; includes recursion stack for DFS.

### 22. Possible Bipartition — 886

[LeetCode/GFG Link](https://leetcode.com/problems/possible-bipartition/)

Split people labeled 1 through n into two groups so every disliked pair is separated. Build an undirected graph and two-color it.

```text
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
```

```python
from collections import deque

class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = [[] for _ in range(n + 1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = [-1] * len(graph)
        for start in range(len(graph)):
            if color[start] != -1:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 6. Topological sorting and dependencies

### 23. Topological Sort — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

Use DFS finish times to order a DAG. Append a node after all its outgoing neighbors finish, then reverse the result. Return an empty list if an active-node edge reveals a cycle.

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,2,1,3] (one valid order)
```

```python
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        state = [0] * V
        order = []
        for start in range(V):
            if state[start] != 0:
                continue
            state[start] = 1
            stack = [(start, iter(adj[start]))]
            while stack:
                u, neighbors = stack[-1]
                v = next(neighbors, None)
                if v is None:
                    order.append(u)
                    state[u] = 2
                    stack.pop()
                elif state[v] == 1:
                    return []
                elif state[v] == 0:
                    state[v] = 1
                    stack.append((v, iter(adj[v])))
        return order[::-1]
```
- **Time:** O(V + E)
- **Space:** O(V + E)

### 24. Topological Sort — Kahn’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

Return a valid ordering of vertices in a directed acyclic graph given V and edges. Returns an empty array/list if a cycle exists.

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,1,2,3] (one valid order)
```

```python
from collections import deque

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
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return order if len(order) == n else []
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 25. Course Schedule II — 210

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule-ii/)

Return a valid course order, or an empty array/list when a cycle makes completion impossible.

```text
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] (one valid order)
```

```python
from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        n = numCourses
        adj = [[] for _ in range(n)]
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
        indegree = [0] * n
        for neighbors in adj:
            for v in neighbors:
                indegree[v] += 1
        queue = deque(u for u in range(n) if indegree[u] == 0)
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return order if len(order) == n else []
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 26. Alien Dictionary — 269

[LeetCode/GFG Link](https://leetcode.com/problems/alien-dictionary/)

Infer any valid ordering of the lowercase letters appearing in sorted alien words. Return an empty string for a cycle or invalid prefix order. LeetCode 269 is Premium. The workbook method is named findOrder.

```text
Input: words = ["za","zb","ca","cb"]
Output: "zacb" (one valid order; z before c and a before b)
```

```python
from collections import deque

class Solution:
    def findOrder(self, words):
        adj = {ch: set() for word in words for ch in word}
        degree = dict.fromkeys(adj, 0)
        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        degree[b] += 1
                    break
            else:
                if len(first) > len(second):
                    return ''
        queue = deque(ch for ch in adj if degree[ch] == 0)
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
- **Time:** O(S + A + E), where S is total input characters, A distinct letters, and E distinct ordering constraints.
- **Space:** O(A + E), excluding input word storage.

### 27. Find All Possible Recipes from Given Supplies — 2115

[LeetCode/GFG Link](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)

Process supplies as available nodes. Each ingredient unlocks dependent recipes by reducing their remaining ingredient count. Enqueue a recipe when all its ingredients are available; cyclic or missing dependencies remain unresolved. Supplies are unlimited.

```text
Input: recipes = ["tea","combo"], ingredients = [["water","leaf"],["tea","bread"]], supplies = ["water","leaf","bread"]
Output: ["tea","combo"]
```

```python
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        dependents = defaultdict(list)
        remaining = [len(items) for items in ingredients]
        for i, items in enumerate(ingredients):
            for item in items:
                dependents[item].append(i)
        queue = deque(supplies)
        available = set(supplies)
        for i, recipe in enumerate(recipes):
            if remaining[i] == 0 and recipe not in available:
                available.add(recipe)
                queue.append(recipe)
        while queue:
            item = queue.popleft()
            for i in dependents[item]:
                remaining[i] -= 1
                if remaining[i] == 0 and recipes[i] not in available:
                    available.add(recipes[i])
                    queue.append(recipes[i])
        return [recipe for recipe in recipes if recipe in available]
```
- **Time:** O(N + I + S) expected hash-table operations; N = recipes, I = ingredient occurrences, S = supplies. String hashing additionally depends on string lengths.
- **Space:** O(N + I + S).

## 7. Unweighted shortest paths and state-based BFS

### 28. Shortest Path in an Undirected Graph with Unit Weights

[LeetCode/GFG Link](https://www.geeksforgeeks.org/dsa/shortest-path-in-undirected-graph-having-unit-distance/)

Find distances from src in an undirected, unweighted graph with V vertices. Return −1 for unreachable vertices.

```text
Input: V = 4, edges = [[0,1],[1,2]], src = 0
Output: [0,1,2,-1]
```

```python
from collections import deque

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
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 29. Shortest Path in Binary Matrix — 1091

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

Find the shortest 8-directional path of 0s from top-left to bottom-right in an n × n grid. Count visited cells; return −1 if impossible. Updates the grid.

```text
Input: grid = [[0,1],[1,0]]
Output: 2
```

```python
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            r, c, length = queue.popleft()
            if r == n - 1 and c == n - 1:
                return length
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == dc == 0:
                        continue
                    x, y = r + dr, c + dc
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x, y, length + 1))
        return -1
```
- **Time:** O(n²)
- **Space:** O(n²) for the BFS queue.

### 30. Word Ladder — 127

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

```python
from collections import deque
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
- **Time:** O((N + 1) × 26 × L²), including string construction/hashing; N = dictionary size.
- **Space:** O((N + 1) × L), for dictionary/queue strings of length L; N = dictionary size.

### 31. Open the Lock — 752

[LeetCode/GFG Link](https://leetcode.com/problems/open-the-lock/)

Find the minimum wheel turns from 0000 to target while avoiding deadends; return −1 if impossible. Each state has four decimal digits.

```text
Input: deadends = [], target = "0009"
Output: 1
```

```python
from collections import deque

class Solution:
    def openLock(self, deadends, target):
        seen = set(deadends)
        if '0000' in seen:
            return -1
        queue = deque([('0000', 0)])
        seen.add('0000')
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            for i in range(4):
                for delta in (-1, 1):
                    digit = str((int(state[i]) + delta) % 10)
                    nxt = state[:i] + digit + state[i + 1:]
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, turns + 1))
        return -1
```
- **Time:** O(D + 10⁴ × 8) for four fixed digits; D = number of deadends.
- **Space:** O(D + 10⁴) for fixed four-digit states; D = deadends.

### 32. Snakes and Ladders — 909

[LeetCode/GFG Link](https://leetcode.com/problems/snakes-and-ladders/)

Use BFS over square numbers to find the minimum dice rolls from 1 to n². Convert each square to its boustrophedon board coordinate. Follow at most one snake or ladder per roll; return −1 if the target is unreachable.

```text
Input: board = [[-1,-1],[-1,-1]]
Output: 1
```

```python
from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        queue = deque([(1, 0)])
        seen = {1}
        while queue:
            square, rolls = queue.popleft()
            if square == n * n:
                return rolls
            for nxt in range(square + 1, min(square + 6, n * n) + 1):
                row_from_bottom, col = divmod(nxt - 1, n)
                row = n - 1 - row_from_bottom
                if row_from_bottom % 2:
                    col = n - 1 - col
                dest = board[row][col] if board[row][col] != -1 else nxt
                if dest not in seen:
                    seen.add(dest)
                    queue.append((dest, rolls + 1))
        return -1
```
- **Time:** O(n²)
- **Space:** O(n²).

## 8. Weighted shortest paths

### 33. Dijkstra’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1)

Find shortest distances from src in an undirected graph with nonnegative edge weights. Edges are [u, v, weight]; unreachable vertices return −1.

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,9]], src = 0
Output: [0,4,6]
```

```python
from heapq import heappop, heappush

class Solution:
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        dist = [float('inf')] * V
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            cost, u = heappop(heap)
            if cost != dist[u]:
                continue
            for v, weight in adj[u]:
                candidate = cost + weight
                if candidate < dist[v]:
                    dist[v] = candidate
                    heappush(heap, (candidate, v))
        return [-1 if d == float('inf') else d for d in dist]
```
- **Time:** O(V + E log(E + 2)) with a heap that can retain outdated entries.
- **Space:** O(V + E), including the adjacency list and heap with outdated entries.

### 34. Network Delay Time — 743

[LeetCode/GFG Link](https://leetcode.com/problems/network-delay-time/)

Find when all nodes receive a signal from k, or −1 if some cannot. Directed edges times use labels 1 through n and nonnegative travel times.

```text
Input: times = [[1,2,2],[2,3,1]], n = 3, k = 1
Output: 3
```

```python
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times, n, k):
        V, edges, src = n + 1, times, k
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
        dist = [float('inf')] * V
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            cost, u = heappop(heap)
            if cost != dist[u]:
                continue
            for v, weight in adj[u]:
                candidate = cost + weight
                if candidate < dist[v]:
                    dist[v] = candidate
                    heappush(heap, (candidate, v))
        answer = max(dist[1:])
        return -1 if answer == float('inf') else answer
```
- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 35. Path With Minimum Effort — 1631

[LeetCode/GFG Link](https://leetcode.com/problems/path-with-minimum-effort/)

Minimize the largest absolute height difference along a 4-directional path from top-left to bottom-right in a nonempty grid.

```text
Input: heights = [[1,3],[2,4]]
Output: 2
```

```python
from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            effort, r, c = heappop(heap)
            if effort != dist[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols:
                    candidate = max(effort, abs(heights[x][y] - heights[r][c]))
                    if candidate < dist[x][y]:
                        dist[x][y] = candidate
                        heappush(heap, (candidate, x, y))
        return 0
```
- **Time:** O(RC log(RC + 1))
- **Space:** O(R × C) for distances and the heap (a grid has O(R × C) edges).

### 36. Cheapest Flights Within K Stops — 787

[LeetCode/GFG Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest route from src to dst using at most k stops (k + 1 edges). Each relaxation round reads only the previous round’s distances.

```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
```

```python
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(k + 1):
            next_dist = dist.copy()
            for u, v, price in flights:
                next_dist[v] = min(next_dist[v], dist[u] + price)
            dist = next_dist
        return -1 if dist[dst] == float('inf') else dist[dst]
```
- **Time:** O((k + 1) × (V + E))
- **Space:** O(V) for two distance arrays.

### 37. Bellman–Ford Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1)

Find distances from src in a directed graph with negative weights allowed. Return [-1] for a reachable negative cycle; use 100000000 for unreachable vertices (GFG convention).

```text
Input: V = 3, edges = [[0,1,4],[1,2,-2],[0,2,5]], src = 0
Output: [0,4,2]
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
            if not changed:
                break
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                return [-1]
        return [100000000 if d == inf else d for d in dist]
```
- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 38. Negative Cycle Detection

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1)

Detect a negative-weight cycle anywhere in a directed graph, including disconnected components. Initialize every distance to zero, equivalent to a super-source. An improvement on the Vth Bellman–Ford pass proves a negative cycle. Return 1 if found, otherwise 0.

```text
Input: V = 4, edges = [[0,1,2],[2,3,-2],[3,2,1]]
Output: 1 (negative cycle is disconnected from vertex 0)
```

```python
class Solution:
    def isNegativeWeightCycle(self, V, edges):
        dist = [0] * V
        for step in range(V):
            changed = False
            for u, v, weight in edges:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    changed = True
                    if step == V - 1:
                        return 1
            if not changed:
                return 0
        return 0
```
- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 39. Floyd–Warshall Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1)

Find all-pairs shortest paths in place. Input matrix has 0 on its diagonal and 100000000 for no edge; negative weights are allowed, but no negative cycles. Finite distances have absolute value below 100000000.

```text
Input: dist = [[0,3,100000000],[100000000,0,2],[100000000,100000000,0]]
Output: dist becomes [[0,3,5],[100000000,0,2],[100000000,100000000,0]]; no return value
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
- **Time:** O(V³)
- **Space:** O(1) auxiliary; the O(V²) input distance matrix is updated in place.

### 40. Find the City With the Smallest Number of Neighbors at a Threshold Distance — 1334

[LeetCode/GFG Link](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

Use Floyd–Warshall for all-pairs shortest distances in an undirected weighted graph. Count other cities within distanceThreshold. On equal counts, choose the city with the larger index.

```text
Input: n = 4, edges = [[0,1,2],[1,2,2],[2,3,2]], distanceThreshold = 2
Output: 3
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
            count = sum(i != j and dist[i][j] <= distanceThreshold for j in range(n))
            if count <= best:
                best, answer = count, i
        return answer
```
- **Time:** O(n³ + E)
- **Space:** O(n²).

### 41. Shortest Path in a Directed Acyclic Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1)

Find distances from vertex 0 in a nonempty DAG with edges [u, v, weight]. Relax edges in topological order; unreachable vertices return −1.

```text
Input: V = 4, edges = [[0,1,2],[0,2,5],[1,2,-1]]
Output: [0,2,1,-1]
```

```python
from collections import deque

class Solution:
    def shortestPath(self, V, edges):
        adj = [[] for _ in range(V)]
        degree = [0] * V
        for u, v, w in edges:
            adj[u].append((v, w))
            degree[v] += 1
        queue = deque(u for u in range(V) if degree[u] == 0)
        dist = [float('inf')] * V
        dist[0] = 0
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if dist[u] != float('inf'):
                    dist[v] = min(dist[v], dist[u] + w)
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)
        return [-1 if d == float('inf') else d for d in dist]
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 9. Disjoint Set Union — Union-Find

### 42. Implement DSU — Path Compression and Union by Size

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1)

Maintain disjoint sets for elements 0 through n − 1 using path compression and union by size. union returns whether two different components were merged.

```text
Input: DSU(4); union(0,1); union(1,2); union(0,2); find(0) == find(2); find(0) == find(3)
Output: true; true; false; true; false (initialization has no output)
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True
```
- **Time:** O(n) initialization; O(α(n)) amortized per find/union, where α is the inverse Ackermann function.
- **Space:** O(n) for parent and size arrays.

### 43. Redundant Connection — 684

[LeetCode/GFG Link](https://leetcode.com/problems/redundant-connection/)

An undirected tree on labels 1 through n has one extra edge. Return the edge that creates a cycle when edges are processed in input order.

```text
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []
```
- **Time:** O(n × α(n))
- **Space:** O(n) for DSU.

### 44. Number of Operations to Make Network Connected — 1319

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Return the fewest cable moves to connect all n computers, or −1 if there are fewer than n − 1 cables.

```text
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
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
- **Time:** O(V + E × α(V))
- **Space:** O(V) for DSU.

### 45. Accounts Merge — 721

[LeetCode/GFG Link](https://leetcode.com/problems/accounts-merge/)

Merge accounts sharing an email and sort each merged email list. Each account has a name and at least one email; shared-email accounts have the same name.

```text
Input: accounts = [["Mira","a@x.com","b@x.com"],["Mira","b@x.com","c@x.com"],["Noah","n@x.com"]]
Output: [["Mira","a@x.com","b@x.com","c@x.com"],["Noah","n@x.com"]] (account groups may appear in any order)
```

```python
from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU(len(accounts))
        owner = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in owner:
                    dsu.union(i, owner[email])
                else:
                    owner[email] = i
        groups = defaultdict(list)
        for email, i in owner.items():
            groups[dsu.find(i)].append(email)
        return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
```
- **Time:** O(A + M × (L + α(A)) + U log(U + 1) × L), where A = accounts, M = email occurrences, U = unique emails, L = maximum email length.
- **Space:** O(A + M + U × L), including temporary email lists and output; sorting can also use linear temporary storage.

### 46. Most Stones Removed with Same Row or Column — 947

[LeetCode/GFG Link](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

Model stones as nodes. Union stones sharing a row or column, using a representative map for each coordinate. Each connected component must keep one stone; return the number of stones minus the number of components.

```text
Input: stones = [[0,0],[0,1],[1,1],[3,4]]
Output: 2
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def removeStones(self, stones):
        dsu = DSU(len(stones))
        rows, cols = {}, {}
        components = len(stones)
        for i, (row, col) in enumerate(stones):
            if row in rows and dsu.union(i, rows[row]):
                components -= 1
            if col in cols and dsu.union(i, cols[col]):
                components -= 1
            rows[row] = cols[col] = i
        return len(stones) - components
```
- **Time:** O(n × α(n)) expected, where n = stones; hash-map operations are expected O(1).
- **Space:** O(n).

## 10. Minimum spanning tree

### 47. Kruskal’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1)

Find the MST weight of a connected undirected graph with edges [u, v, weight]. Process edges by weight and merge different components.

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,7]]
Output: 6
```

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def spanningTree(self, V, edges):
        dsu = DSU(V)
        total = 0
        for u, v, w in sorted(edges, key=lambda e: e[2]):
            if dsu.union(u, v):
                total += w
        return total
```
- **Time:** O(V + E log(E + 2) + E × α(V))
- **Space:** O(V + E), including DSU and the sorted edge copy.

### 48. Prim’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

Find the MST weight of an undirected connected graph with V ≥ 1 and edges [u, v, weight]. Add the cheapest edge reaching an unused vertex.

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,7]]
Output: 6
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
- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 49. Min Cost to Connect All Points — 1584

[LeetCode/GFG Link](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Connect all points with minimum total Manhattan distance. Use dense Prim without building all pairwise edges.

```text
Input: points = [[0,0],[2,0],[2,2]]
Output: 4
```

```python
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        if n == 0:
            return 0
        best = [float('inf')] * n
        used = [False] * n
        best[0] = 0
        total = 0
        for _ in range(n):
            u = min((i for i in range(n) if not used[i]), key=lambda i: best[i])
            used[u] = True
            total += best[u]
            for v in range(n):
                if not used[v]:
                    distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    best[v] = min(best[v], distance)
        return total
```
- **Time:** O(n²)
- **Space:** O(n), excluding input points.

## 11. Strongly connected components and connectivity

### 50. Kosaraju’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

Count strongly connected components in a directed graph given V and edges. Record DFS finish order, then traverse the reversed graph in reverse finish order.

```text
Input: V = 4, edges = [[0,1],[1,0],[1,2],[2,3],[3,2]]
Output: 2
```

```python
class Solution:
    def kosaraju(self, V, edges):
        adj = [[] for _ in range(V)]
        reverse = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            reverse[v].append(u)
        seen = set()
        order = []
        for start in range(V):
            if start in seen:
                continue
            seen.add(start)
            stack = [(start, iter(adj[start]))]
            while stack:
                u, neighbors = stack[-1]
                v = next(neighbors, None)
                if v is None:
                    order.append(u)
                    stack.pop()
                elif v not in seen:
                    seen.add(v)
                    stack.append((v, iter(adj[v])))
        seen.clear()
        count = 0
        for start in reversed(order):
            if start in seen:
                continue
            count += 1
            seen.add(start)
            stack = [start]
            while stack:
                u = stack.pop()
                for v in reverse[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
        return count
```
- **Time:** O(V + E)
- **Space:** O(V + E), including both adjacency lists.

### 51. Critical Connections in a Network — 1192

[LeetCode/GFG Link](https://leetcode.com/problems/critical-connections-in-a-network/)

Find bridges: edges whose removal increases the number of connected components. Iterative DFS tracks discovery times and the lowest reachable ancestor; edge IDs handle parallel edges.

```text
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]] (edge endpoints may be reversed)
```

```python
class Solution:
    def criticalConnections(self, n, connections):
        adj = [[] for _ in range(n)]
        for eid, (u, v) in enumerate(connections):
            adj[u].append((v, eid))
            adj[v].append((u, eid))
        tin = [-1] * n
        low = [0] * n
        parent = [-1] * n
        parent_edge = [-1] * n
        timer = 0
        bridges = []
        for start in range(n):
            if tin[start] != -1:
                continue
            tin[start] = low[start] = timer
            timer += 1
            stack = [(start, iter(adj[start]))]
            while stack:
                u, neighbors = stack[-1]
                edge = next(neighbors, None)
                if edge is None:
                    stack.pop()
                    p = parent[u]
                    if p != -1:
                        if low[u] > tin[p]:
                            bridges.append([p, u])
                        low[p] = min(low[p], low[u])
                    continue
                v, eid = edge
                if eid == parent_edge[u]:
                    continue
                if tin[v] == -1:
                    parent[v], parent_edge[v] = u, eid
                    tin[v] = low[v] = timer
                    timer += 1
                    stack.append((v, iter(adj[v])))
                else:
                    low[u] = min(low[u], tin[v])
        return bridges
```
- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 12. Other important graph patterns

### 52. Evaluate Division — 399

[LeetCode/GFG Link](https://leetcode.com/problems/evaluate-division/)

For a / b = value, store edges a → b with value and b → a with its reciprocal. For each query, DFS multiplies edge weights along a path. Unknown or disconnected variables return −1.0; a known variable divided by itself returns 1.0. Equations are consistent.

```text
Input: equations = [["x","y"],["y","z"]], values = [4.0,2.0], queries = [["x","z"],["z","x"],["u","u"]]
Output: [8.0,0.125,-1.0]
```

```python
from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))
        def evaluate(source, target):
            if source not in graph or target not in graph:
                return -1.0
            stack = [(source, 1.0)]
            seen = {source}
            while stack:
                node, product = stack.pop()
                if node == target:
                    return product
                for neighbor, weight in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, product * weight))
            return -1.0
        return [evaluate(a, b) for a, b in queries]
```
- **Time:** O(V + E + Q(V + E)) expected map/set operations; Q = queries. Variable-name hashing additionally depends on string length.
- **Space:** O(V + E) auxiliary, plus O(Q) output.

### 53. All Paths From Source to Target — 797

[LeetCode/GFG Link](https://leetcode.com/problems/all-paths-from-source-to-target/)

Given a DAG adjacency list, enumerate every path from node 0 to node n − 1. Use DFS/backtracking: append a neighbor before exploring and remove it afterward. A global visited set would incorrectly discard distinct paths.

```text
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]] (any order)
```

```python
class Solution:
    def allPathsSourceTarget(self, graph):
        result, path = [], [0]
        def dfs(node):
            if node == len(graph) - 1:
                result.append(path.copy())
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()
        dfs(0)
        return result
```
- **Time:** O(V × 2^V) worst case, including path copies; the number of paths can be exponential.
- **Space:** O(V) auxiliary for the path and recursion, plus O(V × 2^V) worst-case output.

### 54. Longest Increasing Path in a Matrix — 329

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

Strictly increasing edges form a DAG. DFS memoizes the longest path starting at each cell, so each cell is solved once. The alternative topological-layer solution avoids recursion depth limits on long paths.

```text
Input: matrix = [[3,4],[2,5]]
Output: 4
```

**DFS + memoization**

```python
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        @lru_cache(None)
        def dfs(r, c):
            best = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best
        return max(dfs(r, c) for r in range(rows) for c in range(cols))
```

**Topological layers — avoids recursion**

```python
from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        degree = [[0] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        degree[r][c] += 1
                if degree[r][c] == 0:
                    queue.append((r, c))
        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                        degree[nr][nc] -= 1
                        if degree[nr][nc] == 0:
                            queue.append((nr, nc))
            length += 1
        return length
```
- **Time:** O(R × C)
- **Space:** O(R × C).
