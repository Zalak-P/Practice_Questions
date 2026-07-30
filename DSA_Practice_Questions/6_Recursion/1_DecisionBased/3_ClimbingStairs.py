class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def dfs(n):
            if n <= 2:
                return n

            if dp[n] != -1:
                return dp[n]

            answer1 = dfs(n - 1)
            answer2 = dfs(n - 2)
            dp[n] = answer1 + answer2

            return dp[n]

        return dfs(n)