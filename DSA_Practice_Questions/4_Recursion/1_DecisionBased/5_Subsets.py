#Problem: https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/

#Recursive
class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        def dfs(i):
            if i == len(nums):
                return True
            if i + 1 < len(nums) and nums[i] == nums[i + 1] and dfs(i + 2):
                return True
            if i + 2 < len(nums) and nums[i] == nums[i + 1] == nums[i + 2] and dfs(i + 3):
                return True
            if (i + 2 < len(nums)
                and nums[i] + 1 == nums[i + 1]
                and nums[i + 1] + 1 == nums[i + 2]
                and dfs(i + 3)):
                return True

            return False

        return dfs(0)
    
# Memoized:

class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        memo = {}

        def dfs(i):

            if i == len(nums):
                return True

            if i in memo:
                return memo[i]

            if i + 1 < len(nums) and nums[i] == nums[i + 1] and dfs(i + 2):
                memo[i] = True
                return True

            if i + 2 < len(nums) and nums[i] == nums[i + 1] == nums[i + 2] and dfs(i + 3):
                memo[i] = True
                return True

            if (
                i + 2 < len(nums)
                and nums[i] + 1 == nums[i + 1]
                and nums[i + 1] + 1 == nums[i + 2]
                and dfs(i + 3)
            ):
                memo[i] = True
                return True

            memo[i] = False
            return False

        return dfs(0)