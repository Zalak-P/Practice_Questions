# https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        hashset = set()
        while curr1:
            if curr1 not in hashset:
                hashset.add(curr1)
            curr1 = curr1.next
            
        while curr2:
            if curr2 in hashset:
                return curr2
            curr2 = curr2.next