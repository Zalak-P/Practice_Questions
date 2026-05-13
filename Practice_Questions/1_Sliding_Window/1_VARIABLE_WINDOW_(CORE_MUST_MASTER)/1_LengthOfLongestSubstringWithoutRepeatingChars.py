# Problem: https://takeuforward.org/data-structure/length-of-longest-substring-without-any-repeating-character
#Khandani Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap = {}
        left = right = 0
        result = 0

        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1    # 🔹 shrink → release character
                left += 1
            
            result = max(result, right - left + 1)
            right += 1

        return result