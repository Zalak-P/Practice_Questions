# Problem: https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = right = totalSum = result = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                totalSum += customers[i]

        while right < len(customers):
            if grumpy[right] == 1:
                totalSum += customers[right]
            
            while right - left + 1 > minutes:
                if grumpy[left] == 1:
                    totalSum -= customers[left]
                left += 1

            result = max(result, totalSum)
            right += 1
        
        return result

        