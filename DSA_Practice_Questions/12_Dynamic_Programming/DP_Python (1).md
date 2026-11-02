# Dynamic Programming — Python

## 1. House Robber I

Maximize money robbed from a line of houses without robbing adjacent houses. At each house, choose between skipping it and taking it with the best total two houses back.

[LeetCode 198](https://leetcode.com/problems/house-robber/)

### Recursion + Memoization

At each index, compare skipping the house with taking it and continuing two positions ahead. Cache the answer for each index.

```python
class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = ans
        return ans
```

**Time complexity:** O(n).
**Space complexity:** O(n) memo plus O(n) recursion stack.

### Bottom-Up DP

Fill the DP array from right to left using the same take-or-skip recurrence.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization.
        dp[N], dp[N - 1] = 0, nums[N - 1]

        # DP table.
        for i in range(N - 2, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])

        return dp[0]
```

**Time complexity:** O(n).
**Space complexity:** O(n).

### Constant Space

Keep only the two previous DP values needed for the next decision.

```python
class Solution:
    def rob(self, nums):
        prev2 = prev1 = 0
        for money in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + money)
        return prev1
```

**Time complexity:** O(n), where n is the number of houses.
**Space complexity:** O(1).

## 2. House Robber II

Houses form a circle, so the first and last are adjacent. Take the better result from excluding the first house or excluding the last house.

[LeetCode 213](https://leetcode.com/problems/house-robber-ii/)

### Recursion + Memoization

Solve two linear ranges: exclude the last house or exclude the first. Use a separate memo for each range because its endpoint differs.

```python
class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.memo = {}
        exclude_last = self.robFrom(0, nums[:-1])

        self.memo = {}
        exclude_first = self.robFrom(0, nums[1:])

        return max(exclude_last, exclude_first)

    def robFrom(self, i, nums):
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        self.memo[i] = ans
        return ans
```

**Time complexity:** O(n).
**Space complexity:** O(n) memo plus O(n) recursion stack.

### Bottom-Up DP

Fill the DP array from right to left using the same take-or-skip recurrence.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.robFrom(nums[:-1]),  # Exclude last house
            self.robFrom(nums[1:])    # Exclude first house
        )

    def robFrom(self, nums):
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]
```

**Time complexity:** O(n).
**Space complexity:** O(n).

### Constant Space

Keep only the two previous DP values needed for the next decision.

```python
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_range(start, end):
            prev2 = prev1 = 0
            for i in range(start, end):
                prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
            return prev1

        return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))
```

**Time complexity:** O(n), where n is the number of houses.
**Space complexity:** O(1).

## 3. Frog Jump

Reach the last stone with minimum energy. A jump from i to j costs |height[i] − height[j]|; jump one or two positions.

[GeeksforGeeks: Frog Jump](https://www.geeksforgeeks.org/problems/geek-jump/1)

```python
class Solution:
    def minCost(self, height):
        prev2 = prev1 = 0
        for i in range(1, len(height)):
            one_step = prev1 + abs(heights[i] - heights[i - 1])

            two_steps = float('inf')
            if i > 1:
                two_steps = prev2 + abs(heights[i] - heights[i - 2])

            current = min(one_step, two_steps)
            prev2, prev1 = prev1, current

        return prev1
```

**Time complexity:** O(n), where n is the number of stones.

## 4. Frog Jump with X Distance

Minimize the same height-based energy cost when each jump can move 1 through x positions; x ≥ 1.

[GeeksforGeeks: Minimal Cost of Jumps](https://www.geeksforgeeks.org/problems/minimal-cost/1)

```python
class Solution:
    def minimizeCost(self, x, height):
        n = len(heights)
        if n == 0:
            return 0

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for jump in range(1, min(x, i) + 1):
                energy = (dp[i - jump] + abs(heights[i] - heights[i - jump]))
                dp[i] = min(dp[i], energy)

        return dp[n - 1]
```

**Time complexity:** O(n × min(x, n)), where n is the number of stones.

## 5. Decode Ways

Count decodings of a digit string using 1 → A through 26 → Z. A zero cannot be decoded alone.

[LeetCode 91](https://leetcode.com/problems/decode-ways/)

```python
class Solution:

    @lru_cache(maxsize=None)
    def numDecodings(self, index, s) -> int:
        # If you reach the end of the string, Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == "0":
            return 0

        if index == len(s) - 1:
            return 1

        answer = self.numDecodings(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.numDecodings(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.numDecodings(0, s)
```
### DP
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'. '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
```

**Time complexity:** O(n), where n is the number of houses.
**Space complexity:** O(n).

### Constant Space 

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1 : i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back
```

**Time complexity:** O(n), where n is the number of houses.
**Space complexity:** O(1).

## Grid DP

## 6. Unique Paths I

[LeetCode 62](https://leetcode.com/problems/unique-paths/)

The robot starts at the top-left corner of an `m × n` grid and can move only **right or down**. Return the number of paths to the bottom-right corner.

### 2D DP

`dp[row][col]` stores the number of paths to reach that cell. Each cell can be reached from above or from the left.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]
```

**Time:** O(m × n)  
**Space:** O(m × n)

### 1D DP

Reuse one row because each cell needs only the value above it and to its left.

- `dp[col]`: paths from above, before the update.
- `dp[col - 1]`: paths from the left, already updated for the current row.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for row in range(1, m):
            for col in range(1, n):
                dp[col] = dp[col] + dp[col - 1]

        return dp[n - 1]
```

**Time:** O(m × n)  
**Space:** O(n)

### Constant-space Math Solution

This solution uses **combinatorics, not DP**.
Every path requires:

- `m - 1` down moves.
- `n - 1` right moves.
- `m + n - 2` total moves.
  Choose the positions of the down moves among all moves: **Paths = C(m + n - 2, m - 1)**

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_moves = m + n - 2
        k = min(m - 1, n - 1)
        result = 1

        for i in range(1, k + 1):
            result = result * (total_moves - i + 1) // i

        return result
```

**Time:** O(min(m, n))  
**Space:** O(1) auxiliary variables

## 7. Unique Paths II

The robot starts at the top-left corner and can move only **right or down**.

- `0` = open cell.
- `1` = obstacle.
- Return the number of paths to the bottom-right corner.

### 2D DP

`dp[row][col]` stores the number of paths to reach that cell.

- An obstacle has zero paths.
- An open cell receives paths from above and from the left.

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    if row > 0:
                        dp[row][col] += dp[row - 1][col]
                    if col > 0:
                        dp[row][col] += dp[row][col - 1]

        return dp[m - 1][n - 1]
```

**Time:** O(m × n)  
**Space:** O(m × n)

### 1D DP

Reuse one row.

- `dp[col]` holds the paths from above before the update.
- `dp[col - 1]` holds the paths from the left.
- Reset `dp[col]` to zero when an obstacle is encountered.

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]

        return dp[n - 1]
```

**Time:** O(m × n)  
**Space:** O(n)

### Constant Extra Space — In-place DP

Store the path counts directly in the input grid. Unlike Unique Paths I, the simple combinatorics formula does not handle obstacles.

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                elif row == 0 and col == 0:
                    obstacleGrid[row][col] = 1
                else:
                    above = obstacleGrid[row - 1][col] if row > 0 else 0
                    left = obstacleGrid[row][col - 1] if col > 0 else 0
                    obstacleGrid[row][col] = above + left

        return obstacleGrid[m - 1][n - 1]
```

**Time:** O(m × n)  
**Extra Space:** O(1)

## Subsequence and Knapsack DP

## 8. Subset Sum to Target

GFG - https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

Given an array of positive integers `arr` and a target `sum`, return `True` if a subset adds up to the target. Otherwise, return `False`. Each element can be used at most once.
**Example:** `arr = [3, 34, 4, 12, 5, 2]`, `sum = 9`  
**Output:** `True` — the subset `[4, 5]` adds up to `9`.

### Memoization

At each index, either skip the number or take it.

```python
from functools import lru_cache

class Solution:
    def isSubsetSum(self, arr, sum):
        @lru_cache(None)
        def solve(i, remaining):
            if remaining == 0:
                return True

            if i == len(arr):
                return False

            skip = solve(i + 1, remaining)

            take = False
            if arr[i] <= remaining:
                take = solve(i + 1, remaining - arr[i])

            return skip or take

        return solve(0, sum)
```

**Time:** O(n × (sum + 1))  
**Space:** O(n × (sum + 1)), including memoization and recursion.

### 2D DP

`dp[i][s]` indicates whether a subset of the first `i` elements can make sum `s`. Sum `0` is always possible by choosing the empty subset.

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        n = len(arr)
        dp = [[False] * (sum + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            num = arr[i - 1]

            for s in range(1, sum + 1):
                skip = dp[i - 1][s]

                take = False
                if num <= s:
                    take = dp[i - 1][s - num]

                dp[i][s] = skip or take

        return dp[n][sum]
```

**Time:** O(n × (sum + 1))  
**Space:** O(n × (sum + 1))

### Space-optimized DP

`dp[s]` indicates whether sum `s` can be formed using the elements processed so far. Loop backward so each element is used at most once.

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        dp = [False] * (sum + 1)
        dp[0] = True

        for num in arr:
            for s in range(sum, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[sum]
```

**Time:** O(n × (sum + 1))  
**Space:** O(sum + 1)

## 9. Equal Subset Partition

[LeetCode 416](https://leetcode.com/problems/partition-equal-subset-sum/)

Return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
**Input:** nums = [1, 5, 11, 5]  
**Output:** True
**Input:** nums = [1, 2, 3, 5]  
**Output:** False

### Memoization

```python
from functools import lru_cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        @lru_cache(None)
        def solve(i, remaining):
            if remaining == 0:
                return True

            if i == len(nums):
                return False

            skip = solve(i + 1, remaining)

            take = False
            if nums[i] <= remaining:
                take = solve(i + 1, remaining - nums[i])

            return skip or take

        return solve(0, target)
```

**Time:** O(n × (target + 1))  
**Space:** O(n × (target + 1))

### 2D DP

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            num = nums[i - 1]

            for s in range(1, target + 1):
                skip = dp[i - 1][s]

                take = False
                if num <= s:
                    take = dp[i - 1][s - num]

                dp[i][s] = skip or take

        return dp[n][target]
```

**Time:** O(n × (target + 1))  
**Space:** O(n × (target + 1))

### Space-optimized DP

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 10. Minimum Partition Difference

Split a nonnegative array into two subsets of any sizes, minimizing the absolute difference of their sums. Find the largest reachable sum no greater than half the total.

[GeeksforGeeks: Minimum Partition Difference](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1)

- If one subset sums to `s`, the other sums to `total - s`.
- Their difference is `abs(total - 2 * s)`.
- Find the **largest achievable sum at or below `total // 2`** to minimize the difference.
- An odd total can still produce a valid answer; do not return early.
- In space-optimized DP, loop **backward** so each element is used at most once.

```python
class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in arr:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s
```

The complexity is **pseudo-polynomial** because it depends on the numeric sum.
**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 11. Count Subsets with Sum K

Count subsets of nonnegative integers totaling k; equal-valued elements at different indices are distinct choices. Zeros correctly double existing counts. Return an exact count, without a modulus.

[GeeksforGeeks: Count Subsets with Sum](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1)

```python
class Solution:
    def countSubsets(self, nums, k):
        dp = [0] * (k + 1)
        dp[0] = 1
        for num in nums:
            for s in range(k, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[k]
```

**Time:** O(n × (k + 1))  
**Space:** O(k + 1)

## 12. Count Partitions with Difference

Count assignments to labeled subsets S1 and S2 such that sum(S1) − sum(S2) = d, for nonnegative values and d ≥ 0. Count subsets totaling (total − d) / 2; return an exact count.

[GeeksforGeeks: Partitions with Given Difference](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1)

```python
class Solution:
    def countPartitions(self, arr, d):
        total = sum(arr)

        if total < d or (total - d) % 2 != 0:
            return 0

        target = (total - d) // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in arr:
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[target]
```

**Time complexity:** O(n × (T + 1)) DP updates, where T = (total − d) / 2; exact-integer additions cost O(b) for b-bit counts.
**Space:** O(target + 1)

## 13. Target Sum

Assign + or − to every nonnegative number so the expression equals target. Count subsets assigned minus signs, whose sum must be (total − target) / 2.

[LeetCode 494](https://leetcode.com/problems/target-sum/)

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        subset_sum = (total + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]

```

**Time:** O(n × (subset_sum + 1))  
**Space:** O(subset_sum + 1)

## 14. Minimum Coins

Find the fewest coins needed to form amount using unlimited positive-denomination coins. Return −1 when impossible.

[LeetCode 322](https://leetcode.com/problems/coin-change/)

## 14. Minimum Coins

[LeetCode 322 — Coin Change](https://leetcode.com/problems/coin-change/)

**Input:** coins = [1, 2, 5], amount = 11  
**Output:** 3

**Input:** coins = [2], amount = 3  
**Output:** -1

**Input:** coins = [1], amount = 0  
**Output:** 0

### Recursion + Memo

```python
from functools import lru_cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(i, remaining):
            if remaining == 0:
                return 0

            if i == len(coins):
                return float('inf')

            skip = solve(i + 1, remaining)

            take = float('inf')
            if coins[i] <= remaining:
                take = 1 + solve(i, remaining - coins[i])

            return min(skip, take)

        answer = solve(0, amount)
        return -1 if answer == float('inf') else answer
```

**Time:** O(n × (amount + 1))  
**Space:** O(n × (amount + 1) + n + amount)

### 2D DP

```python
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            coin = coins[i - 1]

            for s in range(1, amount + 1):
                skip = dp[i - 1][s]

                take = float('inf')
                if coin <= s:
                    take = 1 + dp[i][s - coin]

                dp[i][s] = min(skip, take)

        answer = dp[n][amount]
        return -1 if answer == float('inf') else answer
```

**Time:** O(n × (amount + 1))  
**Space:** O((n + 1) × (amount + 1))

### Space-optimized DP

```python
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for s in range(coin, amount + 1):
                dp[s] = min(dp[s], 1 + dp[s - coin])

        answer = dp[amount]
        return -1 if answer == float('inf') else answer
```

**Time:** O(n × (amount + 1))  
**Space:** O(amount + 1)

## 15. Coin Change II

Count unordered combinations forming amount using unlimited coins of distinct positive denominations. Process coins outside the sum loop to avoid counting different orders separately.

[LeetCode 518](https://leetcode.com/problems/coin-change-ii/)

```python
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for total in range(coin, amount + 1):
                dp[total] += dp[total - coin]

        return dp[amount]
```

**Time:** O(n × (amount + 1))  
**Space:** O(amount + 1)

## 16. Unbounded Knapsack

Maximize value within capacity using unlimited copies of items with positive weights and nonnegative values. Ascending capacity updates allow reusing the current item.

[GeeksforGeeks — Knapsack with Duplicate Items](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)

**Input:** val = [10, 40, 50, 70], wt = [1, 3, 4, 5], capacity = 8  
**Output:** 110

**Input:** val = [10, 30], wt = [5, 10], capacity = 4  
**Output:** 0

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def knapSack(self, val, wt, capacity):
        @lru_cache(None)
        def solve(i, remaining):
            if i == len(wt) or remaining == 0:
                return 0

            skip = solve(i + 1, remaining)

            take = 0
            if wt[i] <= remaining:
                take = val[i] + solve(i, remaining - wt[i])

            return max(skip, take)

        return solve(0, capacity)
```

**Time:** O(n × (capacity + 1))  
**Space:** O(n × (capacity + 1) + n + capacity)

### 2D DP

```python
class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(wt)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            weight = wt[i - 1]
            value = val[i - 1]

            for cap in range(1, capacity + 1):
                skip = dp[i - 1][cap]

                take = 0
                if weight <= cap:
                    take = value + dp[i][cap - weight]

                dp[i][cap] = max(skip, take)

        return dp[n][capacity]
```

**Time:** O(n × (capacity + 1))  
**Space:** O((n + 1) × (capacity + 1))

### Space-optimized DP

```python
class Solution:
    def knapSack(self, val, wt, capacity):
        dp = [0] * (capacity + 1)

        for i in range(len(wt)):
            for cap in range(wt[i], capacity + 1):
                dp[cap] = max(dp[cap], val[i] + dp[cap - wt[i]])

        return dp[capacity]
```

**Time:** O(n × (capacity + 1))  
**Space:** O(capacity + 1)

## 17. Rod Cutting

Maximize revenue by cutting a rod of length n. price[i − 1] is the price of a piece of length i; prices are nonnegative and each length can be reused.
**Input:** price = [1, 5, 8, 9, 10, 17, 17, 20]  
**Output:** 22

**Input:** price = [3, 5, 8, 9, 10, 17, 17, 20]  
**Output:** 24

[GeeksforGeeks: Rod Cutting](https://www.geeksforgeeks.org/problems/rod-cutting0840/1)

```python
class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [float('-inf')] * (n + 1)
        dp[0] = 0

        for length in range(1, n + 1):
            for remaining in range(length, n + 1):
                dp[remaining] = max(dp[remaining], price[length - 1] + dp[remaining - length])

        return dp[n]
```

**Time:** O(n²)  
**Space:** O(n)

## Stock DP

## 18. Buy and Sell Stock I, II, III, IV, V

Maximize profit using at most one buy followed by one sell. Track the lowest price seen before each sale.

## 18. Buy and Sell Stock I, II, III, IV, V

### Stock I — One Transaction

[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Input:** prices = [7, 1, 5, 3, 6, 4]  
**Output:** 5

#### Constant Space

```python
class Solution:
    def maxProfit(self, prices):
        minimum_price = float('inf')
        profit = 0

        for price in prices:
            minimum_price = min(minimum_price, price)
            profit = max(profit, price - minimum_price)

        return profit
```

**Time:** O(n)  
**Space:** O(1)

---

### Stock II — Unlimited Transactions

[LeetCode 122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

**Input:** prices = [7, 1, 5, 3, 6, 4]  
**Output:** 7

#### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def maxProfit(self, prices):
        @lru_cache(None)
        def solve(i, holding):
            if i == len(prices):
                return float('-inf') if holding else 0

            if holding:
                return max(solve(i + 1, 1), prices[i] + solve(i + 1, 0))

            return max(solve(i + 1, 0), -prices[i] + solve(i + 1, 1))

        return solve(0, 0)
```

**Time:** O(n)  
**Space:** O(n)

#### Full 2D DP

```python
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0, float('-inf')] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 1][0])

        return dp[0][0]
```

**Time:** O(n)  
**Space:** O(n)

#### Space-optimized DP

```python
class Solution:
    def maxProfit(self, prices):
        next_free = 0
        next_holding = float('-inf')

        for i in range(len(prices) - 1, -1, -1):
            current_free = max(next_free, -prices[i] + next_holding)
            current_holding = max(next_holding, prices[i] + next_free)
            next_free, next_holding = current_free, current_holding

        return next_free
```

**Time:** O(n)  
**Space:** O(1)

#### Important Pointers

- Unlimited transactions are allowed, but you can hold only one share at a time.
- `holding = 0`: buy or skip. `holding = 1`: sell or skip.
- Buying subtracts the price; selling adds it.
- Adding every positive adjacent price difference also solves this variant.

---

### Stock III — At Most Two Transactions

[LeetCode 123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

**Input:** prices = [3, 3, 5, 0, 0, 3, 1, 4]  
**Output:** 6

#### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def maxProfit(self, prices):
        @lru_cache(None)
        def solve(i, holding, remaining):
            if i == len(prices) or remaining == 0:
                return float('-inf') if holding else 0

            if holding:
                return max(solve(i + 1, 1, remaining), prices[i] + solve(i + 1, 0, remaining - 1))

            return max(solve(i + 1, 0, remaining), -prices[i] + solve(i + 1, 1, remaining))

        return solve(0, 0, 2)
```

**Time:** O(n)  
**Space:** O(n)

#### Full 3D DP

```python
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[0] * 3, [float('-inf')] * 3] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for remaining in range(1, 3):
                dp[i][0][remaining] = max(dp[i + 1][0][remaining], -prices[i] + dp[i + 1][1][remaining])
                dp[i][1][remaining] = max(dp[i + 1][1][remaining], prices[i] + dp[i + 1][0][remaining - 1])

        return dp[0][0][2]
```

**Time:** O(n)  
**Space:** O(n)

#### Space-optimized DP

```python
class Solution:
    def maxProfit(self, prices):
        next_dp = [[0] * 3, [float('-inf')] * 3]

        for i in range(len(prices) - 1, -1, -1):
            current = [[0] * 3, [float('-inf')] * 3]

            for remaining in range(1, 3):
                current[0][remaining] = max(next_dp[0][remaining], -prices[i] + next_dp[1][remaining])
                current[1][remaining] = max(next_dp[1][remaining], prices[i] + next_dp[0][remaining - 1])

            next_dp = current

        return next_dp[0][2]
```

**Time:** O(n)  
**Space:** O(1)

#### Important Pointers

- At most two complete transactions are allowed.
- Decrease `remaining` when selling.
- The optimized table has a fixed size, so its space is O(1).

---

### Stock IV — At Most K Transactions

[LeetCode 188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

**Input:** k = 2, prices = [3, 2, 6, 5, 0, 3]  
**Output:** 7

#### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def maxProfit(self, k, prices):
        @lru_cache(None)
        def solve(i, holding, remaining):
            if i == len(prices) or remaining == 0:
                return float('-inf') if holding else 0

            if holding:
                return max(solve(i + 1, 1, remaining), prices[i] + solve(i + 1, 0, remaining - 1))

            return max(solve(i + 1, 0, remaining), -prices[i] + solve(i + 1, 1, remaining))

        return solve(0, 0, k)
```

**Time:** O(n × (k + 1))  
**Space:** O((n + 1) × (k + 1))

#### Full 3D DP

```python
class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        dp = [[[0] * (k + 1), [float('-inf')] * (k + 1)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for remaining in range(1, k + 1):
                dp[i][0][remaining] = max(dp[i + 1][0][remaining], -prices[i] + dp[i + 1][1][remaining])
                dp[i][1][remaining] = max(dp[i + 1][1][remaining], prices[i] + dp[i + 1][0][remaining - 1])

        return dp[0][0][k]
```

**Time:** O(n × (k + 1))  
**Space:** O((n + 1) × (k + 1))

#### Space-optimized DP

```python
class Solution:
    def maxProfit(self, k, prices):
        next_dp = [[0] * (k + 1), [float('-inf')] * (k + 1)]

        for i in range(len(prices) - 1, -1, -1):
            current = [[0] * (k + 1), [float('-inf')] * (k + 1)]

            for remaining in range(1, k + 1):
                current[0][remaining] = max(next_dp[0][remaining], -prices[i] + next_dp[1][remaining])
                current[1][remaining] = max(next_dp[1][remaining], prices[i] + next_dp[0][remaining - 1])

            next_dp = current

        return next_dp[0][k]
```

**Time:** O(n × (k + 1))  
**Space:** O(k + 1)

#### Important Pointers

- This generalizes Stock III from two transactions to `k`.
- Decrease the transaction count when selling.
- If `k >= len(prices) // 2`, use Stock II to achieve O(n) time.
- The optimized solution uses O(k) space, not constant space.

---

### Stock V — With Cooldown

[LeetCode 309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

**Input:** prices = [1, 2, 3, 0, 2]  
**Output:** 3

#### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def maxProfit(self, prices):
        @lru_cache(None)
        def solve(i, holding):
            if i >= len(prices):
                return float('-inf') if holding else 0

            if holding:
                return max(solve(i + 1, 1), prices[i] + solve(i + 2, 0))

            return max(solve(i + 1, 0), -prices[i] + solve(i + 1, 1))

        return solve(0, 0)
```

**Time:** O(n)  
**Space:** O(n)

#### Full 2D DP

```python
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0, float('-inf')] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 2][0])

        return dp[0][0]
```

**Time:** O(n)  
**Space:** O(n)

#### Space-optimized DP

```python
class Solution:
    def maxProfit(self, prices):
        next_free = 0
        next_holding = float('-inf')
        next2_free = 0

        for i in range(len(prices) - 1, -1, -1):
            current_free = max(next_free, -prices[i] + next_holding)
            current_holding = max(next_holding, prices[i] + next2_free)

            next2_free = next_free
            next_free, next_holding = current_free, current_holding

        return next_free
```

**Time:** O(n)  
**Space:** O(1)

#### Important Pointers

- Here, Stock V means the cooldown variant.
- After selling, you cannot buy on the next day.
- Selling moves to day `i + 2`; buying and skipping move to day `i + 1`.
- In all DP versions, negative infinity marks an invalid terminal state where a share remains unsold.
- For long arrays, use iterative DP to avoid Python's recursion depth limit.

## LCS and String DP

## 19. Longest Common Subsequence — Length

Find the longest sequence appearing in both strings in the same order; characters need not be adjacent.
[LeetCode 1143](https://leetcode.com/problems/longest-common-subsequence/)

**Input:** text1 = "abcde", text2 = "ace"  
**Output:** 3

**Input:** text1 = "abc", text2 = "def"  
**Output:** 0

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @lru_cache(None)
        def solve(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + solve(i + 1, j + 1)

            return max(solve(i + 1, j), solve(i, j + 1))

        return solve(0, 0)
```

**Time:** O(m × n)  
**Space:** O(m × n + m + n)

### Full 2D DP

```python
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
```

**Time:** O(m × n)  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP

```python
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        next_row = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            current = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[j] = 1 + next_row[j + 1]
                else:
                    current[j] = max(next_row[j], current[j + 1])

            next_row = current

        return next_row[0]
```

**Time:** O(m × n)  
**Space:** O(min(m, n) + 1)

## 20. Longest Common Subsequence — Printing

Reconstruct and return one LCS by walking backward through the DP table. On a match, take that character; otherwise move toward the larger neighboring value.

[GeeksforGeeks: Printing LCS](https://www.geeksforgeeks.org/dsa/printing-longest-common-subsequence/)

**Input:** text1 = "abcde", text2 = "ace"  
**Output:** "ace"

**Input:** text1 = "abc", text2 = "def"  
**Output:** ""

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def printLCS(self, text1, text2):
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def solve(i, j):
            if i == m or j == n:
                return 0

            if text1[i] == text2[j]:
                return 1 + solve(i + 1, j + 1)

            return max(solve(i + 1, j), solve(i, j + 1))

        solve(0, 0)
        i = j = 0
        result = []

        while i < m and j < n:
            if text1[i] == text2[j]:
                result.append(text1[i])
                i += 1
                j += 1
            elif solve(i + 1, j) >= solve(i, j + 1):
                i += 1
            else:
                j += 1

        return ''.join(result)
```

**Time:** O(m × n + m + n)  
**Space:** O(m × n + m + n)

### Full 2D DP

```python
class Solution:
    def printLCS(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        i = j = 0
        result = []

        while i < m and j < n:
            if text1[i] == text2[j]:
                result.append(text1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] >= dp[i][j + 1]:
                i += 1
            else:
                j += 1

        return ''.join(result)
```

**Time:** O(m × n + m + n)  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP — Store Subsequences

```python
class Solution:
    def printLCS(self, text1, text2):
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        next_row = [''] * (n + 1)

        for i in range(m - 1, -1, -1):
            current = [''] * (n + 1)

            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[j] = text1[i] + next_row[j + 1]
                else:
                    current[j] = max(next_row[j], current[j + 1], key=len)

            next_row = current

        return next_row[0]
```

**Time:** O(m × n × (L + 1))  
**Space:** O((min(m, n) + 1) × (L + 1))

Here, `L` is the length of the LCS. String concatenation copies characters.

## 21. Longest Common Substring

Return the length of the longest contiguous string shared by both inputs. dp[i][j] is the matching suffix length ending at those positions; reset it to zero on a mismatch.

[GeeksforGeeks: Longest Common Substring](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1)

```python
class Solution:
    def longestCommonSubstr(self, a, b):
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        best = 0
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    best = max(best, dp[i][j])
        return best
```

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string lengths.

## 22. Longest Palindromic Subsequence

[LeetCode 516 — Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

**Input:** s = "bbbab"  
**Output:** 4

**Input:** s = "cbbd"  
**Output:** 2

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s):
        @lru_cache(None)
        def solve(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + solve(i + 1, j - 1)

            return max(solve(i + 1, j), solve(i, j - 1))

        return solve(0, len(s) - 1)
```

**Time:** O(n²)  
**Space:** O(n²)

### Full 2D DP

```python
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)

        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
```

**Time:** O(n²)  
**Space:** O(n²)

### Space-optimized DP

```python
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)

        if n == 0:
            return 0

        dp = [0] * n

        for i in range(n - 1, -1, -1):
            diagonal = 0
            dp[i] = 1

            for j in range(i + 1, n):
                old_value = dp[j]

                if s[i] == s[j]:
                    dp[j] = 2 + diagonal
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                diagonal = old_value

        return dp[n - 1]
```

**Time:** O(n²)  
**Space:** O(n)

### Important Pointers

- A subsequence does not need to be contiguous.
- Matching endpoints contribute `2`; a single middle character contributes `1`.
- `diagonal` preserves the previous row's `dp[i + 1][j - 1]`.
- The length also equals the LCS length of `s` and its reverse.

---

## 23. Edit Distance

[LeetCode 72 — Edit Distance](https://leetcode.com/problems/edit-distance/)

**Input:** word1 = "horse", word2 = "ros"  
**Output:** 3

**Input:** word1 = "intention", word2 = "execution"  
**Output:** 5

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        @lru_cache(None)
        def solve(i, j):
            if i == m:
                return n - j

            if j == n:
                return m - i

            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)

            return 1 + min(solve(i, j + 1), solve(i + 1, j), solve(i + 1, j + 1))

        return solve(0, 0)
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O((m + 1) × (n + 1))

### Full 2D DP

```python
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i

        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP

```python
class Solution:
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        m, n = len(word1), len(word2)
        next_row = [n - j for j in range(n + 1)]

        for i in range(m - 1, -1, -1):
            current = [0] * (n + 1)
            current[n] = m - i

            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    current[j] = next_row[j + 1]
                else:
                    current[j] = 1 + min(current[j + 1], next_row[j], next_row[j + 1])

            next_row = current

        return next_row[0]
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O(min(m, n) + 1)

### Important Pointers

- Allowed operations are **insert, delete, and replace**.
- Each operation costs `1`; matching characters cost `0`.
- Insert: `(i, j + 1)`.
- Delete: `(i + 1, j)`.
- Replace: `(i + 1, j + 1)`.
- If one string is exhausted, insert or delete all remaining characters.
- For long strings, use iterative DP to avoid Python's recursion depth limit.

---

## LIS DP

## 24. Longest Increasing Subsequence — Length

[LeetCode 300 — Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

**Input:** nums = [10, 9, 2, 5, 3, 7, 101, 18]  
**Output:** 4

**Input:** nums = [7, 7, 7, 7]  
**Output:** 1

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums):
        @lru_cache(None)
        def solve(i, previous):
            if i == len(nums):
                return 0

            if previous == -1 or nums[i] > nums[previous]:
                return max(solve(i + 1, previous), 1 + solve(i + 1, i))

            return solve(i + 1, previous)

        return solve(0, -1)
```

**Time:** O(n²)  
**Space:** O(n²)

### Full 2D DP

```python
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for previous in range(i - 1, -2, -1):
                if previous == -1 or nums[i] > nums[previous]:
                    dp[i][previous + 1] = max(dp[i + 1][previous + 1], 1 + dp[i + 1][i + 1])
                else:
                    dp[i][previous + 1] = dp[i + 1][previous + 1]

        return dp[0][0]
```

**Time:** O(n²)  
**Space:** O(n²)

### 1D DP

```python
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp, default=0)
```

**Time:** O(n²)  
**Space:** O(n)

### Binary Search

```python
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums):
        tails = []

        for num in nums:
            i = bisect_left(tails, num)

            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num

        return len(tails)
```

**Time:** O(n log n)  
**Space:** O(n)

### Important Pointers

- The subsequence must be **strictly increasing**; equal values do not extend it.
- In 2D DP, `previous + 1` maps index `-1` to column `0`.
- In 1D DP, `dp[i]` is the LIS length ending at index `i`.
- The answer is the maximum DP value, not necessarily the last value.
- `bisect_left` replaces the first tail greater than or equal to the current number.
- The final `tails` list is not necessarily an actual subsequence.

---

## 25. Longest Increasing Subsequence — Printing

[GeeksforGeeks — Printing Longest Increasing Subsequence](https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1)

**Input:** nums = [10, 9, 2, 5, 3, 7, 101, 18]  
**Output:** [2, 5, 7, 101]

**Input:** nums = [7, 7, 7]  
**Output:** [7]

### DP + Parent Tracking

```python
class Solution:
    def printLIS(self, nums):
        n = len(nums)

        if n == 0:
            return []

        dp = [1] * n
        parent = list(range(n))
        best_index = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > dp[best_index]:
                best_index = i

        result = []

        while parent[best_index] != best_index:
            result.append(nums[best_index])
            best_index = parent[best_index]

        result.append(nums[best_index])
        return result[::-1]
```

**Time:** O(n²)  
**Space:** O(n)

### Important Pointers

- `parent[i]` stores the previous index in the chosen subsequence ending at `i`.
- Update the parent only when the LIS length improves.
- Reconstruct from the index with the largest DP value, then reverse the result.
- Multiple valid LIS results may exist; this returns one.
- This does not guarantee a lexicographically smallest LIS.
- The method returns a list; use `print(result)` if console output is required.

---

## Rectangles and Squares

## Largest Histogram Rectangle

[LeetCode 84 — Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

**Input:** heights = [2, 1, 5, 6, 2, 3]  
**Output:** 10

**Input:** heights = [2, 4]  
**Output:** 4

### Monotonic Stack

```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        answer = 0
        n = len(heights)

        for i in range(n + 1):
            current_height = heights[i] if i < n else 0

            while stack and heights[stack[-1]] >= current_height:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                answer = max(answer, height * (i - left - 1))

            if i < n:
                stack.append(i)

        return answer
```

**Time:** O(n)  
**Space:** O(n)

### Important Pointers

- Use a monotonic stack of indices with strictly increasing heights.
- A shorter or equal bar triggers evaluation of bars popped from the stack.
- After popping, `i` is the right boundary and the new stack top is the left boundary.
- Rectangle width is `i - left - 1`.
- The final virtual bar of height `0` processes remaining bars.
- Every index is pushed and popped at most once.

---

## Maximal Rectangle of Ones

[LeetCode 85 — Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

**Input:**
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

**Output:** 6

### Histogram + Monotonic Stack

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        answer = 0

        for row in matrix:
            for col in range(n):
                heights[col] = heights[col] + 1 if row[col] == '1' else 0

            stack = []

            for i in range(n + 1):
                current_height = heights[i] if i < n else 0

                while stack and heights[stack[-1]] >= current_height:
                    height = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    answer = max(answer, height * (i - left - 1))

                if i < n:
                    stack.append(i)

        return answer
```

**Time:** O(rows × cols)  
**Space:** O(cols)

### Important Pointers

- Each row becomes the bottom of a histogram.
- A `'1'` increases the column height; a `'0'` resets it to zero.
- Apply Largest Histogram Rectangle to every row.
- Return the largest **area**, not the height or width.
- LeetCode supplies string cells. For integer cells, compare with `1`.

---

## Count All-One Squares

[LeetCode 1277 — Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

**Input:**
matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

**Output:** 15

### Recursion + Memo

```python
from functools import lru_cache

class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def solve(i, j):
            if i == m or j == n or matrix[i][j] == 0:
                return 0

            return 1 + min(solve(i + 1, j), solve(i, j + 1), solve(i + 1, j + 1))

        return sum(solve(i, j) for i in range(m) for j in range(n))
```

**Time:** O(m × n)  
**Space:** O(m × n + m + n)

### Full 2D DP

```python
class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        answer = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                    answer += dp[i][j]

        return answer
```

**Time:** O(m × n)  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP

```python
class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        next_row = [0] * (n + 1)
        answer = 0

        for i in range(m - 1, -1, -1):
            current = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 1:
                    current[j] = 1 + min(next_row[j], current[j + 1], next_row[j + 1])
                    answer += current[j]

            next_row = current

        return answer
```

**Time:** O(m × n)  
**Space:** O(n)

### Important Pointers

- Cells are integers `0` and `1`.
- Each state stores the largest all-one square starting at that cell.
- Use the minimum of the right, down, and diagonal states to extend a square.
- A state value of `3` contributes three squares: sizes `1 × 1`, `2 × 2`, and `3 × 3`.
- Sum all state values to count every square.
- Taking only the maximum state finds the largest square's side length, not the total count.