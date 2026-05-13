# Problem: https://leetcode.com/problems/next-greater-element-i/
# Core Trick: We are NOT looking for the greatest element on the right. 
# We are looking for the FIRST discovered greater element on the right.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        while stack: # Numbers left in stack never found any greater element on their right.
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]