# Problem: https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False
        hashset = set()
        curr = head
        while curr:
            if curr in hashset:
                return True
            hashset.add(curr)
            curr = curr.next
        return False

# Use Floyd’s Cycle Detection (slow/fast pointers)
# 👉 O(1) space instead of O(n)
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False