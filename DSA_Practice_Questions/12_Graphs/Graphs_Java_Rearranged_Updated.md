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

```java
class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int islands = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    islands++;
                    dfs(grid, r, c);
                }
            }
        }
        return islands;
    }

    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}
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

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original_color = image[sr][sc];
        // Return early if the original color equals the new color, to prevent endless revisits.
        if (original_color == color) return image;
        dfs(image, sr, sc, original_color, color);
        return image;
    }

    private void dfs(int[][] image, int r, int c, int original_color, int color) {
        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] != original_color) return;
        image[r][c] = color;
        dfs(image, r + 1, c, original_color, color);
        dfs(image, r - 1, c, original_color, color);
        dfs(image, r, c + 1, original_color, color);
        dfs(image, r, c - 1, original_color, color);
    }
}
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

```java

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

```java
import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new ArrayDeque<>();
        int minutes = 0, fresh_count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) fresh_count++;
                if (grid[r][c] == 2) queue.offer(new int[]{r, c});
            }
        }
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!queue.isEmpty() && fresh_count > 0) {
            minutes++;
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                int[] cell = queue.poll();
                int r = cell[0], c = cell[1];
                for (int[] direction : directions) {
                    int nr = r + direction[0], nc = c + direction[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh_count--;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
        return fresh_count == 0 ? minutes : -1;
    }
}
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

```java
import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        int[][] answer_matrix = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            Arrays.fill(answer_matrix[r], -1);
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) {
                    answer_matrix[r][c] = 0;
                    queue.offer(new int[]{r, c});
                }
            }
        }
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            for (int[] direction : directions) {
                int nr = r + direction[0], nc = c + direction[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && answer_matrix[nr][nc] == -1) {
                    answer_matrix[nr][nc] = answer_matrix[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        return answer_matrix;
    }
}
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

```java
class Solution {
    public void solve(char[][] board) {
        int rows = board.length, cols = board[0].length;
        // Step 1: Mark border-connected 'O's
        for (int r = 0; r < rows; r++) {
            dfs(board, r, 0);
            dfs(board, r, cols - 1);
        }
        for (int c = 0; c < cols; c++) {
            dfs(board, 0, c);
            dfs(board, rows - 1, c);
        }
        // Step 2: Flip remaining 'O' to 'X', 'T' back to 'O'
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == 'T') board[r][c] = 'O';
            }
        }
    }

    private void dfs(char[][] board, int r, int c) {
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != 'O') return;
        board[r][c] = 'T';
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }
}
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

```java

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

```java

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

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> bfs(ArrayList<ArrayList<Integer>> adj) {
        ArrayList<Integer> result = new ArrayList<>();
        if (adj.isEmpty()) return result;
        boolean[] visited = new boolean[adj.size()];
        Queue<Integer> queue = new ArrayDeque<>();
        visited[0] = true;
        queue.offer(0);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            result.add(node);
            for (int neighbor : adj.get(node)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }
        return result;
    }
}
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

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[adj.size()];
        ArrayList<Integer> result = new ArrayList<>();
        if (!adj.isEmpty()) traverse(0, adj, visited, result);
        return result;
    }

    private void traverse(int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited, ArrayList<Integer> result) {
        visited[node] = true;
        result.add(node);
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) traverse(neighbor, adj, visited, result);
        }
    }
}
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

```java
import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length, answer = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                Queue<Integer> queue = new ArrayDeque<>();
                queue.offer(i);
                visited[i] = true;
                while (!queue.isEmpty()) {
                    int node = queue.poll();
                    for (int neighbor = 0; neighbor < n; neighbor++) {
                        if (isConnected[node][neighbor] == 1 && !visited[neighbor]) {
                            visited[neighbor] = true;
                            queue.offer(neighbor);
                        }
                    }
                }
            }
        }
        return answer;
    }
}
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

```java
import java.util.*;

class Solution {
    public boolean isCycle(ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[adj.size()];
        for (int start = 0; start < adj.size(); start++) {
            if (visited[start]) continue;
            visited[start] = true;
            Queue<int[]> queue = new ArrayDeque<>();
            queue.offer(new int[]{start, -1});
            while (!queue.isEmpty()) {
                int[] entry = queue.poll();
                int node = entry[0], parent = entry[1];
                for (int neighbor : adj.get(node)) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        queue.offer(new int[]{neighbor, node});
                    } else if (neighbor != parent) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
```

```java
import java.util.*;

class Solution {
    public boolean has_cycle_undirected(int vertices, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < vertices; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        boolean[] visited = new boolean[vertices];
        for (int v = 0; v < vertices; v++) {
            if (!visited[v] && dfs(v, -1, adj, visited)) return true;
        }
        return false;
    }

    private boolean dfs(int node, int parent, List<List<Integer>> adj, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, adj, visited)) return true;
            } else if (neighbor != parent) {
                return true;
            }
        }
        return false;
    }
}
```

### 13. ★ Detect Cycle in a Directed adj — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-adj/1)

Detect a directed cycle using DFS states: 0 = unvisited, 1 = active, 2 = completed. An edge to an active node proves a cycle. Explicit stack frames avoid recursion depth limits.

**Input/Output**

```text
Input: V = 5, edges = [[0,1],[1,2],[2,0],[1,3],[3,4]]
Output: true
```

```java
import java.util.*;

class Solution {
    public boolean has_cycle_directed(int vertices, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < vertices; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) adj.get(edge[0]).add(edge[1]);
        boolean[] visited = new boolean[vertices];
        boolean[] rec_stack = new boolean[vertices]; // Tracks nodes in the current recursion path
        for (int v = 0; v < vertices; v++) {
            if (!visited[v] && dfs(v, adj, visited, rec_stack)) return true;
        }
        return false;
    }

    private boolean dfs(int node, List<List<Integer>> adj, boolean[] visited, boolean[] rec_stack) {
        visited[node] = true;
        rec_stack[node] = true;
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, adj, visited, rec_stack)) return true;
            } else if (rec_stack[neighbor]) {
                return true;
            }
        }
        rec_stack[node] = false;
        return false;
    }
}
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

```java
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] adj) {
        int[] color_array = new int[adj.length];
        Arrays.fill(color_array, -1);
        for (int i = 0; i < adj.length; i++) {
            if (color_array[i] != -1) continue;
            color_array[i] = 0;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(i);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : adj[node]) {
                    if (color_array[neighbor] == -1) {
                        color_array[neighbor] = 1 - color_array[node];
                        queue.offer(neighbor);
                    } else if (color_array[neighbor] == color_array[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
```

2. **Odd Cycle Check:** If the adj contains a loop (cycle) with an odd number of edges/vertices, it is not bipartite. (DFS Approach)

```java
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] adj) {
        int[] color_array = new int[adj.length];
        Arrays.fill(color_array, -1);
        for (int node = 0; node < adj.length; node++) {
            if (color_array[node] == -1 && !dfs(node, 0, adj, color_array)) return false;
        }
        return true;
    }

    private boolean dfs(int node, int current_color, int[][] adj, int[] color_array) {
        color_array[node] = current_color;
        for (int neighbor : adj[node]) {
            if (color_array[neighbor] == -1) {
                if (!dfs(neighbor, 1 - current_color, adj, color_array)) return false;
            } else if (color_array[neighbor] == current_color) {
                return false;
            }
        }
        return true;
    }
}
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

```java
class Solution {
    public boolean isCyclic(int[][] adj) {
        int[] state = new int[adj.length];
        for (int node = 0; node < adj.length; node++) {
            if (state[node] == 0 && dfs(node, adj, state)) return true;
        }
        return false;
    }

    private boolean dfs(int node, int[][] adj, int[] state) {
        state[node] = 1;
        for (int neighbor : adj[node]) {
            if (state[neighbor] == 1) return true;
            if (state[neighbor] == 0 && dfs(neighbor, adj, state)) return true;
        }
        state[node] = 2;
        return false;
    }
}
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

```java

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

```java
import java.util.*;

class Solution {
    public boolean isCyclic(int[][] adj) {
        int[] indegree = new int[adj.length];
        for (int node = 0; node < adj.length; node++) {
            for (int neighbor : adj[node]) indegree[neighbor]++;
        }
        // queue containing all nodes whose indegree is 0
        Queue<Integer> queue = new ArrayDeque<>();
        for (int node = 0; node < adj.length; node++) {
            if (indegree[node] == 0) queue.offer(node);
        }
        int processed = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            processed++;
            for (int neighbor : adj[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return processed != adj.length;
    }
}
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

```java
import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] adj) {
        int n = adj.length;
        List<List<Integer>> reverse = new ArrayList<>();
        for (int i = 0; i < n; i++) reverse.add(new ArrayList<>());
        int[] outdegree = new int[n];
        for (int node = 0; node < n; node++) {
            outdegree[node] = adj[node].length;
            for (int neighbor : adj[node]) reverse.get(neighbor).add(node);
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int node = 0; node < n; node++) {
            if (outdegree[node] == 0) queue.offer(node);
        }
        boolean[] safe = new boolean[n];
        while (!queue.isEmpty()) {
            int node = queue.poll();
            safe[node] = true;
            for (int previous : reverse.get(node)) {
                outdegree[previous]--;
                if (outdegree[previous] == 0) queue.offer(previous);
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int node = 0; node < n; node++) {
            if (safe[node]) result.add(node);
        }
        return result;
    }
}
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

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> topoSort(int V, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        int[] indegree = new int[V];
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            indegree[edge[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < V; u++) {
            if (indegree[u] == 0) queue.offer(u);
        }
        ArrayList<Integer> order = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            order.add(node);
            for (int neighbor : adj.get(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return order.size() == V ? order : new ArrayList<>();
    }
}
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

```java
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] prerequisite : prerequisites) {
            int u = prerequisite[0], v = prerequisite[1];
            adj.get(v).add(u);
            indegree[u]++;
        }
        // queue containing all nodes whose indegree is 0
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < numCourses; u++) {
            if (indegree[u] == 0) queue.offer(u);
        }
        int completed = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            completed++;
            for (int neighbor : adj.get(course)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return completed == numCourses;
    }
}
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

```java
import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int n = numCourses;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        int[] indegree = new int[n];
        for (int[] prerequisite : prerequisites) {
            int u = prerequisite[0], v = prerequisite[1];
            adj.get(v).add(u);
            indegree[u]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < n; u++) {
            if (indegree[u] == 0) queue.offer(u);
        }
        int[] order = new int[n];
        int count = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[count++] = course;
            for (int neighbor : adj.get(course)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return count == n ? order : new int[0];
    }
}
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

```java
import java.util.*;

class Solution {
    public String findOrder(String[] words) {
        Map<Character, Set<Character>> adj = new LinkedHashMap<>();
        for (String word : words) {
            for (char ch : word.toCharArray()) adj.putIfAbsent(ch, new LinkedHashSet<>());
        }
        // adj = { "w": set(), "r": set(), "t": set(), "f": set(), "e": set()}
        Map<Character, Integer> degree = new LinkedHashMap<>();
        for (char ch : adj.keySet()) degree.put(ch, 0);
        for (int i = 0; i + 1 < words.length; i++) { // this lets compare each word with next word.
            String curr = words[i], next = words[i + 1];
            int limit = Math.min(curr.length(), next.length());
            int j = 0;
            while (j < limit && curr.charAt(j) == next.charAt(j)) j++;
            if (j == limit) {
                if (curr.length() > next.length()) return "";
            } else {
                char ch1 = curr.charAt(j), ch2 = next.charAt(j);
                if (adj.get(ch1).add(ch2)) {
                    // adj = { "w": {"e"}, "r":{"t"}, "t":{"f"}, "f": set(), "e": {"r"} }
                    degree.put(ch2, degree.get(ch2) + 1); // indegree = { "w": 0, "r": 1, "t": 1, "f": 1, "e": 1}
                }
            }
        }
        Queue<Character> queue = new ArrayDeque<>(); // queue = deque(["w"])
        for (char ch : adj.keySet()) {
            if (degree.get(ch) == 0) queue.offer(ch);
        }
        StringBuilder order = new StringBuilder();
        while (!queue.isEmpty()) {
            char ch = queue.poll();
            order.append(ch);
            for (char nxt : adj.get(ch)) {
                degree.put(nxt, degree.get(nxt) - 1);
                if (degree.get(nxt) == 0) queue.offer(nxt);
            }
        }
        return order.length() == adj.size() ? order.toString() : "";
    }
}
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

```java
import java.util.*;

class Solution {
    public int[] shortestPath(int V, int[][] edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        int[] degree = new int[V];
        for (int[] edge : edges) {
            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
            degree[edge[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int u = 0; u < V; u++) {
            if (degree[u] == 0) queue.offer(u);
        }
        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int[] edge : adj.get(node)) {
                int v = edge[0], w = edge[1];
                if (dist[node] != Integer.MAX_VALUE) dist[v] = Math.min(dist[v], dist[node] + w);
                degree[v]--;
                if (degree[v] == 0) queue.offer(v);
            }
        }
        for (int i = 0; i < V; i++) {
            if (dist[i] == Integer.MAX_VALUE) dist[i] = -1;
        }
        return dist;
    }
}
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

```java
import java.util.*;

class Solution {
    public int[] shortestPath(int V, int[][] edges, int src) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        int[] dist = new int[V];
        Arrays.fill(dist, -1);
        dist[src] = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(src);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int v : adj.get(node)) {
                if (dist[v] == -1) {
                    dist[v] = dist[node] + 1;
                    queue.offer(v);
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

## Shortest Path BFS — Generate the Next States

### 24. ★ Word Ladder — 127

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder/)

Return the shortest transformation length from beginWord to endWord, changing one lowercase letter at a time through wordList; return 0 if impossible. Words have equal length L.

**Input/Output**

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

```java
import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> remaining = new HashSet<>(wordList);
        if (!remaining.contains(endWord)) return 0;
        remaining.remove(beginWord);
        Queue<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);
        int length = 1;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int k = 0; k < levelSize; k++) {
                String word = queue.poll();
                if (word.equals(endWord)) return length;
                char[] chars = word.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char ch = 'a'; ch <= 'z'; ch++) {
                        chars[i] = ch;
                        String candidate = new String(chars);
                        if (remaining.remove(candidate)) queue.offer(candidate);
                    }
                    chars[i] = original;
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

### 25. Minimum Multiplications to Reach End (G-39)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1)

```text
Input: arr = [2, 3, 5, 7, 11], start = 3, end = 2310
Output: 4
```

```java
Queue<Integer> queue = new ArrayDeque<>();
queue.offer(start);
Set<Integer> visited = new HashSet<>();
visited.add(start);
int steps = 0;
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

```java
import java.util.*;

class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<>(wordList);
        if (!words.contains(endWord)) return new ArrayList<>();

        Queue<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);
        Map<String, Integer> distance = new HashMap<>();
        distance.put(beginWord, 0);
        Map<String, List<String>> parents = new HashMap<>();

        while (!queue.isEmpty() && !distance.containsKey(endWord)) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                String word = queue.poll();
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

```java
import java.util.*;

class Solution {
    public long[] dijkstra(int V, int[][] edges, int src) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
            adj.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        long[] distance = new long[V];
        Arrays.fill(distance, Long.MAX_VALUE);
        distance[src] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.offer(new long[]{0, src});
        while (!heap.isEmpty()) {
            long[] entry = heap.poll();
            long cost = entry[0];
            int u = (int) entry[1];
            if (cost != distance[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                long new_cost = cost + weight;
                if (new_cost < distance[v]) {
                    distance[v] = new_cost;
                    heap.offer(new long[]{new_cost, v});
                }
            }
        }
        for (int i = 0; i < V; i++) {
            if (distance[i] == Long.MAX_VALUE) distance[i] = -1;
        }
        return distance;
    }
}
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

```java
import java.util.*;

class Solution {
    public List<Integer> shortestPath(int V, int[][] edges, int source, int destination) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= V; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
            adj.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        long[] distance = new long[V + 1];
        Arrays.fill(distance, Long.MAX_VALUE);
        int[] parent = new int[V + 1];
        Arrays.fill(parent, -1);
        distance[source] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.offer(new long[]{0, source});
        while (!heap.isEmpty()) {
            long[] entry = heap.poll();
            long cost = entry[0];
            int u = (int) entry[1];
            if (cost != distance[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                long new_cost = cost + weight;
                if (new_cost < distance[v]) {
                    distance[v] = new_cost;
                    parent[v] = u;
                    heap.offer(new long[]{new_cost, v});
                }
            }
        }
        if (distance[destination] == Long.MAX_VALUE) return new ArrayList<>(Arrays.asList(-1));
        List<Integer> path = new ArrayList<>();
        int node = destination;
        while (node != -1) {
            path.add(node);
            node = parent[node];
        }
        Collections.reverse(path);
        return path;
    }
}
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

```java
import java.util.*;

class Solution {
    public int minimumEffortPath(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        int[][] effort = new int[rows][cols];
        for (int[] row : effort) Arrays.fill(row, Integer.MAX_VALUE);
        effort[0][0] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, 0, 0});
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!heap.isEmpty()) {
            int[] entry = heap.poll();
            int cost = entry[0], r = entry[1], c = entry[2];
            if (cost != effort[r][c]) continue;
            if (r == rows - 1 && c == cols - 1) return cost;
            for (int[] direction : directions) {
                int nr = r + direction[0], nc = c + direction[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    int new_cost = Math.max(cost, Math.abs(heights[nr][nc] - heights[r][c]));
                    if (new_cost < effort[nr][nc]) {
                        effort[nr][nc] = new_cost;
                        heap.offer(new int[]{new_cost, nr, nc});
                    }
                }
            }
        }
        return 0;
    }
}
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

```java
import java.util.*;

class Solution {
    public int countPaths(int n, int[][] roads) {
        int mod = 1_000_000_007;
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] edge : roads) {
            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
            adj.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        long[] distance = new long[n];
        Arrays.fill(distance, Long.MAX_VALUE);
        int[] ways = new int[n];
        distance[0] = 0;
        ways[0] = 1;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.offer(new long[]{0, 0});
        while (!heap.isEmpty()) {
            long[] entry = heap.poll();
            long cost = entry[0];
            int u = (int) entry[1];
            if (cost != distance[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                long new_cost = cost + weight;
                if (new_cost < distance[v]) {
                    distance[v] = new_cost;
                    ways[v] = ways[u];
                    heap.offer(new long[]{new_cost, v});
                } else if (new_cost == distance[v]) {
                    ways[v] = (int) (((long) ways[v] + ways[u]) % mod);
                }
            }
        }
        return ways[n - 1];
    }
}
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

```java
import java.util.*;

class Solution {
    public int[] bellmanFord(int V, int[][] edges, int src) {
        long inf = Long.MAX_VALUE;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        for (int step = 0; step < V - 1; step++) {
            boolean changed = false;
            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], w = edge[2];
                if (dist[u] != inf && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    changed = true;
                }
            }
            if (changed == false) break;
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u] != inf && dist[u] + w < dist[v]) return new int[]{-1};
        }
        int[] result = new int[V];
        for (int i = 0; i < V; i++) result[i] = dist[i] == inf ? 100000000 : (int) dist[i];
        return result;
    }
}
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

```java
import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dest, int k) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[src] = 0;
        for (int step = 0; step < k + 1; step++) {
            long[] next_dist = dist.clone();
            for (int[] flight : flights) {
                int u = flight[0], v = flight[1], price = flight[2];
                if (dist[u] != Long.MAX_VALUE) next_dist[v] = Math.min(next_dist[v], dist[u] + price);
            }
            dist = next_dist;
        }
        return dist[dest] == Long.MAX_VALUE ? -1 : (int) dist[dest];
    }
}
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

```java
class Solution {
    public void floydWarshall(int[][] dist) {
        int n = dist.length, inf = 100000000;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (dist[i][k] == inf) continue;
                for (int j = 0; j < n; j++) {
                    if (dist[k][j] != inf) dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}
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
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], weight = edge[2];
            dist[u][v] = dist[v][u] = Math.min(dist[u][v], weight);
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
        int answer = -1, best = n;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] <= distanceThreshold) count++;
            }
            if (count <= best) {
                best = count;
                answer = i;
            }
        }
        return answer;
    }
}
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

```java
import java.util.*;

class Solution {
    public int spanningTree(int V, int[][] edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
            adj.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        boolean[] used = new boolean[V];
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, 0});
        int total = 0;
        while (!heap.isEmpty()) {
            int[] entry = heap.poll();
            int weight = entry[0], u = entry[1];
            if (used[u]) continue;
            used[u] = true;
            total += weight;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], w = edge[1];
                if (!used[v]) heap.offer(new int[]{w, v});
            }
        }
        return total;
    }
}
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

```java
class DSU {
    int[] parent;
    int[] rank;

    public DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (rank[root_u] < rank[root_v]) {
            parent[root_u] = root_v;
        } else if (rank[root_u] > rank[root_v]) {
            parent[root_v] = root_u;
        } else {
            parent[root_v] = root_u;
            rank[root_u]++;
        }
        return true;
    }
}
```

2. Union by Size - size array and parent array.

```java
class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}
```

```java
DSU dsu = new DSU(5);

System.out.println(dsu.union(0, 1));           // True
System.out.println(dsu.union(1, 2));           // True
System.out.println(dsu.find(0) == dsu.find(2));  // True
System.out.println(dsu.find(0) == dsu.find(4));  // False
System.out.println(dsu.union(0, 2));           // False: already connected
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

```java
import java.util.*;

class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public int spanningTree(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj) {
        List<int[]> edges = new ArrayList<>();
        //O(V+E)
        for (int u = 0; u < V; u++) {
            for (ArrayList<Integer> edge : adj.get(u)) {
                int v = edge.get(0), weight = edge.get(1);
                if (u < v) edges.add(new int[]{weight, u, v});
            }
        }
        // V log V
        edges.sort(Comparator.comparingInt(a -> a[0]));
        DSU dsu = new DSU(V);
        int total_weight = 0;
        // V x 4 x alpha x 2
        for (int[] edge : edges) {
            if (dsu.union(edge[1], edge[2])) total_weight += edge[0];
        }
        return total_weight;
    }
}
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

```java
class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        DSU dsu = new DSU(n);
        int provinces = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    if (dsu.union(i, j)) provinces--;
                }
            }
        }
        return provinces;
    }
}
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

```java
class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        DSU dsu = new DSU(n);
        int components = n;
        for (int[] edge : connections) {
            if (dsu.union(edge[0], edge[1])) components--;
        }
        return components - 1;
    }
}
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

```java
import java.util.*;

class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU(accounts.size());
        Map<String, Integer> email_owner = new HashMap<>();
        for (int i = 0; i < accounts.size(); i++) {
            List<String> account = accounts.get(i);
            for (int j = 1; j < account.size(); j++) {
                String email = account.get(j);
                if (email_owner.containsKey(email)) dsu.union(i, email_owner.get(email));
                else email_owner.put(email, i);
            }
        }
        Map<Integer, List<String>> groups = new HashMap<>();
        for (Map.Entry<String, Integer> entry : email_owner.entrySet()) {
            int root = dsu.find(entry.getValue());
            groups.computeIfAbsent(root, key -> new ArrayList<>()).add(entry.getKey());
        }
        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> entry : groups.entrySet()) {
            List<String> emails = entry.getValue();
            Collections.sort(emails);
            List<String> merged = new ArrayList<>();
            merged.add(accounts.get(entry.getKey()).get(0));
            merged.addAll(emails);
            result.add(merged);
        }
        return result;
    }
}
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

```java
import java.util.*;

class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public List<Integer> numOfIslands(int n, int m, int[][] operators) {
        DSU dsu = new DSU(n * m);
        boolean[][] land = new boolean[n][m];
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int islands = 0;
        List<Integer> result = new ArrayList<>();
        for (int[] operator : operators) {
            int r = operator[0], c = operator[1];
            if (land[r][c]) {
                result.add(islands);
                continue;
            }
            land[r][c] = true;
            islands++;
            int node = r * m + c;
            for (int[] direction : directions) {
                int nr = r + direction[0], nc = c + direction[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && land[nr][nc]) {
                    int neighbor = nr * m + nc;
                    if (dsu.union(node, neighbor)) islands--;
                }
            }
            result.add(islands);
        }
        return result;
    }
}
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

```java
import java.util.*;

class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public int largestIsland(int[][] grid) {
        int n = grid.length;
        DSU dsu = new DSU(n * n);
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) continue;
                for (int[] direction : directions) {
                    int nr = r + direction[0], nc = c + direction[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        dsu.union(r * n + c, nr * n + nc);
                    }
                }
            }
        }
        int answer = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    answer = Math.max(answer, dsu.size[dsu.find(r * n + c)]);
                    continue;
                }
                Set<Integer> roots = new HashSet<>();
                for (int[] direction : directions) {
                    int nr = r + direction[0], nc = c + direction[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        roots.add(dsu.find(nr * n + nc));
                    }
                }
                int area = 1;
                for (int group : roots) area += dsu.size[group];
                answer = Math.max(answer, area);
            }
        }
        return answer;
    }
}
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

```java
import java.util.*;

class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) parent[node] = find(parent[node]);
        return parent[node];
    }

    public boolean union(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        } else {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
        return true;
    }
}

class Solution {
    public int removeStones(int[][] stones) {
        int n = stones.length;
        DSU dsu = new DSU(n);
        Map<Integer, Integer> row_owner = new HashMap<>();
        Map<Integer, Integer> col_owner = new HashMap<>();
        int components = n;
        for (int i = 0; i < n; i++) {
            int row = stones[i][0], col = stones[i][1];
            if (row_owner.containsKey(row)) {
                if (dsu.union(i, row_owner.get(row))) components--;
            } else {
                row_owner.put(row, i);
            }
            if (col_owner.containsKey(col)) {
                if (dsu.union(i, col_owner.get(col))) components--;
            } else {
                col_owner.put(col, i);
            }
        }
        return n - components;
    }
}
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

```java
import java.util.*;

class Solution {
    public int kosaraju(ArrayList<ArrayList<Integer>> adj) {
        int n = adj.size();
        boolean[] visited = new boolean[n];
        List<Integer> order = new ArrayList<>();
        for (int node = 0; node < n; node++) {
            if (!visited[node]) dfs(node, adj, visited, order);
        }
        ArrayList<ArrayList<Integer>> reverse = new ArrayList<>();
        for (int i = 0; i < n; i++) reverse.add(new ArrayList<>());
        for (int node = 0; node < n; node++) {
            for (int neighbor : adj.get(node)) reverse.get(neighbor).add(node);
        }
        Arrays.fill(visited, false);
        int components = 0;
        for (int i = order.size() - 1; i >= 0; i--) {
            int node = order.get(i);
            if (!visited[node]) {
                components++;
                reverseDfs(node, reverse, visited);
            }
        }
        return components;
    }

    private void dfs(int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited, List<Integer> order) {
        visited[node] = true;
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) dfs(neighbor, adj, visited, order);
        }
        order.add(node);
    }

    private void reverseDfs(int node, ArrayList<ArrayList<Integer>> reverse, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : reverse.get(node)) {
            if (!visited[neighbor]) reverseDfs(neighbor, reverse, visited);
        }
    }
}
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

```java
import java.util.*;

class Solution {
    private int timer;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (List<Integer> edge : connections) {
            int u = edge.get(0), v = edge.get(1);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        int[] discovery = new int[n], low = new int[n];
        Arrays.fill(discovery, -1);
        Arrays.fill(low, -1);
        List<List<Integer>> bridges = new ArrayList<>();
        timer = 0;
        for (int node = 0; node < n; node++) {
            if (discovery[node] == -1) dfs(node, -1, adj, discovery, low, bridges);
        }
        return bridges;
    }

    private void dfs(int node, int parent, List<List<Integer>> adj, int[] discovery, int[] low, List<List<Integer>> bridges) {
        discovery[node] = low[node] = timer++;
        for (int neighbor : adj.get(node)) {
            if (neighbor == parent) continue;
            if (discovery[neighbor] == -1) {
                dfs(neighbor, node, adj, discovery, low, bridges);
                low[node] = Math.min(low[node], low[neighbor]);
                if (low[neighbor] > discovery[node]) bridges.add(Arrays.asList(node, neighbor));
            } else {
                low[node] = Math.min(low[node], discovery[neighbor]);
            }
        }
    }
}
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

```java
import java.util.*;

class Solution {
    private int timer;

    public ArrayList<Integer> articulationPoints(int V, ArrayList<ArrayList<Integer>> adj) {
        int[] discovery = new int[V], low = new int[V];
        Arrays.fill(discovery, -1);
        Arrays.fill(low, -1);
        boolean[] marked = new boolean[V];
        timer = 0;
        for (int node = 0; node < V; node++) {
            if (discovery[node] == -1) dfs(node, -1, adj, discovery, low, marked);
        }
        ArrayList<Integer> result = new ArrayList<>();
        for (int node = 0; node < V; node++) {
            if (marked[node]) result.add(node);
        }
        if (result.isEmpty()) result.add(-1);
        return result;
    }

    private void dfs(int node, int parent, ArrayList<ArrayList<Integer>> adj, int[] discovery, int[] low, boolean[] marked) {
        discovery[node] = low[node] = timer++;
        int children = 0;
        for (int neighbor : adj.get(node)) {
            if (neighbor == parent) continue;
            if (discovery[neighbor] == -1) {
                children++;
                dfs(neighbor, node, adj, discovery, low, marked);
                low[node] = Math.min(low[node], low[neighbor]);
                if (parent != -1 && low[neighbor] >= discovery[node]) marked[node] = true;
            } else {
                low[node] = Math.min(low[node], discovery[neighbor]);
            }
        }
        if (parent == -1 && children > 1) marked[node] = true;
    }
}
```

## Additional Problems — Not in the Agreed List

### 46. ★ Find if Path Exists in adj — 1971

[LeetCode/GFG Link](https://leetcode.com/problems/find-if-path-exists-in-graph/)

**Input/Output**

```text
Input: n = 6, edges = [[0,1],[0,2],[1,3],[2,3],[4,5]], source = 0, destination = 5
Output: false
```

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

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

```java

```

**Time Space Complexity**

- **Time:**
- **Space:**
