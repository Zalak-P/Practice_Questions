# Graphs — Java

V = vertices, E = edges; R and C = grid rows and columns.

## Traversal

### 1. BFS Traversal

[Problem](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

Visit vertices reachable from vertex 0 in breadth-first order. Input: adjacency list; an empty graph returns an empty list.

```java
import java.util.*;

class Solution {
    public List<Integer> bfs(List<List<Integer>> adj) {
        List<Integer> order = new ArrayList<>();
        if (adj.isEmpty()) return order;
        boolean[] seen = new boolean[adj.size()];
        Queue<Integer> queue = new ArrayDeque<>();
        seen[0] = true;
        queue.add(0);
        while (!queue.isEmpty()) {
            int u = queue.remove();
            order.add(u);
            for (int v : adj.get(u)) {
                if (!seen[v]) {
                    seen[v] = true;
                    queue.add(v);
                }
            }
        }
        return order;
    }
}
```

**Time complexity:** O(V + E)

### 2. DFS Traversal

[Problem](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

Visit vertices reachable from vertex 0 in depth-first order, following adjacency-list order. Use explicit stack frames.

```java
import java.util.*;

class Solution {
    public List<Integer> dfs(List<List<Integer>> adj) {
        List<Integer> order = new ArrayList<>();
        if (adj.isEmpty()) return order;
        boolean[] seen = new boolean[adj.size()];
        Deque<int[]> stack = new ArrayDeque<>();
        seen[0] = true;
        order.add(0);
        stack.push(new int[]{0, 0});
        while (!stack.isEmpty()) {
            int[] frame = stack.peek();
            int u = frame[0];
            if (frame[1] == adj.get(u).size()) {
                stack.pop();
                continue;
            }
            int v = adj.get(u).get(frame[1]++);
            if (!seen[v]) {
                seen[v] = true;
                order.add(v);
                stack.push(new int[]{v, 0});
            }
        }
        return order;
    }
}
```

**Time complexity:** O(V + E)

### 3. Path Exists

[Problem](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Check whether source can reach destination in an undirected graph with vertices 0 through n − 1.

```java
import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] seen = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(source);
        seen[source] = true;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            if (u == destination) return true;
            for (int v : adj.get(u)) {
                if (!seen[v]) {
                    seen[v] = true;
                    stack.push(v);
                }
            }
        }
        return false;
    }
}
```

**Time complexity:** O(V + E)

### 4. Connected Components

[Problem](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Count connected components, including isolated vertices, in an undirected graph. LeetCode 323 is Premium.

```java
import java.util.*;

class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] seen = new boolean[n];
        int count = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        for (int start = 0; start < n; start++) {
            if (seen[start]) continue;
            count++;
            seen[start] = true;
            stack.push(start);
            while (!stack.isEmpty()) {
                int u = stack.pop();
                for (int v : adj.get(u)) {
                    if (!seen[v]) {
                        seen[v] = true;
                        stack.push(v);
                    }
                }
            }
        }
        return count;
    }
}
```

**Time complexity:** O(V + E)

### 5. Clone Graph

[Problem](https://leetcode.com/problems/clone-graph/)

Deep-copy the connected component reachable from node. The Node definition is included; use the judge-provided definition on LeetCode.

```java
import java.util.*;

class Node {
    public int val;
    public List<Node> neighbors = new ArrayList<>();
    public Node(int val) { this.val = val; }
}

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Map<Node, Node> copies = new HashMap<>();
        Queue<Node> queue = new ArrayDeque<>();
        copies.put(node, new Node(node.val));
        queue.add(node);
        while (!queue.isEmpty()) {
            Node u = queue.remove();
            for (Node v : u.neighbors) {
                if (!copies.containsKey(v)) {
                    copies.put(v, new Node(v.val));
                    queue.add(v);
                }
                copies.get(u).neighbors.add(copies.get(v));
            }
        }
        return copies.get(node);
    }
}
```

**Time complexity:** O(V + E)

## Grid Traversal

### 6. Number of Islands

[Problem](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

```java
import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length, count = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Deque<int[]> stack = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != '1') continue;
                count++;
                grid[r][c] = '0';
                stack.push(new int[]{r, c});
                while (!stack.isEmpty()) {
                    int[] cell = stack.pop();
                    for (int[] d : dirs) {
                        int x = cell[0] + d[0], y = cell[1] + d[1];
                        if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] == '1') {
                            grid[x][y] = '0';
                            stack.push(new int[]{x, y});
                        }
                    }
                }
            }
        }
        return count;
    }
}
```

**Time complexity:** O(R × C)

### 7. Flood Fill

[Problem](https://leetcode.com/problems/flood-fill/)

Recolor the 4-connected component containing (sr, sc) in a nonempty image. Updates the image in place.

```java
import java.util.*;

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int old = image[sr][sc];
        if (old == color) return image;
        int rows = image.length, cols = image[0].length;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Deque<int[]> stack = new ArrayDeque<>();
        image[sr][sc] = color;
        stack.push(new int[]{sr, sc});
        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            for (int[] d : dirs) {
                int x = cell[0] + d[0], y = cell[1] + d[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && image[x][y] == old) {
                    image[x][y] = color;
                    stack.push(new int[]{x, y});
                }
            }
        }
        return image;
    }
}
```

**Time complexity:** O(R × C)

### 8. Max Island Area

[Problem](https://leetcode.com/problems/max-area-of-island/)

Return the largest 4-connected area of 1s in a nonempty binary grid. Visited land is changed to 0.

```java
import java.util.*;

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length, best = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Deque<int[]> stack = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != 1) continue;
                grid[r][c] = 0;
                stack.push(new int[]{r, c});
                int area = 0;
                while (!stack.isEmpty()) {
                    int[] cell = stack.pop();
                    area++;
                    for (int[] d : dirs) {
                        int x = cell[0] + d[0], y = cell[1] + d[1];
                        if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] == 1) {
                            grid[x][y] = 0;
                            stack.push(new int[]{x, y});
                        }
                    }
                }
                best = Math.max(best, area);
            }
        }
        return best;
    }
}
```

**Time complexity:** O(R × C)

### 9. Rotting Oranges

[Problem](https://leetcode.com/problems/rotting-oranges/)

Spread rot from all rotten oranges simultaneously in a nonempty grid. Return minutes until all fresh oranges rot, or −1. Updates the grid.

```java
import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length, fresh = 0, minutes = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) queue.add(new int[]{r, c});
                else if (grid[r][c] == 1) fresh++;
            }
        }
        while (!queue.isEmpty() && fresh > 0) {
            int size = queue.size();
            while (size-- > 0) {
                int[] cell = queue.remove();
                for (int[] d : dirs) {
                    int x = cell[0] + d[0], y = cell[1] + d[1];
                    if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] == 1) {
                        grid[x][y] = 2;
                        fresh--;
                        queue.add(new int[]{x, y});
                    }
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
}
```

**Time complexity:** O(R × C)

### 10. 01 Matrix

[Problem](https://leetcode.com/problems/01-matrix/)

Find each cell’s distance to its nearest 0 using multi-source BFS. The nonempty binary matrix contains at least one 0.

```java
import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        int[][] dist = new int[rows][cols];
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            Arrays.fill(dist[r], -1);
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) {
                    dist[r][c] = 0;
                    queue.add(new int[]{r, c});
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] cell = queue.remove();
            for (int[] d : dirs) {
                int x = cell[0] + d[0], y = cell[1] + d[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && dist[x][y] == -1) {
                    dist[x][y] = dist[cell[0]][cell[1]] + 1;
                    queue.add(new int[]{x, y});
                }
            }
        }
        return dist;
    }
}
```

**Time complexity:** O(R × C)

### 11. Surrounded Regions

[Problem](https://leetcode.com/problems/surrounded-regions/)

Flip enclosed 'O' regions to 'X' in place. First preserve all 'O' cells connected to the boundary of the nonempty board.

```java
import java.util.*;

class Solution {
    public void solve(char[][] board) {
        int rows = board.length, cols = board[0].length;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if ((r == 0 || r == rows - 1 || c == 0 || c == cols - 1) && board[r][c] == 'O') {
                    board[r][c] = '#';
                    queue.add(new int[]{r, c});
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] cell = queue.remove();
            for (int[] d : dirs) {
                int x = cell[0] + d[0], y = cell[1] + d[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && board[x][y] == 'O') {
                    board[x][y] = '#';
                    queue.add(new int[]{x, y});
                }
            }
        }
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                board[r][c] = board[r][c] == '#' ? 'O' : 'X';
    }
}
```

**Time complexity:** O(R × C)

### 12. Pacific Atlantic

[Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Find cells from which water reaches both oceans. Search backward from ocean boundaries to equal or higher cells in the nonempty height grid.

```java
import java.util.*;

class Solution {
    private boolean[][] reach(int[][] h, boolean pacific) {
        int rows = h.length, cols = h[0].length;
        boolean[][] seen = new boolean[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                boolean border = pacific ? r == 0 || c == 0 : r == rows - 1 || c == cols - 1;
                if (border) {
                    seen[r][c] = true;
                    queue.add(new int[]{r, c});
                }
            }
        }
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.remove();
            for (int[] d : dirs) {
                int x = cell[0] + d[0], y = cell[1] + d[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && !seen[x][y]
                        && h[x][y] >= h[cell[0]][cell[1]]) {
                    seen[x][y] = true;
                    queue.add(new int[]{x, y});
                }
            }
        }
        return seen;
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        boolean[][] p = reach(heights, true), a = reach(heights, false);
        List<List<Integer>> result = new ArrayList<>();
        for (int r = 0; r < heights.length; r++)
            for (int c = 0; c < heights[0].length; c++)
                if (p[r][c] && a[r][c]) result.add(Arrays.asList(r, c));
        return result;
    }
}
```

**Time complexity:** O(R × C)

### 13. Shortest Binary Path

[Problem](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

Find the shortest 8-directional path of 0s from top-left to bottom-right in an n × n grid. Count visited cells; return −1 if impossible. Updates the grid.

```java
import java.util.*;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return -1;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0, 1});
        grid[0][0] = 1;
        while (!queue.isEmpty()) {
            int[] cell = queue.remove();
            if (cell[0] == n - 1 && cell[1] == n - 1) return cell[2];
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) continue;
                    int x = cell[0] + dr, y = cell[1] + dc;
                    if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 0) {
                        grid[x][y] = 1;
                        queue.add(new int[]{x, y, cell[2] + 1});
                    }
                }
            }
        }
        return -1;
    }
}
```

**Time complexity:** O(n²)

### 14. Shortest Bridge

[Problem](https://leetcode.com/problems/shortest-bridge/)

Given exactly two 4-connected islands, return the fewest water cells to flip to connect them. Mark one island, then expand it by BFS. Updates the grid.

```java
import java.util.*;

class Solution {
    public int shortestBridge(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Deque<int[]> stack = new ArrayDeque<>();
        Queue<int[]> queue = new ArrayDeque<>();
        outer:
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    grid[r][c] = 2;
                    stack.push(new int[]{r, c});
                    queue.add(new int[]{r, c});
                    break outer;
                }
            }
        }
        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            for (int[] d : dirs) {
                int x = cell[0] + d[0], y = cell[1] + d[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] == 1) {
                    grid[x][y] = 2;
                    stack.push(new int[]{x, y});
                    queue.add(new int[]{x, y});
                }
            }
        }
        int flips = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                int[] cell = queue.remove();
                for (int[] d : dirs) {
                    int x = cell[0] + d[0], y = cell[1] + d[1];
                    if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] != 2) {
                        if (grid[x][y] == 1) return flips;
                        grid[x][y] = 2;
                        queue.add(new int[]{x, y});
                    }
                }
            }
            flips++;
        }
        return -1;
    }
}
```

**Time complexity:** O(R × C)

## Cycle Detection and Bipartite Graphs

### 15. Undirected Cycle

[Problem](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

Detect a cycle in any component of an undirected graph. Input edges use vertices 0 through V − 1; edge IDs distinguish parallel edges.

```java
import java.util.*;

class Solution {
    public boolean isCycle(int V, int[][] edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0], v = edges[i][1];
            adj.get(u).add(new int[]{v, i});
            adj.get(v).add(new int[]{u, i});
        }
        boolean[] seen = new boolean[V];
        Deque<int[]> stack = new ArrayDeque<>();
        for (int start = 0; start < V; start++) {
            if (seen[start]) continue;
            seen[start] = true;
            stack.push(new int[]{start, -1});
            while (!stack.isEmpty()) {
                int[] cur = stack.pop();
                for (int[] e : adj.get(cur[0])) {
                    if (e[1] == cur[1]) continue;
                    if (seen[e[0]]) return true;
                    seen[e[0]] = true;
                    stack.push(new int[]{e[0], e[1]});
                }
            }
        }
        return false;
    }
}
```

**Time complexity:** O(V + E)

### 16. Directed Cycle

[Problem](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using Kahn’s algorithm: a cycle exists if not all vertices can be removed. Input: V and directed edges.

```java
import java.util.*;

class Solution {
    public boolean isCyclic(int V, int[][] edges) {
        int n = V;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);
        int[] indegree = new int[n];
        for (List<Integer> neighbors : adj)
            for (int v : neighbors) indegree[v]++;
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < n; u++) if (indegree[u] == 0) queue.add(u);
        int[] order = new int[n];
        int count = 0;
        while (!queue.isEmpty()) {
            int u = queue.remove();
            order[count++] = u;
            for (int v : adj.get(u)) if (--indegree[v] == 0) queue.add(v);
        }
        return count != n;
    }
}
```

**Time complexity:** O(V + E)

### 17. Course Schedule

[Problem](https://leetcode.com/problems/course-schedule/)

Determine whether all courses can be completed. Each prerequisite pair is [course, prerequisite].

```java
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int n = numCourses;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : prerequisites) adj.get(e[1]).add(e[0]);
        int[] indegree = new int[n];
        for (List<Integer> neighbors : adj)
            for (int v : neighbors) indegree[v]++;
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < n; u++) if (indegree[u] == 0) queue.add(u);
        int[] order = new int[n];
        int count = 0;
        while (!queue.isEmpty()) {
            int u = queue.remove();
            order[count++] = u;
            for (int v : adj.get(u)) if (--indegree[v] == 0) queue.add(v);
        }
        return count == n;
    }
}
```

**Time complexity:** O(V + E)

### 18. Bipartite Graph

[Problem](https://leetcode.com/problems/is-graph-bipartite/)

Check whether an undirected adjacency-list graph can be colored with two colors so adjacent vertices differ. Covers disconnected components.

```java
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length];
        Arrays.fill(color, -1);
        Queue<Integer> queue = new ArrayDeque<>();
        for (int start = 0; start < graph.length; start++) {
            if (color[start] != -1) continue;
            color[start] = 0;
            queue.add(start);
            while (!queue.isEmpty()) {
                int u = queue.remove();
                for (int v : graph[u]) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        queue.add(v);
                    } else if (color[v] == color[u]) return false;
                }
            }
        }
        return true;
    }
}
```

**Time complexity:** O(V + E)

### 19. Possible Bipartition

[Problem](https://leetcode.com/problems/possible-bipartition/)

Split people labeled 1 through n into two groups so every disliked pair is separated. Build an undirected graph and two-color it.

```java
import java.util.*;

class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] e : dislikes) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        int[] color = new int[graph.size()];
        Arrays.fill(color, -1);
        Queue<Integer> queue = new ArrayDeque<>();
        for (int start = 0; start < graph.size(); start++) {
            if (color[start] != -1) continue;
            color[start] = 0;
            queue.add(start);
            while (!queue.isEmpty()) {
                int u = queue.remove();
                for (int v : graph.get(u)) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        queue.add(v);
                    } else if (color[v] == color[u]) return false;
                }
            }
        }
        return true;
    }
}
```

**Time complexity:** O(V + E)

## Topological Sort

### 20. Topological Sort

[Problem](https://www.geeksforgeeks.org/problems/topological-sort/1)

Return a valid ordering of vertices in a directed acyclic graph given V and edges. Returns an empty array/list if a cycle exists.

```java
import java.util.*;

class Solution {
    public int[] topoSort(int V, int[][] edges) {
        int n = V;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);
        int[] indegree = new int[n];
        for (List<Integer> neighbors : adj)
            for (int v : neighbors) indegree[v]++;
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < n; u++) if (indegree[u] == 0) queue.add(u);
        int[] order = new int[n];
        int count = 0;
        while (!queue.isEmpty()) {
            int u = queue.remove();
            order[count++] = u;
            for (int v : adj.get(u)) if (--indegree[v] == 0) queue.add(v);
        }
        return count == n ? order : new int[0];
    }
}
```

**Time complexity:** O(V + E)

### 21. Course Schedule II

[Problem](https://leetcode.com/problems/course-schedule-ii/)

Return a valid course order, or an empty array/list when a cycle makes completion impossible.

```java
import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int n = numCourses;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : prerequisites) adj.get(e[1]).add(e[0]);
        int[] indegree = new int[n];
        for (List<Integer> neighbors : adj)
            for (int v : neighbors) indegree[v]++;
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < n; u++) if (indegree[u] == 0) queue.add(u);
        int[] order = new int[n];
        int count = 0;
        while (!queue.isEmpty()) {
            int u = queue.remove();
            order[count++] = u;
            for (int v : adj.get(u)) if (--indegree[v] == 0) queue.add(v);
        }
        return count == n ? order : new int[0];
    }
}
```

**Time complexity:** O(V + E)

### 22. Eventual Safe States

[Problem](https://leetcode.com/problems/find-eventual-safe-states/)

Return sorted vertices whose every path eventually terminates. Start with terminal vertices and remove edges in the reversed graph.

```java
import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> reverse = new ArrayList<>();
        int[] degree = new int[n];
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) reverse.add(new ArrayList<>());
        for (int u = 0; u < n; u++) {
            degree[u] = graph[u].length;
            for (int v : graph[u]) reverse.get(v).add(u);
            if (degree[u] == 0) queue.add(u);
        }
        while (!queue.isEmpty()) {
            int u = queue.remove();
            for (int v : reverse.get(u)) if (--degree[v] == 0) queue.add(v);
        }
        List<Integer> result = new ArrayList<>();
        for (int u = 0; u < n; u++) if (degree[u] == 0) result.add(u);
        return result;
    }
}
```

**Time complexity:** O(V + E)

### 23. Alien Dictionary

[Problem](https://www.geeksforgeeks.org/problems/alien-dictionary/1)

Infer any valid ordering of the lowercase letters appearing in sorted alien words. Return an empty string for a cycle or invalid prefix order.

```java
import java.util.*;

class Solution {
    public String findOrder(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> degree = new HashMap<>();
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                adj.putIfAbsent(ch, new HashSet<>());
                degree.putIfAbsent(ch, 0);
            }
        }
        for (int i = 0; i + 1 < words.length; i++) {
            String a = words[i], b = words[i + 1];
            int j = 0, limit = Math.min(a.length(), b.length());
            while (j < limit && a.charAt(j) == b.charAt(j)) j++;
            if (j == limit) {
                if (a.length() > b.length()) return "";
            } else {
                char u = a.charAt(j), v = b.charAt(j);
                if (adj.get(u).add(v)) degree.put(v, degree.get(v) + 1);
            }
        }
        Queue<Character> queue = new ArrayDeque<>();
        for (char ch : adj.keySet()) if (degree.get(ch) == 0) queue.add(ch);
        StringBuilder order = new StringBuilder();
        while (!queue.isEmpty()) {
            char ch = queue.remove();
            order.append(ch);
            for (char next : adj.get(ch)) {
                degree.put(next, degree.get(next) - 1);
                if (degree.get(next) == 0) queue.add(next);
            }
        }
        return order.length() == adj.size() ? order.toString() : "";
    }
}
```

**Time complexity:** O(S + A + E), where S is total input characters, A distinct letters, and E distinct ordering constraints.

## Shortest Paths

### 24. Unit-Weight Shortest Path

[Problem](https://www.geeksforgeeks.org/dsa/shortest-path-in-undirected-graph-having-unit-distance/)

Find distances from src in an undirected, unweighted graph with V vertices. Return −1 for unreachable vertices.

```java
import java.util.*;

class Solution {
    public int[] shortestPath(int V, int[][] edges, int src) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int[] dist = new int[V];
        Arrays.fill(dist, -1);
        dist[src] = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(src);
        while (!queue.isEmpty()) {
            int u = queue.remove();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue.add(v);
                }
            }
        }
        return dist;
    }
}
```

**Time complexity:** O(V + E)

### 25. DAG Shortest Path

[Problem](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1)

Find distances from vertex 0 in a nonempty DAG with edges [u, v, weight]. Relax edges in topological order; unreachable vertices return −1.

```java
import java.util.*;

class Solution {
    public long[] shortestPath(int V, int[][] edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        int[] degree = new int[V];
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            degree[e[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < V; u++) if (degree[u] == 0) queue.add(u);
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[0] = 0;
        while (!queue.isEmpty()) {
            int u = queue.remove();
            for (int[] e : adj.get(u)) {
                int v = e[0], w = e[1];
                if (dist[u] != inf) dist[v] = Math.min(dist[v], dist[u] + w);
                if (--degree[v] == 0) queue.add(v);
            }
        }
        for (int u = 0; u < V; u++) if (dist[u] == inf) dist[u] = -1;
        return dist;
    }
}
```

**Time complexity:** O(V + E)

### 26. Dijkstra

[Problem](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1)

Find shortest distances from src in an undirected graph with nonnegative edge weights. Edges are [u, v, weight]; unreachable vertices return −1.

```java
import java.util.*;

class Solution {
    public long[] dijkstra(int V, int[][] edges, int src) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            adj.get(e[1]).add(new int[]{e[0], e[2]});
        }
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.add(new long[]{0, src});
        while (!heap.isEmpty()) {
            long[] cur = heap.remove();
            long cost = cur[0];
            int u = (int) cur[1];
            if (cost != dist[u]) continue;
            for (int[] e : adj.get(u)) {
                int v = e[0];
                long candidate = cost + e[1];
                if (candidate < dist[v]) {
                    dist[v] = candidate;
                    heap.add(new long[]{candidate, v});
                }
            }
        }
        for (int u = 0; u < V; u++) if (dist[u] == inf) dist[u] = -1;
        return dist;
    }
}
```

**Time complexity:** O(V + E log(E + 2)) with a heap that can retain outdated entries.

### 27. Network Delay

[Problem](https://leetcode.com/problems/network-delay-time/)

Find when all nodes receive a signal from k, or −1 if some cannot. Directed edges times use labels 1 through n and nonnegative travel times.

```java
import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int V = n + 1, src = k;
        int[][] edges = times;
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
        }
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.add(new long[]{0, src});
        while (!heap.isEmpty()) {
            long[] cur = heap.remove();
            long cost = cur[0];
            int u = (int) cur[1];
            if (cost != dist[u]) continue;
            for (int[] e : adj.get(u)) {
                int v = e[0];
                long candidate = cost + e[1];
                if (candidate < dist[v]) {
                    dist[v] = candidate;
                    heap.add(new long[]{candidate, v});
                }
            }
        }
        long answer = 0;
        for (int u = 1; u <= n; u++) answer = Math.max(answer, dist[u]);
        return answer == inf ? -1 : (int) answer;
    }
}
```

**Time complexity:** O(V + E log(E + 2))

### 28. Minimum Effort Path

[Problem](https://leetcode.com/problems/path-with-minimum-effort/)

Minimize the largest absolute height difference along a 4-directional path from top-left to bottom-right in a nonempty grid.

```java
import java.util.*;

class Solution {
    public int minimumEffortPath(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        int[][] dist = new int[rows][cols];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.add(new int[]{0, 0, 0});
        while (!heap.isEmpty()) {
            int[] cur = heap.remove();
            int effort = cur[0], r = cur[1], c = cur[2];
            if (effort != dist[r][c]) continue;
            if (r == rows - 1 && c == cols - 1) return effort;
            for (int[] d : dirs) {
                int x = r + d[0], y = c + d[1];
                if (x >= 0 && x < rows && y >= 0 && y < cols) {
                    int candidate = Math.max(effort, Math.abs(heights[x][y] - heights[r][c]));
                    if (candidate < dist[x][y]) {
                        dist[x][y] = candidate;
                        heap.add(new int[]{candidate, x, y});
                    }
                }
            }
        }
        return 0;
    }
}
```

**Time complexity:** O(RC log(RC + 1))

### 29. Cheapest Flights

[Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest route from src to dst using at most k stops (k + 1 edges). Each relaxation round reads only the previous round’s distances.

```java
import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        for (int step = 0; step <= k; step++) {
            long[] next = dist.clone();
            for (int[] e : flights) {
                if (dist[e[0]] != inf)
                    next[e[1]] = Math.min(next[e[1]], dist[e[0]] + e[2]);
            }
            dist = next;
        }
        return dist[dst] == inf ? -1 : (int) dist[dst];
    }
}
```

**Time complexity:** O((k + 1) × (V + E))

### 30. Bellman–Ford

[Problem](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1)

Find distances from src in a directed graph with negative weights allowed. Return [-1] for a reachable negative cycle; use 100000000 for unreachable vertices (GFG convention).

```java
import java.util.*;

class Solution {
    public long[] bellmanFord(int V, int[][] edges, int src) {
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        for (int step = 0; step < V - 1; step++) {
            boolean changed = false;
            for (int[] e : edges) {
                int u = e[0], v = e[1], w = e[2];
                if (dist[u] != inf && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    changed = true;
                }
            }
            if (!changed) break;
        }
        for (int[] e : edges)
            if (dist[e[0]] != inf && dist[e[0]] + e[2] < dist[e[1]]) return new long[]{-1};
        for (int u = 0; u < V; u++) if (dist[u] == inf) dist[u] = 100000000;
        return dist;
    }
}
```

**Time complexity:** O(V + VE)

### 31. Floyd–Warshall

[Problem](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1)

Find all-pairs shortest paths in place. Input matrix has 0 on its diagonal and 100000000 for no edge; negative weights are allowed, but no negative cycles. Finite distances have absolute value below 100000000.

```java
class Solution {
    public void floydWarshall(int[][] dist) {
        int n = dist.length, inf = 100000000;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (dist[i][k] == inf) continue;
                for (int j = 0; j < n; j++) {
                    if (dist[k][j] != inf)
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}
```

**Time complexity:** O(V³)

## State-Space BFS

### 32. Word Ladder

[Problem](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

```java
import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> remaining = new HashSet<>(wordList);
        if (!remaining.contains(endWord)) return 0;
        remaining.remove(beginWord);
        Queue<String> queue = new ArrayDeque<>();
        queue.add(beginWord);
        int length = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                String word = queue.remove();
                if (word.equals(endWord)) return length;
                char[] chars = word.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char old = chars[i];
                    for (char ch = 'a'; ch <= 'z'; ch++) {
                        chars[i] = ch;
                        String candidate = new String(chars);
                        if (remaining.remove(candidate)) queue.add(candidate);
                    }
                    chars[i] = old;
                }
            }
            length++;
        }
        return 0;
    }
}
```

**Time complexity:** O((N + 1) × 26 × L²), including string construction/hashing; N = dictionary size.

### 33. Open the Lock

[Problem](https://leetcode.com/problems/open-the-lock/)

Find the minimum wheel turns from 0000 to target while avoiding deadends; return −1 if impossible. Each state has four decimal digits.

```java
import java.util.*;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> seen = new HashSet<>(Arrays.asList(deadends));
        if (!seen.add("0000")) return -1;
        Queue<String> queue = new ArrayDeque<>();
        queue.add("0000");
        int turns = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                String state = queue.remove();
                if (state.equals(target)) return turns;
                char[] chars = state.toCharArray();
                for (int i = 0; i < 4; i++) {
                    char old = chars[i];
                    for (int delta : new int[]{-1, 1}) {
                        chars[i] = (char) ('0' + (old - '0' + delta + 10) % 10);
                        String next = new String(chars);
                        if (seen.add(next)) queue.add(next);
                    }
                    chars[i] = old;
                }
            }
            turns++;
        }
        return -1;
    }
}
```

**Time complexity:** O(D + 10⁴ × 8) for four fixed digits; D = number of deadends.

## Disjoint Set Union

### 34. Implement DSU

[Problem](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1)

Maintain disjoint sets for elements 0 through n − 1 using path compression and union by size. union returns whether two different components were merged.

```java
class DSU {
    private final int[] parent;
    private final int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}
```

**Time complexity:** O(n) initialization; O(α(n)) amortized per find/union, where α is the inverse Ackermann function.

### 35. Number of Provinces

[Problem](https://leetcode.com/problems/number-of-provinces/)

Count connected groups in a symmetric n × n adjacency matrix. Scan each undirected connection once and merge its components.

```java
class DSU {
    private final int[] parent;
    private final int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length, count = n;
        DSU dsu = new DSU(n);
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (isConnected[i][j] == 1 && dsu.union(i, j)) count--;
        return count;
    }
}
```

**Time complexity:** O(n² × α(n))

### 36. Redundant Connection

[Problem](https://leetcode.com/problems/redundant-connection/)

An undirected tree on labels 1 through n has one extra edge. Return the edge that creates a cycle when edges are processed in input order.

```java
class DSU {
    private final int[] parent;
    private final int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        DSU dsu = new DSU(edges.length + 1);
        for (int[] e : edges)
            if (!dsu.union(e[0], e[1])) return new int[]{e[0], e[1]};
        return new int[0];
    }
}
```

**Time complexity:** O(n × α(n))

### 37. Connect Network

[Problem](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Return the fewest cable moves to connect all n computers, or −1 if there are fewer than n − 1 cables.

```java
class DSU {
    private final int[] parent;
    private final int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        DSU dsu = new DSU(n);
        int components = n;
        for (int[] e : connections) if (dsu.union(e[0], e[1])) components--;
        return components - 1;
    }
}
```

**Time complexity:** O(V + E × α(V))

### 38. Accounts Merge

[Problem](https://leetcode.com/problems/accounts-merge/)

Merge accounts sharing an email and sort each merged email list. Each account has a name and at least one email; shared-email accounts have the same name.

```java
import java.util.*;


class DSU {
    private final int[] parent;
    private final int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU(accounts.size());
        Map<String, Integer> owner = new HashMap<>();
        for (int i = 0; i < accounts.size(); i++) {
            List<String> account = accounts.get(i);
            for (int j = 1; j < account.size(); j++) {
                String email = account.get(j);
                Integer previous = owner.putIfAbsent(email, i);
                if (previous != null) dsu.union(i, previous);
            }
        }
        Map<Integer, List<String>> groups = new HashMap<>();
        for (Map.Entry<String, Integer> e : owner.entrySet())
            groups.computeIfAbsent(dsu.find(e.getValue()), key -> new ArrayList<>()).add(e.getKey());
        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> e : groups.entrySet()) {
            List<String> emails = e.getValue();
            Collections.sort(emails);
            List<String> merged = new ArrayList<>();
            merged.add(accounts.get(e.getKey()).get(0));
            merged.addAll(emails);
            result.add(merged);
        }
        return result;
    }
}
```

**Time complexity:** O(A + M × (L + α(A)) + U log(U + 1) × L), where A = accounts, M = email occurrences, U = unique emails, L = maximum email length.

## Minimum Spanning Tree

### 39. Prim’s Algorithm

[Problem](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

Find the MST weight of an undirected connected graph with V ≥ 1 and edges [u, v, weight]. Add the cheapest edge reaching an unused vertex.

```java
import java.util.*;

class Solution {
    public long spanningTree(int V, int[][] edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            adj.get(e[1]).add(new int[]{e[0], e[2]});
        }
        boolean[] used = new boolean[V];
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.add(new int[]{0, 0});
        long total = 0;
        while (!heap.isEmpty()) {
            int[] cur = heap.remove();
            int u = cur[1];
            if (used[u]) continue;
            used[u] = true;
            total += cur[0];
            for (int[] e : adj.get(u))
                if (!used[e[0]]) heap.add(new int[]{e[1], e[0]});
        }
        return total;
    }
}
```

**Time complexity:** O(V + E log(E + 2))

### 40. Kruskal’s Algorithm

[Problem](https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1)

Find the MST weight of a connected undirected graph with edges [u, v, weight]. Process edges by weight and merge different components.

```java
import java.util.*;


class DSU {
    private final int[] parent;
    private final int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) {
            int temp = a; a = b; b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public long spanningTree(int V, int[][] edges) {
        int[][] sorted = edges.clone();
        Arrays.sort(sorted, Comparator.comparingInt(e -> e[2]));
        DSU dsu = new DSU(V);
        long total = 0;
        for (int[] e : sorted) if (dsu.union(e[0], e[1])) total += e[2];
        return total;
    }
}
```

**Time complexity:** O(V + E log(E + 2) + E × α(V))

### 41. Connect All Points

[Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Connect all points with minimum total Manhattan distance. Use dense Prim without building all pairwise edges.

```java
import java.util.*;

class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        if (n == 0) return 0;
        int[] best = new int[n];
        Arrays.fill(best, Integer.MAX_VALUE);
        boolean[] used = new boolean[n];
        best[0] = 0;
        int total = 0;
        for (int step = 0; step < n; step++) {
            int u = -1;
            for (int i = 0; i < n; i++)
                if (!used[i] && (u == -1 || best[i] < best[u])) u = i;
            used[u] = true;
            total += best[u];
            for (int v = 0; v < n; v++) {
                if (!used[v]) {
                    int distance = Math.abs(points[u][0] - points[v][0])
                            + Math.abs(points[u][1] - points[v][1]);
                    best[v] = Math.min(best[v], distance);
                }
            }
        }
        return total;
    }
}
```

**Time complexity:** O(n²)

## Advanced Graph Algorithms

### 42. Kosaraju’s Algorithm

[Problem](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

Count strongly connected components in a directed graph given V and edges. Record DFS finish order, then traverse the reversed graph in reverse finish order.

```java
import java.util.*;

class Solution {
    public int kosaraju(int V, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>(), reverse = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
            reverse.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            reverse.get(e[1]).add(e[0]);
        }
        boolean[] seen = new boolean[V];
        List<Integer> order = new ArrayList<>();
        Deque<int[]> frames = new ArrayDeque<>();
        for (int start = 0; start < V; start++) {
            if (seen[start]) continue;
            seen[start] = true;
            frames.push(new int[]{start, 0});
            while (!frames.isEmpty()) {
                int[] frame = frames.peek();
                int u = frame[0];
                if (frame[1] == adj.get(u).size()) {
                    order.add(u);
                    frames.pop();
                } else {
                    int v = adj.get(u).get(frame[1]++);
                    if (!seen[v]) {
                        seen[v] = true;
                        frames.push(new int[]{v, 0});
                    }
                }
            }
        }
        Arrays.fill(seen, false);
        int count = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = order.size() - 1; i >= 0; i--) {
            int start = order.get(i);
            if (seen[start]) continue;
            count++;
            seen[start] = true;
            stack.push(start);
            while (!stack.isEmpty()) {
                int u = stack.pop();
                for (int v : reverse.get(u)) {
                    if (!seen[v]) {
                        seen[v] = true;
                        stack.push(v);
                    }
                }
            }
        }
        return count;
    }
}
```

**Time complexity:** O(V + E)

### 43. Critical Connections

[Problem](https://leetcode.com/problems/critical-connections-in-a-network/)

Find bridges: edges whose removal increases the number of connected components. Iterative DFS tracks discovery times and the lowest reachable ancestor; edge IDs handle parallel edges.

```java
import java.util.*;

class Solution {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int id = 0; id < connections.size(); id++) {
            int u = connections.get(id).get(0), v = connections.get(id).get(1);
            adj.get(u).add(new int[]{v, id});
            adj.get(v).add(new int[]{u, id});
        }
        int[] tin = new int[n], low = new int[n], parent = new int[n], parentEdge = new int[n];
        Arrays.fill(tin, -1);
        Arrays.fill(parent, -1);
        Arrays.fill(parentEdge, -1);
        int timer = 0;
        List<List<Integer>> bridges = new ArrayList<>();
        Deque<int[]> stack = new ArrayDeque<>();
        for (int start = 0; start < n; start++) {
            if (tin[start] != -1) continue;
            tin[start] = low[start] = timer++;
            stack.push(new int[]{start, 0});
            while (!stack.isEmpty()) {
                int[] frame = stack.peek();
                int u = frame[0];
                if (frame[1] == adj.get(u).size()) {
                    stack.pop();
                    int p = parent[u];
                    if (p != -1) {
                        if (low[u] > tin[p]) bridges.add(Arrays.asList(p, u));
                        low[p] = Math.min(low[p], low[u]);
                    }
                    continue;
                }
                int[] e = adj.get(u).get(frame[1]++);
                int v = e[0], id = e[1];
                if (id == parentEdge[u]) continue;
                if (tin[v] == -1) {
                    parent[v] = u;
                    parentEdge[v] = id;
                    tin[v] = low[v] = timer++;
                    stack.push(new int[]{v, 0});
                } else {
                    low[u] = Math.min(low[u], tin[v]);
                }
            }
        }
        return bridges;
    }
}
```

**Time complexity:** O(V + E)
