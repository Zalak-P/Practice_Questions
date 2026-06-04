# Problem: https://leetcode.com/problems/house-robber/
# Code trick: at every house, you have 2 choices:
# rob this house  → add money + skip previous adjacent house
# skip this house → keep previous best

class Solution:

    def rob(self, nums: List[int]) -> int:

        def dfs(i):
            if i >= len(nums):
                return 0

            rob_current = nums[i] + dfs(i + 2)
            skip_current = dfs(i + 1)

            return max(rob_current, skip_current)

        return dfs(0)