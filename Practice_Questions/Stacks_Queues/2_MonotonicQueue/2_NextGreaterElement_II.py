# Problem: https://leetcode.com/problems/next-greater-element-ii/
# Core Trick: Traverse array twice using i % n to simulate circular traversal.
# Stack stores indices, not values, (because of duplicates).

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)

        for i in range(2 * len(nums)):
            curr_num = nums[i % len(nums)]
            while stack and nums[stack[-1]] < curr_num:
                index = stack.pop()
                result[index] = curr_num
            # Only push original indices.
            # Second traversal only helps unresolved indices.
            if i < len(nums):
                stack.append(i)

        return result