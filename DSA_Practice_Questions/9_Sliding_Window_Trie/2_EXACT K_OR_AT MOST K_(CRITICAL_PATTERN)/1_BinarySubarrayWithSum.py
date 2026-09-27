# Problem: https://takeuforward.org/data-structure/binary-subarray-with-sum
# Video Soln Followed: https://www.youtube.com/watch?v=XnMdNUkX6VM
# Core Pattern: atMost(k) counts all subarrays with sum ≤ k; atMost(k−1) counts all with sum ≤ k−1.
# Subtracting removes all subarrays with sum < k, leaving only those with sum = k.
# So, exact(k) = atMost(k) − atMost(k−1).

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal) - self.atMost(nums, goal -  1)

    def atMost(self, nums, goal):
        if goal < 0:
            return 0
            
        left = right = result = totalSum = 0

        while right < len(nums):
            totalSum += nums[right]

            while totalSum > goal:
                totalSum -= nums[left]
                left += 1
            
            result += right - left + 1
            right += 1

        return result