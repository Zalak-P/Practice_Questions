# Linked List — Must-Do Problems

The Python solutions below use the same code and variable style from the supplied GitHub repository wherever a matching implementation exists. Missing repository implementations and cases where the repository approach did not match the generated dry run use a matching optimized solution.

Repository: <https://github.com/Zalak-P/Practice_Questions/tree/main/DSA_Practice_Questions/3_Linked_List/1_MUST_DO>

---

## 1. Reverse a Linked List — Iterative and Recursive

![Reverse a Linked List dry run](images/01_Reverse_Linked_List.png)

### Iterative

```python
class Solution:
    def reverseList(self, head):
        prev = front = None
        temp = head

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
```

### Recursive

```python
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
```

- Iterative: Time `O(n)`, Space `O(1)`
- Recursive: Time `O(n)`, Space `O(n)`

---

## 2. Loop Detection, Starting Point, and Loop Length

![Linked List Loop dry run](images/02_Linked_List_Loop.png)

```python
class Solution:
    def getMeetingPoint(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def hasCycle(self, head):
        return self.getMeetingPoint(head) is not None

    def detectCycle(self, head):
        meeting = self.getMeetingPoint(head)

        if meeting is None:
            return None

        temp = head

        while temp != meeting:
            temp = temp.next
            meeting = meeting.next

        return temp

    def cycleLength(self, head):
        meeting = self.getMeetingPoint(head)

        if meeting is None:
            return 0

        count = 1
        temp = meeting.next

        while temp != meeting:
            count += 1
            temp = temp.next

        return count
```

- Time: `O(n)`
- Space: `O(1)`

---

## 3. Add Two Numbers

[LeetCode 2](https://leetcode.com/problems/add-two-numbers/)

![Add Two Numbers dry run](images/03_Add_Two_Numbers.png)

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
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
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

        return dummy.next
```

- Time: `O(max(m, n))`
- Auxiliary space: `O(1)`, excluding the output list

---

## 4. Merge Two Sorted Linked Lists

[LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/)

![Merge Two Sorted Linked Lists dry run](images/04_Merge_Two_Sorted_Lists.png)

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        l1 = list1
        l2 = list2

        dummy = ListNode(0)
        temp = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        temp.next = l1 if l1 else l2

        return dummy.next
```

- Time: `O(m + n)`
- Space: `O(1)`

---

## 5. Intersection Point of Two Linked Lists

[LeetCode 160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

![Intersection of Two Linked Lists dry run](images/05_Intersection_of_Two_Lists.png)

```python
class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        curr1 = headA
        curr2 = headB

        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA

        return curr1
```

- Time: `O(m + n)`
- Space: `O(1)`

---

## 6. Remove Nth Node From the End

[LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

![Remove Nth Node From End dry run](images/06_Remove_Nth_From_End.png)

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
```

- Time: `O(n)`
- Space: `O(1)`

---

## 7. Clone a Linked List With Next and Random Pointers

[LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/)

![Clone Linked List With Random Pointer dry run](images/07_Clone_List_Random_Pointer.png)

```python
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        temp = head

        # Insert each copied node after its original node.
        while temp:
            front = temp.next
            copy = Node(temp.val)

            temp.next = copy
            copy.next = front

            temp = front

        temp = head

        # Assign random pointers to copied nodes.
        while temp:
            copy = temp.next

            if temp.random:
                copy.random = temp.random.next

            temp = copy.next

        temp = head
        copy_head = head.next

        # Separate the original and copied lists.
        while temp:
            copy = temp.next
            front = copy.next

            temp.next = front
            copy.next = front.next if front else None

            temp = front

        return copy_head
```

- Time: `O(n)`
- Auxiliary space: `O(1)`, excluding the cloned list

---

## 8. Flatten a Linked List Using Next and Child Pointers

This version contains multiple sorted vertical lists connected by `next`. The final sorted list is connected through `child`.

![Flatten Linked List With Next and Child dry run](images/08_Flatten_Next_Child_List.png)

```python
class Solution:
    def merge(self, list1, list2):
        dummy = Node(-1)
        temp = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                temp.child = list1
                list1 = list1.child
            else:
                temp.child = list2
                list2 = list2.child

            temp = temp.child
            temp.next = None

        temp.child = list1 if list1 else list2

        return dummy.child

    def flatten(self, head):
        if head is None or head.next is None:
            return head

        flattened_right = self.flatten(head.next)

        head.next = None

        return self.merge(head, flattened_right)
```

- Time: up to `O(n²)` for the common recursive merge approach
- Recursive space: `O(n)` in the worst case

---

## 9. Flatten a Multilevel Doubly Linked List

[LeetCode 430](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

![Flatten Multilevel Doubly Linked List dry run](images/09_Flatten_Multilevel_DLL.png)

```python
class Solution:
    def flatten(self, head):
        if head is None:
            return None

        def flattenLevel(node):
            temp = node
            tail = node

            while temp:
                front = temp.next

                if temp.child:
                    child_head = temp.child
                    child_tail = flattenLevel(child_head)

                    temp.next = child_head
                    child_head.prev = temp
                    temp.child = None

                    if front:
                        child_tail.next = front
                        front.prev = child_tail

                    tail = child_tail
                else:
                    tail = temp

                temp = front

            return tail

        flattenLevel(head)

        return head
```

- Time: `O(n)`
- Recursive space: `O(d)`, where `d` is the maximum child depth

---

## 10. Rotate a Linked List to the Right by K

[LeetCode 61](https://leetcode.com/problems/rotate-list/)

![Rotate Linked List by K dry run](images/10_Rotate_List_By_K.png)

```python
class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if k == 0:
            return head

        tail.next = head

        steps_to_new_tail = length - k - 1
        new_tail = head

        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
```

- Time: `O(n)`
- Space: `O(1)`

---

## 11. Reverse Nodes in K-Group

[LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group/)

![Reverse Nodes in K-Group dry run](images/11_Reverse_Nodes_K_Group.png)

```python
class Solution:
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        temp = head

        for _ in range(k - 1):
            if temp is None:
                return head

            temp = temp.next

        if temp is None:
            return head

        newHead = temp
        groupHead = head
        prevGroup = None

        while groupHead:
            temp = groupHead
            i = 0

            while i < k:
                if temp is None:
                    return newHead

                temp = temp.next
                i += 1

            nextGroup = temp

            temp = groupHead
            prev = nextGroup
            i = 0

            while i < k:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
                i += 1

            if prevGroup:
                prevGroup.next = prev

            prevGroup = groupHead
            groupHead = nextGroup

        return newHead
```

- Time: `O(n)`
- Space: `O(1)`
