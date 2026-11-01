# Dynamic Programming — Python

## 1. House Robber I

Maximize money robbed from a line of houses without robbing adjacent houses. At each house, choose between skipping it and taking it with the best total two houses back.

[LeetCode 198](https://leetcode.com/problems/house-robber/)

**Recursion + Memoization:**  At each index, compare skipping the house with taking it and continuing two positions ahead. Cache the answer for each index.

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

[LeetCode 416 — Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
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

### Full 2D DP

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

```python
class Solution:
    def minDifference(self, nums):
        total = sum(nums)
        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            for s in range(half, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        for s in range(half, -1, -1):
            if dp[s]:
                return total - 2 * s
```

**Time complexity:** O(n × (S + 1)), where S is the total sum.

### 11. Count Subsets with Sum K

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

**Time complexity:** O(n × (k + 1)) DP updates; exact-integer additions cost O(b) for b-bit counts.

### 12. Count Partitions with Difference

Count assignments to labeled subsets S1 and S2 such that sum(S1) − sum(S2) = d, for nonnegative values and d ≥ 0. Count subsets totaling (total − d) / 2; return an exact count.

[GeeksforGeeks: Partitions with Given Difference](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1)

```python
class Solution:
    def countPartitions(self, nums, d):
        total = sum(nums)
        if d > total or (total - d) % 2:
            return 0
        target = (total - d) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[target]
```

**Time complexity:** O(n × (T + 1)) DP updates, where T = (total − d) / 2; exact-integer additions cost O(b) for b-bit counts.

### 13. Target Sum

Assign + or − to every nonnegative number so the expression equals target. Count subsets assigned minus signs, whose sum must be (total − target) / 2.

[LeetCode 494](https://leetcode.com/problems/target-sum/)

```python
class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        if abs(target) > total or (total - target) % 2:
            return 0
        required = (total - target) // 2
        dp = [0] * (required + 1)
        dp[0] = 1
        for num in nums:
            for s in range(required, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[required]
```

**Time complexity:** O(n × (T + 1)), where T = (total − target) / 2.

### 14. Minimum Coins

Find the fewest coins needed to form amount using unlimited positive-denomination coins. Return −1 when impossible.

[LeetCode 322](https://leetcode.com/problems/coin-change/)

```python
class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], 1 + dp[total - coin])
        return dp[amount] if dp[amount] <= amount else -1
```

**Time complexity:** O(c × amount + amount), where c is the number of denominations.

### 15. Coin Change II

Count unordered combinations forming amount using unlimited coins of distinct positive denominations. Process coins outside the sum loop to avoid counting different orders separately.

[LeetCode 518](https://leetcode.com/problems/coin-change-ii/)

```python
class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for total in range(coin, amount + 1):
                dp[total] += dp[total - coin]
        return dp[amount]
```

**Time complexity:** O(c × (amount + 1)) DP updates; exact-integer additions cost O(b) for b-bit counts. Java uses BigInteger to protect intermediate counts; the problem guarantees the final answer fits int.

### 16. Unbounded Knapsack

Maximize value within capacity using unlimited copies of items with positive weights and nonnegative values. Ascending capacity updates allow reusing the current item.

[GeeksforGeeks: Unbounded Knapsack](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)

```python
class Solution:
    def knapSack(self, values, weights, capacity):
        dp = [0] * (capacity + 1)
        for value, weight in zip(values, weights):
            for c in range(weight, capacity + 1):
                dp[c] = max(dp[c], value + dp[c - weight])
        return dp[capacity]
```

**Time complexity:** O(n × (W + 1)), where n is the number of item types and W is capacity.

### 17. Rod Cutting

Maximize revenue by cutting a rod of length n. price[i − 1] is the price of a piece of length i; prices are nonnegative and each length can be reused.

[GeeksforGeeks: Rod Cutting](https://www.geeksforgeeks.org/problems/rod-cutting0840/1)

```python
class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [0] * (n + 1)
        for length in range(1, n + 1):
            for cut in range(1, length + 1):
                dp[length] = max(dp[length], price[cut - 1] + dp[length - cut])
        return dp[n]
```

**Time complexity:** O(n²), where n is the rod length.

## Stock DP

### 18. Buy and Sell Stock I

Maximize profit using at most one buy followed by one sell. Track the lowest price seen before each sale.

[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```python
class Solution:
    def maxProfit(self, prices):
        minimum, best = float("inf"), 0
        for price in prices:
            minimum = min(minimum, price)
            best = max(best, price - minimum)
        return best
```

**Time complexity:** O(n), where n is the number of days.

### 19. Buy and Sell Stock II

Maximize profit with unlimited transactions while holding at most one share. Track the best profit while holding a share and while holding none.

[LeetCode 122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```python
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash, hold = max(cash, hold + prices[i]), max(hold, cash - prices[i])
        return cash
```

**Time complexity:** O(n), where n is the number of days.

### 20. Buy and Sell Stock III

Maximize profit with at most two completed transactions and at most one share held. A sale consumes one transaction.

[LeetCode 123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

```python
class Solution:
    def maxProfit(self, prices):
        k = 2
        next_day = [[0] * (k + 1) for _ in range(2)]
        for price in reversed(prices):
            current = [[0] * (k + 1) for _ in range(2)]
            for remaining in range(1, k + 1):
                # State 0: no share; state 1: holding a share.
                current[0][remaining] = max(next_day[0][remaining], -price + next_day[1][remaining])
                current[1][remaining] = max(next_day[1][remaining], price + next_day[0][remaining - 1])
            next_day = current
        return next_day[0][k]
```

**Time complexity:** O(n), since the transaction limit is fixed at 2.

### 21. Buy and Sell Stock IV

Maximize profit with at most k completed transactions and at most one share held. For k ≥ n / 2, use the unlimited-transactions shortcut.

[LeetCode 188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

```python
class Solution:
    def maxProfit(self, k, prices):
        if k == 0 or len(prices) < 2:
            return 0
        if k >= len(prices) // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
        next_day = [[0] * (k + 1) for _ in range(2)]
        for price in reversed(prices):
            current = [[0] * (k + 1) for _ in range(2)]
            for remaining in range(1, k + 1):
                # State 0: no share; state 1: holding a share.
                current[0][remaining] = max(next_day[0][remaining], -price + next_day[1][remaining])
                current[1][remaining] = max(next_day[1][remaining], price + next_day[0][remaining - 1])
            next_day = current
        return next_day[0][k]
```

**Time complexity:** O(n × k) in the limited-transactions case; O(n) when k ≥ n / 2.

## LCS and String DP

### 22. Longest Common Subsequence — Length

Find the longest sequence appearing in both strings in the same order; characters need not be adjacent. dp[i][j] stores the LCS length for the first i and j characters. Match: 1 + diagonal; mismatch: max(top, left).

[LeetCode 1143](https://leetcode.com/problems/longest-common-subsequence/)

```python
class Solution:
    def longestCommonSubsequence(self, a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
```

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string lengths.

### 23. Longest Common Subsequence — Printing

Reconstruct and return one LCS by walking backward through the DP table. On a match, take that character; otherwise move toward the larger neighboring value.

[GeeksforGeeks: Printing LCS](https://www.geeksforgeeks.org/dsa/printing-longest-common-subsequence/)

```python
class Solution:
    def printLCS(self, a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        result = []
        i, j = m, n
        while i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                result.append(a[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return "".join(reversed(result))
```

**Time complexity:** O((m + 1) × (n + 1)); reconstruction takes O(m + n).

### 24. Longest Common Substring

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

### 25. Longest Palindromic Subsequence

Return the length of the longest subsequence reading the same forward and backward. Matching interval endpoints contribute two; otherwise skip either endpoint.

[LeetCode 516](https://leetcode.com/problems/longest-palindromic-subsequence/)

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
        return dp[0][-1]
```

**Time complexity:** O(n²), where n is the string length.

### 26. Edit Distance

Return the minimum insertions, deletions, and replacements needed to transform word1 into word2. Matching characters require no edit; otherwise take 1 + min(insert, delete, replace).

[LeetCode 72](https://leetcode.com/problems/edit-distance/)

```python
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
```

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string lengths.

## LIS DP

### 27. Longest Increasing Subsequence — Length

Find the longest strictly increasing subsequence. dp[i] is the best length ending at index i; extend from earlier indices with smaller values.

[LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/)

```python
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp, default=0)
```

**Time complexity:** O(n²), where n is the array length.

### 28. Longest Increasing Subsequence — Printing

Reconstruct and return one strictly increasing subsequence of maximum length. Store a parent index whenever a longer subsequence is found.

[GeeksforGeeks: Printing LIS](https://www.geeksforgeeks.org/dsa/construction-of-longest-increasing-subsequence-using-dynamic-programming/)

```python
class Solution:
    def printLIS(self, nums):
        n = len(nums)
        if n == 0:
            return []
        dp, parent = [1] * n, [-1] * n
        end = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[end]:
                end = i
        result = []
        while end != -1:
            result.append(nums[end])
            end = parent[end]
        return result[::-1]
```

**Time complexity:** O(n²), including O(n) reconstruction.

## Rectangles and Squares

### 29. Largest Histogram Rectangle

Return the largest rectangle under unit-width histogram bars. Use an increasing stack of indices; popping a bar identifies its available width. This is a monotonic-stack problem.

[LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        best = 0
        for i in range(len(heights) + 1):
            current = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] >= current:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (i - left - 1))
            if i < len(heights):
                stack.append(i)
        return best
```

**Time complexity:** O(n), since each bar is pushed and popped at most once.

### 30. Maximal Rectangle of Ones

Return the largest all-1 rectangle in a character matrix containing "0" and "1". Accumulate vertical heights row by row and solve the histogram problem at each row.

[LeetCode 85](https://leetcode.com/problems/maximal-rectangle/)

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        best = 0
        for row in matrix:
            for c, cell in enumerate(row):
                heights[c] = heights[c] + 1 if cell == "1" else 0
            best = max(best, self.largestRectangleArea(heights))
        return best

    def largestRectangleArea(self, heights):
        stack = []
        best = 0
        for i in range(len(heights) + 1):
            current = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] >= current:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (i - left - 1))
            if i < len(heights):
                stack.append(i)
        return best
```

**Time complexity:** O(m × n), where m and n are the matrix dimensions.

### 31. Count All-One Squares

Count every all-1 square in an integer binary matrix. dp[r][c] is the largest square ending at that cell; its value also counts the squares ending there.

[LeetCode 1277](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

```python
class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        total = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if matrix[r - 1][c - 1] == 1:
                    dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])
                    total += dp[r][c]
        return total
```

**Time complexity:** O(m × n), where m and n are the matrix dimensions.
