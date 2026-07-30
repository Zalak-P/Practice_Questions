# Trick:
# - Start from both ends.
# - Area = min(leftHeight, rightHeight) × width.
# - Move the shorter wall because moving the taller one can never increase the area.
# - Time: O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans