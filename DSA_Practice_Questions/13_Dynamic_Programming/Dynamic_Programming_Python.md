**# Dynamic Programming — Python**



**## 1. House Robber I**



Maximize money robbed from a line of houses without robbing adjacent houses. At each house, choose between skipping it and taking it with the best total two houses back.



[LeetCode 198]\(https\://leetcode.com/problems/house-robber/)



**### Recursion + Memoization**



At each index, compare skipping the house with taking it and continuing two positions ahead. Cache the answer for each index.



\`\`\`python

class Solution:

&#x20;   def \_\_init\_\_(self):

&#x20;       self.memo = {}



&#x20;   def rob(self, nums: List[int]) -> int:

&#x20;       self.memo = {}

&#x20;       return self.robFrom(0, nums)



&#x20;   def robFrom(self, i, nums):

&#x20;       \# No more houses left to examine.

&#x20;       if i >= len(nums):

&#x20;           return 0



&#x20;       if i in self.memo:

&#x20;           return self.memo[i]



&#x20;       ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

&#x20;       self.memo[i] = ans

&#x20;       return ans

\`\`\`



**\*\*Time complexity:\*\*** O(n).

**\*\*Space complexity:\*\*** O(n) memo plus O(n) recursion stack.



**### Bottom-Up DP**



Fill the DP array from right to left using the same take-or-skip recurrence.



\`\`\`python

class Solution:

&#x20;   def rob(self, nums: List[int]) -> int:

&#x20;       if not nums:

&#x20;           return 0



&#x20;       dp = [None for \_ in range(len(nums) + 1)]

&#x20;       N = len(nums)



&#x20;       \# Base case initialization.

&#x20;       dp[N], dp[N - 1] = 0, nums[N - 1]



&#x20;       \# DP table.

&#x20;       for i in range(N - 2, -1, -1):

&#x20;           dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])



&#x20;       return dp[0]

\`\`\`



**\*\*Time complexity:\*\*** O(n).

**\*\*Space complexity:\*\*** O(n).



**### Constant Space**



Keep only the two previous DP values needed for the next decision.



\`\`\`python

class Solution:

&#x20;   def rob(self, nums):

&#x20;       prev2 = prev1 = 0

&#x20;       for money in nums:

&#x20;           prev2, prev1 = prev1, max(prev1, prev2 + money)

&#x20;       return prev1

\`\`\`



**\*\*Time complexity:\*\*** O(n), where n is the number of houses.

**\*\*Space complexity:\*\*** O(1).



**## 2. House Robber II**



Houses form a circle, so the first and last are adjacent. Take the better result from excluding the first house or excluding the last house.



[LeetCode 213]\(https\://leetcode.com/problems/house-robber-ii/)



**### Recursion + Memoization**



Solve two linear ranges: exclude the last house or exclude the first. Use a separate memo for each range because its endpoint differs.



\`\`\`python

class Solution:

&#x20;   def \_\_init\_\_(self):

&#x20;       self.memo = {}



&#x20;   def rob(self, nums: List[int]) -> int:

&#x20;       if len(nums) == 1:

&#x20;           return nums[0]

&#x20;       self.memo = {}

&#x20;       exclude_last = self.robFrom(0, nums[:-1])



&#x20;       self.memo = {}

&#x20;       exclude_first = self.robFrom(0, nums[1:])



&#x20;       return max(exclude_last, exclude_first)



&#x20;   def robFrom(self, i, nums):

&#x20;       if i >= len(nums):

&#x20;           return 0



&#x20;       if i in self.memo:

&#x20;           return self.memo[i]



&#x20;       ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])



&#x20;       self.memo[i] = ans

&#x20;       return ans

\`\`\`



**\*\*Time complexity:\*\*** O(n).

**\*\*Space complexity:\*\*** O(n) memo plus O(n) recursion stack.



**### Bottom-Up DP**



Fill the DP array from right to left using the same take-or-skip recurrence.



\`\`\`python

class Solution:

&#x20;   def rob(self, nums: List[int]) -> int:

&#x20;       if len(nums) == 1:

&#x20;           return nums[0]



&#x20;       return max(self.robFrom(nums[:-1]),  # Exclude last house

&#x20;           self.robFrom(nums[1:])    # Exclude first house

&#x20;       )



&#x20;   def robFrom(self, nums):

&#x20;       n = len(nums)

&#x20;       dp = [0] \* (n + 2)



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])



&#x20;       return dp[0]

\`\`\`



**\*\*Time complexity:\*\*** O(n).

**\*\*Space complexity:\*\*** O(n).



**### Constant Space**



Keep only the two previous DP values needed for the next decision.



\`\`\`python

class Solution:

&#x20;   def rob(self, nums):

&#x20;       if not nums:

&#x20;           return 0

&#x20;       if len(nums) == 1:

&#x20;           return nums[0]



&#x20;       def rob_range(start, end):

&#x20;           prev2 = prev1 = 0

&#x20;           for i in range(start, end):

&#x20;               prev2, prev1 = prev1, max(prev1, prev2 + nums[i])

&#x20;           return prev1



&#x20;       return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))

\`\`\`



**\*\*Time complexity:\*\*** O(n), where n is the number of houses.

**\*\*Space complexity:\*\*** O(1).



**## 3. Frog Jump**



Reach the last stone with minimum energy. A jump from i to j costs |height[i] − height[j]|; jump one or two positions.



[GeeksforGeeks: Frog Jump]\(https\://www\.geeksforgeeks.org/problems/geek-jump/1)



\`\`\`python

class Solution:

&#x20;   def minCost(self, height):

&#x20;       prev2 = prev1 = 0

&#x20;       for i in range(1, len(height)):

&#x20;           one_step = prev1 + abs(heights[i] - heights[i - 1])



&#x20;           two_steps = float('inf')

&#x20;           if i > 1:

&#x20;               two_steps = prev2 + abs(heights[i] - heights[i - 2])



&#x20;           current = min(one_step, two_steps)

&#x20;           prev2, prev1 = prev1, current



&#x20;       return prev1

\`\`\`



**\*\*Time complexity:\*\*** O(n), where n is the number of stones.



**## 4. Frog Jump with X Distance**



Minimize the same height-based energy cost when each jump can move 1 through x positions; x ≥ 1.



[GeeksforGeeks: Minimal Cost of Jumps]\(https\://www\.geeksforgeeks.org/problems/minimal-cost/1)



\`\`\`python

class Solution:

&#x20;   def minimizeCost(self, x, height):

&#x20;       n = len(heights)

&#x20;       if n == 0:

&#x20;           return 0



&#x20;       dp = [float('inf')] \* n

&#x20;       dp[0] = 0



&#x20;       for i in range(1, n):

&#x20;           for jump in range(1, min(x, i) + 1):

&#x20;               energy = (dp[i - jump] + abs(heights[i] - heights[i - jump]))

&#x20;               dp[i] = min(dp[i], energy)



&#x20;       return dp[n - 1]

\`\`\`



**\*\*Time complexity:\*\*** O(n × min(x, n)), where n is the number of stones.



**## 5. Decode Ways**



Count decodings of a digit string using 1 → A through 26 → Z. A zero cannot be decoded alone.



[LeetCode 91]\(https\://leetcode.com/problems/decode-ways/)



\`\`\`python

class Solution:



&#x20;   @lru_cache(maxsize=None)

&#x20;   def numDecodings(self, index, s) -> int:

&#x20;       \# If you reach the end of the string, Return 1 for success.

&#x20;       if index == len(s):

&#x20;           return 1



&#x20;       \# If the string starts with a zero, it can't be decoded

&#x20;       if s[index] == "0":

&#x20;           return 0



&#x20;       if index == len(s) - 1:

&#x20;           return 1



&#x20;       answer = self.numDecodings(index + 1, s)

&#x20;       if int(s[index : index + 2]) <= 26:

&#x20;           answer += self.numDecodings(index + 2, s)



&#x20;       return answer



&#x20;   def numDecodings(self, s: str) -> int:

&#x20;       return self.numDecodings(0, s)

\`\`\`



\`\`\`python

class Solution:

&#x20;   def numDecodings(self, s: str) -> int:

&#x20;       dp = [0 for \_ in range(len(s) + 1)]

&#x20;       dp[0] = 1

&#x20;       \# Ways to decode a string of size 1 is 1. Unless the string is '0'. '0' doesn't have a single digit decode.

&#x20;       dp[1] = 0 if s[0] == "0" else 1



&#x20;       for i in range(2, len(dp)):



&#x20;           \# Check if successful single digit decode is possible.

&#x20;           if s[i - 1] != "0":

&#x20;               dp[i] = dp[i - 1]



&#x20;           \# Check if successful two digit decode is possible.

&#x20;           two_digit = int(s[i - 2 : i])

&#x20;           if two_digit >= 10 and two_digit <= 26:

&#x20;               dp[i] += dp[i - 2]



&#x20;       return dp[len(s)]

\`\`\`



**\*\*Time complexity:\*\*** O(n), where n is the number of houses.

**\*\*Space complexity:\*\*** O(n).



\`\`\`python

class Solution:

&#x20;   def numDecodings(self, s: str) -> int:

&#x20;       if s[0] == "0":

&#x20;           return 0



&#x20;       two_back = 1

&#x20;       one_back = 1

&#x20;       for i in range(1, len(s)):

&#x20;           current = 0

&#x20;           if s[i] != "0":

&#x20;               current = one_back

&#x20;           two_digit = int(s[i - 1 : i + 1])

&#x20;           if two_digit >= 10 and two_digit <= 26:

&#x20;               current += two_back

&#x20;           two_back = one_back

&#x20;           one_back = current



&#x20;       return one_back

\`\`\`



**\*\*Time complexity:\*\*** O(n), where n is the number of houses.

**\*\*Space complexity:\*\*** O(1).



**## Grid DP**



**## 6. Unique Paths I**



[LeetCode 62]\(https\://leetcode.com/problems/unique-paths/)



The robot starts at the top-left corner of an \`m × n\` grid and can move only **\*\*right or down\*\***. Return the number of paths to the bottom-right corner.



**### 2D DP**



\`dp[row][col]\` stores the number of paths to reach that cell. Each cell can be reached from above or from the left.



\`\`\`python

class Solution:

&#x20;   def uniquePaths(self, m: int, n: int) -> int:

&#x20;       dp = [[1] \* n for \_ in range(m)]



&#x20;       for row in range(1, m):

&#x20;           for col in range(1, n):

&#x20;               dp[row][col] = dp[row - 1][col] + dp[row][col - 1]



&#x20;       return dp[m - 1][n - 1]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(m × n)



**### 1D DP**



Reuse one row because each cell needs only the value above it and to its left.



\- \`dp[col]\`: paths from above, before the update.

\- \`dp[col - 1]\`: paths from the left, already updated for the current row.



\`\`\`python

class Solution:

&#x20;   def uniquePaths(self, m: int, n: int) -> int:

&#x20;       dp = [1] \* n



&#x20;       for row in range(1, m):

&#x20;           for col in range(1, n):

&#x20;               dp[col] = dp[col] + dp[col - 1]



&#x20;       return dp[n - 1]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(n)



**### Constant-space Math Solution**



This solution uses **\*\*combinatorics, not DP\*\***.

Every path requires:



\- \`m - 1\` down moves.

\- \`n - 1\` right moves.

\- \`m + n - 2\` total moves.

&#x20; Choose the positions of the down moves among all moves: **\*\*Paths = C(m + n - 2, m - 1)\*\***



\`\`\`python

class Solution:

&#x20;   def uniquePaths(self, m: int, n: int) -> int:

&#x20;       total_moves = m + n - 2

&#x20;       k = min(m - 1, n - 1)

&#x20;       result = 1



&#x20;       for i in range(1, k + 1):

&#x20;           result = result \* (total_moves - i + 1) // i



&#x20;       return result

\`\`\`



**\*\*Time:\*\*** O(min(m, n)) &#x20;

**\*\*Space:\*\*** O(1) auxiliary variables



**## 7. Unique Paths II**



The robot starts at the top-left corner and can move only **\*\*right or down\*\***.



\- \`0\` = open cell.

\- \`1\` = obstacle.

\- Return the number of paths to the bottom-right corner.



**### 2D DP**



\`dp[row][col]\` stores the number of paths to reach that cell.



\- An obstacle has zero paths.

\- An open cell receives paths from above and from the left.



\`\`\`python

class Solution:

&#x20;   def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

&#x20;       m = len(obstacleGrid)

&#x20;       n = len(obstacleGrid[0])

&#x20;       dp = [[0] \* n for \_ in range(m)]



&#x20;       if obstacleGrid[0][0] == 1:

&#x20;           return 0



&#x20;       dp[0][0] = 1



&#x20;       for row in range(m):

&#x20;           for col in range(n):

&#x20;               if obstacleGrid[row][col] == 1:

&#x20;                   dp[row][col] = 0

&#x20;               else:

&#x20;                   if row > 0:

&#x20;                       dp[row][col] += dp[row - 1][col]

&#x20;                   if col > 0:

&#x20;                       dp[row][col] += dp[row][col - 1]



&#x20;       return dp[m - 1][n - 1]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(m × n)



**### 1D DP**



Reuse one row.



\- \`dp[col]\` holds the paths from above before the update.

\- \`dp[col - 1]\` holds the paths from the left.

\- Reset \`dp[col]\` to zero when an obstacle is encountered.



\`\`\`python

class Solution:

&#x20;   def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

&#x20;       m = len(obstacleGrid)

&#x20;       n = len(obstacleGrid[0])



&#x20;       dp = [0] \* n

&#x20;       dp[0] = 1



&#x20;       for row in range(m):

&#x20;           for col in range(n):

&#x20;               if obstacleGrid[row][col] == 1:

&#x20;                   dp[col] = 0

&#x20;               elif col > 0:

&#x20;                   dp[col] += dp[col - 1]



&#x20;       return dp[n - 1]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(n)



**### Constant Extra Space — In-place DP**



Store the path counts directly in the input grid. Unlike Unique Paths I, the simple combinatorics formula does not handle obstacles.



\`\`\`python

class Solution:

&#x20;   def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

&#x20;       m = len(obstacleGrid)

&#x20;       n = len(obstacleGrid[0])



&#x20;       for row in range(m):

&#x20;           for col in range(n):

&#x20;               if obstacleGrid[row][col] == 1:

&#x20;                   obstacleGrid[row][col] = 0

&#x20;               elif row == 0 and col == 0:

&#x20;                   obstacleGrid[row][col] = 1

&#x20;               else:

&#x20;                   above = obstacleGrid[row - 1][col] if row > 0 else 0

&#x20;                   left = obstacleGrid[row][col - 1] if col > 0 else 0

&#x20;                   obstacleGrid[row][col] = above + left



&#x20;       return obstacleGrid[m - 1][n - 1]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Extra Space:\*\*** O(1)



**## Subsequence and Knapsack DP**



**## 8. Subset Sum to Target**



GFG - https\://www\.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1



Given an array of positive integers \`arr\` and a target \`sum\`, return \`True\` if a subset adds up to the target. Otherwise, return \`False\`. Each element can be used at most once.

**\*\*Example:\*\*** \`arr = [3, 34, 4, 12, 5, 2]\`, \`sum = 9\` &#x20;

**\*\*Output:\*\*** \`True\` — the subset \`[4, 5]\` adds up to \`9\`.



**### Memoization**



At each index, either skip the number or take it.



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def isSubsetSum(self, arr, sum):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, remaining):

&#x20;           if remaining == 0:

&#x20;               return True



&#x20;           if i == len(arr):

&#x20;               return False



&#x20;           skip = solve(i + 1, remaining)



&#x20;           take = False

&#x20;           if arr[i] <= remaining:

&#x20;               take = solve(i + 1, remaining - arr[i])



&#x20;           return skip or take



&#x20;       return solve(0, sum)

\`\`\`



**\*\*Time:\*\*** O(n × (sum + 1)) &#x20;

**\*\*Space:\*\*** O(n × (sum + 1)), including memoization and recursion.



**### 2D DP**



\`dp[i][s]\` indicates whether a subset of the first \`i\` elements can make sum \`s\`. Sum \`0\` is always possible by choosing the empty subset.



\`\`\`python

class Solution:

&#x20;   def isSubsetSum(self, arr, sum):

&#x20;       n = len(arr)

&#x20;       dp = [[False] \* (sum + 1) for \_ in range(n + 1)]



&#x20;       for i in range(n + 1):

&#x20;           dp[i][0] = True



&#x20;       for i in range(1, n + 1):

&#x20;           num = arr[i - 1]



&#x20;           for s in range(1, sum + 1):

&#x20;               skip = dp[i - 1][s]



&#x20;               take = False

&#x20;               if num <= s:

&#x20;                   take = dp[i - 1][s - num]



&#x20;               dp[i][s] = skip or take



&#x20;       return dp[n][sum]

\`\`\`



**\*\*Time:\*\*** O(n × (sum + 1)) &#x20;

**\*\*Space:\*\*** O(n × (sum + 1))



**### Space-optimized DP**



\`dp[s]\` indicates whether sum \`s\` can be formed using the elements processed so far. Loop backward so each element is used at most once.



\`\`\`python

class Solution:

&#x20;   def isSubsetSum(self, arr, sum):

&#x20;       dp = [False] \* (sum + 1)

&#x20;       dp[0] = True



&#x20;       for num in arr:

&#x20;           for s in range(sum, num - 1, -1):

&#x20;               dp[s] = dp[s] or dp[s - num]



&#x20;       return dp[sum]

\`\`\`



**\*\*Time:\*\*** O(n × (sum + 1)) &#x20;

**\*\*Space:\*\*** O(sum + 1)



**## 9. Equal Subset Partition**



[LeetCode 416]\(https\://leetcode.com/problems/partition-equal-subset-sum/)



Return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

**\*\*Input:\*\*** nums = [1, 5, 11, 5] &#x20;

**\*\*Output:\*\*** True

**\*\*Input:\*\*** nums = [1, 2, 3, 5] &#x20;

**\*\*Output:\*\*** False



**### Memoization**



\`\`\`python

from functools import lru_cache

from typing import List



class Solution:

&#x20;   def canPartition(self, nums: List[int]) -> bool:

&#x20;       total = sum(nums)



&#x20;       if total % 2 != 0:

&#x20;           return False



&#x20;       target = total // 2



&#x20;       @lru_cache(None)

&#x20;       def solve(i, remaining):

&#x20;           if remaining == 0:

&#x20;               return True



&#x20;           if i == len(nums):

&#x20;               return False



&#x20;           skip = solve(i + 1, remaining)



&#x20;           take = False

&#x20;           if nums[i] <= remaining:

&#x20;               take = solve(i + 1, remaining - nums[i])



&#x20;           return skip or take



&#x20;       return solve(0, target)

\`\`\`



**\*\*Time:\*\*** O(n × (target + 1)) &#x20;

**\*\*Space:\*\*** O(n × (target + 1))



**### 2D DP**



\`\`\`python

from typing import List



class Solution:

&#x20;   def canPartition(self, nums: List[int]) -> bool:

&#x20;       total = sum(nums)



&#x20;       if total % 2 != 0:

&#x20;           return False



&#x20;       target = total // 2

&#x20;       n = len(nums)



&#x20;       dp = [[False] \* (target + 1) for \_ in range(n + 1)]



&#x20;       for i in range(n + 1):

&#x20;           dp[i][0] = True



&#x20;       for i in range(1, n + 1):

&#x20;           num = nums[i - 1]



&#x20;           for s in range(1, target + 1):

&#x20;               skip = dp[i - 1][s]



&#x20;               take = False

&#x20;               if num <= s:

&#x20;                   take = dp[i - 1][s - num]



&#x20;               dp[i][s] = skip or take



&#x20;       return dp[n][target]

\`\`\`



**\*\*Time:\*\*** O(n × (target + 1)) &#x20;

**\*\*Space:\*\*** O(n × (target + 1))



**### Space-optimized DP**



\`\`\`python

from typing import List



class Solution:

&#x20;   def canPartition(self, nums: List[int]) -> bool:

&#x20;       total = sum(nums)



&#x20;       if total % 2 != 0:

&#x20;           return False



&#x20;       target = total // 2



&#x20;       dp = [False] \* (target + 1)

&#x20;       dp[0] = True



&#x20;       for num in nums:

&#x20;           for s in range(target, num - 1, -1):

&#x20;               dp[s] = dp[s] or dp[s - num]



&#x20;       return dp[target]

\`\`\`



**\*\*Time:\*\*** O(n × (target + 1)) &#x20;

**\*\*Space:\*\*** O(target + 1)



**## 10. Minimum Partition Difference**



Split a nonnegative array into two subsets of any sizes, minimizing the absolute difference of their sums. Find the largest reachable sum no greater than half the total.



[GeeksforGeeks: Minimum Partition Difference]\(https\://www\.geeksforgeeks.org/problems/minimum-sum-partition3317/1)



\- If one subset sums to \`s\`, the other sums to \`total - s\`.

\- Their difference is \`abs(total - 2 \* s)\`.

\- Find the **\*\*largest achievable sum at or below \`total // 2\`\*\*** to minimize the difference.

\- An odd total can still produce a valid answer; do not return early.

\- In space-optimized DP, loop **\*\*backward\*\*** so each element is used at most once.



\`\`\`python

class Solution:

&#x20;   def minDifference(self, arr):

&#x20;       total = sum(arr)

&#x20;       target = total // 2



&#x20;       dp = [False] \* (target + 1)

&#x20;       dp[0] = True



&#x20;       for num in arr:

&#x20;           for s in range(target, num - 1, -1):

&#x20;               dp[s] = dp[s] or dp[s - num]



&#x20;       for s in range(target, -1, -1):

&#x20;           if dp[s]:

&#x20;               return total - 2 \* s

\`\`\`



The complexity is **\*\*pseudo-polynomial\*\*** because it depends on the numeric sum.

**\*\*Time:\*\*** O(n × (target + 1)) &#x20;

**\*\*Space:\*\*** O(target + 1)



**## 11. Count Subsets with Sum K**



Count subsets of nonnegative integers totaling k; equal-valued elements at different indices are distinct choices. Zeros correctly double existing counts. Return an exact count, without a modulus.



[GeeksforGeeks: Count Subsets with Sum]\(https\://www\.geeksforgeeks.org/problems/perfect-sum-problem5633/1)



\`\`\`python

class Solution:

&#x20;   def countSubsets(self, nums, k):

&#x20;       dp = [0] \* (k + 1)

&#x20;       dp[0] = 1

&#x20;       for num in nums:

&#x20;           for s in range(k, num - 1, -1):

&#x20;               dp[s] += dp[s - num]

&#x20;       return dp[k]

\`\`\`



**\*\*Time:\*\*** O(n × (k + 1)) &#x20;

**\*\*Space:\*\*** O(k + 1)



**## 12. Count Partitions with Difference**



Count assignments to labeled subsets S1 and S2 such that sum(S1) − sum(S2) = d, for nonnegative values and d ≥ 0. Count subsets totaling (total − d) / 2; return an exact count.



[GeeksforGeeks: Partitions with Given Difference]\(https\://www\.geeksforgeeks.org/problems/partitions-with-given-difference/1)



\`\`\`python

class Solution:

&#x20;   def countPartitions(self, arr, d):

&#x20;       total = sum(arr)



&#x20;       if total < d or (total - d) % 2 != 0:

&#x20;           return 0



&#x20;       target = (total - d) // 2



&#x20;       dp = [0] \* (target + 1)

&#x20;       dp[0] = 1



&#x20;       for num in arr:

&#x20;           for s in range(target, num - 1, -1):

&#x20;               dp[s] += dp[s - num]



&#x20;       return dp[target]

\`\`\`



**\*\*Time complexity:\*\*** O(n × (T + 1)) DP updates, where T = (total − d) / 2; exact-integer additions cost O(b) for b-bit counts.

**\*\*Space:\*\*** O(target + 1)



**## 13. Target Sum**



Assign + or − to every nonnegative number so the expression equals target. Count subsets assigned minus signs, whose sum must be (total − target) / 2.



[LeetCode 494]\(https\://leetcode.com/problems/target-sum/)



\`\`\`python

class Solution:

&#x20;   def findTargetSumWays(self, nums: List[int], target: int) -> int:

&#x20;       total = sum(nums)



&#x20;       if abs(target) > total or (total + target) % 2 != 0:

&#x20;           return 0



&#x20;       subset_sum = (total + target) // 2



&#x20;       dp = [0] \* (subset_sum + 1)

&#x20;       dp[0] = 1



&#x20;       for num in nums:

&#x20;           for s in range(subset_sum, num - 1, -1):

&#x20;               dp[s] += dp[s - num]



&#x20;       return dp[subset_sum]



\`\`\`



**\*\*Time:\*\*** O(n × (subset_sum + 1)) &#x20;

**\*\*Space:\*\*** O(subset_sum + 1)



**## 14. Minimum Coins**



Find the fewest coins needed to form amount using unlimited positive-denomination coins. Return −1 when impossible.



[LeetCode 322]\(https\://leetcode.com/problems/coin-change/)



**## 14. Minimum Coins**



[LeetCode 322 — Coin Change]\(https\://leetcode.com/problems/coin-change/)



**\*\*Input:\*\*** coins = [1, 2, 5], amount = 11 &#x20;

**\*\*Output:\*\*** 3



**\*\*Input:\*\*** coins = [2], amount = 3 &#x20;

**\*\*Output:\*\*** -1



**\*\*Input:\*\*** coins = [1], amount = 0 &#x20;

**\*\*Output:\*\*** 0



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache

from typing import List



class Solution:

&#x20;   def coinChange(self, coins: List[int], amount: int) -> int:

&#x20;       @lru_cache(None)

&#x20;       def solve(i, remaining):

&#x20;           if remaining == 0:

&#x20;               return 0



&#x20;           if i == len(coins):

&#x20;               return float('inf')



&#x20;           skip = solve(i + 1, remaining)



&#x20;           take = float('inf')

&#x20;           if coins[i] <= remaining:

&#x20;               take = 1 + solve(i, remaining - coins[i])



&#x20;           return min(skip, take)



&#x20;       answer = solve(0, amount)

&#x20;       return -1 if answer == float('inf') else answer

\`\`\`



**\*\*Time:\*\*** O(n × (amount + 1)) &#x20;

**\*\*Space:\*\*** O(n × (amount + 1) + n + amount)



**### 2D DP**



\`\`\`python

from typing import List



class Solution:

&#x20;   def coinChange(self, coins: List[int], amount: int) -> int:

&#x20;       n = len(coins)

&#x20;       dp = [[float('inf')] \* (amount + 1) for \_ in range(n + 1)]



&#x20;       for i in range(n + 1):

&#x20;           dp[i][0] = 0



&#x20;       for i in range(1, n + 1):

&#x20;           coin = coins[i - 1]



&#x20;           for s in range(1, amount + 1):

&#x20;               skip = dp[i - 1][s]



&#x20;               take = float('inf')

&#x20;               if coin <= s:

&#x20;                   take = 1 + dp[i][s - coin]



&#x20;               dp[i][s] = min(skip, take)



&#x20;       answer = dp[n][amount]

&#x20;       return -1 if answer == float('inf') else answer

\`\`\`



**\*\*Time:\*\*** O(n × (amount + 1)) &#x20;

**\*\*Space:\*\*** O((n + 1) × (amount + 1))



**### Space-optimized DP**



\`\`\`python

from typing import List



class Solution:

&#x20;   def coinChange(self, coins: List[int], amount: int) -> int:

&#x20;       dp = [float('inf')] \* (amount + 1)

&#x20;       dp[0] = 0



&#x20;       for coin in coins:

&#x20;           for s in range(coin, amount + 1):

&#x20;               dp[s] = min(dp[s], 1 + dp[s - coin])



&#x20;       answer = dp[amount]

&#x20;       return -1 if answer == float('inf') else answer

\`\`\`



**\*\*Time:\*\*** O(n × (amount + 1)) &#x20;

**\*\*Space:\*\*** O(amount + 1)



**## 15. Coin Change II**



Count unordered combinations forming amount using unlimited coins of distinct positive denominations. Process coins outside the sum loop to avoid counting different orders separately.



[LeetCode 518]\(https\://leetcode.com/problems/coin-change-ii/)



\`\`\`python

from typing import List



class Solution:

&#x20;   def change(self, amount: int, coins: List[int]) -> int:

&#x20;       dp = [0] \* (amount + 1)

&#x20;       dp[0] = 1



&#x20;       for coin in coins:

&#x20;           for total in range(coin, amount + 1):

&#x20;               dp[total] += dp[total - coin]



&#x20;       return dp[amount]

\`\`\`



**\*\*Time:\*\*** O(n × (amount + 1)) &#x20;

**\*\*Space:\*\*** O(amount + 1)



**## 16. Unbounded Knapsack**



Maximize value within capacity using unlimited copies of items with positive weights and nonnegative values. Ascending capacity updates allow reusing the current item.



[GeeksforGeeks — Knapsack with Duplicate Items]\(https\://www\.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)



**\*\*Input:\*\*** val = [10, 40, 50, 70], wt = [1, 3, 4, 5], capacity = 8 &#x20;

**\*\*Output:\*\*** 110



**\*\*Input:\*\*** val = [10, 30], wt = [5, 10], capacity = 4 &#x20;

**\*\*Output:\*\*** 0



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def knapSack(self, val, wt, capacity):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, remaining):

&#x20;           if i == len(wt) or remaining == 0:

&#x20;               return 0



&#x20;           skip = solve(i + 1, remaining)



&#x20;           take = 0

&#x20;           if wt[i] <= remaining:

&#x20;               take = val[i] + solve(i, remaining - wt[i])



&#x20;           return max(skip, take)



&#x20;       return solve(0, capacity)

\`\`\`



**\*\*Time:\*\*** O(n × (capacity + 1)) &#x20;

**\*\*Space:\*\*** O(n × (capacity + 1) + n + capacity)



**### 2D DP**



\`\`\`python

class Solution:

&#x20;   def knapSack(self, val, wt, capacity):

&#x20;       n = len(wt)

&#x20;       dp = [[0] \* (capacity + 1) for \_ in range(n + 1)]



&#x20;       for i in range(1, n + 1):

&#x20;           weight = wt[i - 1]

&#x20;           value = val[i - 1]



&#x20;           for cap in range(1, capacity + 1):

&#x20;               skip = dp[i - 1][cap]



&#x20;               take = 0

&#x20;               if weight <= cap:

&#x20;                   take = value + dp[i][cap - weight]



&#x20;               dp[i][cap] = max(skip, take)



&#x20;       return dp[n][capacity]

\`\`\`



**\*\*Time:\*\*** O(n × (capacity + 1)) &#x20;

**\*\*Space:\*\*** O((n + 1) × (capacity + 1))



**### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def knapSack(self, val, wt, capacity):

&#x20;       dp = [0] \* (capacity + 1)



&#x20;       for i in range(len(wt)):

&#x20;           for cap in range(wt[i], capacity + 1):

&#x20;               dp[cap] = max(dp[cap], val[i] + dp[cap - wt[i]])



&#x20;       return dp[capacity]

\`\`\`



**\*\*Time:\*\*** O(n × (capacity + 1)) &#x20;

**\*\*Space:\*\*** O(capacity + 1)



**## 17. Rod Cutting**



Maximize revenue by cutting a rod of length n. price[i − 1] is the price of a piece of length i; prices are nonnegative and each length can be reused.

**\*\*Input:\*\*** price = [1, 5, 8, 9, 10, 17, 17, 20] &#x20;

**\*\*Output:\*\*** 22



**\*\*Input:\*\*** price = [3, 5, 8, 9, 10, 17, 17, 20] &#x20;

**\*\*Output:\*\*** 24



[GeeksforGeeks: Rod Cutting]\(https\://www\.geeksforgeeks.org/problems/rod-cutting0840/1)



\`\`\`python

class Solution:

&#x20;   def cutRod(self, price):

&#x20;       n = len(price)

&#x20;       dp = [float('-inf')] \* (n + 1)

&#x20;       dp[0] = 0



&#x20;       for length in range(1, n + 1):

&#x20;           for remaining in range(length, n + 1):

&#x20;               dp[remaining] = max(dp[remaining], price[length - 1] + dp[remaining - length])



&#x20;       return dp[n]

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n)



**## Stock DP**



**## 18. Buy and Sell Stock I, II, III, IV, V**



Maximize profit using at most one buy followed by one sell. Track the lowest price seen before each sale.



**## 18. Buy and Sell Stock I, II, III, IV, V**



**### Stock I — One Transaction**



[LeetCode 121]\(https\://leetcode.com/problems/best-time-to-buy-and-sell-stock/)



**\*\*Input:\*\*** prices = [7, 1, 5, 3, 6, 4] &#x20;

**\*\*Output:\*\*** 5



**#### Constant Space**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       minimum_price = float('inf')

&#x20;       profit = 0



&#x20;       for price in prices:

&#x20;           minimum_price = min(minimum_price, price)

&#x20;           profit = max(profit, price - minimum_price)



&#x20;       return profit

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(1)



\---



**### Stock II — Unlimited Transactions**



[LeetCode 122]\(https\://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)



**\*\*Input:\*\*** prices = [7, 1, 5, 3, 6, 4] &#x20;

**\*\*Output:\*\*** 7



**#### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, holding):

&#x20;           if i == len(prices):

&#x20;               return float('-inf') if holding else 0



&#x20;           if holding:

&#x20;               return max(solve(i + 1, 1), prices[i] + solve(i + 1, 0))



&#x20;           return max(solve(i + 1, 0), -prices[i] + solve(i + 1, 1))



&#x20;       return solve(0, 0)

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**#### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       n = len(prices)

&#x20;       dp = [[0, float('-inf')] for \_ in range(n + 1)]



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])

&#x20;           dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 1][0])



&#x20;       return dp[0][0]

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**#### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       next_free = 0

&#x20;       next_holding = float('-inf')



&#x20;       for i in range(len(prices) - 1, -1, -1):

&#x20;           current_free = max(next_free, -prices[i] + next_holding)

&#x20;           current_holding = max(next_holding, prices[i] + next_free)

&#x20;           next_free, next_holding = current_free, current_holding



&#x20;       return next_free

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(1)



**#### Important Pointers**



\- Unlimited transactions are allowed, but you can hold only one share at a time.

\- \`holding = 0\`: buy or skip. \`holding = 1\`: sell or skip.

\- Buying subtracts the price; selling adds it.

\- Adding every positive adjacent price difference also solves this variant.



\---



**### Stock III — At Most Two Transactions**



[LeetCode 123]\(https\://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)



**\*\*Input:\*\*** prices = [3, 3, 5, 0, 0, 3, 1, 4] &#x20;

**\*\*Output:\*\*** 6



**#### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, holding, remaining):

&#x20;           if i == len(prices) or remaining == 0:

&#x20;               return float('-inf') if holding else 0



&#x20;           if holding:

&#x20;               return max(solve(i + 1, 1, remaining), prices[i] + solve(i + 1, 0, remaining - 1))



&#x20;           return max(solve(i + 1, 0, remaining), -prices[i] + solve(i + 1, 1, remaining))



&#x20;       return solve(0, 0, 2)

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**#### Full 3D DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       n = len(prices)

&#x20;       dp = [[[0] \* 3, [float('-inf')] \* 3] for \_ in range(n + 1)]



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           for remaining in range(1, 3):

&#x20;               dp[i][0][remaining] = max(dp[i + 1][0][remaining], -prices[i] + dp[i + 1][1][remaining])

&#x20;               dp[i][1][remaining] = max(dp[i + 1][1][remaining], prices[i] + dp[i + 1][0][remaining - 1])



&#x20;       return dp[0][0][2]

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**#### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       next_dp = [[0] \* 3, [float('-inf')] \* 3]



&#x20;       for i in range(len(prices) - 1, -1, -1):

&#x20;           current = [[0] \* 3, [float('-inf')] \* 3]



&#x20;           for remaining in range(1, 3):

&#x20;               current[0][remaining] = max(next_dp[0][remaining], -prices[i] + next_dp[1][remaining])

&#x20;               current[1][remaining] = max(next_dp[1][remaining], prices[i] + next_dp[0][remaining - 1])



&#x20;           next_dp = current



&#x20;       return next_dp[0][2]

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(1)



**#### Important Pointers**



\- At most two complete transactions are allowed.

\- Decrease \`remaining\` when selling.

\- The optimized table has a fixed size, so its space is O(1).



\---



**### Stock IV — At Most K Transactions**



[LeetCode 188]\(https\://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)



**\*\*Input:\*\*** k = 2, prices = [3, 2, 6, 5, 0, 3] &#x20;

**\*\*Output:\*\*** 7



**#### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def maxProfit(self, k, prices):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, holding, remaining):

&#x20;           if i == len(prices) or remaining == 0:

&#x20;               return float('-inf') if holding else 0



&#x20;           if holding:

&#x20;               return max(solve(i + 1, 1, remaining), prices[i] + solve(i + 1, 0, remaining - 1))



&#x20;           return max(solve(i + 1, 0, remaining), -prices[i] + solve(i + 1, 1, remaining))



&#x20;       return solve(0, 0, k)

\`\`\`



**\*\*Time:\*\*** O(n × (k + 1)) &#x20;

**\*\*Space:\*\*** O((n + 1) × (k + 1))



**#### Full 3D DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, k, prices):

&#x20;       n = len(prices)

&#x20;       dp = [[[0] \* (k + 1), [float('-inf')] \* (k + 1)] for \_ in range(n + 1)]



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           for remaining in range(1, k + 1):

&#x20;               dp[i][0][remaining] = max(dp[i + 1][0][remaining], -prices[i] + dp[i + 1][1][remaining])

&#x20;               dp[i][1][remaining] = max(dp[i + 1][1][remaining], prices[i] + dp[i + 1][0][remaining - 1])



&#x20;       return dp[0][0][k]

\`\`\`



**\*\*Time:\*\*** O(n × (k + 1)) &#x20;

**\*\*Space:\*\*** O((n + 1) × (k + 1))



**#### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, k, prices):

&#x20;       next_dp = [[0] \* (k + 1), [float('-inf')] \* (k + 1)]



&#x20;       for i in range(len(prices) - 1, -1, -1):

&#x20;           current = [[0] \* (k + 1), [float('-inf')] \* (k + 1)]



&#x20;           for remaining in range(1, k + 1):

&#x20;               current[0][remaining] = max(next_dp[0][remaining], -prices[i] + next_dp[1][remaining])

&#x20;               current[1][remaining] = max(next_dp[1][remaining], prices[i] + next_dp[0][remaining - 1])



&#x20;           next_dp = current



&#x20;       return next_dp[0][k]

\`\`\`



**\*\*Time:\*\*** O(n × (k + 1)) &#x20;

**\*\*Space:\*\*** O(k + 1)



**#### Important Pointers**



\- This generalizes Stock III from two transactions to \`k\`.

\- Decrease the transaction count when selling.

\- If \`k >= len(prices) // 2\`, use Stock II to achieve O(n) time.

\- The optimized solution uses O(k) space, not constant space.



\---



**### Stock V — With Cooldown**



[LeetCode 309]\(https\://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)



**\*\*Input:\*\*** prices = [1, 2, 3, 0, 2] &#x20;

**\*\*Output:\*\*** 3



**#### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, holding):

&#x20;           if i >= len(prices):

&#x20;               return float('-inf') if holding else 0



&#x20;           if holding:

&#x20;               return max(solve(i + 1, 1), prices[i] + solve(i + 2, 0))



&#x20;           return max(solve(i + 1, 0), -prices[i] + solve(i + 1, 1))



&#x20;       return solve(0, 0)

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**#### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       n = len(prices)

&#x20;       dp = [[0, float('-inf')] for \_ in range(n + 2)]



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])

&#x20;           dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 2][0])



&#x20;       return dp[0][0]

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**#### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def maxProfit(self, prices):

&#x20;       next_free = 0

&#x20;       next_holding = float('-inf')

&#x20;       next2_free = 0



&#x20;       for i in range(len(prices) - 1, -1, -1):

&#x20;           current_free = max(next_free, -prices[i] + next_holding)

&#x20;           current_holding = max(next_holding, prices[i] + next2_free)



&#x20;           next2_free = next_free

&#x20;           next_free, next_holding = current_free, current_holding



&#x20;       return next_free

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(1)



**#### Important Pointers**



\- Here, Stock V means the cooldown variant.

\- After selling, you cannot buy on the next day.

\- Selling moves to day \`i + 2\`; buying and skipping move to day \`i + 1\`.

\- In all DP versions, negative infinity marks an invalid terminal state where a share remains unsold.

\- For long arrays, use iterative DP to avoid Python's recursion depth limit.



**## LCS and String DP**



**## 19. Longest Common Subsequence — Length**



Find the longest sequence appearing in both strings in the same order; characters need not be adjacent.

[LeetCode 1143]\(https\://leetcode.com/problems/longest-common-subsequence/)



**\*\*Input:\*\*** text1 = "abcde", text2 = "ace" &#x20;

**\*\*Output:\*\*** 3



**\*\*Input:\*\*** text1 = "abc", text2 = "def" &#x20;

**\*\*Output:\*\*** 0



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def longestCommonSubsequence(self, text1, text2):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, j):

&#x20;           if i == len(text1) or j == len(text2):

&#x20;               return 0



&#x20;           if text1[i] == text2[j]:

&#x20;               return 1 + solve(i + 1, j + 1)



&#x20;           return max(solve(i + 1, j), solve(i, j + 1))



&#x20;       return solve(0, 0)

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(m × n + m + n)



**### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def longestCommonSubsequence(self, text1, text2):

&#x20;       m, n = len(text1), len(text2)

&#x20;       dp = [[0] \* (n + 1) for \_ in range(m + 1)]



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if text1[i] == text2[j]:

&#x20;                   dp[i][j] = 1 + dp[i + 1][j + 1]

&#x20;               else:

&#x20;                   dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])



&#x20;       return dp[0][0]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O((m + 1) × (n + 1))



**### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def longestCommonSubsequence(self, text1, text2):

&#x20;       if len(text1) < len(text2):

&#x20;           text1, text2 = text2, text1



&#x20;       m, n = len(text1), len(text2)

&#x20;       next_row = [0] \* (n + 1)



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           current = [0] \* (n + 1)



&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if text1[i] == text2[j]:

&#x20;                   current[j] = 1 + next_row[j + 1]

&#x20;               else:

&#x20;                   current[j] = max(next_row[j], current[j + 1])



&#x20;           next_row = current



&#x20;       return next_row[0]

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(min(m, n) + 1)



**## 20. Longest Common Subsequence — Printing**



Reconstruct and return one LCS by walking backward through the DP table. On a match, take that character; otherwise move toward the larger neighboring value.



[GeeksforGeeks: Printing LCS]\(https\://www\.geeksforgeeks.org/dsa/printing-longest-common-subsequence/)



**\*\*Input:\*\*** text1 = "abcde", text2 = "ace" &#x20;

**\*\*Output:\*\*** "ace"



**\*\*Input:\*\*** text1 = "abc", text2 = "def" &#x20;

**\*\*Output:\*\*** ""



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def printLCS(self, text1, text2):

&#x20;       m, n = len(text1), len(text2)



&#x20;       @lru_cache(None)

&#x20;       def solve(i, j):

&#x20;           if i == m or j == n:

&#x20;               return 0



&#x20;           if text1[i] == text2[j]:

&#x20;               return 1 + solve(i + 1, j + 1)



&#x20;           return max(solve(i + 1, j), solve(i, j + 1))



&#x20;       solve(0, 0)

&#x20;       i = j = 0

&#x20;       result = []



&#x20;       while i < m and j < n:

&#x20;           if text1[i] == text2[j]:

&#x20;               result.append(text1[i])

&#x20;               i += 1

&#x20;               j += 1

&#x20;           elif solve(i + 1, j) >= solve(i, j + 1):

&#x20;               i += 1

&#x20;           else:

&#x20;               j += 1



&#x20;       return ''.join(result)

\`\`\`



**\*\*Time:\*\*** O(m × n + m + n) &#x20;

**\*\*Space:\*\*** O(m × n + m + n)



**### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def printLCS(self, text1, text2):

&#x20;       m, n = len(text1), len(text2)

&#x20;       dp = [[0] \* (n + 1) for \_ in range(m + 1)]



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if text1[i] == text2[j]:

&#x20;                   dp[i][j] = 1 + dp[i + 1][j + 1]

&#x20;               else:

&#x20;                   dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])



&#x20;       i = j = 0

&#x20;       result = []



&#x20;       while i < m and j < n:

&#x20;           if text1[i] == text2[j]:

&#x20;               result.append(text1[i])

&#x20;               i += 1

&#x20;               j += 1

&#x20;           elif dp[i + 1][j] >= dp[i][j + 1]:

&#x20;               i += 1

&#x20;           else:

&#x20;               j += 1



&#x20;       return ''.join(result)

\`\`\`



**\*\*Time:\*\*** O(m × n + m + n) &#x20;

**\*\*Space:\*\*** O((m + 1) × (n + 1))



**### Space-optimized DP — Store Subsequences**



\`\`\`python

class Solution:

&#x20;   def printLCS(self, text1, text2):

&#x20;       if len(text1) < len(text2):

&#x20;           text1, text2 = text2, text1



&#x20;       m, n = len(text1), len(text2)

&#x20;       next_row = [''] \* (n + 1)



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           current = [''] \* (n + 1)



&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if text1[i] == text2[j]:

&#x20;                   current[j] = text1[i] + next_row[j + 1]

&#x20;               else:

&#x20;                   current[j] = max(next_row[j], current[j + 1], key=len)



&#x20;           next_row = current



&#x20;       return next_row[0]

\`\`\`



**\*\*Time:\*\*** O(m × n × (L + 1)) &#x20;

**\*\*Space:\*\*** O((min(m, n) + 1) × (L + 1))



Here, \`L\` is the length of the LCS. String concatenation copies characters.



**## 21. Longest Common Substring**



Return the length of the longest contiguous string shared by both inputs. dp[i][j] is the matching suffix length ending at those positions; reset it to zero on a mismatch.



[GeeksforGeeks: Longest Common Substring]\(https\://www\.geeksforgeeks.org/problems/longest-common-substring1452/1)



\`\`\`python

class Solution:

&#x20;   def longestCommonSubstr(self, a, b):

&#x20;       dp = [[0] \* (len(b) + 1) for \_ in range(len(a) + 1)]

&#x20;       best = 0

&#x20;       for i in range(1, len(a) + 1):

&#x20;           for j in range(1, len(b) + 1):

&#x20;               if a[i - 1] == b[j - 1]:

&#x20;                   dp[i][j] = 1 + dp[i - 1][j - 1]

&#x20;                   best = max(best, dp[i][j])

&#x20;       return best

\`\`\`



**\*\*Time complexity:\*\*** O((m + 1) × (n + 1)), where m and n are the string lengths.



**## 22. Longest Palindromic Subsequence**



[LeetCode 516 — Longest Palindromic Subsequence]\(https\://leetcode.com/problems/longest-palindromic-subsequence/)



**\*\*Input:\*\*** s = "bbbab" &#x20;

**\*\*Output:\*\*** 4



**\*\*Input:\*\*** s = "cbbd" &#x20;

**\*\*Output:\*\*** 2



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def longestPalindromeSubseq(self, s):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, j):

&#x20;           if i > j:

&#x20;               return 0



&#x20;           if i == j:

&#x20;               return 1



&#x20;           if s[i] == s[j]:

&#x20;               return 2 + solve(i + 1, j - 1)



&#x20;           return max(solve(i + 1, j), solve(i, j - 1))



&#x20;       return solve(0, len(s) - 1)

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n²)



**### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def longestPalindromeSubseq(self, s):

&#x20;       n = len(s)



&#x20;       if n == 0:

&#x20;           return 0



&#x20;       dp = [[0] \* n for \_ in range(n)]



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           dp[i][i] = 1



&#x20;           for j in range(i + 1, n):

&#x20;               if s[i] == s[j]:

&#x20;                   dp[i][j] = 2 + dp[i + 1][j - 1]

&#x20;               else:

&#x20;                   dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])



&#x20;       return dp[0][n - 1]

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n²)



**### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def longestPalindromeSubseq(self, s):

&#x20;       n = len(s)



&#x20;       if n == 0:

&#x20;           return 0



&#x20;       dp = [0] \* n



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           diagonal = 0

&#x20;           dp[i] = 1



&#x20;           for j in range(i + 1, n):

&#x20;               old_value = dp[j]



&#x20;               if s[i] == s[j]:

&#x20;                   dp[j] = 2 + diagonal

&#x20;               else:

&#x20;                   dp[j] = max(dp[j], dp[j - 1])



&#x20;               diagonal = old_value



&#x20;       return dp[n - 1]

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n)



**### Important Pointers**



\- A subsequence does not need to be contiguous.

\- Matching endpoints contribute \`2\`; a single middle character contributes \`1\`.

\- \`diagonal\` preserves the previous row's \`dp[i + 1][j - 1]\`.

\- The length also equals the LCS length of \`s\` and its reverse.



\---



**## 23. Edit Distance**



[LeetCode 72 — Edit Distance]\(https\://leetcode.com/problems/edit-distance/)



**\*\*Input:\*\*** word1 = "horse", word2 = "ros" &#x20;

**\*\*Output:\*\*** 3



**\*\*Input:\*\*** word1 = "intention", word2 = "execution" &#x20;

**\*\*Output:\*\*** 5



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def minDistance(self, word1, word2):

&#x20;       m, n = len(word1), len(word2)



&#x20;       @lru_cache(None)

&#x20;       def solve(i, j):

&#x20;           if i == m:

&#x20;               return n - j



&#x20;           if j == n:

&#x20;               return m - i



&#x20;           if word1[i] == word2[j]:

&#x20;               return solve(i + 1, j + 1)



&#x20;           return 1 + min(solve(i, j + 1), solve(i + 1, j), solve(i + 1, j + 1))



&#x20;       return solve(0, 0)

\`\`\`



**\*\*Time:\*\*** O((m + 1) × (n + 1)) &#x20;

**\*\*Space:\*\*** O((m + 1) × (n + 1))



**### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def minDistance(self, word1, word2):

&#x20;       m, n = len(word1), len(word2)

&#x20;       dp = [[0] \* (n + 1) for \_ in range(m + 1)]



&#x20;       for i in range(m + 1):

&#x20;           dp[i][n] = m - i



&#x20;       for j in range(n + 1):

&#x20;           dp[m][j] = n - j



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if word1[i] == word2[j]:

&#x20;                   dp[i][j] = dp[i + 1][j + 1]

&#x20;               else:

&#x20;                   dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])



&#x20;       return dp[0][0]

\`\`\`



**\*\*Time:\*\*** O((m + 1) × (n + 1)) &#x20;

**\*\*Space:\*\*** O((m + 1) × (n + 1))



**### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def minDistance(self, word1, word2):

&#x20;       if len(word1) < len(word2):

&#x20;           word1, word2 = word2, word1



&#x20;       m, n = len(word1), len(word2)

&#x20;       next_row = [n - j for j in range(n + 1)]



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           current = [0] \* (n + 1)

&#x20;           current[n] = m - i



&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if word1[i] == word2[j]:

&#x20;                   current[j] = next_row[j + 1]

&#x20;               else:

&#x20;                   current[j] = 1 + min(current[j + 1], next_row[j], next_row[j + 1])



&#x20;           next_row = current



&#x20;       return next_row[0]

\`\`\`



**\*\*Time:\*\*** O((m + 1) × (n + 1)) &#x20;

**\*\*Space:\*\*** O(min(m, n) + 1)



**### Important Pointers**



\- Allowed operations are **\*\*insert, delete, and replace\*\***.

\- Each operation costs \`1\`; matching characters cost \`0\`.

\- Insert: \`(i, j + 1)\`.

\- Delete: \`(i + 1, j)\`.

\- Replace: \`(i + 1, j + 1)\`.

\- If one string is exhausted, insert or delete all remaining characters.

\- For long strings, use iterative DP to avoid Python's recursion depth limit.



\---



**## LIS DP**



**## 24. Longest Increasing Subsequence — Length**



[LeetCode 300 — Longest Increasing Subsequence]\(https\://leetcode.com/problems/longest-increasing-subsequence/)



**\*\*Input:\*\*** nums = [10, 9, 2, 5, 3, 7, 101, 18] &#x20;

**\*\*Output:\*\*** 4



**\*\*Input:\*\*** nums = [7, 7, 7, 7] &#x20;

**\*\*Output:\*\*** 1



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def lengthOfLIS(self, nums):

&#x20;       @lru_cache(None)

&#x20;       def solve(i, previous):

&#x20;           if i == len(nums):

&#x20;               return 0



&#x20;           if previous == -1 or nums[i] > nums[previous]:

&#x20;               return max(solve(i + 1, previous), 1 + solve(i + 1, i))



&#x20;           return solve(i + 1, previous)



&#x20;       return solve(0, -1)

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n²)



**### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def lengthOfLIS(self, nums):

&#x20;       n = len(nums)

&#x20;       dp = [[0] \* (n + 1) for \_ in range(n + 1)]



&#x20;       for i in range(n - 1, -1, -1):

&#x20;           for previous in range(i - 1, -2, -1):

&#x20;               if previous == -1 or nums[i] > nums[previous]:

&#x20;                   dp[i][previous + 1] = max(dp[i + 1][previous + 1], 1 + dp[i + 1][i + 1])

&#x20;               else:

&#x20;                   dp[i][previous + 1] = dp[i + 1][previous + 1]



&#x20;       return dp[0][0]

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n²)



**### 1D DP**



\`\`\`python

class Solution:

&#x20;   def lengthOfLIS(self, nums):

&#x20;       dp = [1] \* len(nums)



&#x20;       for i in range(len(nums)):

&#x20;           for j in range(i):

&#x20;               if nums[j] < nums[i]:

&#x20;                   dp[i] = max(dp[i], 1 + dp[j])



&#x20;       return max(dp, default=0)

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n)



**### Binary Search**



\`\`\`python

from bisect import bisect_left



class Solution:

&#x20;   def lengthOfLIS(self, nums):

&#x20;       tails = []



&#x20;       for num in nums:

&#x20;           i = bisect_left(tails, num)



&#x20;           if i == len(tails):

&#x20;               tails.append(num)

&#x20;           else:

&#x20;               tails[i] = num



&#x20;       return len(tails)

\`\`\`



**\*\*Time:\*\*** O(n log n) &#x20;

**\*\*Space:\*\*** O(n)



**### Important Pointers**



\- The subsequence must be **\*\*strictly increasing\*\***; equal values do not extend it.

\- In 2D DP, \`previous + 1\` maps index \`-1\` to column \`0\`.

\- In 1D DP, \`dp[i]\` is the LIS length ending at index \`i\`.

\- The answer is the maximum DP value, not necessarily the last value.

\- \`bisect_left\` replaces the first tail greater than or equal to the current number.

\- The final \`tails\` list is not necessarily an actual subsequence.



\---



**## 25. Longest Increasing Subsequence — Printing**



[GeeksforGeeks — Printing Longest Increasing Subsequence]\(https\://www\.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1)



**\*\*Input:\*\*** nums = [10, 9, 2, 5, 3, 7, 101, 18] &#x20;

**\*\*Output:\*\*** [2, 5, 7, 101]



**\*\*Input:\*\*** nums = [7, 7, 7] &#x20;

**\*\*Output:\*\*** [7]



**### DP + Parent Tracking**



\`\`\`python

class Solution:

&#x20;   def printLIS(self, nums):

&#x20;       n = len(nums)



&#x20;       if n == 0:

&#x20;           return []



&#x20;       dp = [1] \* n

&#x20;       parent = list(range(n))

&#x20;       best_index = 0



&#x20;       for i in range(n):

&#x20;           for j in range(i):

&#x20;               if nums[j] < nums[i] and dp[j] + 1 > dp[i]:

&#x20;                   dp[i] = dp[j] + 1

&#x20;                   parent[i] = j



&#x20;           if dp[i] > dp[best_index]:

&#x20;               best_index = i



&#x20;       result = []



&#x20;       while parent[best_index] != best_index:

&#x20;           result.append(nums[best_index])

&#x20;           best_index = parent[best_index]



&#x20;       result.append(nums[best_index])

&#x20;       return result[::-1]

\`\`\`



**\*\*Time:\*\*** O(n²) &#x20;

**\*\*Space:\*\*** O(n)



**### Important Pointers**



\- \`parent[i]\` stores the previous index in the chosen subsequence ending at \`i\`.

\- Update the parent only when the LIS length improves.

\- Reconstruct from the index with the largest DP value, then reverse the result.

\- Multiple valid LIS results may exist; this returns one.

\- This does not guarantee a lexicographically smallest LIS.

\- The method returns a list; use \`print(result)\` if console output is required.



\---



**## Rectangles and Squares**



**## Largest Histogram Rectangle**



[LeetCode 84 — Largest Rectangle in Histogram]\(https\://leetcode.com/problems/largest-rectangle-in-histogram/)



**\*\*Input:\*\*** heights = [2, 1, 5, 6, 2, 3] &#x20;

**\*\*Output:\*\*** 10



**\*\*Input:\*\*** heights = [2, 4] &#x20;

**\*\*Output:\*\*** 4



**### Monotonic Stack**



\`\`\`python

class Solution:

&#x20;   def largestRectangleArea(self, heights):

&#x20;       stack = []

&#x20;       answer = 0

&#x20;       n = len(heights)



&#x20;       for i in range(n + 1):

&#x20;           current_height = heights[i] if i < n else 0



&#x20;           while stack and heights[stack[-1]] >= current_height:

&#x20;               height = heights[stack.pop()]

&#x20;               left = stack[-1] if stack else -1

&#x20;               answer = max(answer, height \* (i - left - 1))



&#x20;           if i < n:

&#x20;               stack.append(i)



&#x20;       return answer

\`\`\`



**\*\*Time:\*\*** O(n) &#x20;

**\*\*Space:\*\*** O(n)



**### Important Pointers**



\- Use a monotonic stack of indices with strictly increasing heights.

\- A shorter or equal bar triggers evaluation of bars popped from the stack.

\- After popping, \`i\` is the right boundary and the new stack top is the left boundary.

\- Rectangle width is \`i - left - 1\`.

\- The final virtual bar of height \`0\` processes remaining bars.

\- Every index is pushed and popped at most once.



\---



**## Maximal Rectangle of Ones**



[LeetCode 85 — Maximal Rectangle]\(https\://leetcode.com/problems/maximal-rectangle/)



**\*\*Input:\*\***

matrix = [

&#x20;   ["1", "0", "1", "0", "0"],

&#x20;   ["1", "0", "1", "1", "1"],

&#x20;   ["1", "1", "1", "1", "1"],

&#x20;   ["1", "0", "0", "1", "0"]

]



**\*\*Output:\*\*** 6



**### Histogram + Monotonic Stack**



\`\`\`python

class Solution:

&#x20;   def maximalRectangle(self, matrix):

&#x20;       if not matrix or not matrix[0]:

&#x20;           return 0



&#x20;       n = len(matrix[0])

&#x20;       heights = [0] \* n

&#x20;       answer = 0



&#x20;       for row in matrix:

&#x20;           for col in range(n):

&#x20;               heights[col] = heights[col] + 1 if row[col] == '1' else 0



&#x20;           stack = []



&#x20;           for i in range(n + 1):

&#x20;               current_height = heights[i] if i < n else 0



&#x20;               while stack and heights[stack[-1]] >= current_height:

&#x20;                   height = heights[stack.pop()]

&#x20;                   left = stack[-1] if stack else -1

&#x20;                   answer = max(answer, height \* (i - left - 1))



&#x20;               if i < n:

&#x20;                   stack.append(i)



&#x20;       return answer

\`\`\`



**\*\*Time:\*\*** O(rows × cols) &#x20;

**\*\*Space:\*\*** O(cols)



**### Important Pointers**



\- Each row becomes the bottom of a histogram.

\- A \`'1'\` increases the column height; a \`'0'\` resets it to zero.

\- Apply Largest Histogram Rectangle to every row.

\- Return the largest **\*\*area\*\***, not the height or width.

\- LeetCode supplies string cells. For integer cells, compare with \`1\`.



\---



**## Count All-One Squares**



[LeetCode 1277 — Count Square Submatrices with All Ones]\(https\://leetcode.com/problems/count-square-submatrices-with-all-ones/)



**\*\*Input:\*\***

matrix = [

&#x20;   [0, 1, 1, 1],

&#x20;   [1, 1, 1, 1],

&#x20;   [0, 1, 1, 1]

]



**\*\*Output:\*\*** 15



**### Recursion + Memo**



\`\`\`python

from functools import lru_cache



class Solution:

&#x20;   def countSquares(self, matrix):

&#x20;       if not matrix or not matrix[0]:

&#x20;           return 0



&#x20;       m, n = len(matrix), len(matrix[0])



&#x20;       @lru_cache(None)

&#x20;       def solve(i, j):

&#x20;           if i == m or j == n or matrix[i][j] == 0:

&#x20;               return 0



&#x20;           return 1 + min(solve(i + 1, j), solve(i, j + 1), solve(i + 1, j + 1))



&#x20;       return sum(solve(i, j) for i in range(m) for j in range(n))

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(m × n + m + n)



**### Full 2D DP**



\`\`\`python

class Solution:

&#x20;   def countSquares(self, matrix):

&#x20;       if not matrix or not matrix[0]:

&#x20;           return 0



&#x20;       m, n = len(matrix), len(matrix[0])

&#x20;       dp = [[0] \* (n + 1) for \_ in range(m + 1)]

&#x20;       answer = 0



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if matrix[i][j] == 1:

&#x20;                   dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

&#x20;                   answer += dp[i][j]



&#x20;       return answer

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O((m + 1) × (n + 1))



**### Space-optimized DP**



\`\`\`python

class Solution:

&#x20;   def countSquares(self, matrix):

&#x20;       if not matrix or not matrix[0]:

&#x20;           return 0



&#x20;       m, n = len(matrix), len(matrix[0])

&#x20;       next_row = [0] \* (n + 1)

&#x20;       answer = 0



&#x20;       for i in range(m - 1, -1, -1):

&#x20;           current = [0] \* (n + 1)



&#x20;           for j in range(n - 1, -1, -1):

&#x20;               if matrix[i][j] == 1:

&#x20;                   current[j] = 1 + min(next_row[j], current[j + 1], next_row[j + 1])

&#x20;                   answer += current[j]



&#x20;           next_row = current



&#x20;       return answer

\`\`\`



**\*\*Time:\*\*** O(m × n) &#x20;

**\*\*Space:\*\*** O(n)



**### Important Pointers**



\- Cells are integers \`0\` and \`1\`.

\- Each state stores the largest all-one square starting at that cell.

\- Use the minimum of the right, down, and diagonal states to extend a square.

\- A state value of \`3\` contributes three squares: sizes \`1 × 1\`, \`2 × 2\`, and \`3 × 3\`.

\- Sum all state values to count every square.

\- Taking only the maximum state finds the largest square's side length, not the total count.

---

## Additional Core DP Problems

The following 14 additions complete the 29-question core learning checklist. Each code block is independent.

## 29. Climbing Stairs

**Pattern:** Linear DP

Count the ways to climb n stairs using steps of size 1 or 2. To reach a stair, add the ways to reach the previous two stairs.

**Example:** n = 5 → 8

**State:** dp[i] = number of ways to reach stair i; dp[i] = dp[i - 1] + dp[i - 2].

### Bottom-Up DP

```python
class Solution:
    def climbStairs(self, n):
        dp = [0] * (n + 2)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

**Time:** O(n)  
**Space:** O(n)

### Important Pointers

- The empty climb has one way; this makes the recurrence work for the first two stairs.
- Only two previous values are needed, so auxiliary space can be reduced to O(1).

## 30. Maximum Subarray

**Pattern:** Subarray DP / Kadane

Find the largest sum of a nonempty contiguous subarray. At each number, either start a new subarray or extend the best subarray ending just before it.

**Example:** nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6

**State:** ending = maximum sum of a nonempty subarray ending at the current index.

### Bottom-Up DP

```python
class Solution:
    def maxSubArray(self, nums):
        ending = answer = nums[0]
        for i in range(1, len(nums)):
            ending = max(nums[i], ending + nums[i])
            answer = max(answer, ending)
        return answer
```

**Time:** O(n)  
**Space:** O(1)

### Important Pointers

- Input is nonempty. Initialize with nums[0] so all-negative inputs return the largest element.
- The answer can end anywhere; track the maximum over all ending states.

## 31. Maximum Product Subarray

**Pattern:** Subarray DP

Find the largest product of a nonempty contiguous subarray. Track both the largest and smallest products ending at each index because a negative number can swap their roles.

**Example:** nums = [2, 3, -2, 4] → 6

**State:** high and low = maximum and minimum products of subarrays ending at the current index.

### Bottom-Up DP

```python
class Solution:
    def maxProduct(self, nums):
        high = low = answer = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            a, b = high * x, low * x
            high = max(x, a, b)
            low = min(x, a, b)
            answer = max(answer, high)
        return answer
```

**Time:** O(n)  
**Space:** O(1)

### Important Pointers

- Compute both candidates from the previous high and low before updating either state.
- Zero is handled naturally. Java code assumes candidate products fit in int; use wider arithmetic for larger custom inputs.

## 32. Minimum Path Sum

**Pattern:** Grid DP

Find the minimum sum along a path from the top-left cell to the bottom-right cell, moving only right or down. Add the current cell to the cheaper of the two predecessor paths.

**Example:** grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]] → 7

**State:** dp[r][c] = minimum path sum from the top-left cell to (r, c).

### Bottom-Up DP

```python
class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                above = dp[r - 1][c] if r > 0 else float('inf')
                left = dp[r][c - 1] if c > 0 else float('inf')
                dp[r][c] = grid[r][c] + min(above, left)
        return dp[-1][-1]
```

**Time:** O(m × n)  
**Space:** O(m × n)

### Important Pointers

- The first row and first column each have only one predecessor.
- A rolling row reduces space to O(n). These versions preserve the input grid.

## 33. Distinct Subsequences

**Pattern:** Two-String DP

Count the subsequences of s that equal t. Skip the current source character, or use it when it matches the current target character.

**Example:** s = "rabbbit", t = "rabbit" → 3

**State:** dp[i][j] = ways to form t[j:] from s[i:].

### Bottom-Up DP

```python
class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]
```

**Time:** O(m × n) arithmetic operations  
**Space:** O((m + 1) × (n + 1)) DP entries

### Important Pointers

- An empty target has one matching subsequence; an empty source cannot form a nonempty target.
- Counts at intermediate states may be large. Java uses BigInteger and returns int under the standard final-answer constraint. Python integers also grow as needed; big-integer arithmetic adds a bit-length cost.

## 34. Palindrome Partitioning II — Minimum Cuts

**Pattern:** Palindrome / Partition DP

Split a string into palindromic substrings using as few cuts as possible. Precompute which intervals are palindromes, then choose the last palindrome of each prefix.

**Example:** s = "aab" → 1

**State:** pal[i][j] marks a palindrome; cuts[end] = minimum cuts for s[:end + 1].

### Bottom-Up DP

```python
class Solution:
    def minCut(self, s):
        n = len(s)
        if n == 0:
            return 0
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])
        cuts = list(range(n))
        for end in range(n):
            for start in range(end + 1):
                if pal[start][end]:
                    cuts[end] = min(cuts[end], 0 if start == 0 else cuts[start - 1] + 1)
        return cuts[-1]
```

**Time:** O(n²)  
**Space:** O(n²)

### Important Pointers

- A palindrome covering the entire prefix needs zero cuts.
- Count cuts, not pieces. A partition with k nonempty pieces has k - 1 cuts.

## 35. Word Break

**Pattern:** Prefix / Partition DP

Decide whether a string can be split into dictionary words. A prefix is reachable when an earlier reachable prefix is followed by a dictionary word.

**Example:** s = "leetcode", wordDict = ["leet", "code"] → true

**State:** dp[end] = whether s[:end] can be segmented.

### Bottom-Up DP

```python
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in words:
                    dp[end] = True
                    break
        return dp[n]
```

**Time:** O(n³ + D) worst case, including substring creation and hashing; D = total dictionary characters  
**Space:** O(n + D)

### Important Pointers

- Dictionary words may be reused. Greedily taking the longest matching word is not sufficient.
- There are O(n²) transitions, but slicing and hashing are not constant-time in these implementations. A trie can avoid repeated substring creation.

## 36. Number of Longest Increasing Subsequences

**Pattern:** LIS / Sequence DP

Count how many strictly increasing subsequences achieve the maximum length. Track both the best length and the number of ways ending at each index.

**Example:** nums = [1, 3, 5, 4, 7] → 2

**State:** length[i] and count[i] = best length ending at i and number of subsequences attaining it.

### Bottom-Up DP

```python
class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    candidate = length[j] + 1
                    if candidate > length[i]:
                        length[i], count[i] = candidate, count[j]
                    elif candidate == length[i]:
                        count[i] += count[j]
        best = max(length)
        return sum(count[i] for i in range(n) if length[i] == best)
```

**Time:** O(n²)  
**Space:** O(n)

### Important Pointers

- Replace the count when a longer subsequence is found; add counts when the same best length is found.
- Subsequences are distinguished by indices. Equal values do not extend an increasing subsequence. Java counts must fit long and the returned answer must fit int.

## 37. Matrix Chain Multiplication

**Pattern:** Interval DP

Choose how to parenthesize a chain of matrices to minimize scalar multiplications. Try every final split of each interval and combine the two optimal subchains.

**Example:** dims = [40, 20, 30, 10, 30] → 26000

**State:** dp[i][j] = minimum cost to multiply matrices i through j; matrix i has dimensions dims[i - 1] × dims[i].

### Bottom-Up DP

```python
class Solution:
    def matrixMultiplication(self, dims):
        n = len(dims) - 1
        if n <= 1:
            return 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for size in range(2, n + 1):
            for i in range(1, n - size + 2):
                j = i + size - 1
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                               for k in range(i, j))
        return dp[1][n]
```

**Time:** O(n³), n = number of matrices  
**Space:** O(n²)

### Important Pointers

- Multiplying an a × b matrix by a b × c matrix costs a × b × c scalar multiplications.
- A single matrix has zero multiplication cost. Dimensions are positive; Java costs must fit long.

## 38. Burst Balloons

**Pattern:** Interval DP

Burst all balloons to maximize coins. For each interval, choose which balloon is burst last so the two outside neighbors are fixed.

**Example:** nums = [3, 1, 5, 8] → 167

**State:** dp[left][right] = maximum coins from bursting every balloon strictly between left and right.

### Bottom-Up DP

```python
class Solution:
    def maxCoins(self, nums):
        values = [1] + nums + [1]
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                for last in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], dp[left][last] + dp[last][right]
                                          + values[left] * values[last] * values[right])
        return dp[0][-1]
```

**Time:** O(n³), n = original balloon count  
**Space:** O(n²)

### Important Pointers

- Choosing the last balloon makes the left and right subproblems independent.
- Pad the array with 1 on both sides. Inputs are nonnegative; Java totals must fit int.

## 39. House Robber III

**Pattern:** Tree DP

Maximize the value robbed from a binary tree without taking both a parent and its child. Return two answers from each subtree: taking its root and skipping its root.

**Example:** root = [3, 2, 3, null, 3, null, 1] → 7

**State:** For each node, take = node value + both child skip states; skip = best state from each child.

### Postorder Tree DP

```python
# TreeNode is supplied by the platform.
class Solution:
    def rob(self, root):
        def solve(node):
            if node is None:
                return 0, 0
            left_take, left_skip = solve(node.left)
            right_take, right_skip = solve(node.right)
            take = node.val + left_skip + right_skip
            skip = max(left_take, left_skip) + max(right_take, right_skip)
            return take, skip
        return max(solve(root))
```

**Time:** O(n)  
**Space:** O(h), h = tree height

### Important Pointers

- This is postorder tree DP. Each subtree is processed once, so a memo dictionary is unnecessary.
- If you skip a node, each child may independently be taken or skipped. Tree examples use level-order notation.

## 40. Binary Tree Maximum Path Sum

**Pattern:** Tree DP

Find the largest sum of a nonempty path in a binary tree. At each node, evaluate a path joining both child branches, but return only one branch to the parent.

**Example:** root = [-10, 9, 20, null, null, 15, 7] → 42

**State:** gain(node) = maximum sum of a downward path starting at node; answer also considers joining two branches at node.

### Postorder Tree DP

```python
# TreeNode is supplied by the platform.
class Solution:
    def maxPathSum(self, root):
        answer = float('-inf')
        def gain(node):
            nonlocal answer
            if node is None:
                return 0
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))
            answer = max(answer, node.val + left + right)
            return node.val + max(left, right)
        gain(root)
        return answer
```

**Time:** O(n)  
**Space:** O(h), h = tree height

### Important Pointers

- The input tree is nonempty. Initialize the answer below every node value for all-negative trees.
- A path returned to the parent cannot include both child branches. Recursion depth can reach n in a skewed tree.

## 41. Assignment Problem — Minimum Cost, Small N

**Pattern:** Bitmask DP

Assign n workers to n jobs, one job per worker, minimizing total cost. A mask records the jobs already assigned; its set-bit count identifies the next worker.

**Example:** cost = [[9, 2, 7], [6, 4, 3], [5, 8, 1]] → 9

**State:** dp[mask] = minimum cost to assign the first popcount(mask) workers to exactly the jobs in mask.

### Bottom-Up DP

```python
class Solution:
    def minAssignmentCost(self, cost):
        n = len(cost)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            worker = mask.bit_count()
            if worker == n:
                continue
            for job in range(n):
                if mask & (1 << job) == 0:
                    next_mask = mask | (1 << job)
                    dp[next_mask] = min(dp[next_mask], dp[mask] + cost[worker][job])
        return dp[-1]
```

**Time:** O(n × 2ⁿ)  
**Space:** O(2ⁿ)

### Important Pointers

- The cost matrix is square and every assignment is allowed; all masks are reachable.
- Use only for small n, typically around 20 or less. Java bit shifts require n < 31, and memory becomes limiting much earlier.

## 42. Predict the Winner

**Pattern:** Game / Minimax DP

Two players take a number from either end of an array and play optimally. Track the best score advantage the current player can secure from each interval.

**Example:** nums = [1, 5, 2] → false

**State:** dp[left][right] = best current-player score minus opponent score on nums[left:right + 1].

### Bottom-Up DP

```python
class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        if n == 0:
            return True
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for size in range(2, n + 1):
            for left in range(n - size + 1):
                right = left + size - 1
                dp[left][right] = max(nums[left] - dp[left + 1][right],
                                      nums[right] - dp[left][right - 1])
        return dp[0][-1] >= 0
```

**Time:** O(n²)  
**Space:** O(n²)

### Important Pointers

- Subtract the next player’s best advantage because the roles switch after each turn.
- A tie counts as a win for player one. Java differences must fit int.
