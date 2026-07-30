import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -------------------------------
# 1. BRUTE FORCE
# -------------------------------
class SolutionArray:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next

        return random.choice(arr)

"""
Time:  O(n) per call
Space: O(n)
"""
# ---------------------------------------
# 2. OPTIMAL (Reservoir Sampling - k = 1)
# ---------------------------------------
class SolutionArray:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        temp = self.head
        result = temp.val
        i = 1

        while temp:
            # Pick current node with probability 1/i
            if random.randint(1, i) == 1:
                result = temp.val
            temp = temp.next
            i += 1
        
        return result

"""
Time:  O(n)
Space: O(1)

Core Trick: 👉 “At every node, give it a fresh chance: pick it with probability 1 / (nodes seen so far)”
Use when:
→ Linked list size unknown / too large
→ Cannot store all elements
"""