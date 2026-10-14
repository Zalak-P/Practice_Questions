# Heap and Priority Queue Questions — Python

Each code block is independent. Inputs are non-null and satisfy the stated constraints. Python snippets use Python 3 standard-library modules.

## 1. Min Heap / Max Heap Implementation

Implement a priority queue using a binary heap. The same class supports minimum-first or maximum-first ordering, insertion, removal, peek, and bottom-up heap construction.

[GFG: Min Heap](https://www.geeksforgeeks.org/dsa/introduction-to-min-heap-data-structure/) · [GFG: Max Heap](https://www.geeksforgeeks.org/dsa/introduction-to-max-heap-data-structure/)

```python
class BinaryHeap:
    def __init__(self, values=(), is_min=True):
        self.heap = list(values)
        self.is_min = is_min
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    def _before(self, a, b):
        return a < b if self.is_min else a > b

    def __len__(self):
        return len(self.heap)

    def peek(self):
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if not self._before(self.heap[i], self.heap[parent]):
                break
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def pop(self):
        result = self.peek()
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return result

    def _sift_down(self, i):
        while 2 * i + 1 < len(self.heap):
            child = 2 * i + 1
            right = child + 1
            if right < len(self.heap) and self._before(self.heap[right], self.heap[child]):
                child = right
            if not self._before(self.heap[child], self.heap[i]):
                break
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child

min_heap = BinaryHeap([3, 1, 2], is_min=True)
max_heap = BinaryHeap([3, 1, 2], is_min=False)
```

**Time complexity:** Build: O(n). Push/pop: O(log n) amortized with dynamic array storage. Peek/size: O(1).

## 2. Built-in Priority Queue

Use the language library when implementing the heap itself is not required. Python uses negated values for a max heap.

[GFG: Priority Queue using Binary Heap](https://www.geeksforgeeks.org/dsa/priority-queue-using-binary-heap/)

```python
import heapq

min_heap = [3, 1, 2]
heapq.heapify(min_heap)
heapq.heappush(min_heap, 0)
minimum = min_heap[0]
removed_minimum = heapq.heappop(min_heap)

max_heap = [-value for value in [3, 1, 2]]
heapq.heapify(max_heap)
heapq.heappush(max_heap, -4)
maximum = -max_heap[0]
removed_maximum = -heapq.heappop(max_heap)
```

**Time complexity:** Insert/remove: O(log n) amortized; peek: O(1). Java shown initialization: O(n log n); Python heapify: O(n).

## 3. Kth Largest

Return the kth largest value, counting duplicates. Keep the largest k values in a min heap. Requires 1 ≤ k ≤ n.

[LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/)

```python
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
```

**Time complexity:** O(n log(k + 1)), where n is the array length.

## 4. Kth Smallest

Return the kth smallest value, counting duplicates. Keep the smallest k values in a max heap. Requires 1 ≤ k ≤ n.

[GFG: Kth Smallest](https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1)

```python
import heapq

class Solution:
    def kthSmallest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)
        return -heap[0]
```

**Time complexity:** O(n log(k + 1)), where n is the array length.

## 5. Merge K Sorted Arrays

Merge ascending arrays into one sorted result. Store the next available value from each array in a min heap; empty arrays are allowed.

[GFG: Merge K Sorted Arrays](https://www.geeksforgeeks.org/dsa/merge-k-sorted-arrays/)

```python
import heapq

class Solution:
    def mergeKArrays(self, arrays):
        heap = [(arr[0], i, 0) for i, arr in enumerate(arrays) if arr]
        heapq.heapify(heap)
        result = []
        while heap:
            value, row, index = heapq.heappop(heap)
            result.append(value)
            next_index = index + 1
            if next_index < len(arrays[row]):
                heapq.heappush(heap, (arrays[row][next_index], row, next_index))
        return result
```

**Time complexity:** O(k + N log(k + 1)), where k is the number of arrays and N is the total number of elements.

## 6. Merge K Sorted Lists

Merge ascending linked lists using a min heap of their current heads. The solution reuses and relinks input nodes. Omit ListNode when the platform supplies it.

[LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/)

```python
import heapq
from itertools import count

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        sequence = count()
        # A unique tie-breaker prevents comparisons between nodes.
        heap = [(node.val, next(sequence), node) for node in lists if node]
        heapq.heapify(heap)
        dummy = ListNode()
        tail = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, next(sequence), node.next))
            tail.next = node
            tail = node
        tail.next = None
        return dummy.next
```

**Time complexity:** O(k + N log(k + 1)), where k is the number of lists and N is the total number of nodes.

## 7. Top K Frequent

Return the k most frequent distinct values in any order. Count frequencies, then keep k candidates in a min heap. Requires 1 ≤ k ≤ the number of distinct values. This heap approach does not guarantee the LeetCode follow-up’s better-than-O(n log n) bound when k is large.

[LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        frequency = Counter(nums)
        heap = []
        for num, freq in frequency.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
```

**Time complexity:** O(n + u log(k + 1)) expected, where n is the array length and u is the number of distinct values; assumes average O(1) hash-map operations.

## 8. Median from Data Stream

Maintain a max heap for the lower half and a min heap for the upper half. The lower half has either the same number of values or one extra value.

[LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/)

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num):
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self):
        if not self.lower:
            raise ValueError("Empty stream")
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2.0
```

**Time complexity:** addNum: O(log n) amortized; findMedian: O(1), where n is the number of values inserted.

## 9. Connect N Ropes / Merging Ropes

Connect all ropes with minimum total cost; joining two ropes costs their combined length. Repeatedly merge the two shortest ropes. Assumes nonnegative lengths; zero or one rope costs 0. Both requested rope titles refer to this problem.

[GFG: Min Cost to Connect Ropes](https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1)

```python
import heapq

class Solution:
    def minCost(self, ropes):
        heap = list(ropes)
        heapq.heapify(heap)
        total = 0
        while len(heap) > 1:
            merged = heapq.heappop(heap) + heapq.heappop(heap)
            total += merged
            heapq.heappush(heap, merged)
        return total
```

**Time complexity:** O(n log n), where n is the number of ropes.
