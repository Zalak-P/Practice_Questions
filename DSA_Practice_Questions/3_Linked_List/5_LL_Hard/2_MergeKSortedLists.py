# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Video Soln: https://www.youtube.com/watch?v=1zktEppsdig
# Trick: Put each list head in min-heap. Always pop smallest node, attach it in result list, then push its next node.

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minHeap = []

        # Put first node of every list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode(0)
        temp = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next