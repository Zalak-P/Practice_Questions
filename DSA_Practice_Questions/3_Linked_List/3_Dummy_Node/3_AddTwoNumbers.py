# Problem: https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        val1 = val2 = carry = 0 
        dummy = ListNode(0)
        curr = dummy
        
        while l1 or l2 or carry:
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            total = val1 + val2 + carry
            carry = total//10
            curr.next = ListNode(total%10)
            curr = curr.next

        return dummy.next