# Problem: https://takeuforward.org/data-structure/reverse-linked-list-in-groups-of-size-k
# Core Trick: groupHead is old head/future tail, prev is new head after reverse.
# Stitch: prevGroup.next = prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or k == 1:
            return head

        # Find newHead = kth node
        temp = head
        for _ in range(k - 1):
            if temp is None:
                return head
            temp = temp.next
        if temp is None:
            return head
        newHead = temp
        groupHead = head
        prevGroup = None

        while groupHead:
            # Check k nodes exist from groupHead, if yes then define nextGroup
            temp = groupHead
            i = 0
            while i < k:
                if temp is None:
                    return newHead
                temp = temp.next
                i += 1
            nextGroup = temp

            # Reverse k nodes
            temp = groupHead
            prev = nextGroup
            i = 0
            while i < k:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
                i += 1

            # Connect previous group tail to current reversed head
            if prevGroup:  # first group is skipped because prevGroup = None
                prevGroup.next = prev
            # Move pointers
            prevGroup = groupHead
            groupHead = nextGroup

        return newHead