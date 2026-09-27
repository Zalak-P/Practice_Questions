# Stack and Design Problems — Python Notes

---

## 1. Valid Parentheses

[LeetCode 20](https://leetcode.com/problems/valid-parentheses/)

![Valid Parentheses dry run](images/01_Valid_Parentheses.png)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1: Create an empty stack for opening brackets.
        stack = []

        # Step 2: Map every closing bracket to its matching opening bracket.
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Step 3: Process each character from left to right.
        for char in s:
            # Step 4: If char is a closing bracket,
            # it must match the bracket on top of the stack.
            if char in hashmap:
                # Step 5: Return False when the stack is empty
                # or the top opening bracket does not match.
                if not stack or stack[-1] != hashmap[char]:
                    return False

                # Step 6: Remove the matching opening bracket.
                stack.pop()

            # Step 7: Otherwise, char is an opening bracket.
            else:
                stack.append(char)

        # Step 8: The string is valid only when no opening brackets remain.
        return len(stack) == 0
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 2. Min Stack

[LeetCode 155](https://leetcode.com/problems/min-stack/)

![Min Stack dry run](images/02_Min_Stack.png)

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

**Time:** `O(1)` for every operation  
**Space:** `O(n)`

---

## 3. Next Greater and Next Smaller Element

![Next Greater and Next Smaller Element dry run](images/03_Next_Greater_Smaller.png)

```python
class Solution:
    def nextGreaterElement(self, nums: list[int]) -> list[int]:
        # Step 1: Initialize every answer as -1.
        answer = [-1] * len(nums)

        # Step 2: Stack stores possible next-greater values.
        stack = []

        # Step 3: Traverse from right to left.
        for i in range(len(nums) - 1, -1, -1):
            # Step 4: Remove values that are not greater than nums[i].
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            # Step 5: The remaining top is the next greater element.
            if stack:
                answer[i] = stack[-1]

            # Step 6: Add the current value for elements on its left.
            stack.append(nums[i])

        # Step 7: Return the next-greater array.
        return answer

    def nextSmallerElement(self, nums: list[int]) -> list[int]:
        # Step 1: Initialize every answer as -1.
        answer = [-1] * len(nums)

        # Step 2: Stack stores possible next-smaller values.
        stack = []

        # Step 3: Traverse from right to left.
        for i in range(len(nums) - 1, -1, -1):
            # Step 4: Remove values that are not smaller than nums[i].
            while stack and stack[-1] >= nums[i]:
                stack.pop()

            # Step 5: The remaining top is the next smaller element.
            if stack:
                answer[i] = stack[-1]

            # Step 6: Add the current value for elements on its left.
            stack.append(nums[i])

        # Step 7: Return the next-smaller array.
        return answer
```

**Time:** `O(n)` for each method  
**Space:** `O(n)`

---

## 4. Next Greater Element II

[LeetCode 503](https://leetcode.com/problems/next-greater-element-ii/)

![Next Greater Element II dry run](images/04_Next_Greater_Element_II.png)

```python
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # Step 1: Store the array length.
        n = len(nums)

        # Step 2: Initialize every answer as -1.
        answer = [-1] * n

        # Step 3: Stack stores next-greater candidates.
        stack = []

        # Step 4: Traverse the array twice to simulate circular behavior.
        for i in range(2 * n - 1, -1, -1):
            # Step 5: Convert the extended index to a real array index.
            index = i % n

            # Step 6: Remove values that are not greater than nums[index].
            while stack and stack[-1] <= nums[index]:
                stack.pop()

            # Step 7: Fill answers only during the second traversal
            # when i belongs to the original array range.
            if i < n and stack:
                answer[index] = stack[-1]

            # Step 8: Add the current value as a candidate.
            stack.append(nums[index])

        # Step 9: Return the circular next-greater results.
        return answer
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 5. Largest Rectangle in Histogram

[LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

![Largest Rectangle in Histogram dry run](images/05_Largest_Rectangle_Histogram.png)

```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Step 1: Stack stores indices of bars in increasing-height order.
        stack = []

        # Step 2: Track the largest rectangle found.
        max_area = 0
        n = len(heights)

        # Step 3: Traverse one extra index as a height-0 sentinel.
        for i in range(n + 1):
            # Step 4: Use height 0 at the end to process all remaining bars.
            current_height = 0 if i == n else heights[i]

            # Step 5: Process bars taller than the current height.
            while stack and heights[stack[-1]] > current_height:
                # Step 6: Pop the bar whose maximum rectangle is now known.
                height = heights[stack.pop()]

                # Step 7: Calculate the width available to the popped bar.
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                # Step 8: Update the maximum area.
                max_area = max(max_area, height * width)

            # Step 9: Add the current index to the monotonic stack.
            stack.append(i)

        # Step 10: Return the largest rectangle area.
        return max_area
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 6. Trapping Rain Water

[LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)

![Trapping Rain Water dry run](images/06_Trapping_Rain_Water.png)

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        # Step 1: Start one pointer at each end.
        left = 0
        right = len(height) - 1

        # Step 2: Track the highest wall seen from both sides.
        left_max = 0
        right_max = 0

        # Step 3: Track the total trapped water.
        water = 0

        # Step 4: Move inward until both pointers meet.
        while left < right:
            # Step 5: Process the side with the shorter current wall.
            if height[left] <= height[right]:
                # Step 6: Update the left maximum when a taller wall appears.
                if height[left] >= left_max:
                    left_max = height[left]

                # Step 7: Otherwise, water is trapped above this bar.
                else:
                    water += left_max - height[left]

                # Step 8: Move the left pointer inward.
                left += 1

            else:
                # Step 9: Update the right maximum when a taller wall appears.
                if height[right] >= right_max:
                    right_max = height[right]

                # Step 10: Otherwise, water is trapped above this bar.
                else:
                    water += right_max - height[right]

                # Step 11: Move the right pointer inward.
                right -= 1

        # Step 12: Return the total trapped water.
        return water
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 7. Maximal Rectangle

[LeetCode 85](https://leetcode.com/problems/maximal-rectangle/)

![Maximal Rectangle dry run](images/07_Maximal_Rectangle.png)

```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Step 1: Stack stores increasing histogram-bar indices.
        stack = []

        # Step 2: Track the best histogram rectangle.
        max_area = 0

        # Step 3: Traverse one extra sentinel position.
        for i in range(len(heights) + 1):
            # Step 4: Sentinel height 0 clears the remaining stack.
            current_height = 0 if i == len(heights) else heights[i]

            # Step 5: Process bars taller than the current bar.
            while stack and heights[stack[-1]] > current_height:
                # Step 6: Pop the rectangle height.
                height = heights[stack.pop()]

                # Step 7: Calculate how far this height can extend.
                width = i if not stack else i - stack[-1] - 1

                # Step 8: Update the maximum rectangle area.
                max_area = max(max_area, height * width)

            # Step 9: Add the current index.
            stack.append(i)

        # Step 10: Return the largest histogram rectangle.
        return max_area

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # Step 1: Handle an empty matrix.
        if not matrix:
            return 0

        # Step 2: heights[col] stores consecutive 1s ending at the current row.
        heights = [0] * len(matrix[0])

        # Step 3: Track the best rectangle across all rows.
        max_area = 0

        # Step 4: Process the matrix one row at a time.
        for row in matrix:
            # Step 5: Convert the current row into histogram heights.
            for col in range(len(row)):
                if row[col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            # Step 6: Find the largest histogram rectangle for this row.
            max_area = max(
                max_area,
                self.largestRectangleArea(heights)
            )

        # Step 7: Return the largest all-1 rectangle.
        return max_area
```

**Time:** `O(rows × cols)`  
**Space:** `O(cols)`

---

## 8. Remove K Digits

[LeetCode 402](https://leetcode.com/problems/remove-k-digits/)

![Remove K Digits dry run](images/08_Remove_K_Digits.png)

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Step 1: Use a monotonic increasing stack of digits.
        stack = []

        # Step 2: Process each digit from left to right.
        for digit in num:
            # Step 3: Remove larger previous digits while removals remain.
            # Removing an earlier large digit makes the number smaller.
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            # Step 4: Add the current digit.
            stack.append(digit)

        # Step 5: If removals remain, remove digits from the end.
        if k > 0:
            stack = stack[:-k]

        # Step 6: Build the number and remove leading zeroes.
        answer = "".join(stack).lstrip("0")

        # Step 7: Return "0" when no non-zero digits remain.
        return answer if answer else "0"
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 9. Daily Temperatures

[LeetCode 739](https://leetcode.com/problems/daily-temperatures/)

![Daily Temperatures dry run](images/09_Daily_Temperatures.png)

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Step 1: Initialize all waiting times as zero.
        answer = [0] * len(temperatures)

        # Step 2: Stack stores indices whose warmer day is not known yet.
        stack = []

        # Step 3: Traverse temperatures from left to right.
        for i, temperature in enumerate(temperatures):
            # Step 4: Resolve every previous colder temperature.
            while stack and temperatures[stack[-1]] < temperature:
                previous_index = stack.pop()

                # Step 5: The index difference is the number of days waited.
                answer[previous_index] = i - previous_index

            # Step 6: Add the current day as unresolved.
            stack.append(i)

        # Step 7: Unresolved days remain zero.
        return answer
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 10. Evaluate Reverse Polish Notation

[LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

![Reverse Polish Notation dry run](images/10_Reverse_Polish_Notation.png)

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # Step 1: Stack stores numbers and intermediate results.
        stack = []

        # Step 2: Define the supported operators.
        operators = {"+", "-", "*", "/"}

        # Step 3: Process each token from left to right.
        for token in tokens:
            # Step 4: Push numeric tokens directly onto the stack.
            if token not in operators:
                stack.append(int(token))
                continue

            # Step 5: Pop the right operand first.
            right = stack.pop()

            # Step 6: Pop the left operand second.
            left = stack.pop()

            # Step 7: Apply the current operator.
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                # Division must truncate toward zero.
                result = int(left / right)

            # Step 8: Push the intermediate result back onto the stack.
            stack.append(result)

        # Step 9: The final stack value is the expression result.
        return stack[-1]
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 11. LRU Cache

[LeetCode 146](https://leetcode.com/problems/lru-cache/)

![LRU Cache dry run](images/11_LRU_Cache.png)

```python
class Node:

    def __init__(self, key=0, value=0):
        # Step 1: Store the key and value.
        self.key = key
        self.value = value

        # Step 2: Initialize doubly linked-list pointers.
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # Step 1: Store the cache capacity.
        self.capacity = capacity

        # Step 2: Hashmap gives O(1) access from key to node.
        self.hashmap = {}

        # Step 3: Create dummy left and right boundary nodes.
        self.left = Node()
        self.right = Node()

        # Step 4: Connect the empty doubly linked list.
        # Most recently used nodes stay near left.
        # Least recently used nodes stay near right.
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        # Step 1: Save the neighboring nodes.
        prev_node = node.prev
        next_node = node.next

        # Step 2: Bypass node in both directions.
        prev_node.next = next_node
        next_node.prev = prev_node

    def insertAtFront(self, node: Node) -> None:
        # Step 1: Save the current most-recently-used node.
        front = self.left.next

        # Step 2: Connect left dummy to the new node.
        self.left.next = node
        node.prev = self.left

        # Step 3: Connect the new node to the previous front.
        node.next = front
        front.prev = node

    def get(self, key: int) -> int:
        # Step 1: Return -1 when the key is absent.
        if key not in self.hashmap:
            return -1

        # Step 2: Retrieve the node in O(1).
        node = self.hashmap[key]

        # Step 3: Move the accessed node to the MRU position.
        self.remove(node)
        self.insertAtFront(node)

        # Step 4: Return its stored value.
        return node.value

    def put(self, key: int, value: int) -> None:
        # Step 1: If key already exists, update its node.
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value

            # Step 2: Move the updated node to the MRU position.
            self.remove(node)
            self.insertAtFront(node)
            return

        # Step 3: Create and store a new node.
        node = Node(key, value)
        self.hashmap[key] = node

        # Step 4: Insert the new node at the MRU position.
        self.insertAtFront(node)

        # Step 5: Evict the least-recently-used node if over capacity.
        if len(self.hashmap) > self.capacity:
            least_recent = self.right.prev

            # Step 6: Remove it from the list and hashmap.
            self.remove(least_recent)
            del self.hashmap[least_recent.key]
```

**Time:** `O(1)` for `get` and `put`  
**Space:** `O(capacity)`

---

## 12. Design Browser History

[LeetCode 1472](https://leetcode.com/problems/design-browser-history/)

![Browser History dry run](images/12_Browser_History.png)

```python
class Node:

    def __init__(self, url: str):
        # Step 1: Store the page URL.
        self.url = url

        # Step 2: Initialize links to older and newer pages.
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        # Step 1: Create the homepage node.
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        # Step 1: Create a node for the new page.
        node = Node(url)

        # Step 2: Attach it after the current page.
        # This automatically discards any old forward history.
        self.current.next = node
        node.prev = self.current

        # Step 3: Move current to the newly visited page.
        self.current = node

    def back(self, steps: int) -> str:
        # Step 1: Move to older pages while possible
        # and while backward steps remain.
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1

        # Step 2: Return the page reached.
        return self.current.url

    def forward(self, steps: int) -> str:
        # Step 1: Move to newer pages while possible
        # and while forward steps remain.
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1

        # Step 2: Return the page reached.
        return self.current.url
```

**Time:**
- `visit`: `O(1)`
- `back`: `O(steps)`
- `forward`: `O(steps)`

**Space:** `O(n)`
