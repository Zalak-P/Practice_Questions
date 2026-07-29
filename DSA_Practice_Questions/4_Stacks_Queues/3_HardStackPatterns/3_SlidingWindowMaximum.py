# Problem: https://leetcode.com/problems/sliding-window-maximum/
# Trick: Queue stores INDICES, not values. Left of deque always stores index of maximum element for current window.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        result = []

        for i in range(len(nums)):

            # Remove indices outside current window
            while queue and queue[0] <= i - k: 
                queue.popleft()

            # Remove smaller elements because they
            # can never become maximum again
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # Window formed
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result