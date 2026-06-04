class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr_soln):
            if len(curr_soln) == k and sum(curr_soln) == n:
                result.append(curr_soln[:])
                return

            if len(curr_soln) > k or sum(curr_soln) > n:
                return

            for i in range(start, 10):
                curr_soln.append(i)
                backtrack(i+1, curr_soln)
                curr_soln.pop()

        backtrack(1, [])
        return result