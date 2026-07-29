# Trick to remember

# For each digit:

# Remove all bigger digits before it (while you still can remove).
# Push the current digit.
# If removals are still left after processing all digits, remove from the end.
# Remove leading zeros and return "0" if the result is empty.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for char in num:

            while stack and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1

            stack.append(char)

        while k > 0:
            stack.pop()
            k -= 1

        ans = "".join(stack).lstrip("0")

        return ans if ans else "0"