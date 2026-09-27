# Problem: https://takeuforward.org/data-structure/subarray-with-k-different-integers

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.kMost(nums, k) - self.kMost(nums, k-1)

    def kMost(self, nums, k):
        left = right = result = 0
        hashmap = {}

        while right < len(nums):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

            while len(hashmap) > k:
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
            
            result += right - left + 1
            right += 1
            
        return result