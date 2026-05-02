# Problem: https://leetcode.com/problems/rotate-list/
# Core trick: Make it circular → then break at correct point and the reconnet
""""
1 → 2 → 3 → 4 → 5, k = 2
1 → 2 → 3  | 4 → 5
      temp     last
4 → 5 → 1 → 2 → 3

""""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        temp = last = head
        length = 1

        while temp.next:
            temp = temp.next
            length += 1
        
        last = temp
        times = k%length
        
        if times == 0:
            return head

        temp = head

        for i in range(length - times - 1):
            temp = temp.next
        
        newHead = temp.next
        temp.next = None
        last.next = head

        return newHead       