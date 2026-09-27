# Problem: https://takeuforward.org/data-structure/maximum-point-you-can-obtain-from-cards
# Video Soln Approach: https://www.youtube.com/watch?v=pBWCOCS636U&t=1s
# Core Trick:  Loop runs k times to for all right-side picks

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = sum(cardPoints[:k]) 
        rsum = 0
        left = k - 1
        right = len(cardPoints) - 1

        result = lsum #result initialized with base case

        # MIMP - How many iterations to run ? Only K. 
        i = 1
        while i <= k:
            lsum -= cardPoints[left]
            rsum += cardPoints[right]
            result = max(result, lsum + rsum)
            left -= 1
            right -= 1
            i += 1

        return result
