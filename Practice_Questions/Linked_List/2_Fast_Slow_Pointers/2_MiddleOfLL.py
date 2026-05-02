# Problem: https://leetcode.com/problems/middle-of-the-linked-list/description/
"""
FIRST MIDDLE vs SECOND MIDDLE

Rule:
- Second middle → use: while fast and fast.next
- First middle  → use: while fast.next and fast.next.next

Example:
1 -> 2 -> 3 -> 4

Second middle = 3
First middle  = 2

Use cases:
- Need second half (palindrome, twin sum) → SECOND middle
- Need to split list (reorder list)      → FIRST middle
"""


# SECOND MIDDLE (default)
def get_second_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # returns 3 for [1,2,3,4]


# FIRST MIDDLE (for splitting)
def get_first_middle(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # returns 2 for [1,2,3,4]