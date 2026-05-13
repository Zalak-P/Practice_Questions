from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge case:
        # If list is empty OR k = 1, no reversal needed.
        if head is None or k == 1:
            return head

        # ---------------------------------------------------
        # STEP 1: Find newHead
        # ---------------------------------------------------
        # In the first group, kth node becomes the final head.
        #
        # Example:
        # 1 → 2 → 3 → 4 → 5, k = 3
        # First group: 1 → 2 → 3
        # After reverse: 3 → 2 → 1
        # So newHead = 3
        temp = head

        for _ in range(k - 1):
            if temp is None:
                return head
            temp = temp.next

        if temp is None:
            return head

        newHead = temp

        # ---------------------------------------------------
        # Pointer meaning
        # ---------------------------------------------------
        # groupHead = start of current group
        #             old head of group
        #             becomes tail after reversal
        #
        # prevGroup = tail of previous reversed group
        #
        # nextGroup = first node after current k-group
        #
        # prev = new head of current reversed group
        #
        # temp = moving pointer used for check/reversal
        prevGroup = None
        groupHead = head

        # ---------------------------------------------------
        # STEP 2: Process every k-group
        # ---------------------------------------------------
        while groupHead is not None:

            # ---------------------------------------------------
            # Check if k nodes exist from groupHead
            # ---------------------------------------------------
            # Important:
            # We must check from the same node that we will reverse.
            #
            # Check:
            # "Do I have k nodes from groupHead?"
            #
            # Reverse:
            # "Reverse k nodes from groupHead."
            #
            # So both must start from groupHead.
            temp = groupHead
            i = 0

            while i < k:
                if temp is None:
                    return newHead
                temp = temp.next
                i += 1

            # After checking k nodes, temp is now at node after kth node.
            # This is the start of next group.
            nextGroup = temp

            # ---------------------------------------------------
            # Reverse k nodes
            # ---------------------------------------------------
            # Example:
            # 1 → 2 → 3 → 4 → 5, k = 3
            #
            # groupHead = 1
            # nextGroup = 4
            #
            # Set:
            # prev = nextGroup = 4
            # temp = groupHead = 1
            #
            # Why prev = nextGroup?
            # Because old head becomes tail after reversal.
            # So 1 should point to 4 automatically.
            temp = groupHead
            prev = nextGroup
            i = 0

            while i < k:
                front = temp.next      # save next node
                temp.next = prev       # reverse link
                prev = temp            # move prev
                temp = front           # move temp
                i += 1

            # ---------------------------------------------------
            # After reversal
            # ---------------------------------------------------
            # prev = new head of reversed group
            # groupHead = old head = now tail of reversed group
            #
            # Example:
            # Before: 1 → 2 → 3 → 4
            # After:  3 → 2 → 1 → 4
            #
            # prev = 3
            # groupHead = 1

            # ---------------------------------------------------
            # Stitch previous group to current reversed group
            # ---------------------------------------------------
            # For first group:
            # prevGroup = None
            # So nothing to connect before it.
            #
            # For second group onwards:
            # prevGroup is previous reversed group's tail.
            #
            # Example:
            # After first group:
            # 3 → 2 → 1 → 4 → 5 → 6
            # prevGroup = 1
            #
            # After reversing second group:
            # prev = 6
            #
            # Need:
            # 1.next = 6
            if prevGroup:
                prevGroup.next = prev

            # ---------------------------------------------------
            # Move pointers for next group
            # ---------------------------------------------------
            # groupHead was old head.
            # After reversal, it becomes tail.
            #
            # So now:
            # prevGroup = groupHead
            #
            # next group starts at nextGroup.
            prevGroup = groupHead
            groupHead = nextGroup

        return newHead