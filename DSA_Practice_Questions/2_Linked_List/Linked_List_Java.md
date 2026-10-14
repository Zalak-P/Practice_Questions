# Linked List — Must-Do Problems in Java

## ListNode

```java
class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}
```

## 1. Reverse a Linked List

Reverse the next pointers and return the new head.

[LeetCode 206](https://leetcode.com/problems/reverse-linked-list/)

### Iterative

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, temp = head;
        while (temp != null) {
            ListNode front = temp.next;
            temp.next = prev;
            prev = temp;
            temp = front;
        }
        return prev;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(1).

### Recursive

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n) recursion stack.

## 2. Cycle Detection, Start, and Length

Use slow and fast pointers to detect a cycle, find its starting node, and count its nodes. Return null for a missing cycle start and 0 for a missing cycle length.

[LeetCode 141](https://leetcode.com/problems/linked-list-cycle/) · [LeetCode 142](https://leetcode.com/problems/linked-list-cycle-ii/)

```java
class Solution {
    private ListNode getMeetingPoint(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return slow;
        }
        return null;
    }

    public boolean hasCycle(ListNode head) {
        return getMeetingPoint(head) != null;
    }

    public ListNode detectCycle(ListNode head) {
        ListNode meeting = getMeetingPoint(head);
        if (meeting == null) return null;
        ListNode temp = head;
        while (temp != meeting) {
            temp = temp.next;
            meeting = meeting.next;
        }
        return temp;
    }

    public int cycleLength(ListNode head) {
        ListNode meeting = getMeetingPoint(head);
        if (meeting == null) return 0;
        int count = 1;
        ListNode temp = meeting.next;
        while (temp != meeting) {
            count++;
            temp = temp.next;
        }
        return count;
    }
}
```

**Time complexity:** O(n) per operation, where n is the number of distinct reachable nodes.

**Space complexity:** O(1).

## 3. Add Two Numbers

Add two numbers represented by reverse-order digit lists. Build a new list and carry any overflow to the next digit.

[LeetCode 2](https://leetcode.com/problems/add-two-numbers/)

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode dummy = new ListNode(0), current = dummy;
        while (l1 != null || l2 != null || carry != 0) {
            int val1 = l1 == null ? 0 : l1.val;
            int val2 = l2 == null ? 0 : l2.val;
            int total = val1 + val2 + carry;
            carry = total / 10;
            current.next = new ListNode(total % 10);
            current = current.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        return dummy.next;
    }
}
```

**Time complexity:** O(max(m, n)), where m and n are the input lengths.

**Space complexity:** O(1) auxiliary; O(max(m, n)) for the output list.

## 4. Merge Two Sorted Lists

Merge two ascending linked lists by reusing their nodes.

[LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/)

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0), tail = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        tail.next = list1 != null ? list1 : list2;
        return dummy.next;
    }
}
```

**Time complexity:** O(m + n), where m and n are the input lengths.

**Space complexity:** O(1).

## 5. Intersection of Two Lists

Find the first shared node of two acyclic lists. Intersection means the same node object, not equal values. Switch each pointer to the other head when it reaches the end.

[LeetCode 160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

```java
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode current1 = headA, current2 = headB;
        while (current1 != current2) {
            current1 = current1 == null ? headB : current1.next;
            current2 = current2 == null ? headA : current2.next;
        }
        return current1;
    }
}
```

**Time complexity:** O(m + n), where m and n are the input lengths.

**Space complexity:** O(1).

## 6. Remove Nth Node From End

Remove the nth node counted from the end, where 1 ≤ n ≤ list length. A dummy node handles removal of the head.

[LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy, fast = dummy;
        for (int i = 0; i < n; i++) fast = fast.next;
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

**Time complexity:** O(L), where L is the list length.

**Space complexity:** O(1).

## 7. Clone List with Random Pointers

Deep-copy a list whose random pointers reference any node in the list or null. Interleave copies with originals, assign random links, then separate the lists and restore the original.

[LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/)

```java
class Node {
    int val;
    Node next, random;

    Node(int val) {
        this.val = val;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        Node temp = head;
        while (temp != null) {
            Node front = temp.next;
            Node copy = new Node(temp.val);
            temp.next = copy;
            copy.next = front;
            temp = front;
        }
        temp = head;
        while (temp != null) {
            Node copy = temp.next;
            // Each original node's copy is immediately after it.
            copy.random = temp.random == null ? null : temp.random.next;
            temp = copy.next;
        }
        Node copyHead = head.next;
        temp = head;
        while (temp != null) {
            Node copy = temp.next;
            Node front = copy.next;
            temp.next = front;
            copy.next = front == null ? null : front.next;
            temp = front;
        }
        return copyHead;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(1) auxiliary; O(n) for the cloned list.

## 8. Flatten Sorted Child Lists

Multiple sorted vertical lists are connected horizontally through next. Merge them into one sorted list through child pointers. The GFG version calls the vertical pointer bottom; this code preserves child from the source.

[GeeksforGeeks: Flattening a Linked List](https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1)

```java
class Node {
    int data;
    Node next, child;

    Node(int data) {
        this.data = data;
    }
}

class Solution {
    private Node merge(Node list1, Node list2) {
        Node dummy = new Node(-1), tail = dummy;
        while (list1 != null && list2 != null) {
            if (list1.data <= list2.data) {
                tail.child = list1;
                list1 = list1.child;
            } else {
                tail.child = list2;
                list2 = list2.child;
            }
            tail = tail.child;
            tail.next = null;
        }
        tail.child = list1 != null ? list1 : list2;
        return dummy.child;
    }

    public Node flatten(Node head) {
        if (head == null || head.next == null) return head;
        Node flattenedRight = flatten(head.next);
        head.next = null;
        return merge(head, flattenedRight);
    }
}
```

**Time complexity:** O(N × k) upper bound for sequential recursive merging, where N is the total node count and k is the number of vertical lists; O(N²) in the worst case.

**Space complexity:** O(k) recursion stack.

## 9. Flatten Multilevel Doubly Linked List

Flatten child lists in depth-first order, inserting each child immediately after its parent. Preserve next/prev links and clear all child pointers.

[LeetCode 430](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

```java
class Node {
    int val;
    Node prev, next, child;

    Node(int val) {
        this.val = val;
    }
}

class Solution {
    public Node flatten(Node head) {
        if (head == null) return null;
        flattenLevel(head);
        return head;
    }

    private Node flattenLevel(Node node) {
        Node temp = node, tail = node;
        while (temp != null) {
            Node front = temp.next;
            if (temp.child != null) {
                Node childHead = temp.child;
                Node childTail = flattenLevel(childHead);
                temp.next = childHead;
                childHead.prev = temp;
                temp.child = null;
                childTail.next = front;
                if (front != null) front.prev = childTail;
                tail = childTail;
            } else {
                tail = temp;
            }
            temp = front;
        }
        return tail;
    }
}
```

**Time complexity:** O(n), where n is the total node count.

**Space complexity:** O(d), where d is the number of nested levels; O(n) worst case.

## 10. Rotate List Right by K

Rotate a list right by k positions, where k ≥ 0. Reduce k modulo the length, temporarily form a circle, then break it at the new tail.

[LeetCode 61](https://leetcode.com/problems/rotate-list/)

```java
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;
        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }
        k %= length;
        if (k == 0) return head;
        tail.next = head;
        ListNode newTail = head;
        for (int i = 0; i < length - k - 1; i++) newTail = newTail.next;
        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(1).

## 11. Reverse Nodes in K-Group

Reverse each complete group of k nodes, where k ≥ 1. Leave an incomplete final group unchanged.

[LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group/)

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode previousGroup = dummy;
        while (true) {
            ListNode kth = previousGroup;
            for (int i = 0; i < k && kth != null; i++) kth = kth.next;
            if (kth == null) break;

            ListNode nextGroup = kth.next;
            ListNode groupHead = previousGroup.next;
            ListNode current = groupHead, previous = nextGroup;
            while (current != nextGroup) {
                ListNode front = current.next;
                current.next = previous;
                previous = current;
                current = front;
            }
            previousGroup.next = kth;
            previousGroup = groupHead; // The old head is now the group's tail.
        }
        return dummy.next;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(1).
