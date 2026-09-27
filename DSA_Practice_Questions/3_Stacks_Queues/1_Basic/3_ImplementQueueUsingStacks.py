# Problem: https://leetcode.com/problems/implement-queue-using-stacks/description/

import queue

class MyQueue:

    def __init__(self):
        self.stack_1 = []   # push stack
        self.stack_2 = []   # pop/peek stack

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def peek(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]

    def empty(self) -> bool:
        if not self.stack_1 and not self.stack_2:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()