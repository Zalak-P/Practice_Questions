# Problem: https://takeuforward.org/data-structure/longest-repeating-character-replacement
# Core Trick: 👉 max_freq = count of the most frequent character in the current window
# Goal = make all characters in the window identical using ≤ k replacements
# Best strategy = keep the most frequent character, replace the rest, “Keep the largest group, fix the rest”
# Replacements needed = window_size - max_freq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = right = result = 0
        hashmap = {}

        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            max_freq = max(hashmap.values())

            while (right - left + 1) - max_freq > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            
            result = max(right - left + 1, result)
            right += 1

        return result