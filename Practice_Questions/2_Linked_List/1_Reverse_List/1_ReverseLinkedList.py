# Problem: https://takeuforward.org/data-structure/reverse-a-linked-list
# Video Concept Followed: https://www.youtube.com/watch?v=D2vI2DNJGd8

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = front = None
        temp = head
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
            
        return prev