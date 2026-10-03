# Binary Tree & BST Interview Problems — Python

These are independent Python 3 solutions. Each problem uses its own `Solution`
class; run one solution at a time. Problem 2 uses the standalone function
`zigzag_level_order(root)`. Other method names match the original platform
entry points. LeetCode provides the node classes. For local practice, run the
following definitions before a solution or its example:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    # Used by problem 22 for the next pointer.
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
```

`n` is the number of nodes; `h` is the tree height. Space bounds exclude the
returned output unless stated otherwise. Recursive solutions use Python's
call stack and can reach its recursion limit on very deep, skewed trees.
Problems 8 and 9 assume distinct values; both LCA problems assume the queried
nodes exist in the tree. Problem 20 assumes the target belongs to the tree.

## 1. Level Order Traversal — [LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the `root` of a binary tree, return the level order traversal from left to right.

### Example

```text
        3
       / \
      9   20
         /  \
        15   7

Input:
root = [3,9,20,null,null,15,7]

Output:
[
  [3],
  [9,20],
  [15,7]
]
```

### Python

```python
from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            current_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(current_level)
        return result
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Queue`

## 2. Zigzag Level Order Traversal — [LeetCode 103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values.

### Example

```text
        3
       / \
      9   20
         /  \
        15   7

Input:
root = [3,9,20,null,null,15,7]

Output:
[
  [3],
  [20,9],
  [15,7]
]
```

### Python

```python
from collections import deque

def zigzag_level_order(root):
    if root is None:
        return []

    queue = deque([root])
    result = []
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()

        result.append(level)
        left_to_right = not left_to_right

    return result
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Queue + Direction Flag`

## 3. Height of Binary Tree — [LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the `root` of a binary tree, return its maximum depth / height.

### Example

```text
        3
       / \
      9   20
         /  \
        15   7

Input:
root = [3,9,20,null,null,15,7]

Output:
3
```

### Python — Recursive DFS

```python
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)
```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack  
**Pattern:** `DFS + Recursion`

## 4. Mirror Tree / Invert Binary Tree — [LeetCode 226](https://leetcode.com/problems/invert-binary-tree/)

Given the `root` of a binary tree, invert the tree and return its root.

### Python

```python
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Recursion`

## 5. Symmetric Tree — [LeetCode 101](https://leetcode.com/problems/symmetric-tree/)

Given the `root` of a binary tree, check whether it is a mirror of itself.

### Python

```python
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return (self.isMirror(left.left, right.right)
                and self.isMirror(left.right, right.left))
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Mirror Comparison`

## 6. Identical Tree / Same Tree — [LeetCode 100](https://leetcode.com/problems/same-tree/)

Given the roots of two binary trees `p` and `q`, check whether they are exactly the same.

### Python

```python
class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Compare Two Trees`

## 7. Diameter of Binary Tree — [LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/)

Given the `root` of a binary tree, return the diameter of the tree. The diameter is the longest path between any two nodes. The path does not need to include root node.

### Python

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node):
            nonlocal diameter
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Diameter counts edges; height counts nodes.
            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)
        return diameter
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Height + Global Maximum`

## 8. Construct Binary Tree from Preorder and Inorder — [LeetCode 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Given `preorder` and `inorder` traversal arrays, construct the binary tree.

### Core Trick

```text
Preorder = ROOT → LEFT → RIGHT
Inorder  = LEFT → ROOT → RIGHT (most basic, commnly used)
```

### Python

```python
class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index = {
            value: index
            for index, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)
            mid = inorder_index[root_value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Preorder finds ROOT + Inorder splits LEFT/RIGHT`

## 9. Construct Binary Tree from Inorder and Postorder — [LeetCode 106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Given `inorder` and `postorder` traversal arrays, construct the binary tree.

### Core Trick

```text
Inorder   = LEFT → ROOT → RIGHT
Postorder = LEFT → RIGHT → ROOT
```

Build the `RIGHT` subtree before the `LEFT` subtree because postorder is read backwards.

### Python

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_index_map = {
            value: index for index, value in enumerate(inorder)
        }

        def array_to_tree(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_value)

            mid = inorder_index_map[root_value]
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Postorder finds ROOT + Inorder splits LEFT/RIGHT + Build RIGHT first`

## 10. Right View of Binary Tree — [LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/)

Return the nodes visible when the tree is viewed from the right side.

### Python

```python
from collections import deque

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # The last node at this level is visible from the right.
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Last node of every level`

## 11. Left View of Binary Tree

**LeetCode:** No direct standalone equivalent.

Return the nodes visible when the binary tree is viewed from the left side.

### Python

```python
def left_view(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # First node at this level is visible from the left.
            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + First node of every level`

## 12. Top View of Binary Tree

**LeetCode:** No direct standalone equivalent.

Return nodes visible when the tree is viewed from the top.

### Python

```python
from collections import deque

class Solution:
    def topView(self, root):
        if root is None:
            return []

        view = {}

        # Each tuple stores a node and its horizontal distance (HD).
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # Keep the first node seen at this HD.
            view.setdefault(hd, node.val)

            if node.left is not None:
                queue.append((node.left, hd - 1))

            if node.right is not None:
                queue.append((node.right, hd + 1))

        return [view[hd] for hd in sorted(view)]
```

**Time:** `O(n + m log m)` for sorting `m` horizontal distances (`m ≤ n`)  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + First occurrence`

## 13. Bottom View of Binary Tree — Important

**LeetCode:** No direct standalone equivalent.

Return nodes visible when the tree is viewed from the bottom. If two nodes share the same depth and horizontal distance, this BFS keeps the node visited later (the rightward node).

**Example correction:** In the original sample, nodes 4 and 5 both have HD 0 and depth 2. Node 5 is visited later, so the bottom view is `[2, 5, 7, 6]`.

### Python

```python
class Solution:
    def bottomView(self, root):
        if root is None:
            return []

        hashmap = {}
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # Update the bottommost node at this horizontal distance.
            hashmap[hd] = node.val

            if node.left is not None:
                queue.append((node.left, hd - 1))

            if node.right is not None:
                queue.append((node.right, hd + 1))

        result = [hashmap[hd] for hd in sorted(hashmap)]
        return result
```

**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + Last occurrence`

## 14. Vertical Order Traversal - [LeetCode 987](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

“I’ll traverse the tree and store each node’s row and value in a hashmap keyed by column. Then I’ll sort the columns, and within each column sort by row first and value second.”

### Python

```python
from collections import deque

class Solution:
    def verticalTraversal(self, root):
        if root is None:
            return []

        hashmap = {}
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()

            if col not in hashmap:
                hashmap[col] = []

            hashmap[col].append((row, node.val))

            if node.left is not None:
                queue.append((node.left, row + 1, col - 1))

            if node.right is not None:
                queue.append((node.right, row + 1, col + 1))

        result = []

        for col in sorted(hashmap):
            hashmap[col].sort()
            answer = [value for row, value in hashmap[col]]
            result.append(answer)

        return result
```

**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `DFS + Column/Row Maps OR Min-Heaps`

## 15. Boundary Traversal of Binary Tree — [LeetCode 545](https://leetcode.com/problems/boundary-of-binary-tree/) — Very Important

Return the anti-clockwise boundary traversal: root, left boundary, leaves, right boundary reversed.

### Python

```python
class Solution:
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def addLeaves(self, result, root):
        if self.isLeaf(root):
            result.append(root.val)
        else:
            if root.left is not None:
                self.addLeaves(result, root.left)

            if root.right is not None:
                self.addLeaves(result, root.right)

    def boundaryOfBinaryTree(self, root):
        result = []

        if root is None:
            return result

        if not self.isLeaf(root):
            result.append(root.val)

        #Part 1: Left boundary, excluding leaves.
        node = root.left

        while node is not None:
            if not self.isLeaf(node):
                result.append(node.val)

            if node.left is not None:
                node = node.left
            else:
                node = node.right

        # Part 2: All leaves, from left to right.
        self.addLeaves(result, root)

        # Part 3: Right boundary, excluding leaves.
        stack = []
        node = root.right

        while node is not None:
            if not self.isLeaf(node):
                stack.append(node.val)

            if node.right is not None:
                node = node.right
            else:
                node = node.left

        # Add right boundary in reverse order.
        while stack:
            result.append(stack.pop())

        return result
```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack + right-boundary temporary list  
**Pattern:** `Left Boundary + Leaves + Reversed Right Boundary`

## 16. Root to Leaf Path, Binary Tree Paths - [LeetCode 257](https://leetcode.com/problems/binary-tree-paths/)

Return all root-to-leaf paths.

### Python

```python
class Solution:
    def rootToLeafPaths(self, root):
        result = []

        def dfs(node, path):
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                result.append(path.copy())
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            # Undoing the choice
            path.pop()

        dfs(root, [])
        return result
```

**Time:** `O(n × h)` in the worst case because each leaf path may be copied  
**Space:** `O(h)` recursion/path space, excluding output  
**Pattern:** `DFS + Path + Backtracking`

## 17. Flatten Binary Tree to Linked List — [LeetCode 114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

Flatten the tree in place into a preorder singly linked list using the same nodes. Every `left` pointer becomes `None`; each `right` pointer points to the next node.

### Python

```python
class Solution:

    def flatten(self, root: TreeNode) -> None:
        # Handle the null scenario
        if not root:
            return None

        node = root
        while node:

            # If the node has a left child
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right
```

**Time:** `O(n)`  
**Space:** `O(1)`  
**Pattern:** `Iterative Pointer Rewiring + Preorder`

## 17b. Binary Tree to Doubly Linked List — Inorder

Convert a binary tree into a non-circular doubly linked list in inorder order,
reusing its nodes. `left` becomes the previous pointer and `right` becomes the
next pointer. Return the list head. This mutates the original tree.

**Related LeetCode:** [426 — Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)
requires a BST and a **circular** list. The general binary-tree solution below
returns a non-circular list; the adaptation for 426 is shown afterward.

### Python

```python
class Solution:
    def treeToDoublyList(self, root):
        head = None
        previous = None

        def inorder(node):
            nonlocal head, previous
            if node is None:
                return
            # Save the original right subtree before rewiring pointers.
            original_right = node.right
            inorder(node.left)
            node.left = previous
            if previous is None:
                head = node
            else:
                previous.right = node
            previous = node
            inorder(original_right)

        inorder(root)
        if previous is not None:
            previous.right = None
        return head
```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack  
**Pattern:** `Inorder DFS + Previous Pointer`

For LeetCode 426, use its supplied `Node` class and make the list circular:
replace `previous.right = None` with `previous.right = head` and
`head.left = previous` inside the final `if previous is not None` block.

## 18. Minimum Time to Burn Binary Tree from a Node — [LeetCode 2385](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) — Very Important

Fire starts at a target node. In one second, fire spreads to the left child, right child, and parent.

**Correction:** The DFS below counts every edge, including the edge into an opposite subtree and the distance to an ancestor with no opposite subtree. The original helper missed these cases.

### Python

```python
class Solution:
    def minTime(self, root, target):
        # Assumes unique values and a target value present in the tree.
        max_distance = 0

        def traverse(node):
            nonlocal max_distance
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            if node.val == target:
                max_distance = max(max_distance, left, right)
                return -1
            if left < 0:
                # abs(left) is the target-to-current distance;
                # right is the height of the opposite subtree.
                max_distance = max(max_distance, -left + right)
                return left - 1
            if right < 0:
                max_distance = max(max_distance, -right + left)
                return right - 1
            return 1 + max(left, right)

        traverse(root)
        return max_distance
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `Postorder DFS + Height/Target Distance`

## 19. Lowest Common Ancestor — [LeetCode 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

Find the lowest node that has both `p` and `q` in its subtree.

### Python

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Return information upward`

## 20. Print All Nodes at Distance K from Given Node — [LeetCode 863](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) — VV Important

Return all nodes exactly `k` edges away from the target node.

### Python

```python
from collections import deque

class Solution:
    def distanceK(self, root, target, k):
        if root is None or target is None or k < 0:
            return []
        parents = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in (node.left, node.right):
                if child is not None:
                    parents[child] = node
                    queue.append(child)

        queue = deque([target])
        visited = {target}
        distance = 0
        while queue:
            if distance == k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parents.get(node)):
                    if neighbor is not None and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return []
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Parent Map + BFS + Visited`

## 21. Serialize and Deserialize Binary Tree — [LeetCode 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

Serialize a binary tree into a string and deserialize that string back into the same tree.

### Python

```python
class Codec:
    def serialize(self, root):
        values = []

        def dfs(node):
            if node is None:
                values.append("#")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values) + ","

    def deserialize(self, data):
        # Match the serializer's trailing comma without an empty token.
        values = iter(data.rstrip(",").split(","))

        def dfs():
            value = next(values)
            if value == "#":
                return None
            root = TreeNode(int(value))
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Preorder DFS + Null Markers`

## 22. Connect Nodes at Same Level — [LeetCode 116](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) / [LeetCode 117](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

Populate each node's `next` pointer so it points to the next node on the same level.

### Python — General BFS Solution

```python
from collections import deque

class Solution:
    def connect(self, root):
        if root is None:
            return None
        queue = deque([root])
        while queue:
            previous = None
            for _ in range(len(queue)):
                current = queue.popleft()
                if previous is not None:
                    previous.next = current
                previous = current
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            previous.next = None  # Last node on this level.
        return root
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Level Order BFS + Previous Node`

## 23. Morris Traversal — [LeetCode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) — Optional

Perform inorder traversal without recursion or an explicit stack. LeetCode 94 accepts inorder traversal; Morris traversal is one implementation approach.

### Python

```python
class Solution:
    def inorderTraversal(self, root):
        result = []
        current = root
        while current is not None:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while (predecessor.right is not None
                       and predecessor.right is not current):
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current  # Temporary thread.
                    current = current.left
                else:
                    predecessor.right = None  # Restore the original tree.
                    result.append(current.val)
                    current = current.right
        return result
```

**Time:** `O(n)`  
**Space:** `O(1)`  
**Pattern:** `Temporary Threaded Links`

## 24. Path Sum — [LeetCode 112](https://leetcode.com/problems/path-sum/)

Determine whether the tree has a root-to-leaf path whose values sum to `targetSum`.

### Python

```python
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining)
                or self.hasPathSum(root.right, remaining))
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Remaining Sum`

## 25. Path Sum II — [LeetCode 113](https://leetcode.com/problems/path-sum-ii/)

Return all root-to-leaf paths whose sum equals `targetSum`.

### Python

```python
class Solution:
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(node, remaining):
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val
            if node.left is None and node.right is None and remaining == 0:
                result.append(path.copy())
            dfs(node.left, remaining)
            dfs(node.right, remaining)
            path.pop()  # Backtrack.

        dfs(root, targetSum)
        return result
```

**Time:** `O(n × h)` worst case due to copying paths  
**Space:** `O(h)` excluding output  
**Pattern:** `DFS + Backtracking + Running Sum`

## 26. Path Sum III — [LeetCode 437](https://leetcode.com/problems/path-sum-iii/) — Important

Count the number of downward paths whose values sum to `targetSum`. The path does not need to start at root or end at leaf.

### Python — Prefix Sum

```python
class Solution:
    def pathSum(self, root, targetSum):
        prefix_counts = {0: 1}

        def dfs(node, current_sum):
            if node is None:
                return 0
            current_sum += node.val
            count = prefix_counts.get(current_sum - targetSum, 0)
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            # Keep only prefixes from the active root-to-current path.
            prefix_counts[current_sum] -= 1
            if prefix_counts[current_sum] == 0:
                del prefix_counts[current_sum]
            return count

        return dfs(root, 0)
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `DFS + Prefix Sum + Dictionary + Backtracking`

## 27. Binary Tree Maximum Path Sum — [LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — VV Important

Find the maximum possible path sum between any two nodes.

### Python

```python
class Solution:
    def maxPathSum(self, root):
        # The problem guarantees a nonempty tree.
        max_sum = float("-inf")

        def gain(node):
            nonlocal max_sum
            if node is None:
                return 0
            left_gain = max(0, gain(node.left))
            right_gain = max(0, gain(node.right))
            max_sum = max(max_sum, node.val + left_gain + right_gain)
            # A parent can extend only one side of this path.
            return node.val + max(left_gain, right_gain)

        gain(root)
        return max_sum
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `Postorder DFS + Global Maximum`

# BST

## 28. Kth Smallest Element in BST — [LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Given a BST, return its `k`th smallest element.

### Python

```python
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right
        return -1  # Assumes valid k in the problem's normal inputs.
```

**Time:** `O(h + k)` approximately  
**Space:** `O(h)`  
**Pattern:** `BST + Inorder`

## 29. LCA in BST — [LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

Find the lowest common ancestor of two nodes in a BST.

### Python

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current is not None:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current
        return None
```

**Time:** `O(h)`  
**Space:** `O(1)`

## 30. Inorder Predecessor and Successor in BST

**Related LeetCode:** [285 — Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) covers the successor only. The solution below returns both predecessor and successor values.

For a given key, find the largest value smaller than the key and the smallest value greater than the key.

### Python

```python
class Solution:
    def predecessorSuccessor(self, root, key):
        predecessor = -1
        successor = -1
        current = root
        while current is not None:
            if current.val < key:
                predecessor = current.val
                current = current.right
            else:
                current = current.left

        current = root
        while current is not None:
            if current.val > key:
                successor = current.val
                current = current.left
            else:
                current = current.right
        # Preserve the original convention: -1 means no answer.
        return [predecessor, successor]
```

**Time:** `O(h)`  
**Space:** `O(1)`

## 31. Convert Sorted Array to BST — [LeetCode 108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

Given a sorted array, construct a height-balanced BST.

### Python

```python
class Solution:
    def sortedArrayToBST(self, nums):
        def build(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)
```

**Time:** `O(n)`  
**Space:** `O(log n)` for balanced tree  
**Pattern:** `Divide & Conquer + Middle Element`

## 32. Validate Binary Search Tree — [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/)

Determine whether a binary tree is a valid BST.

### Python

```python
class Solution:
    def isValidBST(self, root):
        def validate(node, lower, upper):
            if node is None:
                return True
            if not lower < node.val < upper:
                return False
            return (validate(node.left, lower, node.val)
                    and validate(node.right, node.val, upper))

        return validate(root, float("-inf"), float("inf"))
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Lower/Upper Bounds`

# Quick Revision Table

| Problem                    | Main Trick                            |
| -------------------------- | ------------------------------------- |
| Level Order                | BFS + Queue                           |
| Zigzag                     | BFS + Direction Flag                  |
| Height                     | `1 + max(left, right)`                |
| Mirror Tree                | Swap left/right                       |
| Symmetric Tree             | Cross comparison                      |
| Identical Tree             | Same-side comparison                  |
| Diameter                   | Return height, update `left + right`  |
| Preorder + Inorder Build   | Preorder root + inorder split         |
| Inorder + Postorder Build  | Postorder root + build right first    |
| Right View                 | Last node per level                   |
| Left View                  | First node per level                  |
| Top View                   | First node per HD                     |
| Bottom View                | Last node per HD                      |
| Vertical Traversal         | Column, then row, then value          |
| Boundary Traversal         | Root + left + leaves + reversed right |
| Root-to-Leaf Paths         | DFS + Backtracking                    |
| Flatten to Linked List     | Preorder + pointer rewiring           |
| Tree to Doubly Linked List | Inorder + previous pointer            |
| Burn Tree                  | Postorder + height/target distance    |
| Binary Tree LCA            | Left result + right result            |
| Nodes Distance K           | Parent Map + BFS                      |
| Serialization              | Preorder + `#`                        |
| Connect Same Level         | BFS + previous                        |
| Morris Traversal           | Temporary predecessor link            |
| Path Sum I                 | Remaining sum                         |
| Path Sum II                | DFS + Backtracking                    |
| Path Sum III               | Prefix Sum + dictionary               |
| Maximum Path Sum           | Return one side, update both          |
| BST Kth Smallest           | Inorder = sorted                      |
| BST LCA                    | Smaller / larger / split              |
| BST Predecessor            | Largest `< key`                       |
| BST Successor              | Smallest `> key`                      |
| Sorted Array → BST         | Middle = root                         |
| Validate BST               | Min/max allowed range                 |
