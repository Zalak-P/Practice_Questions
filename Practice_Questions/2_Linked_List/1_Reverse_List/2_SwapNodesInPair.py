# Problem: https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next is None:
            return head
       
        dummy = ListNode(0)
        prev = dummy
        temp = front = head

        while temp and temp.next:
            front = temp.next
            temp.next = front.next 
            prev.next = front
            front.next = temp
            prev = temp

            temp = temp.next

        return dummy.next