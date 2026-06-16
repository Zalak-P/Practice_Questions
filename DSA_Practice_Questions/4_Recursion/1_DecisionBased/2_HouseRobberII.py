class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        # Solve normal House Robber (linear)
        def rob_linear(arr):
            memo = {}

            def dfs(i):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]

                take = arr[i] + dfs(i + 2)
                not_take = dfs(i + 1)

                memo[i] = max(take, not_take)
                return memo[i]

            return dfs(0)

        # Case 1: Exclude last house
        answer1 = rob_linear(nums[:-1])

        # Case 2: Exclude first house
        answer2 = rob_linear(nums[1:])

        return max(answer1, answer2)