# Recursion and Backtracking — Java

## 1. Subsets

Return every subset of an array of distinct integers, including the empty subset.

[LeetCode 78](https://leetcode.com/problems/subsets/)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void dfs(int[] nums, int start, List<Integer> path,
                     List<List<Integer>> result) {
        result.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            dfs(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

**Time complexity:** O(n × 2ⁿ), including copying subsets; n is the array length.

## 2. Subsets II

Return all unique subsets when the array may contain duplicates. Sorting groups duplicates so they can be skipped at the same recursion depth.

[LeetCode 90](https://leetcode.com/problems/subsets-ii/)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        nums = nums.clone();
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void dfs(int[] nums, int start, List<Integer> path,
                     List<List<Integer>> result) {
        result.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            path.add(nums[i]);
            dfs(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

**Time complexity:** O(n log n + n × 2ⁿ) worst case, including sorting and copying subsets.

## 3. Combination Sum

Find combinations of distinct positive candidates totaling the target. Each candidate can be reused any number of times.

[LeetCode 39](https://leetcode.com/problems/combination-sum/)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int[] nums = candidates.clone();
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, target, new ArrayList<>(), result);
        return result;
    }

    private void dfs(int[] nums, int start, int remaining, List<Integer> path,
                     List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            if (nums[i] > remaining) break;
            path.add(nums[i]);
            dfs(nums, i, remaining - nums[i], path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

**Time complexity:** O(n log n + (n + 1)^(D + 1)) loose upper bound, including output copies; n is the candidate count and D = floor(target / smallest candidate).

## 4. Combination Sum II

Find unique combinations of positive candidates totaling the target. Each array position can be used once; duplicate candidate values are allowed.

[LeetCode 40](https://leetcode.com/problems/combination-sum-ii/)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        int[] nums = candidates.clone();
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, target, new ArrayList<>(), result);
        return result;
    }

    private void dfs(int[] nums, int start, int remaining, List<Integer> path,
                     List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            if (nums[i] > remaining) break;
            path.add(nums[i]);
            dfs(nums, i + 1, remaining - nums[i], path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

**Time complexity:** O(n log n + n × 2ⁿ) worst-case upper bound, including sorting and output copies; n is the number of candidates.

## 5. Combination Sum III

Find combinations of k distinct numbers from 1 through 9 that sum to n. Each number can be used once.

[LeetCode 216](https://leetcode.com/problems/combination-sum-iii/)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(1, k, n, new ArrayList<>(), result);
        return result;
    }

    private void dfs(int start, int slots, int remaining, List<Integer> path,
                     List<List<Integer>> result) {
        if (slots == 0) {
            if (remaining == 0) result.add(new ArrayList<>(path));
            return;
        }
        for (int num = start; num <= 10 - slots; num++) {
            if (num > remaining) break;
            path.add(num);
            dfs(num + 1, slots - 1, remaining - num, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

**Time complexity:** O(k × C(9, k)) upper bound for 1 ≤ k ≤ 9, including output copies. The candidate pool is fixed at 9.

## 6. String Permutations

Return unique permutations in sorted order. For `abc`, return `abc, acb, bac, bca, cab, cba`.

[GFG: Permutations of a String](https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1)

```java
import java.util.*;

class Solution {
    public ArrayList<String> findPermutation(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        ArrayList<String> result = new ArrayList<>();
        dfs(chars, new boolean[chars.length], new StringBuilder(), result);
        return result;
    }

    private void dfs(char[] chars, boolean[] used, StringBuilder path,
                     ArrayList<String> result) {
        if (path.length() == chars.length) {
            result.add(path.toString());
            return;
        }
        for (int i = 0; i < chars.length; i++) {
            if (used[i]) continue;
            if (i > 0 && chars[i] == chars[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.append(chars[i]);
            dfs(chars, used, path, result);
            path.deleteCharAt(path.length() - 1);
            used[i] = false;
        }
    }
}
```

**Time complexity:** O(n × n!) worst case for n distinct characters, including copying permutations.

## 7. Phone Letter Combinations

Return all letter combinations represented by digits 2–9 on a phone keypad. An empty input returns an empty list.

[LeetCode 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```java
import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) return result;
        String[] letters = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        dfs(digits, 0, letters, new StringBuilder(), result);
        return result;
    }

    private void dfs(String digits, int index, String[] letters,
                     StringBuilder path, List<String> result) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }
        for (char letter : letters[digits.charAt(index) - '0'].toCharArray()) {
            path.append(letter);
            dfs(digits, index + 1, letters, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

**Time complexity:** O(d × 4ᵈ) worst case, where d is the number of digits; includes copying strings.

## 8. Rat in a Maze

Return all paths from the top-left to bottom-right of an n × n maze. A 1 is open and a 0 is blocked. Move D, L, R, or U without revisiting a cell in the same path; results are in lexicographic order.

[GFG: Rat in a Maze](https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1)

```java
import java.util.*;

class Solution {
    public ArrayList<String> ratInMaze(int[][] maze) {
        ArrayList<String> result = new ArrayList<>();
        int n = maze.length;
        if (n == 0 || maze[0][0] == 0 || maze[n - 1][n - 1] == 0) return result;
        dfs(0, 0, maze, new boolean[n][n], new StringBuilder(), result);
        return result;
    }

    private void dfs(int row, int col, int[][] maze, boolean[][] visited,
                     StringBuilder path, ArrayList<String> result) {
        int n = maze.length;
        if (row == n - 1 && col == n - 1) {
            result.add(path.toString());
            return;
        }
        int[] dr = {1, 0, 0, -1}, dc = {0, -1, 1, 0};
        char[] moves = {'D', 'L', 'R', 'U'};
        visited[row][col] = true;
        for (int i = 0; i < 4; i++) {
            int nr = row + dr[i], nc = col + dc[i];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n
                    && maze[nr][nc] == 1 && !visited[nr][nc]) {
                path.append(moves[i]);
                dfs(nr, nc, maze, visited, path, result);
                path.deleteCharAt(path.length() - 1);
            }
        }
        visited[row][col] = false;
    }
}
```

**Time complexity:** O(n² × 3^(n²)) loose worst-case upper bound, including copying paths. After the first move, at most three directions remain because the previous cell is visited.

## 9. N-Queens

Return all boards placing n queens on an n × n board so no two queens share a row, column, or diagonal.

[LeetCode 51](https://leetcode.com/problems/n-queens/)

```java
import java.util.*;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        List<List<String>> result = new ArrayList<>();
        dfs(0, board, new boolean[n], new boolean[2 * n], new boolean[2 * n], result);
        return result;
    }

    private void dfs(int row, char[][] board, boolean[] cols,
                     boolean[] down, boolean[] up, List<List<String>> result) {
        int n = board.length;
        if (row == n) {
            List<String> solution = new ArrayList<>();
            for (char[] line : board) solution.add(new String(line));
            result.add(solution);
            return;
        }
        for (int col = 0; col < n; col++) {
            int d = row - col + n, u = row + col;
            if (cols[col] || down[d] || up[u]) continue;
            cols[col] = down[d] = up[u] = true;
            board[row][col] = 'Q';
            dfs(row + 1, board, cols, down, up, result);
            board[row][col] = '.';
            cols[col] = down[d] = up[u] = false;
        }
    }
}
```

**Time complexity:** O(n × n! + S × n²) upper bound for this column-scanning implementation, where S is the number of valid boards; Python set operations assume average O(1).

## 10. Sudoku Solver

Fill a valid, solvable 9 × 9 Sudoku board in place. Empty cells contain `.`; each row, column, and 3 × 3 box must contain digits 1–9 once.

[LeetCode 37](https://leetcode.com/problems/sudoku-solver/)

```java
import java.util.*;

class Solution {
    public void solveSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][10], cols = new boolean[9][10];
        boolean[][] boxes = new boolean[9][10];
        List<int[]> empty = new ArrayList<>();
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    empty.add(new int[]{r, c});
                } else {
                    int digit = board[r][c] - '0', box = (r / 3) * 3 + c / 3;
                    rows[r][digit] = cols[c][digit] = boxes[box][digit] = true;
                }
            }
        }
        dfs(0, empty, board, rows, cols, boxes);
    }

    private boolean dfs(int index, List<int[]> empty, char[][] board,
                        boolean[][] rows, boolean[][] cols, boolean[][] boxes) {
        if (index == empty.size()) return true;
        int r = empty.get(index)[0], c = empty.get(index)[1];
        int box = (r / 3) * 3 + c / 3;
        for (int digit = 1; digit <= 9; digit++) {
            if (rows[r][digit] || cols[c][digit] || boxes[box][digit]) continue;
            board[r][c] = (char) ('0' + digit);
            rows[r][digit] = cols[c][digit] = boxes[box][digit] = true;
            if (dfs(index + 1, empty, board, rows, cols, boxes)) return true;
            rows[r][digit] = cols[c][digit] = boxes[box][digit] = false;
            board[r][c] = '.';
        }
        return false;
    }
}
```

**Time complexity:** O(9ᴱ) loose search upper bound, where E is the number of empty cells. Board initialization takes O(81).

## 11. Generate Parentheses

Return all valid strings containing n pairs of parentheses. Add an opening bracket while fewer than n are used; add a closing bracket only when an unmatched opening bracket exists.

[LeetCode 22](https://leetcode.com/problems/generate-parentheses/)

```java
import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        dfs(n, 0, 0, new StringBuilder(), result);
        return result;
    }

    private void dfs(int n, int open, int close, StringBuilder path, List<String> result) {
        if (path.length() == 2 * n) {
            result.add(path.toString());
            return;
        }
        if (open < n) {
            path.append('(');
            dfs(n, open + 1, close, path, result);
            path.deleteCharAt(path.length() - 1);
        }
        if (close < open) {
            path.append(')');
            dfs(n, open, close + 1, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

**Time complexity:** O(n × Cₙ), including copying strings, where Cₙ = (2n)! / (n! × (n + 1)!) is the nth Catalan number; equivalently O(4ⁿ / √n).

## 12. Reverse a Stack

Reverse the stack using recursion and insertion at the bottom. The Java deque uses its front as the top; the Python list uses its end. The buffer alternative stores popped elements and pushes them back in pop order. “No extra data structure” does not mean O(1) total auxiliary space: recursion uses O(n) stack frames.

[Problem link](https://www.geeksforgeeks.org/problems/reverse-a-stack/1)

```java
import java.util.*;

class Solution {
    public void reverseStack(Deque<Integer> stack) {
        if (stack.isEmpty()) return;
        int top = stack.pop();
        reverseStack(stack);
        insertAtBottom(stack, top);
    }

    private void insertAtBottom(Deque<Integer> stack, int value) {
        if (stack.isEmpty()) {
            stack.push(value);
            return;
        }
        int top = stack.pop();
        insertAtBottom(stack, value);
        stack.push(top);
    }

    public void reverseWithBuffer(Deque<Integer> stack) {
        List<Integer> buffer = new ArrayList<>();
        while (!stack.isEmpty()) buffer.add(stack.pop());
        for (int value : buffer) stack.push(value);
    }
}
```

**Time complexity:** Recursive: O(n²). Buffer: O(n).

**Space complexity:** Recursive: O(n) call stack. Buffer: O(n) extra storage.

## 13. Tower of Hanoi

Move n disks from rod 1 to rod 3 using rod 2, never placing a larger disk on a smaller disk. Return moves as (source, destination) pairs; n = 0 gives no moves.

[Problem link](https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)

```java
import java.util.*;

class Solution {
    public List<int[]> towerOfHanoi(int n) {
        List<int[]> moves = new ArrayList<>();
        move(n, 1, 3, 2, moves);
        return moves;
    }

    private void move(int n, int from, int to, int auxiliary, List<int[]> moves) {
        if (n == 0) return;
        move(n - 1, from, auxiliary, to, moves);
        moves.add(new int[]{from, to});
        move(n - 1, auxiliary, to, from, moves);
    }
}
```

**Time complexity:** O(2ⁿ), producing 2ⁿ − 1 moves.

**Space complexity:** O(n) call stack, plus O(2ⁿ) output storage.

## 14. Merge Sort

Sort the input array in place by recursively sorting its halves and merging them through one reusable temporary array. The merge is stable.

[Problem link](https://www.geeksforgeeks.org/problems/merge-sort/1)

```java
class Solution {
    public void mergeSort(int[] nums) {
        sort(nums, new int[nums.length], 0, nums.length - 1);
    }

    private void sort(int[] a, int[] temp, int left, int right) {
        if (left >= right) return;
        int mid = left + (right - left) / 2;
        sort(a, temp, left, mid);
        sort(a, temp, mid + 1, right);
        int i = left, j = mid + 1, k = left;
        while (i <= mid && j <= right) {
            if (a[i] <= a[j]) temp[k++] = a[i++];
            else temp[k++] = a[j++];
        }
        while (i <= mid) temp[k++] = a[i++];
        while (j <= right) temp[k++] = a[j++];
        for (k = left; k <= right; k++) a[k] = temp[k];
    }
}
```

**Time complexity:** O(n log n).

**Space complexity:** O(n) temporary array plus O(log n) call stack.

## 15. Quick Sort

Sort the input array in place using the last element as the pivot. Partition smaller values to its left, then recursively sort both sides.

[Problem link](https://www.geeksforgeeks.org/problems/quick-sort/1)

```java
class Solution {
    public void quickSort(int[] nums) {
        sort(nums, 0, nums.length - 1);
    }

    private void sort(int[] a, int low, int high) {
        if (low >= high) return;
        int pivot = partition(a, low, high);
        sort(a, low, pivot - 1);
        sort(a, pivot + 1, high);
    }

    private int partition(int[] a, int low, int high) {
        int pivot = a[high], boundary = low;
        for (int i = low; i < high; i++) {
            if (a[i] < pivot) swap(a, boundary++, i);
        }
        swap(a, boundary, high);
        return boundary;
    }

    private void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
```

**Time complexity:** O(n log n) average for random input order; O(n²) worst case, including sorted or all-equal input with this pivot choice.

**Space complexity:** O(log n) average call stack; O(n) worst case.

## 16. Flatten BST to Sorted List

Rearrange existing BST nodes into an ascending right-linked chain. Every left pointer becomes null. Uses recursive inorder traversal; omit TreeNode if supplied by the platform.

[Problem link](https://leetcode.com/problems/increasing-order-search-tree/)

```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

class Solution {
    public TreeNode increasingBST(TreeNode root) {
        TreeNode dummy = new TreeNode(0);
        TreeNode[] tail = {dummy};
        inorder(root, tail);
        tail[0].right = null;
        return dummy.right;
    }

    private void inorder(TreeNode node, TreeNode[] tail) {
        if (node == null) return;
        inorder(node.left, tail);
        node.left = null;
        tail[0].right = node;
        tail[0] = node;
        inorder(node.right, tail);
    }
}
```

**Time complexity:** O(n), where n is the number of tree nodes.

**Space complexity:** O(h) call stack, where h is tree height; O(n) worst case.

## 17. Flatten a Linked List

Flatten sorted vertical bottom-linked lists connected horizontally by next into one sorted bottom-linked list. Reuse existing nodes and clear horizontal links. This is the sorted-list flattening problem, distinct from multilevel doubly linked-list flattening.

[Problem link](https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1)

```java
class Node {
    int data;
    Node next, bottom;
    Node(int data) { this.data = data; }
}

class Solution {
    public Node flatten(Node root) {
        if (root == null || root.next == null) return root;
        Node right = flatten(root.next);
        root.next = null;
        return merge(root, right);
    }

    private Node merge(Node a, Node b) {
        Node dummy = new Node(0), tail = dummy;
        while (a != null || b != null) {
            if (b == null || (a != null && a.data <= b.data)) {
                tail.bottom = a;
                a = a.bottom;
            } else {
                tail.bottom = b;
                b = b.bottom;
            }
            tail = tail.bottom;
            tail.next = null;
        }
        return dummy.bottom;
    }
}
```

**Time complexity:** O(N × k) upper bound, where N is the total node count and k is the number of vertical lists; O(N²) worst case.

**Space complexity:** O(k) call stack.

## 18. Permutations II

Return unique permutations of an integer array that may contain duplicates. Sort a copy and skip equal unused candidates at the same recursion depth. This is the array counterpart of String Permutations.

[Problem link](https://leetcode.com/problems/permutations-ii/)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        nums = nums.clone();
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, new boolean[nums.length], new ArrayList<>(), result);
        return result;
    }

    private void dfs(int[] nums, boolean[] used, List<Integer> path,
                     List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.add(nums[i]);
            dfs(nums, used, path, result);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
```

**Time complexity:** O(n × n!) worst case, including output copies.

**Space complexity:** O(n) auxiliary, excluding output.

## 19. Regular Expression Matching

Match the entire string using a valid pattern: dot matches one character, and star repeats the preceding element zero or more times. Memoized recursion avoids recomputing the same string/pattern index pair.

[Problem link](https://leetcode.com/problems/regular-expression-matching/)

```java
class Solution {
    public boolean isMatch(String s, String p) {
        Boolean[][] memo = new Boolean[s.length() + 1][p.length() + 1];
        return match(s, p, 0, 0, memo);
    }

    private boolean match(String s, String p, int i, int j, Boolean[][] memo) {
        if (memo[i][j] != null) return memo[i][j];
        boolean result;
        if (j == p.length()) {
            result = i == s.length();
        } else {
            boolean first = i < s.length()
                    && (p.charAt(j) == '.' || p.charAt(j) == s.charAt(i));
            if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                result = match(s, p, i, j + 2, memo)
                        || (first && match(s, p, i + 1, j, memo));
            } else {
                result = first && match(s, p, i + 1, j + 1, memo);
            }
        }
        memo[i][j] = result;
        return result;
    }
}
```

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string and pattern lengths.

**Space complexity:** O((m + 1) × (n + 1)) memo, plus O(m + n) call stack.
