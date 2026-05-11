# Problem: https://leetcode.com/problems/next-greater-element-ii/
# Core Trick: Traverse array twice using i % n to simulate circular traversal.
# Stack stores indices, not values, (because of duplicates).

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        stack = []
        result = [-1] * n

        for i in range(2 * n):
            curr_num = nums[i % n]

            while stack and nums[stack[-1]] < curr_num:
                index = stack.pop()
                result[index] = curr_num

            # Only push original indices.
            # Second traversal only helps unresolved indices.
            if i < n:
                stack.append(i)

        return result