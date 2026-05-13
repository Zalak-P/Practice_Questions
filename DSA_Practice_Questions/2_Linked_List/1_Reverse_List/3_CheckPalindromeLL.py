# Problem: https://leetcode.com/problems/palindrome-linked-list/description/
# Core trick: 👉 “Reverse the second half of the list, then compare both halves.”

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = temp = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        curr = head
        for i in range(count//2):
            temp = temp.next
        prev = front = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        first = head
        second = prev #now new half-head pointer is prev because list is reversed
        for _ in range(count // 2):
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True