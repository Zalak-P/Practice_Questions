# Problem: https://takeuforward.org/data-structure/count-number-of-nice-subarrays

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.kMost(nums, k) - self.kMost(nums, k-1)
        
    def kMost(self, nums, k):
        
        left = right = result = totalCount = 0

        while right < len(nums):
            if nums[right]%2 == 1:
                totalCount += 1

            while totalCount > k:
                if nums[left]%2 == 1:
                    totalCount -= 1 
                left += 1
            
            result += right - left + 1
            right += 1
        
        return result
