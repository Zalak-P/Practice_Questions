# Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = temp = head
        count = result = 0
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
            result = max(result, first.val + second.val)
            first = first.next
            second = second.next
        return result 