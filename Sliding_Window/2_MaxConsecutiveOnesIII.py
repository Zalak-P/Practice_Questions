#Problem: https://takeuforward.org/data-structure/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = curr_k = result = 0
        while right < len(nums):
            if nums[right] == 0:
                curr_k += 1
            
            while curr_k > k:
                if nums[left] == 0:
                    curr_k -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1
        return result