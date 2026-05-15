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
            next_node = curr.next
            random_node = curr.random
            if next_node:
                hashmap[curr].next = hashmap[next_node]
            if random_node:
                hashmap[curr].random = hashmap[random_node]
            curr = curr.next

        return hashmap[head]