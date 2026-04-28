class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hashmap = {'a', 'e', 'i', 'o', 'u'}
        left = right = counter = result = 0

        while right < len(s):
            if s[right] in hashmap:
                counter += 1

            if right - left + 1 > k:
                if s[left] in hashmap:
                    counter -= 1
                left += 1
            
            result = max(result, counter)
            right += 1
            
        return result
