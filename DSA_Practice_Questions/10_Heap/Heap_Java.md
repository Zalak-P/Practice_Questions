# Heap and Priority Queue Questions — Java

Each code block is independent. Inputs are non-null and satisfy the stated constraints. Java snippets use standard Java 8+ APIs; platform method signatures may need adapting.

## 1. Min Heap / Max Heap Implementation

Implement a priority queue using a binary heap. The same class supports minimum-first or maximum-first ordering, insertion, removal, peek, and bottom-up heap construction.

[GFG: Min Heap](https://www.geeksforgeeks.org/dsa/introduction-to-min-heap-data-structure/) · [GFG: Max Heap](https://www.geeksforgeeks.org/dsa/introduction-to-max-heap-data-structure/)

```java
import java.util.*;

class BinaryHeap {
    private final List<Integer> heap = new ArrayList<>();
    private final boolean isMin;

    BinaryHeap(int[] values, boolean isMin) {
        this.isMin = isMin;
        for (int value : values) heap.add(value);
        for (int i = heap.size() / 2 - 1; i >= 0; i--) siftDown(i);
    }

    private boolean before(int a, int b) {
        return isMin ? a < b : a > b;
    }

    public int size() {
        return heap.size();
    }

    public int peek() {
        if (heap.isEmpty()) throw new NoSuchElementException("Empty heap");
        return heap.get(0);
    }

    public void push(int value) {
        heap.add(value);
        int i = heap.size() - 1;
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (!before(heap.get(i), heap.get(parent))) break;
            Collections.swap(heap, i, parent);
            i = parent;
        }
    }

    public int pop() {
        int result = peek();
        int last = heap.remove(heap.size() - 1);
        if (!heap.isEmpty()) {
            heap.set(0, last);
            siftDown(0);
        }
        return result;
    }

    private void siftDown(int i) {
        while (2 * i + 1 < heap.size()) {
            int child = 2 * i + 1;
            int right = child + 1;
            if (right < heap.size() && before(heap.get(right), heap.get(child))) {
                child = right;
            }
            if (!before(heap.get(child), heap.get(i))) break;
            Collections.swap(heap, i, child);
            i = child;
        }
    }
}

// true: min heap; false: max heap.
// BinaryHeap minHeap = new BinaryHeap(new int[]{3, 1, 2}, true);
// BinaryHeap maxHeap = new BinaryHeap(new int[]{3, 1, 2}, false);
```

**Time complexity:** Build: O(n). Push/pop: O(log n) amortized with dynamic array storage. Peek/size: O(1).

## 2. Built-in Priority Queue

Use the language library when implementing the heap itself is not required. Python uses negated values for a max heap.

[GFG: Priority Queue using Binary Heap](https://www.geeksforgeeks.org/dsa/priority-queue-using-binary-heap/)

```java
import java.util.*;

class PriorityQueueDemo {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int value : new int[]{3, 1, 2}) {
            minHeap.offer(value);
            maxHeap.offer(value);
        }
        System.out.println(minHeap.peek());
        System.out.println(minHeap.poll());
        System.out.println(maxHeap.peek());
        System.out.println(maxHeap.poll());
    }
}
```

**Time complexity:** Insert/remove: O(log n) amortized; peek: O(1). Java shown initialization: O(n log n); Python heapify: O(n).

## 3. Kth Largest

Return the kth largest value, counting duplicates. Keep the largest k values in a min heap. Requires 1 ≤ k ≤ n.

[LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/)

```java
import java.util.*;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int num : nums) {
            heap.offer(num);
            if (heap.size() > k) heap.poll();
        }
        return heap.peek();
    }
}
```

**Time complexity:** O(n log(k + 1)), where n is the array length.

## 4. Kth Smallest

Return the kth smallest value, counting duplicates. Keep the smallest k values in a max heap. Requires 1 ≤ k ≤ n.

[GFG: Kth Smallest](https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1)

```java
import java.util.*;

class Solution {
    public int kthSmallest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int num : nums) {
            heap.offer(num);
            if (heap.size() > k) heap.poll();
        }
        return heap.peek();
    }
}
```

**Time complexity:** O(n log(k + 1)), where n is the array length.

## 5. Merge K Sorted Arrays

Merge ascending arrays into one sorted result. Store the next available value from each array in a min heap; empty arrays are allowed.

[GFG: Merge K Sorted Arrays](https://www.geeksforgeeks.org/dsa/merge-k-sorted-arrays/)

```java
import java.util.*;

class Solution {
    public List<Integer> mergeKArrays(int[][] arrays) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            Comparator.comparingInt(entry -> entry[0]));
        for (int i = 0; i < arrays.length; i++) {
            if (arrays[i].length > 0) heap.offer(new int[]{arrays[i][0], i, 0});
        }
        List<Integer> result = new ArrayList<>();
        while (!heap.isEmpty()) {
            int[] entry = heap.poll(); // value, array index, element index
            result.add(entry[0]);
            int row = entry[1], next = entry[2] + 1;
            if (next < arrays[row].length) {
                heap.offer(new int[]{arrays[row][next], row, next});
            }
        }
        return result;
    }
}
```

**Time complexity:** O(k + N log(k + 1)), where k is the number of arrays and N is the total number of elements.

## 6. Merge K Sorted Lists

Merge ascending linked lists using a min heap of their current heads. The solution reuses and relinks input nodes. Omit ListNode when the platform supplies it.

[LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/)

```java
import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>(
            Comparator.comparingInt(node -> node.val));
        for (ListNode node : lists) {
            if (node != null) heap.offer(node);
        }
        ListNode dummy = new ListNode(0), tail = dummy;
        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            if (node.next != null) heap.offer(node.next);
            tail.next = node;
            tail = node;
        }
        tail.next = null;
        return dummy.next;
    }
}
```

**Time complexity:** O(k + N log(k + 1)), where k is the number of lists and N is the total number of nodes.

## 7. Top K Frequent

Return the k most frequent distinct values in any order. Count frequencies, then keep k candidates in a min heap. Requires 1 ≤ k ≤ the number of distinct values. This heap approach does not guarantee the LeetCode follow-up’s better-than-O(n log n) bound when k is large.

[LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

```java
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequency = new HashMap<>();
        for (int num : nums) frequency.merge(num, 1, Integer::sum);
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            Comparator.comparingInt((Integer num) -> frequency.get(num)));
        for (int num : frequency.keySet()) {
            heap.offer(num);
            if (heap.size() > k) heap.poll();
        }
        int[] result = new int[k];
        for (int i = 0; i < k; i++) result[i] = heap.poll();
        return result;
    }
}
```

**Time complexity:** O(n + u log(k + 1)) expected, where n is the array length and u is the number of distinct values; assumes average O(1) hash-map operations.

## 8. Median from Data Stream

Maintain a max heap for the lower half and a min heap for the upper half. The lower half has either the same number of values or one extra value.

[LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/)

```java
import java.util.*;

class MedianFinder {
    private final PriorityQueue<Integer> lower = new PriorityQueue<>(Comparator.reverseOrder());
    private final PriorityQueue<Integer> upper = new PriorityQueue<>();

    public void addNum(int num) {
        lower.offer(num);
        upper.offer(lower.poll());
        if (upper.size() > lower.size()) lower.offer(upper.poll());
    }

    public double findMedian() {
        if (lower.isEmpty()) throw new NoSuchElementException("Empty stream");
        if (lower.size() > upper.size()) return lower.peek();
        return ((long) lower.peek() + upper.peek()) / 2.0;
    }
}
```

**Time complexity:** addNum: O(log n) amortized; findMedian: O(1), where n is the number of values inserted.

## 9. Connect N Ropes / Merging Ropes

Connect all ropes with minimum total cost; joining two ropes costs their combined length. Repeatedly merge the two shortest ropes. Assumes nonnegative lengths; zero or one rope costs 0. Both requested rope titles refer to this problem.

[GFG: Min Cost to Connect Ropes](https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1)

```java
import java.util.*;

class Solution {
    public long minCost(int[] ropes) {
        PriorityQueue<Long> heap = new PriorityQueue<>();
        for (int rope : ropes) heap.offer((long) rope);
        long total = 0;
        while (heap.size() > 1) {
            long merged = heap.poll() + heap.poll();
            total += merged;
            heap.offer(merged);
        }
        return total;
    }
}
```

**Time complexity:** O(n log n), where n is the number of ropes.
