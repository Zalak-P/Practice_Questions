# Problem: https://takeuforward.org/data-structure/number-of-substring-containing-all-three-characters
# Video Soln Followed: https://www.youtube.com/watch?v=wafDgldM9MA
# Core trick: 👉 When your window becomes valid, don’t count just one substring. (i.e. result += 1)
# 👉 Instead, count all possible substrings starting at left. Every extension to the right will still be valid.
# You won’t come back to this same starting point again

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        left = right = result = 0
        hashmap = {}

        while right < len(s):

            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            while len(hashmap) == 3:
                result += len(s) - right
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            
            right += 1 

        return result