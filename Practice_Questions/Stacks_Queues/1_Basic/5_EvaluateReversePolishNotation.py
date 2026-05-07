# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Core Trick: If token is number, push it. If token is operator, pop num2 then num1, calculate num1 operator num2, and push result back.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in "+-/*":
                stack.append(int(item)) #bit integer cannot be 
                continue

            num2 = stack.pop()
            num1 = stack.pop()
            ans = 0 
            
            if item == '+':
                ans = num1 + num2
            elif item == '-':
                ans = num1 - num2
            elif item == '*':
                ans = num1 * num2
            else:
                ans = int(num1 / num2) #bit integer cannot be 
            
            stack.append(ans)

        return stack.pop()