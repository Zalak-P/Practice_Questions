# Core Trick: You need to calculate total treapped water everywhere.

class Solution:
    def trap(self, height):
        area = 0
        current = 0
        stack = []
        while current < len(height):
            while len(stack) != 0 and height[current] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if len(stack) == 0:
                    break
                distance = current - stack[-1] - 1
                trapped = (min(height[current], height[stack[-1]]) - height[top])
                area += distance * trapped
            stack.append(current)
            current += 1
        return area