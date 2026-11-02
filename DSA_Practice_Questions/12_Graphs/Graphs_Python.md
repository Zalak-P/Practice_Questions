# Graphs — Python

V = vertices, E = edges; R and C = grid rows and columns.

## Traversal

### 1. BFS Traversal

[Problem](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

Visit vertices reachable from vertex 0 in breadth-first order. Input: adjacency list; an empty graph returns an empty list.

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

**Time complexity:** O(V + E)

### 2. DFS Traversal

[Problem](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

Visit vertices reachable from vertex 0 in depth-first order, following adjacency-list order. Use explicit stack frames.

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

**Time complexity:** O(V + E)

### 3. Path Exists

[Problem](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Check whether source can reach destination in an undirected graph with vertices 0 through n − 1.

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

**Time complexity:** O(V + E)

### 4. Connected Components

[Problem](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Count connected components, including isolated vertices, in an undirected graph. LeetCode 323 is Premium.

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

**Time complexity:** O(V + E)

### 5. Clone Graph

[Problem](https://leetcode.com/problems/clone-graph/)

Deep-copy the connected component reachable from node. The Node definition is included; use the judge-provided definition on LeetCode.

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

**Time complexity:** O(V + E)

## Grid Traversal

### 6. Number of Islands

[Problem](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

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

**Time complexity:** O(R × C)

### 7. Flood Fill

[Problem](https://leetcode.com/problems/flood-fill/)

Recolor the 4-connected component containing (sr, sc) in a nonempty image. Updates the image in place.

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

**Time complexity:** O(R × C)

### 8. Max Island Area

[Problem](https://leetcode.com/problems/max-area-of-island/)

Return the largest 4-connected area of 1s in a nonempty binary grid. Visited land is changed to 0.

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

**Time complexity:** O(R × C)

### 9. Rotting Oranges

[Problem](https://leetcode.com/problems/rotting-oranges/)

Spread rot from all rotten oranges simultaneously in a nonempty grid. Return minutes until all fresh oranges rot, or −1. Updates the grid.

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

**Time complexity:** O(R × C)

### 10. 01 Matrix

[Problem](https://leetcode.com/problems/01-matrix/)

Find each cell’s distance to its nearest 0 using multi-source BFS. The nonempty binary matrix contains at least one 0.

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

**Time complexity:** O(R × C)

### 11. Surrounded Regions

[Problem](https://leetcode.com/problems/surrounded-regions/)

Flip enclosed 'O' regions to 'X' in place. First preserve all 'O' cells connected to the boundary of the nonempty board.

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

**Time complexity:** O(R × C)

### 12. Pacific Atlantic

[Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Find cells from which water reaches both oceans. Search backward from ocean boundaries to equal or higher cells in the nonempty height grid.

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

**Time complexity:** O(R × C)

### 13. Shortest Binary Path

[Problem](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

Find the shortest 8-directional path of 0s from top-left to bottom-right in an n × n grid. Count visited cells; return −1 if impossible. Updates the grid.

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

**Time complexity:** O(n²)

### 14. Shortest Bridge

[Problem](https://leetcode.com/problems/shortest-bridge/)

Given exactly two 4-connected islands, return the fewest water cells to flip to connect them. Mark one island, then expand it by BFS. Updates the grid.

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

**Time complexity:** O(R × C)

## Cycle Detection and Bipartite Graphs

### 15. Undirected Cycle

[Problem](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

Detect a cycle in any component of an undirected graph. Input edges use vertices 0 through V − 1; edge IDs distinguish parallel edges.

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

**Time complexity:** O(V + E)

### 16. Directed Cycle

[Problem](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using Kahn’s algorithm: a cycle exists if not all vertices can be removed. Input: V and directed edges.

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

**Time complexity:** O(V + E)

### 17. Course Schedule

[Problem](https://leetcode.com/problems/course-schedule/)

Determine whether all courses can be completed. Each prerequisite pair is [course, prerequisite].

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

**Time complexity:** O(V + E)

### 18. Bipartite Graph

[Problem](https://leetcode.com/problems/is-graph-bipartite/)

Check whether an undirected adjacency-list graph can be colored with two colors so adjacent vertices differ. Covers disconnected components.

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

**Time complexity:** O(V + E)

### 19. Possible Bipartition

[Problem](https://leetcode.com/problems/possible-bipartition/)

Split people labeled 1 through n into two groups so every disliked pair is separated. Build an undirected graph and two-color it.

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

**Time complexity:** O(V + E)

## Topological Sort

### 20. Topological Sort

[Problem](https://www.geeksforgeeks.org/problems/topological-sort/1)

Return a valid ordering of vertices in a directed acyclic graph given V and edges. Returns an empty array/list if a cycle exists.

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

**Time complexity:** O(V + E)

### 21. Course Schedule II

[Problem](https://leetcode.com/problems/course-schedule-ii/)

Return a valid course order, or an empty array/list when a cycle makes completion impossible.

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

**Time complexity:** O(V + E)

### 22. Eventual Safe States

[Problem](https://leetcode.com/problems/find-eventual-safe-states/)

Return sorted vertices whose every path eventually terminates. Start with terminal vertices and remove edges in the reversed graph.

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

**Time complexity:** O(V + E)

### 23. Alien Dictionary

[Problem](https://www.geeksforgeeks.org/problems/alien-dictionary/1)

Infer any valid ordering of the lowercase letters appearing in sorted alien words. Return an empty string for a cycle or invalid prefix order.

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

**Time complexity:** O(S + A + E), where S is total input characters, A distinct letters, and E distinct ordering constraints.

## Shortest Paths

### 24. Unit-Weight Shortest Path

[Problem](https://www.geeksforgeeks.org/dsa/shortest-path-in-undirected-graph-having-unit-distance/)

Find distances from src in an undirected, unweighted graph with V vertices. Return −1 for unreachable vertices.

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

**Time complexity:** O(V + E)

### 25. DAG Shortest Path

[Problem](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1)

Find distances from vertex 0 in a nonempty DAG with edges [u, v, weight]. Relax edges in topological order; unreachable vertices return −1.

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

**Time complexity:** O(V + E)

### 26. Dijkstra

[Problem](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1)

Find shortest distances from src in an undirected graph with nonnegative edge weights. Edges are [u, v, weight]; unreachable vertices return −1.

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

**Time complexity:** O(V + E log(E + 2)) with a heap that can retain outdated entries.

### 27. Network Delay

[Problem](https://leetcode.com/problems/network-delay-time/)

Find when all nodes receive a signal from k, or −1 if some cannot. Directed edges times use labels 1 through n and nonnegative travel times.

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

**Time complexity:** O(V + E log(E + 2))

### 28. Minimum Effort Path

[Problem](https://leetcode.com/problems/path-with-minimum-effort/)

Minimize the largest absolute height difference along a 4-directional path from top-left to bottom-right in a nonempty grid.

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

**Time complexity:** O(RC log(RC + 1))

### 29. Cheapest Flights

[Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest route from src to dst using at most k stops (k + 1 edges). Each relaxation round reads only the previous round’s distances.

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

**Time complexity:** O((k + 1) × (V + E))

### 30. Bellman–Ford

[Problem](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1)

Find distances from src in a directed graph with negative weights allowed. Return [-1] for a reachable negative cycle; use 100000000 for unreachable vertices (GFG convention).

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

**Time complexity:** O(V + VE)

### 31. Floyd–Warshall

[Problem](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1)

Find all-pairs shortest paths in place. Input matrix has 0 on its diagonal and 100000000 for no edge; negative weights are allowed, but no negative cycles. Finite distances have absolute value below 100000000.

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

**Time complexity:** O(V³)

## State-Space BFS

### 32. Word Ladder

[Problem](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

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

**Time complexity:** O((N + 1) × 26 × L²), including string construction/hashing; N = dictionary size.

### 33. Open the Lock

[Problem](https://leetcode.com/problems/open-the-lock/)

Find the minimum wheel turns from 0000 to target while avoiding deadends; return −1 if impossible. Each state has four decimal digits.

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

**Time complexity:** O(D + 10⁴ × 8) for four fixed digits; D = number of deadends.

## Disjoint Set Union

### 34. Implement DSU

[Problem](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1)

Maintain disjoint sets for elements 0 through n − 1 using path compression and union by size. union returns whether two different components were merged.

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

**Time complexity:** O(n) initialization; O(α(n)) amortized per find/union, where α is the inverse Ackermann function.

### 35. Number of Provinces

[Problem](https://leetcode.com/problems/number-of-provinces/)

Count connected groups in a symmetric n × n adjacency matrix. Scan each undirected connection once and merge its components.

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

**Time complexity:** O(n² × α(n))

### 36. Redundant Connection

[Problem](https://leetcode.com/problems/redundant-connection/)

An undirected tree on labels 1 through n has one extra edge. Return the edge that creates a cycle when edges are processed in input order.

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

**Time complexity:** O(n × α(n))

### 37. Connect Network

[Problem](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Return the fewest cable moves to connect all n computers, or −1 if there are fewer than n − 1 cables.

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

**Time complexity:** O(V + E × α(V))

### 38. Accounts Merge

[Problem](https://leetcode.com/problems/accounts-merge/)

Merge accounts sharing an email and sort each merged email list. Each account has a name and at least one email; shared-email accounts have the same name.

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

**Time complexity:** O(A + M × (L + α(A)) + U log(U + 1) × L), where A = accounts, M = email occurrences, U = unique emails, L = maximum email length.

## Minimum Spanning Tree

### 39. Prim’s Algorithm

[Problem](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

Find the MST weight of an undirected connected graph with V ≥ 1 and edges [u, v, weight]. Add the cheapest edge reaching an unused vertex.

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

**Time complexity:** O(V + E log(E + 2))

### 40. Kruskal’s Algorithm

[Problem](https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1)

Find the MST weight of a connected undirected graph with edges [u, v, weight]. Process edges by weight and merge different components.

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

**Time complexity:** O(V + E log(E + 2) + E × α(V))

### 41. Connect All Points

[Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Connect all points with minimum total Manhattan distance. Use dense Prim without building all pairwise edges.

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

**Time complexity:** O(n²)

## Advanced Graph Algorithms

### 42. Kosaraju’s Algorithm

[Problem](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

Count strongly connected components in a directed graph given V and edges. Record DFS finish order, then traverse the reversed graph in reverse finish order.

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

**Time complexity:** O(V + E)

### 43. Critical Connections

[Problem](https://leetcode.com/problems/critical-connections-in-a-network/)

Find bridges: edges whose removal increases the number of connected components. Iterative DFS tracks discovery times and the lowest reachable ancestor; edge IDs handle parallel edges.

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

**Time complexity:** O(V + E)
