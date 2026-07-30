# Trick:
# - Maintain three pointers:
#   low -> next position of 0
#   mid -> current element
#   high -> next position of 2
# - 0 → swap with low
# - 1 → move mid
# - 2 → swap with high (don't move mid)
# - Time: O(n)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1