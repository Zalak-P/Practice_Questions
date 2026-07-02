# Problem: https://leetcode.com/problems/target-sum/
# Video Link: https://www.youtube.com/watch?v=zHKfpI5c0_I

# Recursion:
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr_sum = index = 0

        def dfs(index, curr_sum):
            
            if index == len(nums):
                return 1 if curr_sum == target else 0            

            add = dfs(index + 1, curr_sum + nums[index])
            minus = dfs(index + 1, curr_sum - nums[index])
            return add + minus
        
        return dfs(0, 0)
    
# Memoized:
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr_sum = index = 0
        memo = {}
        
        def dfs(index, curr_sum):
            if index == len(nums):
                return 1 if curr_sum == target else 0           

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            add = dfs(index + 1, curr_sum + nums[index])
            minus = dfs(index + 1, curr_sum - nums[index])
            
            memo[(index, curr_sum)] = add + minus
            return memo[(index, curr_sum)]

        return dfs(0, 0)

