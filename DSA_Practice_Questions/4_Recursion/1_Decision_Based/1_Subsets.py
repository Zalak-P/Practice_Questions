class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
         
        def backtrack(start, curr_sol):
            result.append(curr_sol[:])  # add current subset

            for i in range(start, len(nums)):
                curr_sol.append(nums[i])        # include
                backtrack(i + 1, curr_sol)     # recurse
                curr_sol.pop()                 # backtrack

        backtrack(0, [])
        return result