# Recursion and Backtracking — Python

## 1. Subsets

Return every subset of an array of distinct integers, including the empty subset.

[LeetCode 78](https://leetcode.com/problems/subsets/)

```python
class Solution:
    def subsets(self, nums):
        result, path = [], []

        def dfs(start):
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result
```

```
flowchart TD
    A["dfs(0) → save []"]
    B["dfs(1) → save [1]"]
    C["dfs(2) → save [2]"]
    D["dfs(3) → save [3]"]
    E["dfs(2) → save [1, 2]"]
    F["dfs(3) → save [1, 3]"]
    G["dfs(3) → save [2, 3]"]
    H["dfs(3) → save [1, 2, 3]"]

    A -->|"append 1"| B
    A -->|"append 2"| C
    A -->|"append 3"| D
    B -->|"append 2"| E
    B -->|"append 3"| F
    E -->|"append 3"| H
    C -->|"append 3"| G
```

DFS visits from left to right, going as deep as possible.

**Time complexity:** O(n × 2ⁿ), including copying subsets; n is the array length.

## 2. Subsets II

Return all unique subsets when the array may contain duplicates. Sorting groups duplicates so they can be skipped at the same recursion depth.

[LeetCode 90](https://leetcode.com/problems/subsets-ii/)

```python
class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        result, path = [], []

        def dfs(start):
            result.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result
```

**Time complexity:** O(n log n + n × 2ⁿ) worst case, including sorting and copying subsets.

## 3. Combination Sum

Find combinations of distinct positive candidates totaling the target. Each candidate can be reused any number of times.

[LeetCode 39](https://leetcode.com/problems/combination-sum/)

```python
class Solution:
    def combinationSum(self, candidates, target):
        nums = sorted(candidates)
        result, path = [], []

        def dfs(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                dfs(i, remaining - nums[i])
                path.pop()

        dfs(0, target)
        return result
```

**Time complexity:** O(n log n + (n + 1)^(D + 1)) loose upper bound, including output copies; n is the candidate count and D = floor(target / smallest candidate).

## 4. Combination Sum II

Find unique combinations of positive candidates totaling the target. Each array position can be used once; duplicate candidate values are allowed.

[LeetCode 40](https://leetcode.com/problems/combination-sum-ii/)

```python
class Solution:
    def combinationSum2(self, candidates, target):
        nums = sorted(candidates)
        result, path = [], []

        def dfs(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                dfs(i + 1, remaining - nums[i])
                path.pop()

        dfs(0, target)
        return result
```

**Time complexity:** O(n log n + n × 2ⁿ) worst-case upper bound, including sorting and output copies; n is the number of candidates.

## 5. Combination Sum III

Find combinations of k distinct numbers from 1 through 9 that sum to n. Each number can be used once.

[LeetCode 216](https://leetcode.com/problems/combination-sum-iii/)

```python
class Solution:
    def combinationSum3(self, k, n):
        result, path = [], []

        def dfs(start, slots, remaining):
            if slots == 0:
                if remaining == 0:
                    result.append(path.copy())
                return
            for num in range(start, 11 - slots):
                if num > remaining:
                    break
                path.append(num)
                dfs(num + 1, slots - 1, remaining - num)
                path.pop()

        dfs(1, k, n)
        return result
```

**Time complexity:** O(k × C(9, k)) upper bound for 1 ≤ k ≤ 9, including output copies. The candidate pool is fixed at 9.

## 6. String Permutations

Return unique permutations in sorted order. For `abc`, return `abc, acb, bac, bca, cab, cba`.

[GFG: Permutations of a String](https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1)

```python
class Solution:
    def findPermutation(self, s):
        chars = sorted(s)
        used = [False] * len(chars)
        result, path = [], []

        def dfs():
            if len(path) == len(chars):
                result.append("".join(path))
                return
            for i, char in enumerate(chars):
                if used[i]:
                    continue
                if i > 0 and char == chars[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(char)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return result
```

**Time complexity:** O(n × n!) worst case for n distinct characters, including copying permutations.

## 7. Phone Letter Combinations

Return all letter combinations represented by digits 2–9 on a phone keypad. An empty input returns an empty list.

[LeetCode 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```python
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result, path = [], []

        def dfs(index):
            if index == len(digits):
                result.append("".join(path))
                return
            for letter in letters[digits[index]]:
                path.append(letter)
                dfs(index + 1)
                path.pop()

        dfs(0)
        return result
```

**Time complexity:** O(d × 4ᵈ) worst case, where d is the number of digits; includes copying strings.

## 8. Rat in a Maze

Return all paths from the top-left to bottom-right of an n × n maze. A 1 is open and a 0 is blocked. Move D, L, R, or U without revisiting a cell in the same path; results are in lexicographic order.

[GFG: Rat in a Maze](https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1)

```python
class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        if n == 0 or maze[0][0] == 0 or maze[-1][-1] == 0:
            return []
        visited = [[False] * n for _ in range(n)]
        moves = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]
        result, path = [], []

        def dfs(row, col):
            if row == n - 1 and col == n - 1:
                result.append("".join(path))
                return
            visited[row][col] = True
            for dr, dc, move in moves:
                nr, nc = row + dr, col + dc
                if (0 <= nr < n and 0 <= nc < n
                        and maze[nr][nc] == 1 and not visited[nr][nc]):
                    path.append(move)
                    dfs(nr, nc)
                    path.pop()
            visited[row][col] = False

        dfs(0, 0)
        return result
```

**Time complexity:** O(n² × 3^(n²)) loose worst-case upper bound, including copying paths. After the first move, at most three directions remain because the previous cell is visited.

## 9. N-Queens

Return all boards placing n queens on an n × n board so no two queens share a row, column, or diagonal.

[LeetCode 51](https://leetcode.com/problems/n-queens/)

```python
class Solution:
    def solveNQueens(self, n):
        board = [["."] * n for _ in range(n)]
        cols, down, up = set(), set(), set()
        result = []

        def dfs(row):
            if row == n:
                result.append(["".join(line) for line in board])
                return
            for col in range(n):
                d, u = row - col, row + col
                if col in cols or d in down or u in up:
                    continue
                cols.add(col)
                down.add(d)
                up.add(u)
                board[row][col] = "Q"
                dfs(row + 1)
                board[row][col] = "."
                cols.remove(col)
                down.remove(d)
                up.remove(u)

        dfs(0)
        return result
```

**Time complexity:** O(n × n! + S × n²) upper bound for this column-scanning implementation, where S is the number of valid boards; Python set operations assume average O(1).

## 10. Sudoku Solver

Fill a valid, solvable 9 × 9 Sudoku board in place. Empty cells contain `.`; each row, column, and 3 × 3 box must contain digits 1–9 once.

[LeetCode 37](https://leetcode.com/problems/sudoku-solver/)

```python
class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    empty.append((r, c))
                else:
                    box = (r // 3) * 3 + c // 3
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box].add(value)

        def dfs(index):
            if index == len(empty):
                return True
            r, c = empty[index]
            box = (r // 3) * 3 + c // 3
            for value in "123456789":
                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    continue
                board[r][c] = value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
                if dfs(index + 1):
                    return True
                rows[r].remove(value)
                cols[c].remove(value)
                boxes[box].remove(value)
                board[r][c] = "."
            return False

        dfs(0)
```

**Time complexity:** O(9ᴱ) loose search upper bound, where E is the number of empty cells. Board initialization takes O(81).

## 11. Generate Parentheses

Return all valid strings containing n pairs of parentheses. Add an opening bracket while fewer than n are used; add a closing bracket only when an unmatched opening bracket exists.

[LeetCode 22](https://leetcode.com/problems/generate-parentheses/)

```python
class Solution:
    def generateParenthesis(self, n):
        result, path = [], []

        def dfs(open_count, close_count):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                dfs(open_count, close_count + 1)
                path.pop()

        dfs(0, 0)
        return result
```

**Time complexity:** O(n × Cₙ), including copying strings, where Cₙ = (2n)! / (n! × (n + 1)!) is the nth Catalan number; equivalently O(4ⁿ / √n).
