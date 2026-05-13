# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Core Trick: Stack stores indices of increasing heights.
# When smaller height appears, popped bar gets:
# left boundary = stack[-1]
# right boundary = current index i
# So rectangle exists between: previous smaller element and next smaller element

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            if not stack:
                width = len(heights)
            else:
                width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area