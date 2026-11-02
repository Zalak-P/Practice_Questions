# Graphs — Java

V = vertices; E = edges; R and C = grid dimensions; α = inverse Ackermann function. Space excludes input storage unless stated. Examples use language-neutral notation. Grids are nonempty unless the method handles empty input explicitly.

## 1. BFS, DFS, and connected components

### 1. BFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

Visit vertices reachable from vertex 0 in breadth-first order. Input: adjacency list; an empty graph returns an empty list.

**Input/Output**

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,2,3]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 2. DFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

Visit vertices reachable from vertex 0 in depth-first order, following adjacency-list order. Use explicit stack frames.

**Input/Output**

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,3,2]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 3. Find if Path Exists in Graph — 1971

[LeetCode/GFG Link](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Check whether source can reach destination in an undirected graph with vertices 0 through n − 1.

**Input/Output**

```text
Input: n = 3, edges = [[0,1],[1,2]], source = 0, destination = 2
Output: true
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 4. Number of Connected Components in an Undirected Graph — 323

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Count connected components, including isolated vertices, in an undirected graph. LeetCode 323 is Premium.

**Input/Output**

```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 5. Clone Graph — 133

[LeetCode/GFG Link](https://leetcode.com/problems/clone-graph/)

Deep-copy the connected component reachable from node. The Node definition is included; use the judge-provided definition on LeetCode.

**Input/Output**

```text
Input: Adjacency list: [[2],[1]] (node values are 1 and 2)
Output: A new graph with adjacency list [[2],[1]], sharing no nodes with the input
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V) auxiliary for the map and queue, plus O(V + E) for the cloned output graph.

### 6. Keys and Rooms — 841

[LeetCode/GFG Link](https://leetcode.com/problems/keys-and-rooms/)

Visit room 0 and follow its keys to other rooms. Return whether every room can be reached. Use iterative DFS; each room is processed once.

**Input/Output**

```text
Input: rooms = [[1],[2],[3],[]]
Output: true
```

**Code**

```java
import java.util.*;

class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] seen = new boolean[rooms.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        seen[0] = true;
        stack.push(0);
        int count = 1;
        while (!stack.isEmpty()) {
            int room = stack.pop();
            for (int key : rooms.get(room)) {
                if (!seen[key]) {
                    seen[key] = true;
                    count++;
                    stack.push(key);
                }
            }
        }
        return count == rooms.size();
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input; E is the total number of keys.

### 7. Number of Provinces — 547

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-provinces/)

Count connected groups in a symmetric n × n adjacency matrix. Scan each undirected connection once and merge its components.

**Input/Output**

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Code**

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

**Time Space Complexity**

- **Time:** O(n² × α(n))
- **Space:** O(n) auxiliary for DSU; the input matrix is excluded.

## 2. Grid traversal

### 8. Number of Islands — 200

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

**Input/Output**

```text
Input: grid = [["1","1","0"],["0","0","1"]]
Output: 2
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 9. Flood Fill — 733

[LeetCode/GFG Link](https://leetcode.com/problems/flood-fill/)

Recolor the 4-connected component containing (sr, sc) in a nonempty image. Updates the image in place.

**Input/Output**

```text
Input: image = [[1,1],[1,0]], sr = 0, sc = 0, color = 2
Output: [[2,2],[2,0]]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 10. Max Area of Island — 695

[LeetCode/GFG Link](https://leetcode.com/problems/max-area-of-island/)

Return the largest 4-connected area of 1s in a nonempty binary grid. Visited land is changed to 0.

**Input/Output**

```text
Input: grid = [[1,1,0],[1,0,1]]
Output: 3
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 11. Surrounded Regions — 130

[LeetCode/GFG Link](https://leetcode.com/problems/surrounded-regions/)

Flip enclosed 'O' regions to 'X' in place. First preserve all 'O' cells connected to the boundary of the nonempty board.

**Input/Output**

```text
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","O","X","X"]]
Output: board becomes [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]; no return value
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the BFS queue.

### 12. Pacific Atlantic Water Flow — 417

[LeetCode/GFG Link](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Find cells from which water reaches both oceans. Search backward from ocean boundaries to equal or higher cells in the nonempty height grid.

**Input/Output**

```text
Input: heights = [[1,2],[4,3]]
Output: [[0,1],[1,0],[1,1]] (any order)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the two reachable sets/arrays and BFS queues.

## 3. Multi-source BFS

### 13. Rotting Oranges — 994

[LeetCode/GFG Link](https://leetcode.com/problems/rotting-oranges/)

Spread rot from all rotten oranges simultaneously in a nonempty grid. Return minutes until all fresh oranges rot, or −1. Updates the grid.

**Input/Output**

```text
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the BFS queue.

### 14. 01 Matrix — 542

[LeetCode/GFG Link](https://leetcode.com/problems/01-matrix/)

Find each cell’s distance to its nearest 0 using multi-source BFS. The nonempty binary matrix contains at least one 0.

**Input/Output**

```text
Input: mat = [[0,1,1],[1,1,1]]
Output: [[0,1,2],[1,2,3]]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C), including the distance matrix and BFS queue.

### 15. Shortest Bridge — 934

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-bridge/)

Given exactly two 4-connected islands, return the fewest water cells to flip to connect them. Mark one island, then expand it by BFS. Updates the grid.

**Input/Output**

```text
Input: grid = [[0,1],[1,0]]
Output: 1
```

**Code**

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

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack and BFS queue.

## 4. Cycle detection

### 16. Detect Cycle in an Undirected Graph — BFS and DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

Detect a cycle in any component of an undirected graph. Input edges use vertices 0 through V − 1; edge IDs distinguish parallel edges. Mark vertices when scheduling them. Ignore only the edge used to enter the current vertex; another edge to a seen vertex proves a cycle. Both BFS and DFS are included.

**Input/Output**

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

**Code**

**BFS**

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
        Queue<int[]> queue = new ArrayDeque<>();
        for (int start = 0; start < V; start++) {
            if (seen[start]) continue;
            seen[start] = true;
            queue.add(new int[]{start, -1});
            while (!queue.isEmpty()) {
                int[] cur = queue.remove();
                for (int[] e : adj.get(cur[0])) {
                    if (e[1] == cur[1]) continue;
                    if (seen[e[0]]) return true;
                    seen[e[0]] = true;
                    queue.add(new int[]{e[0], e[1]});
                }
            }
        }
        return false;
    }
}
```

**DFS — explicit stack**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list; O(V) traversal storage for either variant.

### 17. Detect Cycle in a Directed Graph — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using DFS states: 0 = unvisited, 1 = active, 2 = completed. An edge to an active node proves a cycle. Explicit stack frames avoid recursion depth limits.

**Input/Output**

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

**Code**

```java
import java.util.*;

class Solution {
    public boolean isCyclic(int V, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);
        int[] state = new int[V];
        Deque<int[]> stack = new ArrayDeque<>();
        for (int start = 0; start < V; start++) {
            if (state[start] != 0) continue;
            state[start] = 1;
            stack.push(new int[]{start, 0});
            while (!stack.isEmpty()) {
                int[] frame = stack.peek();
                int u = frame[0];
                if (frame[1] == adj.get(u).size()) {
                    state[u] = 2;
                    stack.pop();
                    continue;
                }
                int v = adj.get(u).get(frame[1]++);
                if (state[v] == 1) return true;
                if (state[v] == 0) {
                    state[v] = 1;
                    stack.push(new int[]{v, 0});
                }
            }
        }
        return false;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E)

### 18. Detect Cycle in a Directed Graph — Kahn’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)

Detect a directed cycle using Kahn’s algorithm: a cycle exists if not all vertices can be removed. Input: V and directed edges.

**Input/Output**

```text
Input: V = 3, edges = [[0,1],[1,2],[2,0]]
Output: true
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 19. Course Schedule — 207

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule/)

Determine whether all courses can be completed. Each prerequisite pair is [course, prerequisite].

**Input/Output**

```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 20. Find Eventual Safe States — 802

[LeetCode/GFG Link](https://leetcode.com/problems/find-eventual-safe-states/)

Return sorted vertices whose every path eventually terminates. Start with terminal vertices and remove edges in the reversed graph.

**Input/Output**

```text
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the reversed graph.

## 5. Bipartite graphs

### 21. Is Graph Bipartite? — 785

[LeetCode/GFG Link](https://leetcode.com/problems/is-graph-bipartite/)

Check whether an undirected adjacency-list graph can be colored with two colors so adjacent vertices differ. Covers disconnected components.

**Input/Output**

```text
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
```

**Code**

**BFS**

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

**DFS — recursive**

```java
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length];
        Arrays.fill(color, -1);
        for (int node = 0; node < graph.length; node++)
            if (color[node] == -1 && !dfs(node, 0, graph, color)) return false;
        return true;
    }
    private boolean dfs(int node, int currentColor, int[][] graph, int[] color) {
        color[node] = currentColor;
        for (int neighbor : graph[node]) {
            if (color[neighbor] == -1) {
                if (!dfs(neighbor, 1 - currentColor, graph, color)) return false;
            } else if (color[neighbor] == currentColor) return false;
        }
        return true;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list; includes recursion stack for DFS.

### 22. Possible Bipartition — 886

[LeetCode/GFG Link](https://leetcode.com/problems/possible-bipartition/)

Split people labeled 1 through n into two groups so every disliked pair is separated. Build an undirected graph and two-color it.

**Input/Output**

```text
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 6. Topological sorting and dependencies

### 23. Topological Sort — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

Use DFS finish times to order a DAG. Append a node after all its outgoing neighbors finish, then reverse the result. Return an empty list if an active-node edge reveals a cycle.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,2,1,3] (one valid order)
```

**Code**

```java
import java.util.*;

class Solution {
    public List<Integer> topoSort(int V, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) adj.get(e[0]).add(e[1]);
        int[] state = new int[V];
        List<Integer> order = new ArrayList<>();
        Deque<int[]> stack = new ArrayDeque<>();
        for (int start = 0; start < V; start++) {
            if (state[start] != 0) continue;
            state[start] = 1;
            stack.push(new int[]{start, 0});
            while (!stack.isEmpty()) {
                int[] frame = stack.peek();
                int u = frame[0];
                if (frame[1] == adj.get(u).size()) {
                    order.add(u);
                    state[u] = 2;
                    stack.pop();
                    continue;
                }
                int v = adj.get(u).get(frame[1]++);
                if (state[v] == 1) return new ArrayList<>();
                if (state[v] == 0) {
                    state[v] = 1;
                    stack.push(new int[]{v, 0});
                }
            }
        }
        Collections.reverse(order);
        return order;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E)

### 24. Topological Sort — Kahn’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

Return a valid ordering of vertices in a directed acyclic graph given V and edges. Returns an empty array/list if a cycle exists.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,1,2,3] (one valid order)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 25. Course Schedule II — 210

[LeetCode/GFG Link](https://leetcode.com/problems/course-schedule-ii/)

Return a valid course order, or an empty array/list when a cycle makes completion impossible.

**Input/Output**

```text
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] (one valid order)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 26. Alien Dictionary — 269

[LeetCode/GFG Link](https://leetcode.com/problems/alien-dictionary/)

Infer any valid ordering of the lowercase letters appearing in sorted alien words. Return an empty string for a cycle or invalid prefix order. LeetCode 269 is Premium. The workbook method is named findOrder.

**Input/Output**

```text
Input: words = ["za","zb","ca","cb"]
Output: "zacb" (one valid order; z before c and a before b)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(S + A + E), where S is total input characters, A distinct letters, and E distinct ordering constraints.
- **Space:** O(A + E), excluding input word storage.

### 27. Find All Possible Recipes from Given Supplies — 2115

[LeetCode/GFG Link](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)

Process supplies as available nodes. Each ingredient unlocks dependent recipes by reducing their remaining ingredient count. Enqueue a recipe when all its ingredients are available; cyclic or missing dependencies remain unresolved. Supplies are unlimited.

**Input/Output**

```text
Input: recipes = ["tea","combo"], ingredients = [["water","leaf"],["tea","bread"]], supplies = ["water","leaf","bread"]
Output: ["tea","combo"]
```

**Code**

```java
import java.util.*;

class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients,
                                       String[] supplies) {
        Map<String, List<Integer>> dependents = new HashMap<>();
        int[] remaining = new int[recipes.length];
        for (int i = 0; i < recipes.length; i++) {
            remaining[i] = ingredients.get(i).size();
            for (String item : ingredients.get(i))
                dependents.computeIfAbsent(item, x -> new ArrayList<>()).add(i);
        }
        Queue<String> queue = new ArrayDeque<>();
        Set<String> available = new HashSet<>();
        for (String item : supplies) if (available.add(item)) queue.add(item);
        for (int i = 0; i < recipes.length; i++)
            if (remaining[i] == 0 && available.add(recipes[i])) queue.add(recipes[i]);
        while (!queue.isEmpty()) {
            String item = queue.remove();
            for (int i : dependents.getOrDefault(item, Collections.emptyList())) {
                if (--remaining[i] == 0 && available.add(recipes[i])) queue.add(recipes[i]);
            }
        }
        List<String> result = new ArrayList<>();
        for (String recipe : recipes) if (available.contains(recipe)) result.add(recipe);
        return result;
    }
}
```

**Time Space Complexity**

- **Time:** O(N + I + S) expected hash-table operations; N = recipes, I = ingredient occurrences, S = supplies. String hashing additionally depends on string lengths.
- **Space:** O(N + I + S).

## 7. Unweighted shortest paths and state-based BFS

### 28. Shortest Path in an Undirected Graph with Unit Weights

[LeetCode/GFG Link](https://www.geeksforgeeks.org/dsa/shortest-path-in-undirected-graph-having-unit-distance/)

Find distances from src in an undirected, unweighted graph with V vertices. Return −1 for unreachable vertices.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[1,2]], src = 0
Output: [0,1,2,-1]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 29. Shortest Path in Binary Matrix — 1091

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

Find the shortest 8-directional path of 0s from top-left to bottom-right in an n × n grid. Count visited cells; return −1 if impossible. Updates the grid.

**Input/Output**

```text
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Code**

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

**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n²) for the BFS queue.

### 30. Word Ladder — 127

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

**Input/Output**

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

**Code**

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

**Time Space Complexity**

- **Time:** O((N + 1) × 26 × L²), including string construction/hashing; N = dictionary size.
- **Space:** O((N + 1) × L), for dictionary/queue strings of length L; N = dictionary size.

### 31. Open the Lock — 752

[LeetCode/GFG Link](https://leetcode.com/problems/open-the-lock/)

Find the minimum wheel turns from 0000 to target while avoiding deadends; return −1 if impossible. Each state has four decimal digits.

**Input/Output**

```text
Input: deadends = [], target = "0009"
Output: 1
```

**Code**

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

**Time Space Complexity**

- **Time:** O(D + 10⁴ × 8) for four fixed digits; D = number of deadends.
- **Space:** O(D + 10⁴) for fixed four-digit states; D = deadends.

### 32. Snakes and Ladders — 909

[LeetCode/GFG Link](https://leetcode.com/problems/snakes-and-ladders/)

Use BFS over square numbers to find the minimum dice rolls from 1 to n². Convert each square to its boustrophedon board coordinate. Follow at most one snake or ladder per roll; return −1 if the target is unreachable.

**Input/Output**

```text
Input: board = [[-1,-1],[-1,-1]]
Output: 1
```

**Code**

```java
import java.util.*;

class Solution {
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        boolean[] seen = new boolean[n * n + 1];
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{1, 0});
        seen[1] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.remove();
            if (cur[0] == n * n) return cur[1];
            for (int next = cur[0] + 1; next <= Math.min(cur[0] + 6, n * n); next++) {
                int fromBottom = (next - 1) / n, col = (next - 1) % n;
                int row = n - 1 - fromBottom;
                if (fromBottom % 2 == 1) col = n - 1 - col;
                int dest = board[row][col] == -1 ? next : board[row][col];
                if (!seen[dest]) {
                    seen[dest] = true;
                    queue.add(new int[]{dest, cur[1] + 1});
                }
            }
        }
        return -1;
    }
}
```

**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n²).

## 8. Weighted shortest paths

### 33. Dijkstra’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1)

Find shortest distances from src in an undirected graph with nonnegative edge weights. Edges are [u, v, weight]; unreachable vertices return −1.

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,9]], src = 0
Output: [0,4,6]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E log(E + 2)) with a heap that can retain outdated entries.
- **Space:** O(V + E), including the adjacency list and heap with outdated entries.

### 34. Network Delay Time — 743

[LeetCode/GFG Link](https://leetcode.com/problems/network-delay-time/)

Find when all nodes receive a signal from k, or −1 if some cannot. Directed edges times use labels 1 through n and nonnegative travel times.

**Input/Output**

```text
Input: times = [[1,2,2],[2,3,1]], n = 3, k = 1
Output: 3
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 35. Path With Minimum Effort — 1631

[LeetCode/GFG Link](https://leetcode.com/problems/path-with-minimum-effort/)

Minimize the largest absolute height difference along a 4-directional path from top-left to bottom-right in a nonempty grid.

**Input/Output**

```text
Input: heights = [[1,3],[2,4]]
Output: 2
```

**Code**

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

**Time Space Complexity**

- **Time:** O(RC log(RC + 1))
- **Space:** O(R × C) for distances and the heap (a grid has O(R × C) edges).

### 36. Cheapest Flights Within K Stops — 787

[LeetCode/GFG Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest route from src to dst using at most k stops (k + 1 edges). Each relaxation round reads only the previous round’s distances.

**Input/Output**

```text
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
```

**Code**

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

**Time Space Complexity**

- **Time:** O((k + 1) × (V + E))
- **Space:** O(V) for two distance arrays.

### 37. Bellman–Ford Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1)

Find distances from src in a directed graph with negative weights allowed. Return [-1] for a reachable negative cycle; use 100000000 for unreachable vertices (GFG convention).

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,-2],[0,2,5]], src = 0
Output: [0,4,2]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 38. Negative Cycle Detection

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1)

Detect a negative-weight cycle anywhere in a directed graph, including disconnected components. Initialize every distance to zero, equivalent to a super-source. An improvement on the Vth Bellman–Ford pass proves a negative cycle. Return 1 if found, otherwise 0.

**Input/Output**

```text
Input: V = 4, edges = [[0,1,2],[2,3,-2],[3,2,1]]
Output: 1 (negative cycle is disconnected from vertex 0)
```

**Code**

```java
class Solution {
    public int isNegativeWeightCycle(int V, int[][] edges) {
        long[] dist = new long[V];
        for (int step = 0; step < V; step++) {
            boolean changed = false;
            for (int[] e : edges) {
                if (dist[e[0]] + e[2] < dist[e[1]]) {
                    dist[e[1]] = dist[e[0]] + e[2];
                    changed = true;
                    if (step == V - 1) return 1;
                }
            }
            if (!changed) return 0;
        }
        return 0;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + VE)
- **Space:** O(V), excluding the input edge list.

### 39. Floyd–Warshall Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1)

Find all-pairs shortest paths in place. Input matrix has 0 on its diagonal and 100000000 for no edge; negative weights are allowed, but no negative cycles. Finite distances have absolute value below 100000000.

**Input/Output**

```text
Input: dist = [[0,3,100000000],[100000000,0,2],[100000000,100000000,0]]
Output: dist becomes [[0,3,5],[100000000,0,2],[100000000,100000000,0]]; no return value
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V³)
- **Space:** O(1) auxiliary; the O(V²) input distance matrix is updated in place.

### 40. Find the City With the Smallest Number of Neighbors at a Threshold Distance — 1334

[LeetCode/GFG Link](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

Use Floyd–Warshall for all-pairs shortest distances in an undirected weighted graph. Count other cities within distanceThreshold. On equal counts, choose the city with the larger index.

**Input/Output**

```text
Input: n = 4, edges = [[0,1,2],[1,2,2],[2,3,2]], distanceThreshold = 2
Output: 3
```

**Code**

```java
import java.util.*;

class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        long inf = Long.MAX_VALUE / 4;
        long[][] dist = new long[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], inf);
            dist[i][i] = 0;
        }
        for (int[] e : edges)
            dist[e[0]][e[1]] = dist[e[1]][e[0]] = Math.min(dist[e[0]][e[1]], e[2]);
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        int answer = -1, best = n;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++)
                if (i != j && dist[i][j] <= distanceThreshold) count++;
            if (count <= best) { best = count; answer = i; }
        }
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(n³ + E)
- **Space:** O(n²).

### 41. Shortest Path in a Directed Acyclic Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1)

Find distances from vertex 0 in a nonempty DAG with edges [u, v, weight]. Relax edges in topological order; unreachable vertices return −1.

**Input/Output**

```text
Input: V = 4, edges = [[0,1,2],[0,2,5],[1,2,-1]]
Output: [0,2,1,-1]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 9. Disjoint Set Union — Union-Find

### 42. Implement DSU — Path Compression and Union by Size

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1)

Maintain disjoint sets for elements 0 through n − 1 using path compression and union by size. union returns whether two different components were merged.

**Input/Output**

```text
Input: DSU(4); union(0,1); union(1,2); union(0,2); find(0) == find(2); find(0) == find(3)
Output: true; true; false; true; false (initialization has no output)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(n) initialization; O(α(n)) amortized per find/union, where α is the inverse Ackermann function.
- **Space:** O(n) for parent and size arrays.

### 43. Redundant Connection — 684

[LeetCode/GFG Link](https://leetcode.com/problems/redundant-connection/)

An undirected tree on labels 1 through n has one extra edge. Return the edge that creates a cycle when edges are processed in input order.

**Input/Output**

```text
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Code**

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

**Time Space Complexity**

- **Time:** O(n × α(n))
- **Space:** O(n) for DSU.

### 44. Number of Operations to Make Network Connected — 1319

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Return the fewest cable moves to connect all n computers, or −1 if there are fewer than n − 1 cables.

**Input/Output**

```text
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E × α(V))
- **Space:** O(V) for DSU.

### 45. Accounts Merge — 721

[LeetCode/GFG Link](https://leetcode.com/problems/accounts-merge/)

Merge accounts sharing an email and sort each merged email list. Each account has a name and at least one email; shared-email accounts have the same name.

**Input/Output**

```text
Input: accounts = [["Mira","a@x.com","b@x.com"],["Mira","b@x.com","c@x.com"],["Noah","n@x.com"]]
Output: [["Mira","a@x.com","b@x.com","c@x.com"],["Noah","n@x.com"]] (account groups may appear in any order)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(A + M × (L + α(A)) + U log(U + 1) × L), where A = accounts, M = email occurrences, U = unique emails, L = maximum email length.
- **Space:** O(A + M + U × L), including temporary email lists and output; sorting can also use linear temporary storage.

### 46. Most Stones Removed with Same Row or Column — 947

[LeetCode/GFG Link](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

Model stones as nodes. Union stones sharing a row or column, using a representative map for each coordinate. Each connected component must keep one stone; return the number of stones minus the number of components.

**Input/Output**

```text
Input: stones = [[0,0],[0,1],[1,1],[3,4]]
Output: 2
```

**Code**

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
    public int removeStones(int[][] stones) {
        DSU dsu = new DSU(stones.length);
        Map<Integer, Integer> rows = new HashMap<>(), cols = new HashMap<>();
        int components = stones.length;
        for (int i = 0; i < stones.length; i++) {
            int row = stones[i][0], col = stones[i][1];
            if (rows.containsKey(row) && dsu.union(i, rows.get(row))) components--;
            if (cols.containsKey(col) && dsu.union(i, cols.get(col))) components--;
            rows.put(row, i);
            cols.put(col, i);
        }
        return stones.length - components;
    }
}
```

**Time Space Complexity**

- **Time:** O(n × α(n)) expected, where n = stones; hash-map operations are expected O(1).
- **Space:** O(n).

## 10. Minimum spanning tree

### 47. Kruskal’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1)

Find the MST weight of a connected undirected graph with edges [u, v, weight]. Process edges by weight and merge different components.

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,7]]
Output: 6
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E log(E + 2) + E × α(V))
- **Space:** O(V + E), including DSU and the sorted edge copy.

### 48. Prim’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

Find the MST weight of an undirected connected graph with V ≥ 1 and edges [u, v, weight]. Add the cheapest edge reaching an unused vertex.

**Input/Output**

```text
Input: V = 3, edges = [[0,1,4],[1,2,2],[0,2,7]]
Output: 6
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 49. Min Cost to Connect All Points — 1584

[LeetCode/GFG Link](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Connect all points with minimum total Manhattan distance. Use dense Prim without building all pairwise edges.

**Input/Output**

```text
Input: points = [[0,0],[2,0],[2,2]]
Output: 4
```

**Code**

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

**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n), excluding input points.

## 11. Strongly connected components and connectivity

### 50. Kosaraju’s Algorithm

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)

Count strongly connected components in a directed graph given V and edges. Record DFS finish order, then traverse the reversed graph in reverse finish order.

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[1,0],[1,2],[2,3],[3,2]]
Output: 2
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including both adjacency lists.

### 51. Critical Connections in a Network — 1192

[LeetCode/GFG Link](https://leetcode.com/problems/critical-connections-in-a-network/)

Find bridges: edges whose removal increases the number of connected components. Iterative DFS tracks discovery times and the lowest reachable ancestor; edge IDs handle parallel edges.

**Input/Output**

```text
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]] (edge endpoints may be reversed)
```

**Code**

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

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## 12. Other important graph patterns

### 52. Evaluate Division — 399

[LeetCode/GFG Link](https://leetcode.com/problems/evaluate-division/)

For a / b = value, store edges a → b with value and b → a with its reciprocal. For each query, DFS multiplies edge weights along a path. Unknown or disconnected variables return −1.0; a known variable divided by itself returns 1.0. Equations are consistent.

**Input/Output**

```text
Input: equations = [["x","y"],["y","z"]], values = [4.0,2.0], queries = [["x","z"],["z","x"],["u","u"]]
Output: [8.0,0.125,-1.0]
```

**Code**

```java
import java.util.*;

class Solution {
    static class Edge {
        String node;
        double weight;
        Edge(String node, double weight) { this.node = node; this.weight = weight; }
    }
    public double[] calcEquation(List<List<String>> equations, double[] values,
                                  List<List<String>> queries) {
        Map<String, List<Edge>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, x -> new ArrayList<>()).add(new Edge(b, values[i]));
            graph.computeIfAbsent(b, x -> new ArrayList<>()).add(new Edge(a, 1.0 / values[i]));
        }
        double[] answer = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String source = queries.get(i).get(0), target = queries.get(i).get(1);
            answer[i] = -1.0;
            if (!graph.containsKey(source) || !graph.containsKey(target)) continue;
            Deque<Edge> stack = new ArrayDeque<>();
            Set<String> seen = new HashSet<>();
            stack.push(new Edge(source, 1.0));
            seen.add(source);
            while (!stack.isEmpty()) {
                Edge cur = stack.pop();
                if (cur.node.equals(target)) { answer[i] = cur.weight; break; }
                for (Edge next : graph.get(cur.node)) {
                    if (seen.add(next.node)) stack.push(new Edge(next.node, cur.weight * next.weight));
                }
            }
        }
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E + Q(V + E)) expected map/set operations; Q = queries. Variable-name hashing additionally depends on string length.
- **Space:** O(V + E) auxiliary, plus O(Q) output.

### 53. All Paths From Source to Target — 797

[LeetCode/GFG Link](https://leetcode.com/problems/all-paths-from-source-to-target/)

Given a DAG adjacency list, enumerate every path from node 0 to node n − 1. Use DFS/backtracking: append a neighbor before exploring and remove it afterward. A global visited set would incorrectly discard distinct paths.

**Input/Output**

```text
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]] (any order)
```

**Code**

```java
import java.util.*;

class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(0, graph, path, result);
        return result;
    }
    private void dfs(int node, int[][] graph, List<Integer> path, List<List<Integer>> result) {
        if (node == graph.length - 1) { result.add(new ArrayList<>(path)); return; }
        for (int neighbor : graph[node]) {
            path.add(neighbor);
            dfs(neighbor, graph, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

**Time Space Complexity**

- **Time:** O(V × 2^V) worst case, including path copies; the number of paths can be exponential.
- **Space:** O(V) auxiliary for the path and recursion, plus O(V × 2^V) worst-case output.

### 54. Longest Increasing Path in a Matrix — 329

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

Strictly increasing edges form a DAG. DFS memoizes the longest path starting at each cell, so each cell is solved once. The alternative topological-layer solution avoids recursion depth limits on long paths.

**Input/Output**

```text
Input: matrix = [[3,4],[2,5]]
Output: 4
```

**Code**

**DFS + memoization**

```java
class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int[][] memo = new int[matrix.length][matrix[0].length];
        int best = 0;
        for (int r = 0; r < matrix.length; r++)
            for (int c = 0; c < matrix[0].length; c++)
                best = Math.max(best, dfs(r, c, matrix, memo));
        return best;
    }
    private int dfs(int r, int c, int[][] matrix, int[][] memo) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < matrix.length && nc >= 0 && nc < matrix[0].length
                    && matrix[nr][nc] > matrix[r][c])
                best = Math.max(best, 1 + dfs(nr, nc, matrix, memo));
        }
        return memo[r][c] = best;
    }
}
```

**Topological layers — avoids recursion**

```java
import java.util.*;

class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        int[][] degree = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                for (int[] d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                            && matrix[nr][nc] > matrix[r][c]) degree[r][c]++;
                }
                if (degree[r][c] == 0) queue.add(new int[]{r, c});
            }
        }
        int length = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                int[] cur = queue.remove();
                for (int[] d : dirs) {
                    int nr = cur[0] + d[0], nc = cur[1] + d[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                            && matrix[nr][nc] < matrix[cur[0]][cur[1]]
                            && --degree[nr][nc] == 0) queue.add(new int[]{nr, nc});
                }
            }
            length++;
        }
        return length;
    }
}
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C).
