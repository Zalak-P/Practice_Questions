# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        hashmap = {}
        curr = head

        while curr:       
            hashmap[curr] = Node(curr.val)   
            curr = curr.next    

        curr = head 

        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]