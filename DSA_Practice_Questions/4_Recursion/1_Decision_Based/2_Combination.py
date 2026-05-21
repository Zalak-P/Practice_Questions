# Problems: https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
         
        def backtrack(start, curr_sol):
            if len(curr_sol) == k:
                result.append(curr_sol[:])  # add current subset
                return

            for i in range(start, n+1):
                curr_sol.append(i)        # include
                backtrack(i + 1, curr_sol)     # recurse
                curr_sol.pop()                 # backtrack

        backtrack(1, [])
        return result 