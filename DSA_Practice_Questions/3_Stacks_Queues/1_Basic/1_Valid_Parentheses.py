# Problem: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if stack:
                    open_ = stack.pop()
                    if open_ != hashmap[char]:
                        return False
                else:
                    return False
        return True if not stack else False