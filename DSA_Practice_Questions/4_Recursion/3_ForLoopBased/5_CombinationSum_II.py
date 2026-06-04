# Problem: https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, curr_soln):
            if sum(curr_soln) > target:
                return
                            
            if sum(curr_soln) == target:
                result.append(curr_soln[:])
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                        continue

                curr_soln.append(candidates[i])
                backtrack(i + 1, curr_soln)
                curr_soln.pop()

        backtrack(0, [])
        return result