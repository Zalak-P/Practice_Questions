class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        hashmap = Counter(t)
        left = right = counter = 0
        curr_min = float('inf')
        result = ""

        while right < len(s):

            # 🔹 expand → consume character
            if hashmap[s[right]] > 0:
                counter += 1
            hashmap[s[right]] -= 1

            # 🔹 when all chars matched
            while counter == len(t):
                # update result
                if right - left + 1 < curr_min:
                    curr_min = right - left + 1
                    result = s[left:right+1]

                # 🔹 shrink → release character
                hashmap[s[left]] += 1
                if hashmap[s[left]] > 0:
                    counter -= 1

                left += 1
                
            right += 1
        return result