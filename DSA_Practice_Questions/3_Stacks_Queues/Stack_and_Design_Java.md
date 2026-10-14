# Stack and Design Problems — Java

## 1. Valid Parentheses

Check whether opening and closing brackets are correctly matched and nested.

[LeetCode 20](https://leetcode.com/problems/valid-parentheses/)

```java
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) return false;
                char open = stack.pop();
                if ((ch == ')' && open != '(')
                        || (ch == ']' && open != '[')
                        || (ch == '}' && open != '{')) return false;
            }
        }
        return stack.isEmpty();
    }
}
```

**Time complexity:** O(n), where n is the string length.

**Space complexity:** O(n).

## 2. Min Stack

Support push, pop, top, and retrieving the minimum. A second stack stores minimum values, including duplicates. Pop, top, and getMin are called only on a nonempty stack.

[LeetCode 155](https://leetcode.com/problems/min-stack/)

```java
import java.util.*;

class MinStack {
    private final Deque<Integer> stack = new ArrayDeque<>();
    private final Deque<Integer> minStack = new ArrayDeque<>();

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) minStack.push(val);
    }

    public void pop() {
        int value = stack.pop();
        if (value == minStack.peek()) minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
```

**Time complexity:** Push: O(1) amortized; pop, top, and getMin: O(1).

**Space complexity:** O(n), where n is the number of stored values.

## 3. Next Greater and Next Smaller

For every position, return the first strictly greater or strictly smaller value to its right, or −1 if none exists. Scan right to left using a monotonic stack.

[GeeksforGeeks: Next Greater Element](https://www.geeksforgeeks.org/dsa/next-greater-element/) · [Next Smaller Element](https://www.geeksforgeeks.org/dsa/next-smaller-element/)

```java
import java.util.*;

class Solution {
    public int[] nextGreaterElement(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i]) stack.pop();
            if (!stack.isEmpty()) answer[i] = stack.peek();
            stack.push(nums[i]);
        }
        return answer;
    }

    public int[] nextSmallerElement(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() >= nums[i]) stack.pop();
            if (!stack.isEmpty()) answer[i] = stack.peek();
            stack.push(nums[i]);
        }
        return answer;
    }
}
```

**Time complexity:** O(n) per method.

**Space complexity:** O(n).

## 4. Next Greater Element II

Find the next strictly greater value in a circular array, or −1 if none exists. Traverse twice to account for wraparound.

[LeetCode 503](https://leetcode.com/problems/next-greater-element-ii/)

```java
import java.util.*;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        Arrays.fill(answer, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 2 * n - 1; i >= 0; i--) {
            int index = i % n;
            while (!stack.isEmpty() && stack.peek() <= nums[index]) stack.pop();
            if (i < n && !stack.isEmpty()) answer[index] = stack.peek();
            stack.push(nums[index]);
        }
        return answer;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n).

## 5. Largest Rectangle in Histogram

Find the maximum rectangle area under unit-width histogram bars. A monotonic stack identifies each popped bar’s available width.

[LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

```java
import java.util.*;

class Solution {

    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        for (int i = 0; i <= heights.length; i++) {
            int currentHeight = i == heights.length ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > currentHeight) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            if (i < heights.length) stack.push(i);
        }
        return maxArea;
    }
}
```

**Time complexity:** O(n), since each index is pushed and popped at most once.

**Space complexity:** O(n).

## 6. Trapping Rain Water

Calculate trapped water above nonnegative unit-width bars. Move inward from the shorter side, tracking the highest wall seen from each end.

[LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (left < right) {
            if (height[left] <= height[right]) {
                leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
                left++;
            } else {
                rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(1).

## 7. Maximal Rectangle

Find the largest all-1 rectangle in a character matrix. Convert each row into consecutive-one heights and solve a histogram problem.

[LeetCode 85](https://leetcode.com/problems/maximal-rectangle/)

```java
import java.util.*;

class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int[] heights = new int[matrix[0].length];
        int maxArea = 0;
        for (char[] row : matrix) {
            for (int col = 0; col < row.length; col++) {
                heights[col] = row[col] == '1' ? heights[col] + 1 : 0;
            }
            maxArea = Math.max(maxArea, largestRectangleArea(heights));
        }
        return maxArea;
    }

    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        for (int i = 0; i <= heights.length; i++) {
            int currentHeight = i == heights.length ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > currentHeight) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            if (i < heights.length) stack.push(i);
        }
        return maxArea;
    }
}
```

**Time complexity:** O(rows × cols).

**Space complexity:** O(cols).

## 8. Remove K Digits

Remove exactly k digits to obtain the smallest possible number, where 0 ≤ k ≤ num.length(). Remove larger preceding digits first, then strip leading zeros.

[LeetCode 402](https://leetcode.com/problems/remove-k-digits/)

```java
class Solution {
    public String removeKdigits(String num, int k) {
        char[] stack = new char[num.length()];
        int size = 0;
        for (int i = 0; i < num.length(); i++) {
            char digit = num.charAt(i);
            while (size > 0 && k > 0 && stack[size - 1] > digit) {
                size--;
                k--;
            }
            stack[size++] = digit;
        }
        size -= k;
        int start = 0;
        while (start < size && stack[start] == '0') start++;
        return start == size ? "0" : new String(stack, start, size - start);
    }
}
```

**Time complexity:** O(n), where n is the number of digits.

**Space complexity:** O(n).

## 9. Daily Temperatures

Return how many days each temperature must wait for a strictly warmer day. Return 0 when no warmer day follows.

[LeetCode 739](https://leetcode.com/problems/daily-temperatures/)

```java
import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int previousIndex = stack.pop();
                answer[previousIndex] = i - previousIndex;
            }
            stack.push(i);
        }
        return answer;
    }
}
```

**Time complexity:** O(n).

**Space complexity:** O(n).

## 10. Evaluate Reverse Polish Notation

Evaluate a valid postfix expression. Pop the right operand before the left operand; Java integer division truncates toward zero.

[LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

```java
import java.util.*;

class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String token : tokens) {
            if (!token.equals("+") && !token.equals("-")
                    && !token.equals("*") && !token.equals("/")) {
                stack.push(Integer.parseInt(token));
                continue;
            }
            int right = stack.pop();
            int left = stack.pop();
            switch (token) {
                case "+": stack.push(left + right); break;
                case "-": stack.push(left - right); break;
                case "*": stack.push(left * right); break;
                case "/": stack.push(left / right); break;
            }
        }
        return stack.pop();
    }
}
```

**Time complexity:** O(n) for n bounded-length tokens.

**Space complexity:** O(n).

## 11. LRU Cache

Store up to capacity key-value pairs. Reads and updates mark a key as recently used; evict the least recently used key when full. Combine a hash map with a doubly linked list.

[LeetCode 146](https://leetcode.com/problems/lru-cache/)

```java
import java.util.*;

class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node left = new Node(0, 0);
    private final Node right = new Node(0, 0);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        left.next = right;
        right.prev = left;
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insertAtFront(Node node) {
        // Most recent near left; least recent near right.
        Node front = left.next;
        left.next = node;
        node.prev = left;
        node.next = front;
        front.prev = node;
    }

    public int get(int key) {
        Node node = map.get(key);
        if (node == null) return -1;
        remove(node);
        insertAtFront(node);
        return node.value;
    }

    public void put(int key, int value) {
        Node node = map.get(key);
        if (node != null) {
            node.value = value;
            remove(node);
            insertAtFront(node);
            return;
        }
        node = new Node(key, value);
        map.put(key, node);
        insertAtFront(node);
        if (map.size() > capacity) {
            Node leastRecent = right.prev;
            remove(leastRecent);
            map.remove(leastRecent.key);
        }
    }
}
```

**Time complexity:** get and put: O(1) average/amortized, assuming average O(1) hash-map operations.

**Space complexity:** O(capacity).

## 12. Design Browser History

Track visited pages using a doubly linked list. Visiting a new page discards the old forward history. Back and forward move at most the requested number of steps.

[LeetCode 1472](https://leetcode.com/problems/design-browser-history/)

```java
class BrowserHistory {
    private static class Node {
        String url;
        Node prev, next;

        Node(String url) {
            this.url = url;
        }
    }

    private Node current;

    public BrowserHistory(String homepage) {
        current = new Node(homepage);
    }

    public void visit(String url) {
        Node node = new Node(url);
        current.next = node;
        node.prev = current;
        current = node;
    }

    public String back(int steps) {
        while (current.prev != null && steps > 0) {
            current = current.prev;
            steps--;
        }
        return current.url;
    }

    public String forward(int steps) {
        while (current.next != null && steps > 0) {
            current = current.next;
            steps--;
        }
        return current.url;
    }
}
```

**Time complexity:** visit: O(1); back/forward: O(min(steps, available pages) + 1), excluding garbage collection.

**Space complexity:** O(n) nodes for retained history, plus stored URL characters.
