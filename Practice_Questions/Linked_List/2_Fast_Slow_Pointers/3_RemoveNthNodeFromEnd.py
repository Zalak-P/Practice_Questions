# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        slow = fast = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both until fast reaches last node
        # slow will be at node BEFORE the one to delete
        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete node
        slow.next = slow.next.next

        return dummy.next