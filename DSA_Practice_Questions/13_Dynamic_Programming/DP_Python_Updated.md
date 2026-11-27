# Dynamic Programming

## 1D DP — Previous States and Non-adjacent Choices

### 1. Climbing Stairs — 70

[LeetCode/GFG Link](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase with n steps. Each time, you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

**Input/Output**

```text
Input: n = 5
Output: 8
```

```python
class Solution:
    def climbStairs(self, n):
        previous = 1
        current = 1

        for step in range(2, n + 1):
            previous, current = current, previous + current

        return current
```

**Time Space Complexity**

- **Time:** O(n)
- **Space:** O(1)

### 2. Frog Jump

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/geek-jump/1)

A frog starts at index 0 and can jump one or two indices forward. A jump from i to j costs abs(heights[i] - heights[j]). Return the minimum total cost to reach the last index.

**Input/Output**

```text
Input: heights = [10,20,30,10,40,20,10]
Output: 40
```

```python


```

**Time Space Complexity**

- **Time:**
- **Space:**

### 3. Frog Jump with K Distance

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimal-cost/1)

A frog starts at index 0 and may jump between 1 and k indices forward. Each jump costs the absolute difference in heights. Return the minimum total cost to reach the last index.

**Input/Output**

```text
Input: heights = [10,30,40,50,20,60,30], k = 3
Output: 40
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 4. Maximum Sum of Non-adjacent Elements

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/stickler-thief/1)

Given nonnegative values in a linear array, return the maximum sum obtainable without choosing adjacent elements.

**Input/Output**

```text
Input: nums = [2,1,4,9,3,6,5]
Output: 17
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 5. House Robber — Circular Houses — 213

[LeetCode/GFG Link](https://leetcode.com/problems/house-robber-ii/)

Houses are arranged in a circle, so the first and last houses are adjacent. Return the maximum amount that can be robbed without robbing adjacent houses.

**Input/Output**

```text
Input: nums = [2,3,2,5,1,7,4]
Output: 15
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## DP on Days — Activity Choices

### 6. Ninja Training

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/geeks-training/1)

Choose one of three activities on each day. The same activity cannot be chosen on consecutive days. Return the maximum total points. Each row contains the three activity scores for one day.

**Input/Output**

```text
Input: points = [
    [10,40,70],
    [20,50,80],
    [30,60,90],
    [40,70,100]
]
Output: 280
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Grid DP — Paths and Path Sums

### 7. Grid Unique Paths — 62

[LeetCode/GFG Link](https://leetcode.com/problems/unique-paths/)

Count paths from the top-left to the bottom-right of an m × n grid when only right and down moves are allowed.

**Input/Output**

```text
Input: m = 4, n = 4
Output: 20
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 8. Unique Paths II — 63

[LeetCode/GFG Link](https://leetcode.com/problems/unique-paths-ii/)

Count paths from the top-left to the bottom-right, moving only right or down. A 1 is an obstacle and a 0 is an open cell.

**Input/Output**

```text
Input: obstacleGrid = [
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
Output: 8
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 9. Minimum Path Sum in a Grid — 64

[LeetCode/GFG Link](https://leetcode.com/problems/minimum-path-sum/)

Return the minimum sum along a path from the top-left to the bottom-right. Move only right or down, including both endpoint values.

**Input/Output**

```text
Input: grid = [
    [1,1,1,1],
    [2,2,2,1],
    [3,3,3,1],
    [4,4,4,1]
]
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 10. Triangle — 120

[LeetCode/GFG Link](https://leetcode.com/problems/triangle/)

Return the minimum sum from the top to the bottom of the triangle. From position j in one row, move to j or j + 1 in the next row.

**Input/Output**

```text
Input: triangle = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
Output: 11
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 11. Minimum or Maximum Falling Path Sum

[LeetCode/GFG Link](https://leetcode.com/problems/minimum-falling-path-sum/)

Start at any cell in the first row. Each move goes to the next row in the same column, one column left, or one column right. Find the minimum and maximum possible sums. The linked problem asks for the minimum; the maximum is the corresponding practice variant.

**Input/Output**

```text
Input: matrix = [
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6],
    [4,5,6,7]
]
Output: minimum = 10, maximum = 22
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Grid DP — Two Moving Agents

### 12. Cherry Pickup II — 1463

[LeetCode/GFG Link](https://leetcode.com/problems/cherry-pickup-ii/)

Two robots start at the first and last columns of the top row. Each moves to the next row with column change -1, 0, or 1. Maximize collected cherries; a cell visited by both robots is counted only once.

**Input/Output**

```text
Input: grid = [
    [1,0,0,1],
    [1,0,0,1],
    [1,0,0,1],
    [1,0,0,1]
]
Output: 8
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Subsequence DP — Subset Sum and 0/1 Knapsack

### 13. Subset Sum Equals Target

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1)

Given nonnegative integers, determine whether some subset sums to target. Each index can be selected at most once.

**Input/Output**

```text
Input: nums = [1,2,3,4,5,6,7], target = 18
Output: true
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 14. Partition Equal Subset Sum — 416

[LeetCode/GFG Link](https://leetcode.com/problems/partition-equal-subset-sum/)

Determine whether all elements can be partitioned into two subsets with equal sums. Each element must belong to exactly one subset.

**Input/Output**

```text
Input: nums = [1,5,11,5,2,4,4]
Output: true
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 15. Partition a Set into Two Subsets with Minimum Absolute Sum Difference

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1)

Partition nonnegative array elements into two subsets, with each index in exactly one subset. Minimize the absolute difference between their sums. Subset sizes need not be equal.

**Input/Output**

```text
Input: nums = [1,6,11,5,3,8,7]
Output: 1
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 16. Count Subsets with Sum K

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1)

Count subsets of a nonnegative array whose sum is k. Equal values at different indices are distinct choices. Include the empty subset when k = 0.

**Input/Output**

```text
Input: nums = [1,2,2,3,4,5,6], k = 7
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 17. Count Partitions with Given Difference

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1)

Count partitions into S1 and S2 such that sum(S1) - sum(S2) = difference. Each array index belongs to exactly one subset, and equal values at different indices are distinct choices.

**Input/Output**

```text
Input: nums = [5,2,6,4,1,3,2], difference = 3
Output: 9
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 18. 0/1 Knapsack

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)

Given item weights, values, and a capacity, maximize total value without exceeding the capacity. Each item may be chosen at most once.

**Input/Output**

```text
Input: weights = [1,2,4,5,3,6,7], values = [5,4,8,6,7,12,14], capacity = 12
Output: 28
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Subsequence DP — Coin Change, Target Sum, and Unbounded Choices

### 19. Minimum Coins — 322

[LeetCode/GFG Link](https://leetcode.com/problems/coin-change/)

Return the minimum number of coins needed to make amount. Each denomination can be used unlimited times. Return -1 if the amount cannot be formed.

**Input/Output**

```text
Input: coins = [1,2,5,7,10,12,15], amount = 29
Output: 3
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 20. Target Sum — 494

[LeetCode/GFG Link](https://leetcode.com/problems/target-sum/)

Assign either + or - to every array element. Count assignments whose resulting sum equals target. Each index receives exactly one sign.

**Input/Output**

```text
Input: nums = [1,1,2,3,2,1,2], target = 4
Output: 15
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 21. Coin Change II — 518

[LeetCode/GFG Link](https://leetcode.com/problems/coin-change-ii/)

Count combinations of coins summing to amount. Denominations are distinct and may be reused unlimited times. Different orders of the same combination count once.

**Input/Output**

```text
Input: amount = 12, coins = [1,2,3,5,7,8,10]
Output: 41
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 22. Unbounded Knapsack

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)

Maximize total value without exceeding capacity. Any item type may be selected unlimited times; weights are positive.

**Input/Output**

```text
Input: weights = [2,4,6,3,5,7,8], values = [5,11,13,8,14,20,21], capacity = 15
Output: 42
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 23. Rod Cutting Problem

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/rod-cutting0840/1)

A rod has length n, and price[i] is the selling price of a piece of length i + 1. Cut the rod into pieces totaling exactly n and maximize the selling price. Piece lengths may repeat.

**Input/Output**

```text
Input: n = 7, price = [2,5,7,8,10,13,17]
Output: 17
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## String DP — Common Subsequences and Substrings

### 24. Longest Common Subsequence — 1143

[LeetCode/GFG Link](https://leetcode.com/problems/longest-common-subsequence/)

Return the length of the longest sequence appearing in both strings in the same relative order. Its characters do not need to be contiguous.

**Input/Output**

```text
Input: text1 = "abcdefghij", text2 = "axbyczef"
Output: 5
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 25. Print Longest Common Subsequence

[LeetCode/GFG Link](https://leetcode.com/problems/longest-common-subsequence/)

Return one longest common subsequence of the two strings, rather than only its length. Any longest answer is accepted for this practice variant of the linked length problem.

**Input/Output**

```text
Input: text1 = "abcdefghij", text2 = "axbyczef"
Output: "abcef" (one valid answer)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 26. Longest Common Substring

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1)

Return the length of the longest contiguous substring shared by both strings.

**Input/Output**

```text
Input: s1 = "abcdxyzpq", s2 = "xyzabcdmn"
Output: 4
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## String DP — Palindromes and Insertions / Deletions

### 27. Longest Palindromic Subsequence — 516

[LeetCode/GFG Link](https://leetcode.com/problems/longest-palindromic-subsequence/)

Return the length of the longest subsequence that reads the same forward and backward. Characters need not be contiguous.

**Input/Output**

```text
Input: s = "bbabcbcab"
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 28. Minimum Insertions to Make a String Palindrome — 1312

[LeetCode/GFG Link](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

Return the minimum number of character insertions needed to make the string a palindrome. Insertions may occur at any position.

**Input/Output**

```text
Input: s = "mbadmnop"
Output: 5
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 29. Minimum Insertions or Deletions to Convert String A to String B

[LeetCode/GFG Link](https://leetcode.com/problems/delete-operation-for-two-strings/)

Convert A into B using only single-character insertions and deletions. Return the minimum total number of operations. The linked problem deletes from both strings to a common result; its minimum count is the same.

**Input/Output**

```text
Input: A = "heapabcd", B = "peaxybcd"
Output: 6
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 30. Shortest Common Supersequence — 1092

[LeetCode/GFG Link](https://leetcode.com/problems/shortest-common-supersequence/)

Return one shortest string containing both input strings as subsequences. Any shortest valid answer is accepted.

**Input/Output**

```text
Input: str1 = "abacdefg", str2 = "cabefghi"
Output: "cabacdefghi" (one valid answer)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## String DP — Counting, Editing, and Matching

### 31. Distinct Subsequences — 115

[LeetCode/GFG Link](https://leetcode.com/problems/distinct-subsequences/)

Count the subsequences of s that equal t. Different selections of indices count separately, even when they produce the same string.

**Input/Output**

```text
Input: s = "rabbbitxyz", t = "rabbitxyz"
Output: 3
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 32. Edit Distance — 72

[LeetCode/GFG Link](https://leetcode.com/problems/edit-distance/)

Return the minimum number of insertions, deletions, and replacements required to convert word1 into word2. Each operation changes one character.

**Input/Output**

```text
Input: word1 = "intention", word2 = "execution"
Output: 5
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 33. Wildcard Matching — 44

[LeetCode/GFG Link](https://leetcode.com/problems/wildcard-matching/)

Determine whether the entire string s matches pattern p. The wildcard ? matches one character, and \* matches any sequence, including the empty sequence.

**Input/Output**

```text
Input: s = "abefcdgiescdfimde", p = "ab*cd?i*de"
Output: true
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Stock DP — Buy / Sell States and Transaction Limits

### 34. Best Time to Buy and Sell Stock I — 121

[LeetCode/GFG Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Return the maximum profit from at most one buy followed by one sell on a later day. Return 0 if no profitable transaction exists.

**Input/Output**

```text
Input: prices = [7,1,5,3,6,4,8]
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 35. Best Time to Buy and Sell Stock II — 122

[LeetCode/GFG Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

Maximize profit with unlimited transactions. Hold at most one share at a time and sell it before buying again.

**Input/Output**

```text
Input: prices = [7,1,5,3,6,4,8]
Output: 11
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 36. Best Time to Buy and Sell Stock III — 123

[LeetCode/GFG Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

Maximize profit using at most two transactions. Each transaction is one buy followed by one sell. Hold at most one share at a time.

**Input/Output**

```text
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 37. Best Time to Buy and Sell Stock IV — 188

[LeetCode/GFG Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

Maximize profit using at most k transactions, holding at most one share at a time.

**Input/Output**

```text
Input: k = 2, prices = [3,2,6,5,0,3,1,4]
Output: 8
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 38. Buy and Sell Stocks with Cooldown — 309

[LeetCode/GFG Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

Maximize profit with unlimited transactions and at most one held share. After selling, wait one full day before buying again.

**Input/Output**

```text
Input: prices = [1,2,3,0,2,4,1,5]
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 39. Buy and Sell Stocks with Transaction Fee — 714

[LeetCode/GFG Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

Maximize profit with unlimited transactions and at most one held share. Pay the fixed fee once per completed transaction.

**Input/Output**

```text
Input: prices = [1,3,2,8,4,9,2,10], fee = 2
Output: 14
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Sequence DP — Increasing Subsequences and Reconstruction

### 40. Longest Increasing Subsequence — 300

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-subsequence/)

Return the length of the longest strictly increasing subsequence. Elements must preserve their original relative order.

**Input/Output**

```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 41. Printing Longest Increasing Subsequence

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-subsequence/)

Return one longest strictly increasing subsequence, rather than only its length. Any longest valid answer is accepted for this reconstruction variant.

**Input/Output**

```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: [2,3,7,18] (one valid answer)
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 42. Longest Increasing Subsequence — Binary Search Approach — 300

[LeetCode/GFG Link](https://leetcode.com/problems/longest-increasing-subsequence/)

Solve the same LIS length problem using the binary-search approach. This is the repeated LIS entry from the question list.

**Input/Output**

```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 43. Largest Divisible Subset — 368

[LeetCode/GFG Link](https://leetcode.com/problems/largest-divisible-subset/)

Given distinct positive integers, return a largest subset such that every pair has one value divisible by the other. Any maximum-size answer is accepted.

**Input/Output**

```text
Input: nums = [1,2,3,4,8,9,16,18]
Output: [1,2,4,8,16]
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 44. Longest String Chain — 1048

[LeetCode/GFG Link](https://leetcode.com/problems/longest-string-chain/)

A word is a predecessor of another if inserting exactly one character produces the other word without changing the order of existing characters. Return the longest chain length.

**Input/Output**

```text
Input: words = ["abcdefgh","abcdefghi","abcdefghij","abcdefghijk","abcdefghijkl","abcdefghijklm","abcdefghijklmn","mnopqrst"]
Output: 7
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 45. Longest Bitonic Subsequence

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1)

Return the maximum subsequence length that strictly increases and then strictly decreases. Require at least one increase and one decrease; return 0 if no such subsequence exists.

**Input/Output**

```text
Input: nums = [1,11,2,10,4,5,2,1]
Output: 6
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 46. Number of Longest Increasing Subsequences — 673

[LeetCode/GFG Link](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

Count the strictly increasing subsequences whose length equals the maximum possible length. Different selections of indices count separately.

**Input/Output**

```text
Input: nums = [1,3,5,4,7,6,8]
Output: 4
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Interval DP — Splits, Cuts, and Parenthesization

### 47. Matrix Chain Multiplication

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1)

For dimensions arr, matrix i has dimensions arr[i - 1] × arr[i]. Find the minimum scalar multiplication count for the whole chain without changing matrix order. Practice recursion with memoization.

**Input/Output**

```text
Input: arr = [10,20,30,40,30,20,10]
Output: 38000
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 48. Matrix Chain Multiplication — Bottom Up

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1)

Find the minimum scalar multiplication count for the same matrix-chain problem using bottom-up tabulation.

**Input/Output**

```text
Input: arr = [10,20,30,40,30,20,10]
Output: 38000
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 49. Minimum Cost to Cut a Stick — 1547

[LeetCode/GFG Link](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)

Cut a stick of length n at every requested position. Each cut costs the length of the current piece being cut. Choose the cut order minimizing total cost.

**Input/Output**

```text
Input: n = 12, cuts = [1,2,3,5,7,8,10]
Output: 36
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 50. Burst Balloons — 312

[LeetCode/GFG Link](https://leetcode.com/problems/burst-balloons/)

Burst every balloon in an order maximizing collected coins. Bursting i earns left × nums[i] × right using its current remaining neighbors; missing boundary neighbors have value 1.

**Input/Output**

```text
Input: nums = [3,1,5,8,2,4,6]
Output: 625
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 51. Evaluate Boolean Expression to True

[LeetCode/GFG Link](https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1)

Given T/F operands and &, |, ^ operators, count full parenthesizations that evaluate to true. Keep operand and operator order unchanged.

**Input/Output**

```text
Input: expression = "T|T&F^T|F"
Output: 12
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Partition DP — Choose the Next Segment

### 52. Palindrome Partitioning II — 132

[LeetCode/GFG Link](https://leetcode.com/problems/palindrome-partitioning-ii/)

Return the minimum cuts needed to split the string into contiguous palindromic substrings.

**Input/Output**

```text
Input: s = "aabcbddc"
Output: 3
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 53. Partition Array for Maximum Sum — 1043

[LeetCode/GFG Link](https://leetcode.com/problems/partition-array-for-maximum-sum/)

Partition the array into contiguous blocks of length at most k. Replace every value in a block by that block’s maximum. Return the maximum possible total sum.

**Input/Output**

```text
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

## Matrix DP — Rectangles and Squares

### 54. Maximum Rectangle Area with All Ones — 85

[LeetCode/GFG Link](https://leetcode.com/problems/maximal-rectangle/)

Return the largest rectangular area containing only 1s in a binary matrix. A common approach builds row-wise histogram heights and uses a monotonic stack.

**Input/Output**

```text
Input: matrix = [
    ["1","0","1","0"],
    ["1","1","1","1"],
    ["1","1","1","1"],
    ["1","0","0","1"]
]
Output: 8
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**

### 55. Count Square Submatrices with All Ones — 1277

[LeetCode/GFG Link](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

Count every square submatrix containing only 1s, including 1 × 1 squares. Squares with different positions or side lengths count separately.

**Input/Output**

```text
Input: matrix = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
Output: 30
```

```python

```

**Time Space Complexity**

- **Time:**
- **Space:**
