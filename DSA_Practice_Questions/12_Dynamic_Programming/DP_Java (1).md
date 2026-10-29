# Dynamic Programming — Java

## House Robber

### 1. House Robber I

Maximize money robbed from a line of houses without robbing adjacent houses. At each house, choose between skipping it and taking it with the best total two houses back.

[LeetCode 198](https://leetcode.com/problems/house-robber/)

#### Recursion + Memoization

At each index, compare skipping the house with taking it and continuing two positions ahead. Cache the answer for each index.

```java
import java.util.*;

class Solution {
    public int rob(int[] nums) {
        int[] memo = new int[nums.length];
        Arrays.fill(memo, -1);
        return solve(nums, 0, memo);
    }

    private int solve(int[] nums, int i, int[] memo) {
        if (i >= nums.length) return 0;
        if (memo[i] != -1) return memo[i];
        memo[i] = Math.max(solve(nums, i + 1, memo),
                nums[i] + solve(nums, i + 2, memo));
        return memo[i];
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n) memo plus O(n) recursion stack.

#### Bottom-Up DP

Fill the DP array from right to left using the same take-or-skip recurrence.

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 2];
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = Math.max(dp[i + 1], nums[i] + dp[i + 2]);
        }
        return dp[0];
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n).

#### Constant Space

Keep only the two previous DP values needed for the next decision.

```java
import java.util.*;

class Solution {
    public int rob(int[] nums) {
        int prev2 = 0, prev1 = 0;
        for (int money : nums) {
            int current = Math.max(prev1, prev2 + money);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time complexity:** O(n), where n is the number of houses.

**Space complexity:** O(1).

### 2. House Robber II

Houses form a circle, so the first and last are adjacent. Take the better result from excluding the first house or excluding the last house.

[LeetCode 213](https://leetcode.com/problems/house-robber-ii/)

#### Recursion + Memoization

Solve two linear ranges: exclude the last house or exclude the first. Use a separate memo for each range because its endpoint differs.

```java
import java.util.*;

class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        return Math.max(robRange(nums, 0, n - 1), robRange(nums, 1, n));
    }

    private int robRange(int[] nums, int start, int end) {
        int[] memo = new int[nums.length];
        Arrays.fill(memo, -1);
        return solve(nums, start, end, memo);
    }

    private int solve(int[] nums, int i, int end, int[] memo) {
        if (i >= end) return 0;
        if (memo[i] != -1) return memo[i];
        memo[i] = Math.max(solve(nums, i + 1, end, memo),
                nums[i] + solve(nums, i + 2, end, memo));
        return memo[i];
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n) memo plus O(n) recursion stack.

#### Bottom-Up DP

Fill the DP array from right to left using the same take-or-skip recurrence.

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        return Math.max(robRange(nums, 0, n - 1), robRange(nums, 1, n));
    }

    private int robRange(int[] nums, int start, int end) {
        int length = end - start;
        int[] dp = new int[length + 2];
        for (int i = length - 1; i >= 0; i--) {
            dp[i] = Math.max(dp[i + 1], nums[start + i] + dp[i + 2]);
        }
        return dp[0];
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n).

#### Constant Space

Keep only the two previous DP values needed for the next decision.

```java
import java.util.*;

class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        return Math.max(robRange(nums, 0, nums.length - 1), robRange(nums, 1, nums.length));
    }

    private int robRange(int[] nums, int start, int end) {
        int prev2 = 0, prev1 = 0;
        for (int i = start; i < end; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time complexity:** O(n), where n is the number of houses.

**Space complexity:** O(1).

## 1D DP

### 3. Frog Jump

Reach the last stone with minimum energy. A jump from i to j costs |height[i] − height[j]|; jump one or two positions.

[GeeksforGeeks: Frog Jump](https://www.geeksforgeeks.org/problems/geek-jump/1)

```java
import java.util.*;

class Solution {
    public int minCost(int[] height) {
        int prev2 = 0, prev1 = 0;
        for (int i = 1; i < height.length; i++) {
            int current = prev1 + Math.abs(height[i] - height[i - 1]);
            if (i > 1) current = Math.min(current, prev2 + Math.abs(height[i] - height[i - 2]));
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time complexity:** O(n), where n is the number of stones.

### 4. Frog Jump with X Distance

Minimize the same height-based energy cost when each jump can move 1 through x positions; x ≥ 1.

[GeeksforGeeks: Minimal Cost of Jumps](https://www.geeksforgeeks.org/problems/minimal-cost/1)

```java
import java.util.*;

class Solution {
    public int minimizeCost(int x, int[] height) {
        int n = height.length;
        if (n == 0) return 0;
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 1; i < n; i++) {
            for (int jump = 1; jump <= x && jump <= i; jump++) {
                dp[i] = Math.min(dp[i], dp[i - jump] + Math.abs(height[i] - height[i - jump]));
            }
        }
        return dp[n - 1];
    }
}
```

**Time complexity:** O(n × min(x, n)), where n is the number of stones.

### 5. Decode Ways

Count decodings of a digit string using 1 → A through 26 → Z. A zero cannot be decoded alone.

[LeetCode 91](https://leetcode.com/problems/decode-ways/) · [NeetCode](https://neetcode.io/problems/decode-ways)

```java
import java.util.*;

class Solution {
    public int numDecodings(String s) {
        if (s.isEmpty()) return 0;
        int prev2 = 1, prev1 = s.charAt(0) == '0' ? 0 : 1;
        for (int i = 1; i < s.length(); i++) {
            int current = s.charAt(i) == '0' ? 0 : prev1;
            int pair = (s.charAt(i - 1) - '0') * 10 + s.charAt(i) - '0';
            if (pair >= 10 && pair <= 26) current += prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

**Time complexity:** O(n), where n is the string length.

## Grid DP

### 6. Unique Paths I

Count paths from the top-left to bottom-right of an m × n grid, moving only right or down.

[LeetCode 62](https://leetcode.com/problems/unique-paths/)

```java
import java.util.*;

class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int r = 1; r < m; r++) {
            for (int c = 1; c < n; c++) dp[c] += dp[c - 1];
        }
        return dp[n - 1];
    }
}
```

**Time complexity:** O(m × n).

### 7. Unique Paths II

Count right/down paths through a grid where 1 is an obstacle and 0 is open. An obstacle resets the number of paths at that cell to zero.

[LeetCode 63](https://leetcode.com/problems/unique-paths-ii/)

```java
import java.util.*;

class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return 0;
        int[] dp = new int[grid[0].length];
        dp[0] = 1;
        for (int[] row : grid) {
            for (int c = 0; c < row.length; c++) {
                if (row[c] == 1) dp[c] = 0;
                else if (c > 0) dp[c] += dp[c - 1];
            }
        }
        return dp[dp.length - 1];
    }
}
```

**Time complexity:** O(m × n), where m and n are the grid dimensions.

## Subsequence and Knapsack DP

### 8. Subset Sum to Target

Check whether a subset of nonnegative integers sums to target. Descending sum updates ensure each array position is used at most once.

[GeeksforGeeks: Subset Sum](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1)

```java
import java.util.*;

class Solution {
    public boolean isSubsetSum(int[] nums, int target) {
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int s = target; s >= num; s--) dp[s] |= dp[s - num];
        }
        return dp[target];
    }
}
```

**Time complexity:** O(n × (target + 1)), where n is the array length.

### 9. Equal Subset Partition

Check whether a nonnegative array can be divided into two subsets with equal sums. An odd total is impossible; otherwise find a subset with half the total.

[LeetCode 416](https://leetcode.com/problems/partition-equal-subset-sum/)

```java
import java.util.*;

class Solution {
    public boolean canPartition(int[] nums) {
        int total = Arrays.stream(nums).sum();
        if (total % 2 != 0) return false;
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int s = target; s >= num; s--) dp[s] |= dp[s - num];
        }
        return dp[target];
    }
}
```

**Time complexity:** O(n × (S + 1)), where S is the total sum.

### 10. Minimum Partition Difference

Split a nonnegative array into two subsets of any sizes, minimizing the absolute difference of their sums. Find the largest reachable sum no greater than half the total.

[GeeksforGeeks: Minimum Partition Difference](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1)

```java
import java.util.*;

class Solution {
    public int minDifference(int[] nums) {
        int total = Arrays.stream(nums).sum(), half = total / 2;
        boolean[] dp = new boolean[half + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int s = half; s >= num; s--) dp[s] |= dp[s - num];
        }
        for (int s = half; s >= 0; s--) {
            if (dp[s]) return total - 2 * s;
        }
        return 0;
    }
}
```

**Time complexity:** O(n × (S + 1)), where S is the total sum.

### 11. Count Subsets with Sum K

Count subsets of nonnegative integers totaling k; equal-valued elements at different indices are distinct choices. Zeros correctly double existing counts. Return an exact count, without a modulus.

[GeeksforGeeks: Count Subsets with Sum](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1)

```java
import java.util.*;
import java.math.BigInteger;

class Solution {
    public BigInteger countSubsets(int[] nums, int k) {
        BigInteger[] dp = new BigInteger[k + 1];
        Arrays.fill(dp, BigInteger.ZERO);
        dp[0] = BigInteger.ONE;
        for (int num : nums) {
            for (int s = k; s >= num; s--) dp[s] = dp[s].add(dp[s - num]);
        }
        return dp[k];
    }
}
```

**Time complexity:** O(n × (k + 1)) DP updates; exact-integer additions cost O(b) for b-bit counts.

### 12. Count Partitions with Difference

Count assignments to labeled subsets S1 and S2 such that sum(S1) − sum(S2) = d, for nonnegative values and d ≥ 0. Count subsets totaling (total − d) / 2; return an exact count.

[GeeksforGeeks: Partitions with Given Difference](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1)

```java
import java.util.*;
import java.math.BigInteger;

class Solution {
    public BigInteger countPartitions(int[] nums, int d) {
        int total = Arrays.stream(nums).sum();
        if (d > total || (total - d) % 2 != 0) return BigInteger.ZERO;
        int target = (total - d) / 2;
        BigInteger[] dp = new BigInteger[target + 1];
        Arrays.fill(dp, BigInteger.ZERO);
        dp[0] = BigInteger.ONE;
        for (int num : nums) {
            for (int s = target; s >= num; s--) dp[s] = dp[s].add(dp[s - num]);
        }
        return dp[target];
    }
}
```

**Time complexity:** O(n × (T + 1)) DP updates, where T = (total − d) / 2; exact-integer additions cost O(b) for b-bit counts.

### 13. Target Sum

Assign + or − to every nonnegative number so the expression equals target. Count subsets assigned minus signs, whose sum must be (total − target) / 2.

[LeetCode 494](https://leetcode.com/problems/target-sum/)

```java
import java.util.*;

class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int total = Arrays.stream(nums).sum();
        if (Math.abs((long) target) > total || (total - target) % 2 != 0) return 0;
        int sum = (total - target) / 2;
        int[] dp = new int[sum + 1];
        dp[0] = 1;
        for (int num : nums) {
            for (int s = sum; s >= num; s--) dp[s] += dp[s - num];
        }
        return dp[sum];
    }
}
```

**Time complexity:** O(n × (T + 1)), where T = (total − target) / 2.

### 14. Minimum Coins

Find the fewest coins needed to form amount using unlimited positive-denomination coins. Return −1 when impossible.

[LeetCode 322](https://leetcode.com/problems/coin-change/)

```java
import java.util.*;

class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int sum = 1; sum <= amount; sum++) {
            for (int coin : coins) {
                if (coin <= sum) dp[sum] = Math.min(dp[sum], 1 + dp[sum - coin]);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

**Time complexity:** O(c × amount + amount), where c is the number of denominations.

### 15. Coin Change II

Count unordered combinations forming amount using unlimited coins of distinct positive denominations. Process coins outside the sum loop to avoid counting different orders separately.

[LeetCode 518](https://leetcode.com/problems/coin-change-ii/)

```java
import java.util.*;
import java.math.BigInteger;

class Solution {
    public int change(int amount, int[] coins) {
        BigInteger[] dp = new BigInteger[amount + 1];
        Arrays.fill(dp, BigInteger.ZERO);
        dp[0] = BigInteger.ONE;
        for (int coin : coins) {
            for (int sum = coin; sum <= amount; sum++) {
                dp[sum] = dp[sum].add(dp[sum - coin]);
            }
        }
        return dp[amount].intValueExact();
    }
}
```

**Time complexity:** O(c × (amount + 1)) DP updates; exact-integer additions cost O(b) for b-bit counts. Java uses BigInteger to protect intermediate counts; the problem guarantees the final answer fits int.

### 16. Unbounded Knapsack

Maximize value within capacity using unlimited copies of items with positive weights and nonnegative values. Ascending capacity updates allow reusing the current item.

[GeeksforGeeks: Unbounded Knapsack](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)

```java
import java.util.*;

class Solution {
    public int knapSack(int[] values, int[] weights, int capacity) {
        int[] dp = new int[capacity + 1];
        for (int i = 0; i < values.length; i++) {
            for (int c = weights[i]; c <= capacity; c++) {
                dp[c] = Math.max(dp[c], values[i] + dp[c - weights[i]]);
            }
        }
        return dp[capacity];
    }
}
```

**Time complexity:** O(n × (W + 1)), where n is the number of item types and W is capacity.

### 17. Rod Cutting

Maximize revenue by cutting a rod of length n. price[i − 1] is the price of a piece of length i; prices are nonnegative and each length can be reused.

[GeeksforGeeks: Rod Cutting](https://www.geeksforgeeks.org/problems/rod-cutting0840/1)

```java
import java.util.*;

class Solution {
    public int cutRod(int[] price) {
        int n = price.length;
        int[] dp = new int[n + 1];
        for (int length = 1; length <= n; length++) {
            for (int cut = 1; cut <= length; cut++) {
                dp[length] = Math.max(dp[length], price[cut - 1] + dp[length - cut]);
            }
        }
        return dp[n];
    }
}
```

**Time complexity:** O(n²), where n is the rod length.

## Stock DP

### 18. Buy and Sell Stock I

Maximize profit using at most one buy followed by one sell. Track the lowest price seen before each sale.

[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```java
import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int minimum = Integer.MAX_VALUE, best = 0;
        for (int price : prices) {
            minimum = Math.min(minimum, price);
            best = Math.max(best, price - minimum);
        }
        return best;
    }
}
```

**Time complexity:** O(n), where n is the number of days.

### 19. Buy and Sell Stock II

Maximize profit with unlimited transactions while holding at most one share. Track the best profit while holding a share and while holding none.

[LeetCode 122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```java
import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            int previousCash = cash;
            cash = Math.max(cash, hold + prices[i]);
            hold = Math.max(hold, previousCash - prices[i]);
        }
        return cash;
    }
}
```

**Time complexity:** O(n), where n is the number of days.

### 20. Buy and Sell Stock III

Maximize profit with at most two completed transactions and at most one share held. A sale consumes one transaction.

[LeetCode 123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

```java
import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int k = 2;
        int[][] next = new int[2][k + 1];
        for (int day = prices.length - 1; day >= 0; day--) {
            int[][] current = new int[2][k + 1];
            for (int remaining = 1; remaining <= k; remaining++) {
                // State 0: no share; state 1: holding a share.
                current[0][remaining] = Math.max(next[0][remaining], -prices[day] + next[1][remaining]);
                current[1][remaining] = Math.max(next[1][remaining], prices[day] + next[0][remaining - 1]);
            }
            next = current;
        }
        return next[0][k];
    }
}
```

**Time complexity:** O(n), since the transaction limit is fixed at 2.

### 21. Buy and Sell Stock IV

Maximize profit with at most k completed transactions and at most one share held. For k ≥ n / 2, use the unlimited-transactions shortcut.

[LeetCode 188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

```java
import java.util.*;

class Solution {
    public int maxProfit(int k, int[] prices) {
        if (k == 0 || prices.length < 2) return 0;
        if (k >= prices.length / 2) {
            int profit = 0;
            for (int i = 1; i < prices.length; i++) profit += Math.max(0, prices[i] - prices[i - 1]);
            return profit;
        }
        int[][] next = new int[2][k + 1];
        for (int day = prices.length - 1; day >= 0; day--) {
            int[][] current = new int[2][k + 1];
            for (int remaining = 1; remaining <= k; remaining++) {
                // State 0: no share; state 1: holding a share.
                current[0][remaining] = Math.max(next[0][remaining], -prices[day] + next[1][remaining]);
                current[1][remaining] = Math.max(next[1][remaining], prices[day] + next[0][remaining - 1]);
            }
            next = current;
        }
        return next[0][k];
    }
}
```

**Time complexity:** O(n × k) in the limited-transactions case; O(n) when k ≥ n / 2.

## LCS and String DP

### 22. Longest Common Subsequence — Length

Find the longest sequence appearing in both strings in the same order; characters need not be adjacent. dp[i][j] stores the LCS length for the first i and j characters. Match: 1 + diagonal; mismatch: max(top, left).

[LeetCode 1143](https://leetcode.com/problems/longest-common-subsequence/)

```java
import java.util.*;

class Solution {
    public int longestCommonSubsequence(String a, String b) {
        int m = a.length(), n = b.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m][n];
    }
}
```

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string lengths.

### 23. Longest Common Subsequence — Printing

Reconstruct and return one LCS by walking backward through the DP table. On a match, take that character; otherwise move toward the larger neighboring value.

[GeeksforGeeks: Printing LCS](https://www.geeksforgeeks.org/dsa/printing-longest-common-subsequence/)

```java
import java.util.*;

class Solution {
    public String printLCS(String a, String b) {
        int m = a.length(), n = b.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        StringBuilder result = new StringBuilder();
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (a.charAt(i - 1) == b.charAt(j - 1)) {
                result.append(a.charAt(i - 1));
                i--;
                j--;
            } else if (dp[i - 1][j] >= dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
        return result.reverse().toString();
    }
}
```

**Time complexity:** O((m + 1) × (n + 1)); reconstruction takes O(m + n).

### 24. Longest Common Substring

Return the length of the longest contiguous string shared by both inputs. dp[i][j] is the matching suffix length ending at those positions; reset it to zero on a mismatch.

[GeeksforGeeks: Longest Common Substring](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1)

```java
import java.util.*;

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

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string lengths.

### 25. Longest Palindromic Subsequence

Return the length of the longest subsequence reading the same forward and backward. Matching interval endpoints contribute two; otherwise skip either endpoint.

[LeetCode 516](https://leetcode.com/problems/longest-palindromic-subsequence/)

```java
import java.util.*;

class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int[][] dp = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) dp[i][j] = 2 + dp[i + 1][j - 1];
                else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][n - 1];
    }
}
```

**Time complexity:** O(n²), where n is the string length.

### 26. Edit Distance

Return the minimum insertions, deletions, and replacements needed to transform word1 into word2. Matching characters require no edit; otherwise take 1 + min(insert, delete, replace).

[LeetCode 72](https://leetcode.com/problems/edit-distance/)

```java
import java.util.*;

class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
            }
        }
        return dp[m][n];
    }
}
```

**Time complexity:** O((m + 1) × (n + 1)), where m and n are the string lengths.

## LIS DP

### 27. Longest Increasing Subsequence — Length

Find the longest strictly increasing subsequence. dp[i] is the best length ending at index i; extend from earlier indices with smaller values.

[LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/)

```java
import java.util.*;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int best = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            }
            best = Math.max(best, dp[i]);
        }
        return best;
    }
}
```

**Time complexity:** O(n²), where n is the array length.

### 28. Longest Increasing Subsequence — Printing

Reconstruct and return one strictly increasing subsequence of maximum length. Store a parent index whenever a longer subsequence is found.

[GeeksforGeeks: Printing LIS](https://www.geeksforgeeks.org/dsa/construction-of-longest-increasing-subsequence-using-dynamic-programming/)

```java
import java.util.*;

class Solution {
    public List<Integer> printLIS(int[] nums) {
        int n = nums.length;
        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;
        int[] dp = new int[n], parent = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(parent, -1);
        int end = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i] && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
            if (dp[i] > dp[end]) end = i;
        }
        while (end != -1) {
            result.add(nums[end]);
            end = parent[end];
        }
        Collections.reverse(result);
        return result;
    }
}
```

**Time complexity:** O(n²), including O(n) reconstruction.

## Rectangles and Squares

### 29. Largest Histogram Rectangle

Return the largest rectangle under unit-width histogram bars. Use an increasing stack of indices; popping a bar identifies its available width. This is a monotonic-stack problem.

[LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

```java
import java.util.*;

class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int best = 0;
        for (int i = 0; i <= heights.length; i++) {
            int current = i == heights.length ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] >= current) {
                int height = heights[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            if (i < heights.length) stack.push(i);
        }
        return best;
    }
}
```

**Time complexity:** O(n), since each bar is pushed and popped at most once.

### 30. Maximal Rectangle of Ones

Return the largest all-1 rectangle in a character matrix containing "0" and "1". Accumulate vertical heights row by row and solve the histogram problem at each row.

[LeetCode 85](https://leetcode.com/problems/maximal-rectangle/)

```java
import java.util.*;

class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int[] heights = new int[matrix[0].length];
        int best = 0;
        for (char[] row : matrix) {
            for (int c = 0; c < row.length; c++) heights[c] = row[c] == '1' ? heights[c] + 1 : 0;
            best = Math.max(best, largestRectangleArea(heights));
        }
        return best;
    }

    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int best = 0;
        for (int i = 0; i <= heights.length; i++) {
            int current = i == heights.length ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] >= current) {
                int height = heights[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            if (i < heights.length) stack.push(i);
        }
        return best;
    }
}
```

**Time complexity:** O(m × n), where m and n are the matrix dimensions.

### 31. Count All-One Squares

Count every all-1 square in an integer binary matrix. dp[r][c] is the largest square ending at that cell; its value also counts the squares ending there.

[LeetCode 1277](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

```java
import java.util.*;

class Solution {
    public int countSquares(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length, n = matrix[0].length, total = 0;
        int[][] dp = new int[m + 1][n + 1];
        for (int r = 1; r <= m; r++) {
            for (int c = 1; c <= n; c++) {
                if (matrix[r - 1][c - 1] == 1) {
                    dp[r][c] = 1 + Math.min(dp[r - 1][c - 1], Math.min(dp[r - 1][c], dp[r][c - 1]));
                    total += dp[r][c];
                }
            }
        }
        return total;
    }
}
```

**Time complexity:** O(m × n), where m and n are the matrix dimensions.
