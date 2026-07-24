# Problem: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            if char in hashmap:
                _open = stack.pop() if stack else '#'
                if hashmap[char] != _open:
                    return False
            else:
                stack.append(char)
                
        return not stack
