# Problem: https://leetcode.com/problems/odd-even-linked-list/

"""
MISTAKE IN PATTERN RECOGNITION (Odd-Even Linked List)

What I did:
- Treated this like a "swap / reverse" problem
- Tried to break links and rearrange nodes in-place

Why it's wrong:
- This problem is NOT about reversing or swapping
- It requires GROUPING while preserving order

Correct pattern:
- Maintain TWO chains:
    odd list  (1st, 3rd, 5th...)
    even list (2nd, 4th, 6th...)
- Then connect odd → even

"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        front = even_head = head.next
        
        while front and front.next:
            temp.next = front.next            
            temp = temp.next

            front.next = temp.next
            front = front.next

        temp.next = even_head

        return head        