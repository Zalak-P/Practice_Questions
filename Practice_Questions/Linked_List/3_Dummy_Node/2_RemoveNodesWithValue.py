# Problem: https://leetcode.com/problems/remove-linked-list-elements/description/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
        