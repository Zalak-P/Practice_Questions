# Graphs — Java

V = vertices; E = edges; R and C = grid dimensions; α = inverse Ackermann function. Recursive alternatives can exceed Python recursion limits or Java stack depth on long paths; use the iterative alternative where supplied.

Video series and approaches follwed - https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

## Basic Grid — Explore One Connected Component at a Time

### 1. ★ Number of Islands — 200

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands/)

Count 4-directionally connected groups of '1' cells in a nonempty grid. Visited land is changed to '0'.

**Input/Output**

```text
Input: grid = [["1","1","0"],["0","0","1"]]
Output: 2
```

**Code**

```java
class Solution {
    public int numIslands(char[][] grid) {
        int islands = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
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
Input: image = [[1,1],[1,0]], sr = 0, sc = 0, color = 2
Output: [[2,2],[2,0]]
```

**Code**

```java
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int originalColor = image[sr][sc];
        // Return early if the original color equals the new color, to prevent endless revisits.
        if (originalColor == color) return image;
        dfs(image, sr, sc, originalColor, color);
        return image;
    }

    private void dfs(int[][] image, int r, int c, int originalColor, int color) {
        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] != originalColor) return;
        image[r][c] = color;
        dfs(image, r + 1, c, originalColor, color);
        dfs(image, r - 1, c, originalColor, color);
        dfs(image, r, c + 1, originalColor, color);
        dfs(image, r, c - 1, originalColor, color);
    }
}
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 3. Number of Distinct Islands (G-16)

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-distinct-islands/)

**Code**

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
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Code**

```java
import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new ArrayDeque<>();
        int minutes = 0, freshCount = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) freshCount++;
                if (grid[r][c] == 2) queue.offer(new int[]{r, c});
            }
        }
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!queue.isEmpty() && freshCount > 0) {
            minutes++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int[] direction : directions) {
                    int nr = cell[0] + direction[0], nc = cell[1] + direction[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        freshCount--;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
        return freshCount == 0 ? minutes : -1;
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
Input: mat = [[0,1,1],[1,1,1]]
Output: [[0,1,2],[1,2,3]]
```

**Code**

```java
import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        int[][] answerMatrix = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            Arrays.fill(answerMatrix[r], -1);
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) {
                    answerMatrix[r][c] = 0;
                    queue.offer(new int[]{r, c});
                }
            }
        }
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int[] direction : directions) {
                int nr = cell[0] + direction[0], nc = cell[1] + direction[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && answerMatrix[nr][nc] == -1) {
                    answerMatrix[nr][nc] = answerMatrix[cell[0]][cell[1]] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        return answerMatrix;
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

**Code**

```java
class Solution {
    public void solve(char[][] board) {
        int rows = board.length, cols = board[0].length;
        // Step 1: Mark border-connected 'O's.
        for (int r = 0; r < rows; r++) {
            dfs(board, r, 0);
            dfs(board, r, cols - 1);
        }
        for (int c = 0; c < cols; c++) {
            dfs(board, 0, c);
            dfs(board, rows - 1, c);
        }
        // Step 2: Flip remaining 'O' to 'X', 'T' back to 'O'.
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == 'T') board[r][c] = 'O';
            }
        }
    }

    private void dfs(char[][] board, int r, int c) {
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != 'O') return;
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

**Code**

```java

```

## Grid Shortest Path — BFS with Queue and Distance

### 8. Shortest Distance in a Binary Maze (G-36)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1)

**Code**

```java

```

## BFS / DFS — Graph Traversal

### 9. ★ BFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)

BFS visits nodes level by level, using a queue. Mark each node visited when adding it to the queue to prevent duplicates.

**Input/Output**

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,2,3]
```

**Code**

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> bfs(ArrayList<ArrayList<Integer>> adj) {
        ArrayList<Integer> result = new ArrayList<>();
        if (adj.isEmpty()) return result;
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new ArrayDeque<>();
        visited.add(0);
        queue.offer(0);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            result.add(node);
            for (int neighbor : adj.get(node)) {
                if (visited.add(neighbor)) queue.offer(neighbor);
            }
        }
        return result;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input adjacency list.

### 10. ★ DFS Traversal of a Graph

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

DFS explores one branch as deeply as possible before backtracking. Start from vertex 0 and follow adjacency-list order.

**Input/Output**

```text
Input: adj = [[1,2],[0,3],[0],[1]]
Output: [0,1,3,2]
```

**Code**

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
        Set<Integer> visited = new HashSet<>();
        ArrayList<Integer> result = new ArrayList<>();
        if (!adj.isEmpty()) traverse(0, adj, visited, result);
        return result;
    }

    private void traverse(int node, ArrayList<ArrayList<Integer>> adj, Set<Integer> visited, ArrayList<Integer> result) {
        visited.add(node);
        result.add(node);
        for (int neighbor : adj.get(node)) {
            if (!visited.contains(neighbor)) traverse(neighbor, adj, visited, result);
        }
    }
}
```

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

### 11. ★ Number of Provinces — 547

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-provinces/)

Given an adjacency matrix isConnected, count the groups of directly or indirectly connected cities.

**Input/Output**

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Code**

```java
import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        Set<Integer> visited = new HashSet<>();
        int answer = 0, n = isConnected.length;
        for (int i = 0; i < n; i++) {
            if (visited.contains(i)) continue;
            answer++;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(i);
            visited.add(i);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor = 0; neighbor < n; neighbor++) {
                    if (isConnected[node][neighbor] == 1 && visited.add(neighbor)) queue.offer(neighbor);
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

### 12. ★ Detect Cycle in an Undirected Graph — BFS and DFS

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

```java
import java.util.*;

class Solution {
    public boolean isCycle(ArrayList<ArrayList<Integer>> adj) {
        Set<Integer> visited = new HashSet<>();
        for (int start = 0; start < adj.size(); start++) {
            if (!visited.add(start)) continue;
            Queue<int[]> queue = new ArrayDeque<>();
            queue.offer(new int[]{start, -1});
            while (!queue.isEmpty()) {
                int[] current = queue.poll();
                int node = current[0], parent = current[1];
                for (int neighbor : adj.get(node)) {
                    if (visited.add(neighbor)) queue.offer(new int[]{neighbor, node});
                    else if (neighbor != parent) return true;
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
    public boolean hasCycleUndirected(int vertices, int[][] edges) {
        // Build the adjacency list.
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < vertices; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        Set<Integer> visited = new HashSet<>();
        // Check all vertices to handle disconnected components.
        for (int v = 0; v < vertices; v++) {
            if (!visited.contains(v) && dfs(v, -1, graph, visited)) return true;
        }
        return false;
    }

    private boolean dfs(int node, int parent, List<List<Integer>> graph, Set<Integer> visited) {
        visited.add(node);
        for (int neighbor : graph.get(node)) {
            // If the neighbor has not been visited, explore it.
            if (!visited.contains(neighbor)) {
                if (dfs(neighbor, node, graph, visited)) return true;
            // If the neighbor is visited and is not the parent, a cycle exists.
            } else if (neighbor != parent) return true;
        }
        return false;
    }
}
```

### 13. ★ Detect Cycle in a Directed Graph — DFS

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
    public boolean hasCycleDirected(int vertices, int[][] edges) {
        // Build the adjacency list.
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < vertices; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) graph.get(edge[0]).add(edge[1]);
        Set<Integer> visited = new HashSet<>();
        Set<Integer> recStack = new HashSet<>();
        // Check all vertices to handle disconnected components.
        for (int v = 0; v < vertices; v++) {
            if (!visited.contains(v) && dfs(v, graph, visited, recStack)) return true;
        }
        return false;
    }

    private boolean dfs(int node, List<List<Integer>> graph, Set<Integer> visited, Set<Integer> recStack) {
        visited.add(node);
        recStack.add(node); // Tracks nodes in the current recursion path.
        for (int neighbor : graph.get(node)) {
            // If unvisited, recurse on the neighbor.
            if (!visited.contains(neighbor)) {
                if (dfs(neighbor, graph, visited, recStack)) return true;
            // If the neighbor is in the active recursion stack, a cycle exists.
            } else if (recStack.contains(neighbor)) return true;
        }
        // Backtrack: remove the node from the active path before returning.
        recStack.remove(node);
        return false;
    }
}
```

Use three states:

- 0: Unvisited.
- 1: Previously visited is not enough—the node must still be active in the current path.
- 2: Completed—all outgoing neighbors explored.

```java
import java.util.*;

class Solution {
    public boolean isCyclic(ArrayList<ArrayList<Integer>> adj) {
        int[] state = new int[adj.size()];
        for (int node = 0; node < adj.size(); node++) {
            if (state[node] == 0 && dfs(node, adj, state)) return true;
        }
        return false;
    }

    private boolean dfs(int node, ArrayList<ArrayList<Integer>> adj, int[] state) {
        state[node] = 1;
        for (int neighbor : adj.get(node)) {
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

## Bipartite Graph — Two-color BFS / DFS


A bipartite graph is a graph whose nodes have 2 different colors, or you can assign 2 diff colors to the adjcent nodes.
Thus dividing the graph in 2 groups where no edges are interconnected within same group.
                                                                  
                                                                     6 - 8
Observations:-                                                       |
- Linear graphs with no cycles are always Bipartite, 1 -> 2-> 4 -> 5 10
                                                                    \
                                                                    7 - 9
- Any graph with even cycle **length** is also bipartite.

### 14. ★ Is Graph Bipartite? — 785

[LeetCode/GFG Link](https://leetcode.com/problems/is-graph-bipartite/)

Check whether an undirected adjacency-list graph can be colored with two colors. Covers disconnected components.

**Input/Output**

```text
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
```

**Code**

1. **Two-Coloring Test:** Try to color every vertex using any two colors (e.g., Red and Blue) so that no two adjecent connected vertices share the same color. If you can do it, it is bipartite. (BFS Approach)

```java
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length];
        Arrays.fill(color, -1);
        for (int start = 0; start < graph.length; start++) {
            if (color[start] != -1) continue;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(start);
            color[start] = 0;
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == -1) {
                        color[neighbor] = 1 - color[node];
                        queue.offer(neighbor);
                    } else if (color[neighbor] == color[node]) return false;
                }
            }
        }
        return true;
    }
}
```

2. **Odd Cycle Check:** If the graph contains a loop (cycle) with an odd number of edges/vertices, it is not bipartite. (DFS Approach)

```java
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] color = new int[graph.length];
        Arrays.fill(color, -1);
        for (int node = 0; node < graph.length; node++) {
            if (color[node] == -1 && !dfs(node, 0, graph, color)) return false;
        }
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

## Directed Graph — DFS State Tracking

### 15. Find Eventual Safe States — DFS State Tracking (G-20)

[LeetCode/GFG Link](https://leetcode.com/problems/find-eventual-safe-states/)

**Code**

```java

```

## Kahn’s Algorithm — Indegree / Outdegree


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

### 16. ★ Detect Cycle in a Directed Graph

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

```java
import java.util.*;

class Solution {
    public boolean isCyclic(ArrayList<ArrayList<Integer>> adj) {
        int[] indegree = new int[adj.size()];
        for (List<Integer> neighbors : adj) {
            for (int neighbor : neighbors) indegree[neighbor]++;
        }
        // Queue containing all nodes whose indegree is 0.
        Queue<Integer> queue = new ArrayDeque<>();
        for (int node = 0; node < adj.size(); node++) {
            if (indegree[node] == 0) queue.offer(node);
        }
        int processed = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            processed++;
            for (int neighbor : adj.get(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return processed != adj.size();
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E)

### 17. ★ Find Eventual Safe States — 802

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
        for (int i = 0; i < n; i++) reverse.add(new ArrayList<>());
        int[] outdegree = new int[n];
        for (int node = 0; node < n; node++) {
            outdegree[node] = graph[node].length;
            for (int neighbor : graph[node]) reverse.get(neighbor).add(node);
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
        List<Integer> answer = new ArrayList<>();
        for (int node = 0; node < n; node++) {
            if (safe[node]) answer.add(node);
        }
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the reversed graph.

### 18. ★ Topological Sort — Kahn’s Algorithm

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
            int u = queue.poll();
            order.add(u);
            for (int v : adj.get(u)) {
                if (--indegree[v] == 0) queue.offer(v);
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
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Code**

```java
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[1]).add(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int node = 0; node < numCourses; node++) {
            if (indegree[node] == 0) queue.offer(node);
        }
        int processed = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            processed++;
            for (int neighbor : adj.get(node)) {
                if (--indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return processed == numCourses;
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
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] (one valid order)
```

**Code**

```java
import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[1]).add(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int node = 0; node < numCourses; node++) {
            if (indegree[node] == 0) queue.offer(node);
        }
        int[] order = new int[numCourses];
        int count = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            order[count++] = node;
            for (int neighbor : adj.get(node)) {
                if (--indegree[neighbor] == 0) queue.offer(neighbor);
            }
        }
        return count == numCourses ? order : new int[0];
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
Input: words = ["za","zb","ca","cb"]
Output: "zacb" (one valid order; z before c and a before b)
```

**Code**

```java
import java.util.*;

class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adj = new LinkedHashMap<>();
        Map<Character, Integer> degree = new HashMap<>();
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                adj.putIfAbsent(ch, new HashSet<>());
                degree.putIfAbsent(ch, 0);
            }
        }
        for (int i = 0; i + 1 < words.length; i++) {
            String first = words[i], second = words[i + 1];
            int j = 0, limit = Math.min(first.length(), second.length());
            while (j < limit && first.charAt(j) == second.charAt(j)) j++;
            if (j == limit) {
                if (first.length() > second.length()) return "";
            } else {
                char a = first.charAt(j), b = second.charAt(j);
                if (adj.get(a).add(b)) degree.put(b, degree.get(b) + 1);
            }
        }
        Queue<Character> queue = new ArrayDeque<>();
        for (char ch : adj.keySet()) {
            if (degree.get(ch) == 0) queue.offer(ch);
        }
        StringBuilder order = new StringBuilder();
        while (!queue.isEmpty()) {
            char ch = queue.poll();
            order.append(ch);
            for (char next : adj.get(ch)) {
                degree.put(next, degree.get(next) - 1);
                if (degree.get(next) == 0) queue.offer(next);
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

### 22. ★ Shortest Path in a Directed Acyclic Graph

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
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[0] = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                if (dist[u] != inf) dist[v] = Math.min(dist[v], dist[u] + weight);
                if (--degree[v] == 0) queue.offer(v);
            }
        }
        int[] answer = new int[V];
        for (int i = 0; i < V; i++) answer[i] = dist[i] == inf ? -1 : Math.toIntExact(dist[i]);
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

## Shortest Path BFS — Explicit Graph

### 23. ★ Shortest Path in an Undirected Graph with Unit Weights

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
            int u = queue.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
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

**Code**

```java
import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<>(wordList);
        if (!words.contains(endWord)) return 0;
        Queue<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);
        words.remove(beginWord);
        int length = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                if (word.equals(endWord)) return length;
                char[] letters = word.toCharArray();
                for (int position = 0; position < letters.length; position++) {
                    char original = letters[position];
                    for (char ch = 'a'; ch <= 'z'; ch++) {
                        letters[position] = ch;
                        String next = new String(letters);
                        if (words.remove(next)) queue.offer(next);
                    }
                    letters[position] = original;
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

**Code**

```java

```

## All Shortest Sequences — BFS and Backtracking

### 26. Word Ladder II (G-30, G-31)

[LeetCode/GFG Link](https://leetcode.com/problems/word-ladder-ii/)

**Code**

```java

```

## Dijkstra’s Algorithm

### 27. ★ Dijkstra’s Algorithm

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
    public int[] dijkstra(int V, int[][] edges, int src) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
            adj.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        long[] dist = new long[V];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[src] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.offer(new long[]{0, src});
        while (!heap.isEmpty()) {
            long[] current = heap.poll();
            long cost = current[0];
            int u = (int) current[1];
            if (cost != dist[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                long candidate = cost + weight;
                if (candidate < dist[v]) {
                    dist[v] = candidate;
                    heap.offer(new long[]{candidate, v});
                }
            }
        }
        int[] answer = new int[V];
        for (int i = 0; i < V; i++) answer[i] = dist[i] == Long.MAX_VALUE ? -1 : Math.toIntExact(dist[i]);
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2)) with a heap that can retain outdated entries.
- **Space:** O(V + E), including the adjacency list and heap with outdated entries.

### 28. Print Shortest Path in a Weighted Undirected Graph (G-35)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1)

**Code**

```java

```

### 29. ★ Path With Minimum Effort — 1631

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
        int[][] effort = new int[rows][cols];
        for (int[] row : effort) Arrays.fill(row, Integer.MAX_VALUE);
        effort[0][0] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[]{0, 0, 0});
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!heap.isEmpty()) {
            int[] current = heap.poll();
            int cost = current[0], r = current[1], c = current[2];
            if (cost != effort[r][c]) continue;
            if (r == rows - 1 && c == cols - 1) return cost;
            for (int[] direction : directions) {
                int nr = r + direction[0], nc = c + direction[1];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                int candidate = Math.max(cost, Math.abs(heights[r][c] - heights[nr][nc]));
                if (candidate < effort[nr][nc]) {
                    effort[nr][nc] = candidate;
                    heap.offer(new int[]{candidate, nr, nc});
                }
            }
        }
        return -1;
    }
}
```

**Time Space Complexity**

- **Time:** O(RC log(RC + 1))
- **Space:** O(R × C) for distances and the heap (a grid has O(R × C) edges).

### 30. Number of Ways to Arrive at Destination (G-40)

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)

**Code**

```java

```

## Bellman–Ford — Repeated Edge Relaxation

### 31. ★ Bellman–Ford Algorithm

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
    public int[] bellmanFord(int V, int[][] edges, int src) {
        long inf = Long.MAX_VALUE / 4;
        long[] dist = new long[V];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        for (int pass = 0; pass < V - 1; pass++) {
            boolean changed = false;
            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], weight = edge[2];
                if (dist[u] != inf && dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    changed = true;
                }
            }
            if (!changed) break;
        }
        for (int[] edge : edges) {
            if (dist[edge[0]] != inf && dist[edge[0]] + edge[2] < dist[edge[1]]) return new int[]{-1};
        }
        int[] answer = new int[V];
        for (int i = 0; i < V; i++) answer[i] = dist[i] == inf ? 100000000 : Math.toIntExact(dist[i]);
        return answer;
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
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
```

**Code**

```java
import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int inf = Integer.MAX_VALUE;
        int[] dist = new int[n];
        Arrays.fill(dist, inf);
        dist[src] = 0;
        for (int pass = 0; pass <= k; pass++) {
            int[] next = dist.clone();
            for (int[] flight : flights) {
                int u = flight[0], v = flight[1], price = flight[2];
                if (dist[u] != inf) next[v] = Math.min(next[v], dist[u] + price);
            }
            dist = next;
        }
        return dist[dst] == inf ? -1 : dist[dst];
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
        int inf = Integer.MAX_VALUE / 4;
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], inf);
            dist[i][i] = 0;
        }
        for (int[] edge : edges) {
            dist[edge[0]][edge[1]] = Math.min(dist[edge[0]][edge[1]], edge[2]);
            dist[edge[1]][edge[0]] = Math.min(dist[edge[1]][edge[0]], edge[2]);
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
        int answer = -1, smallest = n;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] <= distanceThreshold) count++;
            }
            if (count <= smallest) {
                smallest = count;
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

## DSU / Union Find — Basic Operations

### 35. ★ Implement DSU — Path Compression and Union by Size

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
            int temp = a;
            a = b;
            b = temp;
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

## DSU — Count Components and Redundant Connections

### 36. ★ Number of Operations to Make Network Connected — 1319

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
            int temp = a;
            a = b;
            b = temp;
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
        for (int[] connection : connections) {
            if (dsu.union(connection[0], connection[1])) components--;
        }
        return components - 1;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E × α(V))
- **Space:** O(V) for DSU.

## DSU — Merge Entities through Shared Identifiers

### 37. ★ Accounts Merge — 721

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
            int temp = a;
            a = b;
            b = temp;
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
                if (owner.containsKey(email)) dsu.union(i, owner.get(email));
                else owner.put(email, i);
            }
        }
        Map<Integer, List<String>> groups = new HashMap<>();
        for (Map.Entry<String, Integer> entry : owner.entrySet()) {
            int root = dsu.find(entry.getValue());
            groups.computeIfAbsent(root, key -> new ArrayList<>()).add(entry.getKey());
        }
        List<List<String>> answer = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> entry : groups.entrySet()) {
            List<String> emails = entry.getValue();
            Collections.sort(emails);
            List<String> merged = new ArrayList<>();
            merged.add(accounts.get(entry.getKey()).get(0));
            merged.addAll(emails);
            answer.add(merged);
        }
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(A + M × (L + α(A)) + U log(U + 1) × L), where A = accounts, M = email occurrences, U = unique emails, L = maximum email length.
- **Space:** O(A + M + U × L), including temporary email lists and output; sorting can also use linear temporary storage.

### 38. ★ Most Stones Removed with Same Row or Column — 947

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
            int temp = a;
            a = b;
            b = temp;
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

## DSU on Grids — Merge Neighboring Land

### 39. Number of Islands II — Online Queries (G-51)

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-islands-ii/)

**Code**

```java

```

### 40. Making a Large Island (G-52)

[LeetCode/GFG Link](https://leetcode.com/problems/making-a-large-island/)

**Code**

```java

```

## Minimum Spanning Tree — Grow a Tree Using a Min-heap

### 41. ★ Prim’s Algorithm

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
            int[] current = heap.poll();
            int weight = current[0], u = current[1];
            if (used[u]) continue;
            used[u] = true;
            total += weight;
            for (int[] edge : adj.get(u)) {
                if (!used[edge[0]]) heap.offer(new int[]{edge[1], edge[0]});
            }
        }
        return total;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

## Minimum Spanning Tree — Sort Edges and Merge Using DSU

### 42. ★ Kruskal’s Algorithm

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
            int temp = a;
            a = b;
            b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public int spanningTree(int V, int[][] edges) {
        DSU dsu = new DSU(V);
        int total = 0;
        int[][] sorted = edges.clone();
        Arrays.sort(sorted, Comparator.comparingInt(edge -> edge[2]));
        for (int[] edge : sorted) {
            if (dsu.union(edge[0], edge[1])) total += edge[2];
        }
        return total;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2) + E × α(V))
- **Space:** O(V + E), including DSU and the sorted edge copy.

## Advanced DFS — Finishing Order and Reversed Graph

### 43. ★ Kosaraju’s Algorithm

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
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            reverse.get(edge[1]).add(edge[0]);
        }
        boolean[] seen = new boolean[V];
        List<Integer> order = new ArrayList<>();
        for (int start = 0; start < V; start++) {
            if (seen[start]) continue;
            seen[start] = true;
            Deque<int[]> stack = new ArrayDeque<>();
            stack.push(new int[]{start, 0});
            while (!stack.isEmpty()) {
                int[] frame = stack.peek();
                int u = frame[0];
                if (frame[1] == adj.get(u).size()) {
                    order.add(u);
                    stack.pop();
                } else {
                    int v = adj.get(u).get(frame[1]++);
                    if (!seen[v]) {
                        seen[v] = true;
                        stack.push(new int[]{v, 0});
                    }
                }
            }
        }
        Arrays.fill(seen, false);
        int count = 0;
        for (int i = order.size() - 1; i >= 0; i--) {
            int start = order.get(i);
            if (seen[start]) continue;
            count++;
            seen[start] = true;
            Deque<Integer> stack = new ArrayDeque<>();
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

## Advanced DFS — Discovery Times and Low-link Values

### 44. ★ Critical Connections in a Network — 1192

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
        for (int eid = 0; eid < connections.size(); eid++) {
            int u = connections.get(eid).get(0), v = connections.get(eid).get(1);
            adj.get(u).add(new int[]{v, eid});
            adj.get(v).add(new int[]{u, eid});
        }
        int[] tin = new int[n], low = new int[n], parent = new int[n], parentEdge = new int[n];
        Arrays.fill(tin, -1);
        Arrays.fill(parent, -1);
        Arrays.fill(parentEdge, -1);
        int timer = 0;
        List<List<Integer>> bridges = new ArrayList<>();
        for (int start = 0; start < n; start++) {
            if (tin[start] != -1) continue;
            tin[start] = low[start] = timer++;
            Deque<int[]> stack = new ArrayDeque<>();
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
                int[] edge = adj.get(u).get(frame[1]++);
                int v = edge[0], eid = edge[1];
                if (eid == parentEdge[u]) continue;
                if (tin[v] == -1) {
                    parent[v] = u;
                    parentEdge[v] = eid;
                    tin[v] = low[v] = timer++;
                    stack.push(new int[]{v, 0});
                } else low[u] = Math.min(low[u], tin[v]);
            }
        }
        return bridges;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the adjacency list.

### 45. Articulation Points in a Graph (G-56)

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/articulation-point-1/1)

**Code**

```java

```

## Additional Problems — Not in the Agreed List

### 46. ★ Find if Path Exists in Graph — 1971

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
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        queue.offer(source);
        visited.add(source);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (node == destination) return true;
            for (int neighbor : graph.get(node)) {
                if (visited.add(neighbor)) queue.offer(neighbor);
            }
        }
        return false;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 47. ★ Clone Graph — 133

[LeetCode/GFG Link](https://leetcode.com/problems/clone-graph/)

Given a node in a connected undirected graph, return a deep copy of the graph. Every cloned node must be a new object with the same value and corresponding cloned neighbors.

**Input/Output**

```text
Input: Adjacency list: [[2],[1]] (node values are 1 and 2)
Output: A new graph with adjacency list [[2],[1]], sharing no nodes with the input
```

**Code**

```java
import java.util.*;

// Node is provided by LeetCode.
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Map<Node, Node> clones = new HashMap<>();
        clones.put(node, new Node(node.val));
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(node);
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            for (Node neighbor : current.neighbors) {
                if (!clones.containsKey(neighbor)) {
                    clones.put(neighbor, new Node(neighbor.val));
                    queue.offer(neighbor);
                }
                clones.get(current).neighbors.add(clones.get(neighbor));
            }
        }
        return clones.get(node);
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V) auxiliary for the map and queue, plus O(V + E) for the cloned output graph.

### 48. ★ Keys and Rooms — 841

[LeetCode/GFG Link](https://leetcode.com/problems/keys-and-rooms/)

Visit room 0 and follow its keys to other rooms. Return whether every room can be reached. Each room is processed once.

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
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new ArrayDeque<>();
        visited.add(0);
        queue.offer(0);
        while (!queue.isEmpty()) {
            int room = queue.poll();
            for (int key : rooms.get(room)) {
                if (visited.add(key)) queue.offer(key);
            }
        }
        return visited.size() == rooms.size();
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V), excluding the input; E is the total number of keys.

### 49. ★ Number of Connected Components in an Undirected Graph — 323

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Count connected components, including isolated vertices, in an undirected graph.

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
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        Set<Integer> visited = new HashSet<>();
        int components = 0;
        for (int start = 0; start < n; start++) {
            if (!visited.add(start)) continue;
            components++;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(start);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph.get(node)) {
                    if (visited.add(neighbor)) queue.offer(neighbor);
                }
            }
        }
        return components;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E)
- **Space:** O(V + E), including the constructed adjacency list.

### 50. ★ Shortest Bridge — 934

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
        int[] start = null;
        for (int r = 0; r < rows && start == null; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    start = new int[]{r, c};
                    break;
                }
            }
        }
        if (start == null) return -1;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Deque<int[]> stack = new ArrayDeque<>();
        Queue<int[]> queue = new ArrayDeque<>();
        stack.push(start);
        queue.offer(start);
        grid[start[0]][start[1]] = 2;
        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            for (int[] direction : directions) {
                int r = cell[0] + direction[0], c = cell[1] + direction[1];
                if (r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] == 1) {
                    grid[r][c] = 2;
                    int[] next = {r, c};
                    stack.push(next);
                    queue.offer(next);
                }
            }
        }
        int flips = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int[] direction : directions) {
                    int r = cell[0] + direction[0], c = cell[1] + direction[1];
                    if (r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] != 2) {
                        if (grid[r][c] == 1) return flips;
                        grid[r][c] = 2;
                        queue.offer(new int[]{r, c});
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

### 51. ★ Max Area of Island — 695

[LeetCode/GFG Link](https://leetcode.com/problems/max-area-of-island/)

Return the largest 4-connected area of 1s in a nonempty binary grid. Visited land is changed to 0.

**Input/Output**

```text
Input: grid = [[1,1,0],[1,0,1]]
Output: 3
```

**Code**

```java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int answer = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) answer = Math.max(answer, dfs(grid, r, c));
            }
        }
        return answer;
    }

    private int dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != 1) return 0;
        grid[r][c] = 0;
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
    }
}
```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C) for the DFS stack.

### 52. ★ Pacific Atlantic Water Flow — 417

[LeetCode/GFG Link](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Find cells from which water reaches both oceans. Search backward from ocean boundaries to equal or higher cells in the nonempty height grid.

**Input/Output**

```text
Input: heights = [[1,2],[4,3]]
Output: [[0,1],[1,0],[1,1]] (any order)
```

**Code**

```java

```

**Time Space Complexity**

- **Time:** O(R × C)
- **Space:** O(R × C)

### 53. ★ Possible Bipartition — 886

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
        for (int[] edge : dislikes) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        int[] color = new int[n + 1];
        Arrays.fill(color, -1);
        for (int start = 1; start <= n; start++) {
            if (color[start] != -1) continue;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(start);
            color[start] = 0;
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph.get(node)) {
                    if (color[neighbor] == -1) {
                        color[neighbor] = 1 - color[node];
                        queue.offer(neighbor);
                    } else if (color[neighbor] == color[node]) return false;
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

### 54. ★ Topological Sort — DFS

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

**Input/Output**

```text
Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
Output: [0,2,1,3] (one valid order)
```

**Code**

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> topoSort(int V, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) adj.get(edge[0]).add(edge[1]);
        int[] state = new int[V];
        ArrayList<Integer> order = new ArrayList<>();
        for (int start = 0; start < V; start++) {
            if (state[start] != 0) continue;
            state[start] = 1;
            Deque<int[]> stack = new ArrayDeque<>();
            stack.push(new int[]{start, 0});
            while (!stack.isEmpty()) {
                int[] frame = stack.peek();
                int u = frame[0];
                if (frame[1] == adj.get(u).size()) {
                    order.add(u);
                    state[u] = 2;
                    stack.pop();
                } else {
                    int v = adj.get(u).get(frame[1]++);
                    if (state[v] == 1) return new ArrayList<>();
                    if (state[v] == 0) {
                        state[v] = 1;
                        stack.push(new int[]{v, 0});
                    }
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

### 55. ★ Find All Possible Recipes from Given Supplies — 2115

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
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        Map<String, List<Integer>> dependents = new HashMap<>();
        int[] remaining = new int[recipes.length];
        for (int i = 0; i < recipes.length; i++) {
            remaining[i] = ingredients.get(i).size();
            for (String item : ingredients.get(i)) {
                dependents.computeIfAbsent(item, key -> new ArrayList<>()).add(i);
            }
        }
        Queue<String> queue = new ArrayDeque<>();
        Set<String> available = new HashSet<>();
        for (String supply : supplies) {
            if (available.add(supply)) queue.offer(supply);
        }
        for (int i = 0; i < recipes.length; i++) {
            if (remaining[i] == 0 && available.add(recipes[i])) queue.offer(recipes[i]);
        }
        while (!queue.isEmpty()) {
            String item = queue.poll();
            for (int i : dependents.getOrDefault(item, Collections.emptyList())) {
                remaining[i]--;
                if (remaining[i] == 0 && available.add(recipes[i])) queue.offer(recipes[i]);
            }
        }
        List<String> answer = new ArrayList<>();
        for (String recipe : recipes) {
            if (available.contains(recipe)) answer.add(recipe);
        }
        return answer;
    }
}
```

**Time Space Complexity**

- **Time:** O(N + I + S) expected hash-table operations; N = recipes, I = ingredient occurrences, S = supplies. String hashing additionally depends on string lengths.
- **Space:** O(N + I + S).

### 56. ★ Shortest Path in Binary Matrix — 1091

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
        queue.offer(new int[]{0, 0, 1});
        grid[0][0] = 1;
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1], distance = cell[2];
            if (r == n - 1 && c == n - 1) return distance;
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) continue;
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        queue.offer(new int[]{nr, nc, distance + 1});
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

### 57. ★ Open the Lock — 752

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
        Set<String> blocked = new HashSet<>(Arrays.asList(deadends));
        if (blocked.contains("0000")) return -1;
        Queue<String> queue = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        queue.offer("0000");
        seen.add("0000");
        int moves = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String state = queue.poll();
                if (state.equals(target)) return moves;
                char[] digits = state.toCharArray();
                for (int position = 0; position < 4; position++) {
                    char original = digits[position];
                    for (int change : new int[]{-1, 1}) {
                        digits[position] = (char) ('0' + (original - '0' + change + 10) % 10);
                        String next = new String(digits);
                        if (!blocked.contains(next) && seen.add(next)) queue.offer(next);
                    }
                    digits[position] = original;
                }
            }
            moves++;
        }
        return -1;
    }
}
```

**Time Space Complexity**

- **Time:** O(D + 10⁴ × 8) for four fixed digits; D = number of deadends.
- **Space:** O(D + 10⁴) for fixed four-digit states; D = deadends.

### 58. ★ Snakes and Ladders — 909

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
        Queue<int[]> queue = new ArrayDeque<>();
        Set<Integer> seen = new HashSet<>();
        queue.offer(new int[]{1, 0});
        seen.add(1);
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int square = current[0], rolls = current[1];
            if (square == n * n) return rolls;
            for (int next = square + 1; next <= Math.min(square + 6, n * n); next++) {
                int rowFromBottom = (next - 1) / n, col = (next - 1) % n;
                int row = n - 1 - rowFromBottom;
                if (rowFromBottom % 2 == 1) col = n - 1 - col;
                int destination = board[row][col] == -1 ? next : board[row][col];
                if (seen.add(destination)) queue.offer(new int[]{destination, rolls + 1});
            }
        }
        return -1;
    }
}
```

**Time Space Complexity**

- **Time:** O(n²)
- **Space:** O(n²).

### 59. ★ Network Delay Time — 743

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
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] edge : times) adj.get(edge[0]).add(new int[]{edge[1], edge[2]});
        long[] dist = new long[n + 1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[k] = 0;
        PriorityQueue<long[]> heap = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        heap.offer(new long[]{0, k});
        while (!heap.isEmpty()) {
            long[] current = heap.poll();
            long cost = current[0];
            int u = (int) current[1];
            if (cost != dist[u]) continue;
            for (int[] edge : adj.get(u)) {
                int v = edge[0], weight = edge[1];
                long candidate = cost + weight;
                if (candidate < dist[v]) {
                    dist[v] = candidate;
                    heap.offer(new long[]{candidate, v});
                }
            }
        }
        long answer = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Long.MAX_VALUE) return -1;
            answer = Math.max(answer, dist[i]);
        }
        return Math.toIntExact(answer);
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E log(E + 2))
- **Space:** O(V + E), including the adjacency list and heap.

### 60. ★ Negative Cycle Detection

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
            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], weight = edge[2];
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
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

### 61. ★ Redundant Connection — 684

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
            int temp = a;
            a = b;
            b = temp;
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
}

class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        DSU dsu = new DSU(edges.length + 1);
        for (int[] edge : edges) {
            if (!dsu.union(edge[0], edge[1])) return new int[]{edge[0], edge[1]};
        }
        return new int[0];
    }
}
```

**Time Space Complexity**

- **Time:** O(n × α(n))
- **Space:** O(n) for DSU.

### 62. ★ Min Cost to Connect All Points — 1584

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
            for (int i = 0; i < n; i++) {
                if (!used[i] && (u == -1 || best[i] < best[u])) u = i;
            }
            used[u] = true;
            total += best[u];
            for (int v = 0; v < n; v++) {
                if (!used[v]) {
                    int distance = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
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

### 63. ★ Evaluate Division — 399

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
    private static class Edge {
        String node;
        double weight;
        Edge(String node, double weight) {
            this.node = node;
            this.weight = weight;
        }
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, List<Edge>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, key -> new ArrayList<>()).add(new Edge(b, values[i]));
            graph.computeIfAbsent(b, key -> new ArrayList<>()).add(new Edge(a, 1.0 / values[i]));
        }
        double[] answer = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            answer[i] = evaluate(queries.get(i).get(0), queries.get(i).get(1), graph);
        }
        return answer;
    }

    private double evaluate(String source, String target, Map<String, List<Edge>> graph) {
        if (!graph.containsKey(source) || !graph.containsKey(target)) return -1.0;
        Deque<Edge> stack = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        stack.push(new Edge(source, 1.0));
        seen.add(source);
        while (!stack.isEmpty()) {
            Edge current = stack.pop();
            if (current.node.equals(target)) return current.weight;
            for (Edge edge : graph.get(current.node)) {
                if (seen.add(edge.node)) stack.push(new Edge(edge.node, current.weight * edge.weight));
            }
        }
        return -1.0;
    }
}
```

**Time Space Complexity**

- **Time:** O(V + E + Q(V + E)) expected map/set operations; Q = queries. Variable-name hashing additionally depends on string length.
- **Space:** O(V + E) auxiliary, plus O(Q) output.

### 64. ★ All Paths From Source to Target — 797

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
        if (node == graph.length - 1) {
            result.add(new ArrayList<>(path));
            return;
        }
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

### 65. ★ Longest Increasing Path in a Matrix — 329

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
        int answer = 0;
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[0].length; c++) answer = Math.max(answer, dfs(r, c, matrix, memo));
        }
        return answer;
    }

    private int dfs(int r, int c, int[][] matrix, int[][] memo) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] direction : directions) {
            int nr = r + direction[0], nc = c + direction[1];
            if (nr >= 0 && nr < matrix.length && nc >= 0 && nc < matrix[0].length && matrix[nr][nc] > matrix[r][c]) {
                best = Math.max(best, 1 + dfs(nr, nc, matrix, memo));
            }
        }
        memo[r][c] = best;
        return best;
    }
}
```

**Topological layers — avoids recursion**

```java
import java.util.*;

class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int[][] degree = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                for (int[] direction : directions) {
                    int nr = r + direction[0], nc = c + direction[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && matrix[nr][nc] > matrix[r][c]) degree[r][c]++;
                }
                if (degree[r][c] == 0) queue.offer(new int[]{r, c});
            }
        }
        int length = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                int r = cell[0], c = cell[1];
                for (int[] direction : directions) {
                    int nr = r + direction[0], nc = c + direction[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && matrix[nr][nc] < matrix[r][c]) {
                        if (--degree[nr][nc] == 0) queue.offer(new int[]{nr, nc});
                    }
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
