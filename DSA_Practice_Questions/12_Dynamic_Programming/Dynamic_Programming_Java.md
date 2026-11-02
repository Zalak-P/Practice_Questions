# Dynamic Programming — Java

Each Java block is an independent `Solution` class. Copy one block at a time. Java 8+ syntax is used.

Counting helpers use `long` where appropriate; counts must fit in 64 bits. Apply a modulus only when required by the problem. Recursion can overflow the Java stack on large inputs.

## 1. House Robber I

[Problem link](https://leetcode.com/problems/house-robber/)

**Input:** nums = [2, 7, 9, 3, 1]  
**Output:** 12

**Important pointers:** Amounts are nonnegative. For circular houses, solve two ranges excluding either endpoint.

### Recursion + Memo

```java
class Solution {
    public int rob(int[] nums) {
        return range(nums, 0, nums.length - 1);
    }

    private int range(int[] nums, int start, int end) {
        return solve(nums, start, end, new Integer[nums.length]);
    }
    private int solve(int[] nums, int i, int end, Integer[] memo) {
        if (i > end) return 0;
        if (memo[i] != null) return memo[i];
        return memo[i] = Math.max(solve(nums, i + 1, end, memo), nums[i] + solve(nums, i + 2, end, memo));
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Bottom-Up DP

```java
class Solution {
    public int rob(int[] nums) {
        return range(nums, 0, nums.length - 1);
    }

    private int range(int[] nums, int start, int end) {
        int[] dp = new int[nums.length + 2];
        for (int i = end; i >= start; i--) {
            dp[i] = Math.max(dp[i + 1], nums[i] + dp[i + 2]);
        }
        return dp[start];
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Constant Space

```java
class Solution {
    public int rob(int[] nums) {
        return range(nums, 0, nums.length - 1);
    }

    private int range(int[] nums, int start, int end) {
        int prev2 = 0, prev1 = 0;
        for (int i = start; i <= end; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## 2. House Robber II

[Problem link](https://leetcode.com/problems/house-robber-ii/)

**Input:** nums = [2, 3, 2]  
**Output:** 3

**Important pointers:** Amounts are nonnegative. For circular houses, solve two ranges excluding either endpoint.

### Recursion + Memo

```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        return Math.max(range(nums, 0, nums.length - 2), range(nums, 1, nums.length - 1));
    }

    private int range(int[] nums, int start, int end) {
        return solve(nums, start, end, new Integer[nums.length]);
    }
    private int solve(int[] nums, int i, int end, Integer[] memo) {
        if (i > end) return 0;
        if (memo[i] != null) return memo[i];
        return memo[i] = Math.max(solve(nums, i + 1, end, memo), nums[i] + solve(nums, i + 2, end, memo));
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Bottom-Up DP

```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        return Math.max(range(nums, 0, nums.length - 2), range(nums, 1, nums.length - 1));
    }

    private int range(int[] nums, int start, int end) {
        int[] dp = new int[nums.length + 2];
        for (int i = end; i >= start; i--) {
            dp[i] = Math.max(dp[i + 1], nums[i] + dp[i + 2]);
        }
        return dp[start];
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Constant Space

```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        return Math.max(range(nums, 0, nums.length - 2), range(nums, 1, nums.length - 1));
    }

    private int range(int[] nums, int start, int end) {
        int prev2 = 0, prev1 = 0;
        for (int i = start; i <= end; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## 3. Frog Jump

[Problem link](https://www.geeksforgeeks.org/problems/geek-jump/1)

**Input:** height = [10, 20, 30, 10]  
**Output:** 20

**Important pointers:** Jump one or two positions. A jump costs the absolute height difference.

### Constant Space

```java
class Solution {
    public int minCost(int[] height) {
        int prev2 = 0, prev1 = 0;
        for (int i = 1; i < height.length; i++) {
            int one = prev1 + Math.abs(height[i] - height[i - 1]);
            int two = i > 1 ? prev2 + Math.abs(height[i] - height[i - 2]) : Integer.MAX_VALUE;
            int current = Math.min(one, two);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## 4. Frog Jump with X Distance

[Problem link](https://www.geeksforgeeks.org/problems/minimal-cost/1)

**Input:** x = 3, height = [10, 30, 40, 50, 20]  
**Output:** 30

**Important pointers:** Jump 1 through x positions; x must be at least 1.

### Bottom-Up DP

```java
class Solution {
    public int minimizeCost(int x, int[] height) {
        int n = height.length;
        if (n == 0) return 0;
        int[] dp = new int[n];
        for (int i = 1; i < n; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int jump = 1; jump <= Math.min(x, i); jump++) {
                dp[i] = Math.min(dp[i], dp[i - jump] + Math.abs(height[i] - height[i - jump]));
            }
        }
        return dp[n - 1];
    }
}
```

**Time:** O(n × min(x, n))  
**Space:** O(n)

## 5. Decode Ways

[Problem link](https://leetcode.com/problems/decode-ways/)

**Input:** s = "226"  
**Output:** 3

**Important pointers:** A zero cannot be decoded alone. Valid two-digit codes range from 10 through 26. Input is a nonempty digit string.

### Recursion + Memo

```java
class Solution {
    public int numDecodings(String s) {
        return solve(0, s, new Integer[s.length()]);
    }
    private int solve(int i, String s, Integer[] memo) {
        if (i == s.length()) return 1;
        if (s.charAt(i) == '0') return 0;
        if (memo[i] != null) return memo[i];
        int answer = solve(i + 1, s, memo);
        if (i + 1 < s.length() && Integer.parseInt(s.substring(i, i + 2)) <= 26) {
            answer += solve(i + 2, s, memo);
        }
        return memo[i] = answer;
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Bottom-Up DP

```java
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '0') continue;
            dp[i] = dp[i + 1];
            if (i + 1 < n && Integer.parseInt(s.substring(i, i + 2)) <= 26) dp[i] += dp[i + 2];
        }
        return dp[0];
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Constant Space

```java
class Solution {
    public int numDecodings(String s) {
        int next1 = 1, next2 = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            int current = s.charAt(i) == '0' ? 0 : next1;
            if (s.charAt(i) != '0' && i + 1 < s.length() && Integer.parseInt(s.substring(i, i + 2)) <= 26) current += next2;
            next2 = next1;
            next1 = current;
        }
        return next1;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## Grid DP

## 6. Unique Paths I

[Problem link](https://leetcode.com/problems/unique-paths/)

**Input:** m = 3, n = 7  
**Output:** 28

**Important pointers:** Move only right or down. Grid dimensions are positive.

### Full 2D DP

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = i == 0 || j == 0 ? 1 : dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
}
```

**Time:** O(m × n)  
**Space:** O(m × n)

### Space-optimized DP

```java
import java.util.Arrays;
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) dp[j] = dp[j] + dp[j - 1];
        }
        return dp[n - 1];
    }
}
```

**Time:** O(m × n)  
**Space:** O(n)

### Constant-space Math

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int moves = m + n - 2, k = Math.min(m - 1, n - 1);
        long result = 1;
        for (int i = 1; i <= k; i++) result = result * (moves - i + 1) / i;
        return (int) result;
    }
}
```

**Time:** O(min(m, n))  
**Space:** O(1)

The math version uses combinatorics, not DP. These `int` APIs follow the standard constraint that the answer fits a signed 32-bit integer.

## 7. Unique Paths II

[Problem link](https://leetcode.com/problems/unique-paths-ii/)

**Input:** obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]  
**Output:** 2

**Important pointers:** 1 means obstacle; 0 means open. The in-place version modifies the input. The grid is nonempty.

### Full 2D DP

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) continue;
                if (i == 0 && j == 0) dp[i][j] = 1;
                else dp[i][j] = (i > 0 ? dp[i - 1][j] : 0) + (j > 0 ? dp[i][j - 1] : 0);
            }
        }
        return dp[m - 1][n - 1];
    }
}
```

**Time:** O(m × n)  
**Space:** O(m × n)

### Space-optimized DP

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int[] dp = new int[grid[0].length];
        dp[0] = 1;
        for (int[] row : grid) {
            for (int j = 0; j < row.length; j++) {
                if (row[j] == 1) dp[j] = 0;
                else if (j > 0) dp[j] += dp[j - 1];
            }
        }
        return dp[dp.length - 1];
    }
}
```

**Time:** O(m × n)  
**Space:** O(n)

### Constant Extra Space — In-place DP

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) grid[i][j] = 0;
                else if (i == 0 && j == 0) grid[i][j] = 1;
                else grid[i][j] = (i > 0 ? grid[i - 1][j] : 0) + (j > 0 ? grid[i][j - 1] : 0);
            }
        }
        return grid[m - 1][n - 1];
    }
}
```

**Time:** O(m × n)  
**Space:** O(1)

## Subsequence and Knapsack DP

## 8. Subset Sum to Target

[Problem link](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1)

**Input:** arr = [3, 34, 4, 12, 5, 2], target = 9  
**Output:** true

**Important pointers:** Each element is used at most once. Values and target are nonnegative; iterate sums backward in 1D DP.

### Recursion + Memo

```java
class Solution {
    public boolean isSubsetSum(int[] arr, int target) {
        return solve(arr, 0, target, new Boolean[arr.length][target + 1]);
    }
    private boolean solve(int[] arr, int i, int remaining, Boolean[][] memo) {
        if (remaining == 0) return true;
        if (i == arr.length) return false;
        if (memo[i][remaining] != null) return memo[i][remaining];
        return memo[i][remaining] = solve(arr, i + 1, remaining, memo) || (arr[i] <= remaining && solve(arr, i + 1, remaining - arr[i], memo));
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(n × (target + 1))

### Full 2D DP

```java
class Solution {
    public boolean isSubsetSum(int[] arr, int target) {

        boolean[][] dp = new boolean[arr.length + 1][target + 1];
        for (int i = 0; i <= arr.length; i++) dp[i][0] = true;
        for (int i = 1; i <= arr.length; i++) {
            for (int s = 1; s <= target; s++) {
                dp[i][s] = dp[i - 1][s] || (arr[i - 1] <= s && dp[i - 1][s - arr[i - 1]]);
            }
        }
        return dp[arr.length][target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O((n + 1) × (target + 1))

### Space-optimized DP

```java
class Solution {
    public boolean isSubsetSum(int[] arr, int target) {

        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : arr) {
            for (int s = target; s >= num; s--) dp[s] = dp[s] || dp[s - num];
        }
        return dp[target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 9. Equal Subset Partition

[Problem link](https://leetcode.com/problems/partition-equal-subset-sum/)

**Input:** nums = [1, 5, 11, 5]  
**Output:** true

**Important pointers:** Each element is used at most once. Values and target are nonnegative; iterate sums backward in 1D DP.

### Recursion + Memo

```java
class Solution {
    public boolean canPartition(int[] arr) {
        int total = 0;
        for (int num : arr) total += num;
        if (total % 2 != 0) return false;
        int target = total / 2;
        return solve(arr, 0, target, new Boolean[arr.length][target + 1]);
    }
    private boolean solve(int[] arr, int i, int remaining, Boolean[][] memo) {
        if (remaining == 0) return true;
        if (i == arr.length) return false;
        if (memo[i][remaining] != null) return memo[i][remaining];
        return memo[i][remaining] = solve(arr, i + 1, remaining, memo) || (arr[i] <= remaining && solve(arr, i + 1, remaining - arr[i], memo));
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(n × (target + 1))

### Full 2D DP

```java
class Solution {
    public boolean canPartition(int[] arr) {
        int total = 0;
        for (int num : arr) total += num;
        if (total % 2 != 0) return false;
        int target = total / 2;

        boolean[][] dp = new boolean[arr.length + 1][target + 1];
        for (int i = 0; i <= arr.length; i++) dp[i][0] = true;
        for (int i = 1; i <= arr.length; i++) {
            for (int s = 1; s <= target; s++) {
                dp[i][s] = dp[i - 1][s] || (arr[i - 1] <= s && dp[i - 1][s - arr[i - 1]]);
            }
        }
        return dp[arr.length][target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O((n + 1) × (target + 1))

### Space-optimized DP

```java
class Solution {
    public boolean canPartition(int[] arr) {
        int total = 0;
        for (int num : arr) total += num;
        if (total % 2 != 0) return false;
        int target = total / 2;

        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : arr) {
            for (int s = target; s >= num; s--) dp[s] = dp[s] || dp[s - num];
        }
        return dp[target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 10. Minimum Partition Difference

[Problem link](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1)

**Input:** arr = [1, 6, 11, 5]  
**Output:** 1

**Important pointers:** Nonnegative values; subset sizes may differ. Find the largest reachable sum at most total / 2. This is not LeetCode 2035, which requires equal-sized subsets and permits negative values.

### Space-optimized DP

```java
class Solution {
    public int minDifference(int[] arr) {
        int total = 0;
        for (int num : arr) total += num;
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : arr) {
            for (int s = target; s >= num; s--) dp[s] = dp[s] || dp[s - num];
        }
        for (int s = target; s >= 0; s--) {
            if (dp[s]) return total - 2 * s;
        }
        return 0;
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 11. Count Subsets with Sum K

[Problem link](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1)

**Input:** nums = [0, 0, 1], k = 1  
**Output:** 4

**Important pointers:** Nonnegative array values. Each index is a separate choice. Zeros double the count. Iterate sums backward. For difference partitions, d ≥ 0 and the subsets are labeled.

### Space-optimized DP

```java
class Solution {
    public long countSubsets(int[] nums, int k) {
        int target = k;
        long[] dp = new long[target + 1];
        dp[0] = 1;
        for (int num : nums) {
            for (int s = target; s >= num; s--) dp[s] += dp[s - num];
        }
        return dp[target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 12. Count Partitions with Difference

[Problem link](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1)

**Input:** nums = [5, 2, 6, 4], d = 3  
**Output:** 1

**Important pointers:** Nonnegative array values. Each index is a separate choice. Zeros double the count. Iterate sums backward. For difference partitions, d ≥ 0 and the subsets are labeled.

### Space-optimized DP

```java
class Solution {
    public long countPartitions(int[] nums, int d) {
        int total = 0;
        for (int num : nums) total += num;
        if (total < d || (total - d) % 2 != 0) return 0;
        int target = (total - d) / 2;
        long[] dp = new long[target + 1];
        dp[0] = 1;
        for (int num : nums) {
            for (int s = target; s >= num; s--) dp[s] += dp[s - num];
        }
        return dp[target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 13. Target Sum

[Problem link](https://leetcode.com/problems/target-sum/)

**Input:** nums = [1, 1, 1, 1, 1], target = 3  
**Output:** 5

**Important pointers:** Nonnegative array values. Each index is a separate choice. Zeros double the count. Iterate sums backward. For difference partitions, d ≥ 0 and the subsets are labeled.

### Space-optimized DP

```java
class Solution {
    public int findTargetSumWays(int[] nums, int goal) {
        int total = 0;
        for (int num : nums) total += num;
        if (Math.abs((long) goal) > total || (total + goal) % 2 != 0) return 0;
        int target = (total + goal) / 2;
        long[] dp = new long[target + 1];
        dp[0] = 1;
        for (int num : nums) {
            for (int s = target; s >= num; s--) dp[s] += dp[s - num];
        }
        return (int) dp[target];
    }
}
```

**Time:** O(n × (target + 1))  
**Space:** O(target + 1)

## 14. Minimum Coins

[Problem link](https://leetcode.com/problems/coin-change/)

**Input:** coins = [1, 2, 5], amount = 11  
**Output:** 3

**Input:** coins = [2], amount = 3  
**Output:** -1

**Important pointers:** Positive denominations can be reused. Minimize the coin count. Return -1 if unreachable. Forward sums permit reuse.

### Recursion + Memo

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int answer = solve(coins, 0, amount, new Integer[coins.length][amount + 1], amount + 1);
        return answer > amount ? -1 : answer;
    }
    private int solve(int[] coins, int i, int remaining, Integer[][] memo, int inf) {
        if (remaining == 0) return 0;
        if (i == coins.length) return inf;
        if (memo[i][remaining] != null) return memo[i][remaining];
        int take = coins[i] <= remaining ? 1 + solve(coins, i, remaining - coins[i], memo, inf) : inf;
        return memo[i][remaining] = Math.min(solve(coins, i + 1, remaining, memo, inf), take);
    }
}
```

**Time:** O(n × (amount + 1))  
**Space:** O(n × (amount + 1) + n + amount)

### Full 2D DP

```java
import java.util.Arrays;
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[][] dp = new int[coins.length + 1][amount + 1];
        for (int[] row : dp) Arrays.fill(row, amount + 1);
        for (int i = 0; i <= coins.length; i++) dp[i][0] = 0;
        for (int i = 1; i <= coins.length; i++) {
            for (int s = 1; s <= amount; s++) {
                dp[i][s] = Math.min(dp[i - 1][s], coins[i - 1] <= s ? 1 + dp[i][s - coins[i - 1]] : amount + 1);
            }
        }
        return dp[coins.length][amount] > amount ? -1 : dp[coins.length][amount];
    }
}
```

**Time:** O(n × (amount + 1))  
**Space:** O((n + 1) × (amount + 1))

### Space-optimized DP

```java
import java.util.Arrays;
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int total = 1; total <= amount; total++) {
            for (int coin : coins) {
                if (coin <= total) dp[total] = Math.min(dp[total], 1 + dp[total - coin]);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

**Time:** O(n × (amount + 1))  
**Space:** O(amount + 1)

## 15. Coin Change II

[Problem link](https://leetcode.com/problems/coin-change-ii/)

**Input:** amount = 5, coins = [1, 2, 5]  
**Output:** 4

**Important pointers:** Count combinations, not ordered sequences. Denominations are distinct and positive. Coin loop outside; amount loop forward. Amount 0 has one combination.

### Space-optimized DP

```java
class Solution {
    public int change(int amount, int[] coins) {
        long[] dp = new long[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int total = coin; total <= amount; total++) dp[total] += dp[total - coin];
        }
        return (int) dp[amount];
    }
}
```

**Time:** O(n × (amount + 1))  
**Space:** O(amount + 1)

## 16. Unbounded Knapsack

[Problem link](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)

**Input:** val = [10,40,50,70], wt = [1,3,4,5], capacity = 8  
**Output:** 110

**Important pointers:** Weights are positive. Reuse items without limit. Filling capacity exactly is not required.

### Recursion + Memo

```java
class Solution {
    public int knapSack(int[] val, int[] wt, int capacity) {
        return solve(val, wt, 0, capacity, new Integer[wt.length][capacity + 1]);
    }
    private int solve(int[] val, int[] wt, int i, int remaining, Integer[][] memo) {
        if (i == wt.length || remaining == 0) return 0;
        if (memo[i][remaining] != null) return memo[i][remaining];
        int take = wt[i] <= remaining ? val[i] + solve(val, wt, i, remaining - wt[i], memo) : 0;
        return memo[i][remaining] = Math.max(solve(val, wt, i + 1, remaining, memo), take);
    }
}
```

**Time:** O(n × (capacity + 1))  
**Space:** O(n × (capacity + 1) + n + capacity)

### Full 2D DP

```java
class Solution {
    public int knapSack(int[] val, int[] wt, int capacity) {
        int[][] dp = new int[wt.length + 1][capacity + 1];
        for (int i = 1; i <= wt.length; i++) {
            for (int cap = 1; cap <= capacity; cap++) {
                dp[i][cap] = Math.max(dp[i - 1][cap], wt[i - 1] <= cap ? val[i - 1] + dp[i][cap - wt[i - 1]] : 0);
            }
        }
        return dp[wt.length][capacity];
    }
}
```

**Time:** O(n × (capacity + 1))  
**Space:** O((n + 1) × (capacity + 1))

### Space-optimized DP

```java
class Solution {
    public int knapSack(int[] val, int[] wt, int capacity) {
        int[] dp = new int[capacity + 1];
        for (int i = 0; i < wt.length; i++) {
            for (int cap = wt[i]; cap <= capacity; cap++) dp[cap] = Math.max(dp[cap], val[i] + dp[cap - wt[i]]);
        }
        return dp[capacity];
    }
}
```

**Time:** O(n × (capacity + 1))  
**Space:** O(capacity + 1)

## 17. Rod Cutting

[Problem link](https://www.geeksforgeeks.org/problems/rod-cutting0840/1)

**Input:** price = [1,5,8,9,10,17,17,20]  
**Output:** 22

**Important pointers:** Rod length is price.length. price[length - 1] is the price of that piece length. Use the whole rod; lengths may repeat. Prices are nonnegative.

### Space-optimized DP

```java
class Solution {
    public int cutRod(int[] price) {
        int n = price.length;
        int[] dp = new int[n + 1];
        for (int length = 1; length <= n; length++) {
            for (int remaining = length; remaining <= n; remaining++) dp[remaining] = Math.max(dp[remaining], price[length - 1] + dp[remaining - length]);
        }
        return dp[n];
    }
}
```

**Time:** O(n²)  
**Space:** O(n)

## 18. Buy and Sell Stock I, II, III, IV, V

## Stock I — One Transaction

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Input:** prices = [7,1,5,3,6,4]  
**Output:** 5

### Constant Space

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minimumPrice = Integer.MAX_VALUE, profit = 0;
        for (int price : prices) {
            minimumPrice = Math.min(minimumPrice, price);
            profit = Math.max(profit, price - minimumPrice);
        }
        return profit;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## Stock II — Unlimited Transactions

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

**Input → Output:** prices = [7,1,5,3,6,4] → 7

**Important pointers:** Hold at most one share. Selling completes a transaction. Stock V here means one-day cooldown: selling moves to i + 2. Invalid terminal holding states use a safe negative sentinel.

### Recursion + Memo

```java
class Solution {
    private static final int NEG = Integer.MIN_VALUE / 4;
    public int maxProfit(int[] prices) {
        return solve(prices, 0, 0, new Integer[prices.length][2]);
    }
    private int solve(int[] p, int i, int holding, Integer[][] memo) {
        if (i >= p.length) return holding == 1 ? NEG : 0;
        if (memo[i][holding] != null) return memo[i][holding];
        if (holding == 1) return memo[i][holding] = Math.max(solve(p, i + 1, 1, memo), p[i] + solve(p, i + 1, 0, memo));
        return memo[i][holding] = Math.max(solve(p, i + 1, 0, memo), -p[i] + solve(p, i + 1, 1, memo));
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Full 2D DP

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n + 2][2];
        for (int[] row : dp) row[1] = Integer.MIN_VALUE / 4;
        for (int i = n - 1; i >= 0; i--) {
            dp[i][0] = Math.max(dp[i + 1][0], -prices[i] + dp[i + 1][1]);
            dp[i][1] = Math.max(dp[i + 1][1], prices[i] + dp[i + 1][0]);
        }
        return dp[0][0];
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Space-optimized DP

```java
class Solution {
    public int maxProfit(int[] prices) {
        int nextFree = 0, nextHolding = Integer.MIN_VALUE / 4, next2Free = 0;
        for (int i = prices.length - 1; i >= 0; i--) {
            int currentFree = Math.max(nextFree, -prices[i] + nextHolding);
            int currentHolding = Math.max(nextHolding, prices[i] + nextFree);
            next2Free = nextFree;
            nextFree = currentFree;
            nextHolding = currentHolding;
        }
        return nextFree;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## Stock III — At Most Two Transactions

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

**Input → Output:** prices = [3,3,5,0,0,3,1,4] → 6

**Important pointers:** Hold at most one share. Selling completes a transaction. Stock V here means one-day cooldown: selling moves to i + 2. Invalid terminal holding states use a safe negative sentinel.

### Recursion + Memo

```java
class Solution {
    private static final int NEG = Integer.MIN_VALUE / 4;
    public int maxProfit(int[] prices) {
        return solve(prices, 0, 0, 2, new Integer[prices.length][2][2 + 1]);
    }
    private int solve(int[] p, int i, int holding, int remaining, Integer[][][] memo) {
        if (i == p.length || remaining == 0) return holding == 1 ? NEG : 0;
        if (memo[i][holding][remaining] != null) return memo[i][holding][remaining];
        if (holding == 1) return memo[i][holding][remaining] = Math.max(solve(p, i + 1, 1, remaining, memo), p[i] + solve(p, i + 1, 0, remaining - 1, memo));
        return memo[i][holding][remaining] = Math.max(solve(p, i + 1, 0, remaining, memo), -p[i] + solve(p, i + 1, 1, remaining, memo));
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Full 3D DP

```java
import java.util.Arrays;
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length, limit = 2;
        int[][][] dp = new int[n + 1][2][limit + 1];
        for (int i = 0; i <= n; i++) Arrays.fill(dp[i][1], Integer.MIN_VALUE / 4);
        for (int i = n - 1; i >= 0; i--) {
            for (int remaining = 1; remaining <= limit; remaining++) {
                dp[i][0][remaining] = Math.max(dp[i + 1][0][remaining], -prices[i] + dp[i + 1][1][remaining]);
                dp[i][1][remaining] = Math.max(dp[i + 1][1][remaining], prices[i] + dp[i + 1][0][remaining - 1]);
            }
        }
        return dp[0][0][limit];
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Space-optimized DP

```java
import java.util.Arrays;
class Solution {
    public int maxProfit(int[] prices) {
        int limit = 2;
        int[][] next = new int[2][limit + 1];
        Arrays.fill(next[1], Integer.MIN_VALUE / 4);
        for (int i = prices.length - 1; i >= 0; i--) {
            int[][] current = new int[2][limit + 1];
            Arrays.fill(current[1], Integer.MIN_VALUE / 4);
            for (int remaining = 1; remaining <= limit; remaining++) {
                current[0][remaining] = Math.max(next[0][remaining], -prices[i] + next[1][remaining]);
                current[1][remaining] = Math.max(next[1][remaining], prices[i] + next[0][remaining - 1]);
            }
            next = current;
        }
        return next[0][limit];
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## Stock IV — At Most K Transactions

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

**Input → Output:** k = 2, prices = [3,2,6,5,0,3] → 7

**Important pointers:** Hold at most one share. Selling completes a transaction. Stock V here means one-day cooldown: selling moves to i + 2. Invalid terminal holding states use a safe negative sentinel.

### Recursion + Memo

```java
class Solution {
    private static final int NEG = Integer.MIN_VALUE / 4;
    public int maxProfit(int k, int[] prices) {
        return solve(prices, 0, 0, k, new Integer[prices.length][2][k + 1]);
    }
    private int solve(int[] p, int i, int holding, int remaining, Integer[][][] memo) {
        if (i == p.length || remaining == 0) return holding == 1 ? NEG : 0;
        if (memo[i][holding][remaining] != null) return memo[i][holding][remaining];
        if (holding == 1) return memo[i][holding][remaining] = Math.max(solve(p, i + 1, 1, remaining, memo), p[i] + solve(p, i + 1, 0, remaining - 1, memo));
        return memo[i][holding][remaining] = Math.max(solve(p, i + 1, 0, remaining, memo), -p[i] + solve(p, i + 1, 1, remaining, memo));
    }
}
```

**Time:** O(n × (k + 1))  
**Space:** O((n + 1) × (k + 1))

### Full 3D DP

```java
import java.util.Arrays;
class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length, limit = k;
        int[][][] dp = new int[n + 1][2][limit + 1];
        for (int i = 0; i <= n; i++) Arrays.fill(dp[i][1], Integer.MIN_VALUE / 4);
        for (int i = n - 1; i >= 0; i--) {
            for (int remaining = 1; remaining <= limit; remaining++) {
                dp[i][0][remaining] = Math.max(dp[i + 1][0][remaining], -prices[i] + dp[i + 1][1][remaining]);
                dp[i][1][remaining] = Math.max(dp[i + 1][1][remaining], prices[i] + dp[i + 1][0][remaining - 1]);
            }
        }
        return dp[0][0][limit];
    }
}
```

**Time:** O(n × (k + 1))  
**Space:** O((n + 1) × (k + 1))

### Space-optimized DP

```java
import java.util.Arrays;
class Solution {
    public int maxProfit(int k, int[] prices) {
        int limit = k;
        int[][] next = new int[2][limit + 1];
        Arrays.fill(next[1], Integer.MIN_VALUE / 4);
        for (int i = prices.length - 1; i >= 0; i--) {
            int[][] current = new int[2][limit + 1];
            Arrays.fill(current[1], Integer.MIN_VALUE / 4);
            for (int remaining = 1; remaining <= limit; remaining++) {
                current[0][remaining] = Math.max(next[0][remaining], -prices[i] + next[1][remaining]);
                current[1][remaining] = Math.max(next[1][remaining], prices[i] + next[0][remaining - 1]);
            }
            next = current;
        }
        return next[0][limit];
    }
}
```

**Time:** O(n × (k + 1))  
**Space:** O(k + 1)

## Stock V — With Cooldown

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

**Input → Output:** prices = [1,2,3,0,2] → 3

**Important pointers:** Hold at most one share. Selling completes a transaction. Stock V here means one-day cooldown: selling moves to i + 2. Invalid terminal holding states use a safe negative sentinel.

### Recursion + Memo

```java
class Solution {
    private static final int NEG = Integer.MIN_VALUE / 4;
    public int maxProfit(int[] prices) {
        return solve(prices, 0, 0, new Integer[prices.length][2]);
    }
    private int solve(int[] p, int i, int holding, Integer[][] memo) {
        if (i >= p.length) return holding == 1 ? NEG : 0;
        if (memo[i][holding] != null) return memo[i][holding];
        if (holding == 1) return memo[i][holding] = Math.max(solve(p, i + 1, 1, memo), p[i] + solve(p, i + 2, 0, memo));
        return memo[i][holding] = Math.max(solve(p, i + 1, 0, memo), -p[i] + solve(p, i + 1, 1, memo));
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Full 2D DP

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n + 2][2];
        for (int[] row : dp) row[1] = Integer.MIN_VALUE / 4;
        for (int i = n - 1; i >= 0; i--) {
            dp[i][0] = Math.max(dp[i + 1][0], -prices[i] + dp[i + 1][1]);
            dp[i][1] = Math.max(dp[i + 1][1], prices[i] + dp[i + 2][0]);
        }
        return dp[0][0];
    }
}
```

**Time:** O(n)  
**Space:** O(n)

### Space-optimized DP

```java
class Solution {
    public int maxProfit(int[] prices) {
        int nextFree = 0, nextHolding = Integer.MIN_VALUE / 4, next2Free = 0;
        for (int i = prices.length - 1; i >= 0; i--) {
            int currentFree = Math.max(nextFree, -prices[i] + nextHolding);
            int currentHolding = Math.max(nextHolding, prices[i] + next2Free);
            next2Free = nextFree;
            nextFree = currentFree;
            nextHolding = currentHolding;
        }
        return nextFree;
    }
}
```

**Time:** O(n)  
**Space:** O(1)

## 19. Longest Common Subsequence — Length

[Problem link](https://leetcode.com/problems/longest-common-subsequence/)

**Input:** text1 = "abcde", text2 = "ace"  
**Output:** 3

**Important pointers:** Subsequences preserve order but need not be contiguous.

### Recursion + Memo

```java
class Solution {
    public int longestCommonSubsequence(String a, String b) {
        return solve(a, b, 0, 0, new Integer[a.length()][b.length()]);
    }
    private int solve(String a, String b, int i, int j, Integer[][] memo) {
        if (i == a.length() || j == b.length()) return 0;
        if (memo[i][j] != null) return memo[i][j];
        if (a.charAt(i) == b.charAt(j)) return memo[i][j] = 1 + solve(a, b, i + 1, j + 1, memo);
        return memo[i][j] = Math.max(solve(a, b, i + 1, j, memo), solve(a, b, i, j + 1, memo));
    }
}
```

**Time:** O(m × n + m + n)  
**Space:** O(m × n + m + n)

### Full 2D DP

```java
class Solution {
    public int longestCommonSubsequence(String a, String b) {
        int m = a.length(), n = b.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                dp[i][j] = a.charAt(i) == b.charAt(j) ? 1 + dp[i + 1][j + 1] : Math.max(dp[i + 1][j], dp[i][j + 1]);
            }
        }
        return dp[0][0];
    }
}
```

**Time:** O(m × n + m + n)  
**Space:** O(m × n + m + n)

### Space-optimized DP

```java
class Solution {
    public int longestCommonSubsequence(String a, String b) {
        if (a.length() < b.length()) { String temp = a; a = b; b = temp; }
        int[] next = new int[b.length() + 1];
        for (int i = a.length() - 1; i >= 0; i--) {
            int[] current = new int[b.length() + 1];
            for (int j = b.length() - 1; j >= 0; j--) {
                current[j] = a.charAt(i) == b.charAt(j) ? 1 + next[j + 1] : Math.max(next[j], current[j + 1]);
            }
            next = current;
        }
        return next[0];
    }
}
```

**Time:** O(m × n + m + n)  
**Space:** O(min(m, n) + 1)

## 20. Longest Common Subsequence — Printing

[Problem link](https://www.geeksforgeeks.org/problems/print-longest-common-subsequence/1)

**Input:** text1 = "abcde", text2 = "ace"  
**Output:** "ace"

**Important pointers:** Return any valid LCS. A lexicographically smallest answer is not guaranteed. Printing helpers use custom method names.

### Recursion + Memo

```java
class Solution {
    public String printLCS(String a, String b) {
        Integer[][] memo = new Integer[a.length()][b.length()];
        solve(a, b, 0, 0, memo);

        StringBuilder result = new StringBuilder();
        int i = 0, j = 0;
        while (i < a.length() && j < b.length()) {
            if (a.charAt(i) == b.charAt(j)) {
                result.append(a.charAt(i));
                i++;
                j++;
            } else if (solve(a, b, i + 1, j, memo) >= solve(a, b, i, j + 1, memo)) i++;
            else j++;
        }
        return result.toString();

    }
    private int solve(String a, String b, int i, int j, Integer[][] memo) {
        if (i == a.length() || j == b.length()) return 0;
        if (memo[i][j] != null) return memo[i][j];
        if (a.charAt(i) == b.charAt(j)) return memo[i][j] = 1 + solve(a, b, i + 1, j + 1, memo);
        return memo[i][j] = Math.max(solve(a, b, i + 1, j, memo), solve(a, b, i, j + 1, memo));
    }
}
```

**Time:** O(m × n + m + n)  
**Space:** O(m × n + m + n)

### Full 2D DP

```java
class Solution {
    public String printLCS(String a, String b) {
        int[][] dp = new int[a.length() + 1][b.length() + 1];
        for (int i = a.length() - 1; i >= 0; i--) {
            for (int j = b.length() - 1; j >= 0; j--) {
                dp[i][j] = a.charAt(i) == b.charAt(j) ? 1 + dp[i + 1][j + 1] : Math.max(dp[i + 1][j], dp[i][j + 1]);
            }
        }

        StringBuilder result = new StringBuilder();
        int i = 0, j = 0;
        while (i < a.length() && j < b.length()) {
            if (a.charAt(i) == b.charAt(j)) {
                result.append(a.charAt(i));
                i++;
                j++;
            } else if (dp[i + 1][j] >= dp[i][j + 1]) i++;
            else j++;
        }
        return result.toString();

    }
}
```

**Time:** O(m × n + m + n)  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP — Store Subsequences

```java
import java.util.Arrays;
class Solution {
    public String printLCS(String a, String b) {
        if (a.length() < b.length()) { String temp = a; a = b; b = temp; }
        String[] next = new String[b.length() + 1];
        Arrays.fill(next, "");
        for (int i = a.length() - 1; i >= 0; i--) {
            String[] current = new String[b.length() + 1];
            Arrays.fill(current, "");
            for (int j = b.length() - 1; j >= 0; j--) {
                if (a.charAt(i) == b.charAt(j)) current[j] = a.charAt(i) + next[j + 1];
                else current[j] = next[j].length() >= current[j + 1].length() ? next[j] : current[j + 1];
            }
            next = current;
        }
        return next[0];
    }
}
```

**Time:** O(m × n × (L + 1) + m + n)  
**Space:** O((min(m, n) + 1) × (L + 1))

L is the LCS length. Strings are copied during concatenation; this is not O(min(m, n)) space in characters.

## 21. Longest Common Substring

[Problem link](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1)

**Input:** a = "ABCDGH", b = "ACDGHR"  
**Output:** 4

**Important pointers:** Substrings are contiguous. Reset the matching length to zero on a mismatch. Track the maximum across all cells.

### Full 2D DP

```java
class Solution {
    public int longestCommonSubstr(String a, String b) {
        int[][] dp = new int[a.length() + 1][b.length() + 1];
        int best = 0;
        for (int i = 1; i <= a.length(); i++) {
            for (int j = 1; j <= b.length(); j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                    best = Math.max(best, dp[i][j]);
                }
            }
        }
        return best;
    }
}
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O((m + 1) × (n + 1))

## 22. Longest Palindromic Subsequence

[Problem link](https://leetcode.com/problems/longest-palindromic-subsequence/)

**Input:** s = "bbbab"  
**Output:** 4

**Important pointers:** A subsequence need not be contiguous. Matching endpoints add 2; one middle character adds 1.

### Recursion + Memo

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        return solve(s, 0, s.length() - 1, new Integer[s.length()][s.length()]);
    }
    private int solve(String s, int i, int j, Integer[][] memo) {
        if (i > j) return 0;
        if (i == j) return 1;
        if (memo[i][j] != null) return memo[i][j];
        if (s.charAt(i) == s.charAt(j)) return memo[i][j] = 2 + solve(s, i + 1, j - 1, memo);
        return memo[i][j] = Math.max(solve(s, i + 1, j, memo), solve(s, i, j - 1, memo));
    }
}
```

**Time:** O(n²)  
**Space:** O(n²)

### Full 2D DP

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int[][] dp = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = s.charAt(i) == s.charAt(j) ? 2 + dp[i + 1][j - 1] : Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][n - 1];
    }
}
```

**Time:** O(n²)  
**Space:** O(n²)

### Space-optimized DP

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int[] dp = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int diagonal = 0;
            dp[i] = 1;
            for (int j = i + 1; j < n; j++) {
                int oldValue = dp[j];
                dp[j] = s.charAt(i) == s.charAt(j) ? 2 + diagonal : Math.max(dp[j], dp[j - 1]);
                diagonal = oldValue;
            }
        }
        return dp[n - 1];
    }
}
```

**Time:** O(n²)  
**Space:** O(n)

## 23. Edit Distance

[Problem link](https://leetcode.com/problems/edit-distance/)

**Input:** word1 = "horse", word2 = "ros"  
**Output:** 3

**Important pointers:** Insert, delete, or replace one character, each at cost 1. Matches cost 0.

### Recursion + Memo

```java
class Solution {
    public int minDistance(String a, String b) {
        return solve(a, b, 0, 0, new Integer[a.length()][b.length()]);
    }
    private int solve(String a, String b, int i, int j, Integer[][] memo) {
        if (i == a.length()) return b.length() - j;
        if (j == b.length()) return a.length() - i;
        if (memo[i][j] != null) return memo[i][j];
        if (a.charAt(i) == b.charAt(j)) return memo[i][j] = solve(a, b, i + 1, j + 1, memo);
        return memo[i][j] = 1 + Math.min(solve(a, b, i, j + 1, memo), Math.min(solve(a, b, i + 1, j, memo), solve(a, b, i + 1, j + 1, memo)));
    }
}
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O((m + 1) × (n + 1))

### Full 2D DP

```java
class Solution {
    public int minDistance(String a, String b) {
        int m = a.length(), n = b.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][n] = m - i;
        for (int j = 0; j <= n; j++) dp[m][j] = n - j;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                dp[i][j] = a.charAt(i) == b.charAt(j) ? dp[i + 1][j + 1] : 1 + Math.min(dp[i][j + 1], Math.min(dp[i + 1][j], dp[i + 1][j + 1]));
            }
        }
        return dp[0][0];
    }
}
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP

```java
class Solution {
    public int minDistance(String a, String b) {
        if (a.length() < b.length()) { String temp = a; a = b; b = temp; }
        int m = a.length(), n = b.length();
        int[] next = new int[n + 1];
        for (int j = 0; j <= n; j++) next[j] = n - j;
        for (int i = m - 1; i >= 0; i--) {
            int[] current = new int[n + 1];
            current[n] = m - i;
            for (int j = n - 1; j >= 0; j--) {
                current[j] = a.charAt(i) == b.charAt(j) ? next[j + 1] : 1 + Math.min(current[j + 1], Math.min(next[j], next[j + 1]));
            }
            next = current;
        }
        return next[0];
    }
}
```

**Time:** O((m + 1) × (n + 1))  
**Space:** O(min(m, n) + 1)

## LIS DP

## 24. Longest Increasing Subsequence — Length

[Problem link](https://leetcode.com/problems/longest-increasing-subsequence/)

**Input:** nums = [10,9,2,5,3,7,101,18]  
**Output:** 4

**Important pointers:** Strictly increasing: equal values do not extend the subsequence. Binary-search tails are not necessarily an actual subsequence.

### Recursion + Memo

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        return solve(nums, 0, -1, new Integer[nums.length][nums.length + 1]);
    }
    private int solve(int[] nums, int i, int previous, Integer[][] memo) {
        if (i == nums.length) return 0;
        if (memo[i][previous + 1] != null) return memo[i][previous + 1];
        int take = previous == -1 || nums[i] > nums[previous] ? 1 + solve(nums, i + 1, i, memo) : 0;
        return memo[i][previous + 1] = Math.max(solve(nums, i + 1, previous, memo), take);
    }
}
```

**Time:** O(n²)  
**Space:** O(n²)

### Full 2D DP

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n + 1][n + 1];
        for (int i = n - 1; i >= 0; i--) {
            for (int previous = i - 1; previous >= -1; previous--) {
                dp[i][previous + 1] = Math.max(dp[i + 1][previous + 1], previous == -1 || nums[i] > nums[previous] ? 1 + dp[i + 1][i + 1] : 0);
            }
        }
        return dp[0][0];
    }
}
```

**Time:** O(n²)  
**Space:** O(n²)

### 1D DP

```java
import java.util.Arrays;
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int answer = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], 1 + dp[j]);
            }
            answer = Math.max(answer, dp[i]);
        }
        return answer;
    }
}
```

**Time:** O(n²)  
**Space:** O(n)

### Binary Search

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int num : nums) {
            int left = 0, right = size;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (tails[mid] < num) left = mid + 1;
                else right = mid;
            }
            tails[left] = num;
            if (left == size) size++;
        }
        return size;
    }
}
```

**Time:** O(n log n)  
**Space:** O(n)

## 25. Longest Increasing Subsequence — Printing

[Problem link](https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1)

**Input:** nums = [10,9,2,5,3,7,101,18]  
**Output:** [2,5,7,101]

**Important pointers:** Return any LIS. Track predecessor indices and reverse after reconstruction. No lexicographic tie guarantee.

### DP + Parent Tracking

```java
import java.util.*;
class Solution {
    public List<Integer> printLIS(int[] nums) {
        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        if (n == 0) return result;
        int[] dp = new int[n], parent = new int[n];
        Arrays.fill(dp, 1);
        int best = 0;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i] && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
            if (dp[i] > dp[best]) best = i;
        }
        while (parent[best] != best) {
            result.add(nums[best]);
            best = parent[best];
        }
        result.add(nums[best]);
        Collections.reverse(result);
        return result;
    }
}
```

**Time:** O(n²)  
**Space:** O(n)

## Rectangles and Squares

## 26. Largest Histogram Rectangle

[Problem link](https://leetcode.com/problems/largest-rectangle-in-histogram/)

**Input:** heights = [2,1,5,6,2,3]  
**Output:** 10

**Important pointers:** Maintain increasing heights by index. Width after popping is i - left - 1. A virtual height 0 flushes the stack.

### Monotonic Stack

```java
import java.util.*;
class Solution {
    public int largestRectangleArea(int[] heights) {
        return histogram(heights);
    }

    private int histogram(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int answer = 0;
        for (int i = 0; i <= heights.length; i++) {
            int currentHeight = i < heights.length ? heights[i] : 0;
            while (!stack.isEmpty() && heights[stack.peek()] >= currentHeight) {
                int height = heights[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                answer = Math.max(answer, height * (i - left - 1));
            }
            if (i < heights.length) stack.push(i);
        }
        return answer;
    }
}
```

**Time:** O(n)  
**Space:** O(n)

## 27. Maximal Rectangle of Ones

[Problem link](https://leetcode.com/problems/maximal-rectangle/)

**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  
**Output:** 6

**Important pointers:** Use char[][] with characters '0' and '1'. Build a histogram for each row; zeros reset heights. Return area.

### Histogram + Monotonic Stack

```java
import java.util.*;
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int[] heights = new int[matrix[0].length];
        int answer = 0;
        for (char[] row : matrix) {
            for (int j = 0; j < row.length; j++) heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            answer = Math.max(answer, histogram(heights));
        }
        return answer;
    }

    private int histogram(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int answer = 0;
        for (int i = 0; i <= heights.length; i++) {
            int currentHeight = i < heights.length ? heights[i] : 0;
            while (!stack.isEmpty() && heights[stack.peek()] >= currentHeight) {
                int height = heights[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                answer = Math.max(answer, height * (i - left - 1));
            }
            if (i < heights.length) stack.push(i);
        }
        return answer;
    }
}
```

**Time:** O(rows × cols)  
**Space:** O(cols)

## 28. Count All-One Squares

[Problem link](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

**Input:** matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]  
**Output:** 15

**Important pointers:** Integer cells. Each state is the largest square starting at that cell. A state of 3 counts three squares; sum all states.

### Recursion + Memo

```java
class Solution {
    public int countSquares(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        Integer[][] memo = new Integer[matrix.length][matrix[0].length];
        int answer = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) answer += solve(matrix, i, j, memo);
        }
        return answer;
    }
    private int solve(int[][] matrix, int i, int j, Integer[][] memo) {
        if (i == matrix.length || j == matrix[0].length || matrix[i][j] == 0) return 0;
        if (memo[i][j] != null) return memo[i][j];
        return memo[i][j] = 1 + Math.min(solve(matrix, i + 1, j, memo), Math.min(solve(matrix, i, j + 1, memo), solve(matrix, i + 1, j + 1, memo)));
    }
}
```

**Time:** O(m × n)  
**Space:** O(m × n + m + n)

### Full 2D DP

```java
class Solution {
    public int countSquares(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length, n = matrix[0].length, answer = 0;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = 1 + Math.min(dp[i + 1][j], Math.min(dp[i][j + 1], dp[i + 1][j + 1]));
                    answer += dp[i][j];
                }
            }
        }
        return answer;
    }
}
```

**Time:** O(m × n)  
**Space:** O((m + 1) × (n + 1))

### Space-optimized DP

```java
class Solution {
    public int countSquares(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length, n = matrix[0].length, answer = 0;
        int[] next = new int[n + 1];
        for (int i = m - 1; i >= 0; i--) {
            int[] current = new int[n + 1];
            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == 1) {
                    current[j] = 1 + Math.min(next[j], Math.min(current[j + 1], next[j + 1]));
                    answer += current[j];
                }
            }
            next = current;
        }
        return answer;
    }
}
```

**Time:** O(m × n)  
**Space:** O(n)

## Java Notes

- Input arrays and grids are assumed non-null and rectangular.
- `int` optimization APIs assume totals, costs, areas, and profits fit in signed 32-bit integers, as in the standard problem constraints. Use `long` consistently for larger custom inputs.
- Stock examples use nonnegative prices within standard constraints; the negative sentinel is deliberately away from `Integer.MIN_VALUE` to avoid overflow on transitions.
- `Integer`/`Boolean` memo arrays use `null` for uncomputed states. Complexity includes recursion where applicable.
- Some helpers use descriptive names or `long` return types. Adapt the method signature to the judge stub.
- For sum-based DP, time is pseudo-polynomial in the numeric target or capacity.
