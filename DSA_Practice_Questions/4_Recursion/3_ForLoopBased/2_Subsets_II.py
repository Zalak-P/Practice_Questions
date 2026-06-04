# Problem: https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, curr_soln):
            result.append(curr_soln[:])

            for i in range(start, len(nums)):
                
                if i > start and nums[i] == nums[i - 1]:
                    continue

                curr_soln.append(nums[i])
                backtrack(i + 1, curr_soln)
                curr_soln.pop()

        backtrack(0, [])
        
        return result