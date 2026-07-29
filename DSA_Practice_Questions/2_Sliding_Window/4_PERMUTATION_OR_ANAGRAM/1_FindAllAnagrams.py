# Problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Core Trick: 👉 Invalid characters are not tracked in the hashmap, so they don’t trigger any shrink condition.
# 👉 So you reset by: moving left to → right + 1

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = Counter(p)
        left = right = 0
        result = []

        while right < len(s):

            # 🔴 Case 1: invalid char → RESET window
            if s[right] not in hashmap:
                while left <= right:
                    if s[left] in hashmap:
                        hashmap[s[left]] += 1
                    left += 1
                right += 1
                continue   # 🔥 IMPORTANT
            
            # Traditional Sliding Window starts from here
            if s[right] in hashmap:
                hashmap[s[right]] -= 1
            
            while hashmap[s[right]] < 0:
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                left += 1
            
            # check window size - 👉 Even if frequencies match, if length ≠ len(p), it’s not a valid anagram.
            if right - left + 1 == len(p):
                result.append(left)
            right += 1

        return result
