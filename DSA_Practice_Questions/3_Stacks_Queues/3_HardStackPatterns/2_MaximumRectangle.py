# Problem: https://leetcode.com/problems/maximal-rectangle/
# Video Soln: https://www.youtube.com/watch?v=sH5yj83ta_Y
# Core Trick: Treat every row as the base of a histogram. Update heights column-wise.
# For every row, run Largest Rectangle in Histogram.

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in range(rows):
            # Build histogram heights
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            stack = []
            for i in range(cols):
                while stack and heights[i] <= heights[stack[-1]]:
                    height = heights[stack.pop()]
                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            # Remaining unresolved bars
            while stack:
                height = heights[stack.pop()]
                if not stack:
                    width = cols
                else:
                    width = cols - stack[-1] - 1
                max_area = max(max_area, height * width)

        return max_area