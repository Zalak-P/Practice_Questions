# Problem: https://leetcode.com/problems/permutation-in-string/description/
# Core Trick: invalid char = hard reset, don’t touch anything else in this iteration
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = Counter(s1)
        left = right = 0
       
        while right < len(s2):

            # Case: when invalid char encountered
            if s2[right] not in hashmap:
                while left <= right:
                    if s2[left] in hashmap:
                        hashmap[s2[left]] += 1
                    left += 1
                right += 1
                continue   # 🔥 IMPORTANT

            if s2[right] in hashmap:
                hashmap[s2[right]] -= 1

            while hashmap[s2[right]] < 0:
                if s2[right] in hashmap:
                    hashmap[s2[left]] += 1
                left += 1

            if right - left + 1 == len(s1):
                return True 
            right += 1

        return False