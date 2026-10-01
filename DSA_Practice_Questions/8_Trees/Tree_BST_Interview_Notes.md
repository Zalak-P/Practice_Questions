# Binary Tree & BST Interview Problems — Java

## 1. Level Order Traversal — LeetCode 102

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

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        if (root == null) {
            return new ArrayList<>();
        }

        List<List<Integer>> result = new ArrayList<>();

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {

                TreeNode node = queue.poll();

                currentLevel.add(node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(currentLevel);
        }

        return result;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Queue`

## 2. Zigzag Level Order Traversal — LeetCode 103

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

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {

        if (root == null) {
            return new ArrayList<>();
        }

        List<List<Integer>> result = new ArrayList<>();

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        boolean leftToRight = true;

        while (!queue.isEmpty()) {

            int levelSize = queue.size();

            LinkedList<Integer> currentLevel = new LinkedList<>();

            for (int i = 0; i < levelSize; i++) {

                TreeNode node = queue.poll();

                // Add based on current direction
                if (leftToRight) {
                    currentLevel.addLast(node.val);
                } else {
                    currentLevel.addFirst(node.val);
                }

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(currentLevel);

            // Reverse direction for next level
            leftToRight = !leftToRight;
        }

        return result;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Queue + Direction Flag`

## 3. Height of Binary Tree — LeetCode 104

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

### Java — Recursive DFS

```java
class Solution {
    public int maxDepth(TreeNode root) {

        if (root == null) {
            return 0;
        }

        int leftHeight = maxDepth(root.left);
        int rightHeight = maxDepth(root.right);

        return 1 + Math.max(leftHeight, rightHeight);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack  
**Pattern:** `DFS + Recursion`

## 4. Mirror Tree / Invert Binary Tree — LeetCode 226

Given the `root` of a binary tree, invert the tree and return its root.

### Java

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {

        if (root == null) {
            return null;
        }

        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);

        root.left = right;
        root.right = left;

        return root;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Recursion`

## 5. Symmetric Tree — LeetCode 101

Given the `root` of a binary tree, check whether it is a mirror of itself.

### Java

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {

        if (root == null) {
            return true;
        }

        return isMirror(root.left, root.right);
    }

    private boolean isMirror(TreeNode left, TreeNode right) {

        if (left == null && right == null) {
            return true;
        }

        if (left == null || right == null) {
            return false;
        }

        if (left.val != right.val) {
            return false;
        }

        return isMirror(left.left, right.right)
                && isMirror(left.right, right.left);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Mirror Comparison`

## 6. Identical Tree / Same Tree — LeetCode 100

Given the roots of two binary trees `p` and `q`, check whether they are exactly the same.

### Java

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {

        if (p == null && q == null) {
            return true;
        }

        if (p == null || q == null) {
            return false;
        }

        if (p.val != q.val) {
            return false;
        }

        return isSameTree(p.left, q.left)
                && isSameTree(p.right, q.right);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Compare Two Trees`

## 7. Diameter of Binary Tree — LeetCode 543

Given the `root` of a binary tree, return the diameter of the tree. The diameter is the longest path between any two nodes.

### Java

```java
class Solution {

    int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {

        height(root);

        return diameter;
    }

    private int height(TreeNode node) {

        if (node == null) {
            return 0;
        }

        int leftHeight = height(node.left);
        int rightHeight = height(node.right);

        // Longest path passing through current node
        diameter = Math.max(
            diameter,
            leftHeight + rightHeight
        );

        // Return height to parent
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Height + Global Maximum`

## 8. Construct Binary Tree from Preorder and Inorder — LeetCode 105

Given `preorder` and `inorder` traversal arrays, construct the binary tree.

### Core Trick

```text
Preorder = ROOT → LEFT → RIGHT
Inorder  = LEFT → ROOT → RIGHT
```

### Java

```java
import java.util.*;

class Solution {

    int preorderIndex = 0;

    Map<Integer, Integer> inorderMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        // Store inorder value -> index
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int left, int right) {

        if (left > right) {
            return null;
        }

        // Preorder gives us the root
        int rootValue = preorder[preorderIndex++];

        TreeNode root = new TreeNode(rootValue);

        // Find root position in inorder
        int rootIndex = inorderMap.get(rootValue);

        // Build left subtree
        root.left = build(preorder, left, rootIndex - 1);

        // Build right subtree
        root.right = build(preorder, rootIndex + 1, right);

        return root;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Preorder finds ROOT + Inorder splits LEFT/RIGHT`

## 9. Construct Binary Tree from Inorder and Postorder — LeetCode 106

Given `inorder` and `postorder` traversal arrays, construct the binary tree.

### Core Trick

```text
Inorder   = LEFT → ROOT → RIGHT
Postorder = LEFT → RIGHT → ROOT
```

Build the `RIGHT` subtree before the `LEFT` subtree because postorder is read backwards.

### Java

```java
import java.util.*;

class Solution {

    int postorderIndex;

    Map<Integer, Integer> inorderMap = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {

        postorderIndex = postorder.length - 1;

        // Store inorder value -> index
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        return build(postorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] postorder, int left, int right) {

        if (left > right) {
            return null;
        }

        // Postorder gives root from the end
        int rootValue = postorder[postorderIndex--];

        TreeNode root = new TreeNode(rootValue);

        // Find root position in inorder
        int rootIndex = inorderMap.get(rootValue);

        // IMPORTANT: Build right first
        root.right = build(postorder, rootIndex + 1, right);

        // Then build left
        root.left = build(postorder, left, rootIndex - 1);

        return root;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Postorder finds ROOT + Inorder splits LEFT/RIGHT + Build RIGHT first`

## 10. Right View of Binary Tree

Return the nodes visible when the tree is viewed from the right side.

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {

                TreeNode node = queue.poll();

                // Last node of each level
                if (i == levelSize - 1) {
                    result.add(node.val);
                }

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }

        return result;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Last node of every level`

## 11. Left View of Binary Tree

Return the nodes visible when the binary tree is viewed from the left side.

### Java

```java

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

public class Solution {

    public List<Integer> leftView(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        ArrayDeque<TreeNode> queue = new ArrayDeque<>();
        queue.addLast(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            result.add(queue.getFirst().val);

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.removeFirst();

                if (node.left != null) {
                    queue.addLast(node.left);
                }
                if (node.right != null) {
                    queue.addLast(node.right);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Concrete Example Tree:
        //          1
        //        /   \
        //       2     3
        //        \   /
        //         4 5
        //          /
        //         6
        //
        // Level 1: [1] -> Visible: 1
        // Level 2: [2, 3] -> Visible: 2
        // Level 3: [4, 5] -> Visible: 4
        // Level 4: [6] -> Visible: 6

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(5);
        root.right.left.left = new TreeNode(6);

        List<Integer> view = sol.leftView(root);
        System.out.println("Left View Result: " + view);
        // Expected Console Output: Left View Result: [1, 2, 4, 6]
    }
}

```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + First node of every level`

## 12. Top View of Binary Tree

Return nodes visible when the tree is viewed from the top.

### Java

```java

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

// Pair class to track a node alongside its horizontal distance
class Pair {
    TreeNode node;
    int hd; // Horizontal Distance
    Pair(TreeNode node, int hd) {
        this.node = node;
        this.hd = hd;
    }
}

public class TopViewBinaryTree {
    public static List<Integer> topView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        // TreeMap automatically sorts keys (horizontal distances) from left to right
        Map<Integer, Integer> map = new TreeMap<>();
        ArrayDeque<Pair> queue = new ArrayDeque<>();

        queue.addLast(new Pair(root, 0));

        while (!queue.isEmpty()) {
            Pair current = queue.removeFirst();
            TreeNode node = current.node;
            int hd = current.hd;

            // putIfAbsent ensures we only record the FIRST node visible at this horizontal angle
            map.putIfAbsent(hd, node.val);

            if (node.left != null) {
                queue.addLast(new Pair(node.left, hd - 1));
            }
            if (node.right != null) {
                queue.addLast(new Pair(node.right, hd + 1));
            }
        }

        // Collect values in order of sorted horizontal distances
        result.addAll(map.values());
        return result;
    }

    public static void main(String[] args) {
        // Constructing the following sample binary tree:
        //
        //          1 (hd=0)
        //        /   \
        // (hd=-1) 2     3 (hd=1)
        //         \     / \
        //  (hd=0)  4   5   6 (hd=2)
        //               \
        //                7 (hd=1)
        //
        // Left-to-right top view values should be: [2, 1, 3, 6]
        // Note: '4', '5', and '7' are hidden by '1', '3', and '5' respectively from above.

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);
        root.right.left.right = new TreeNode(7);

        List<Integer> view = topView(root);
        System.out.println("Top View: " + view);
        // Expected Output: Top View: [2, 1, 3, 6]
    }
}

```

**Time:** `O(n log n)` using `TreeMap`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + First occurrence`

## 13. Bottom View of Binary Tree — Important

Return nodes visible when the tree is viewed from the bottom.

### Java

```java

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

public class Solution {

    static class Pair {
        TreeNode node;
        int hd;

        Pair(TreeNode node, int hd) {
            this.node = node;
            this.hd = hd;
        }
    }

    public List<Integer> bottomView(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        // TreeMap automatically sorts horizontal distances from left to right
        Map<Integer, Integer> map = new TreeMap<>();

        // Java 21 optimized ArrayDeque
        ArrayDeque<Pair> queue = new ArrayDeque<>();
        queue.addLast(new Pair(root, 0));

        while (!queue.isEmpty()) {
            Pair current = queue.removeFirst();
            TreeNode node = current.node;
            int hd = current.hd;

            // Overwrite existing values so that the bottom-most node at this HD remains
            map.put(hd, node.val);

            if (node.left != null) {
                queue.addLast(new Pair(node.left, hd - 1));
            }

            if (node.right != null) {
                queue.addLast(new Pair(node.right, hd + 1));
            }
        }

        // Collect values in sorted horizontal order
        result.addAll(map.values());
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Concrete Example Tree:
        //          1 (hd=0)
        //        /   \
        // (hd=-1) 2     3 (hd=1)
        //         \     / \
        //  (hd=0)  4   5   6 (hd=2)
        //               \
        //                7 (hd=1)
        //
        // Overwriting progression by horizontal distance:
        // hd -1 -> [2]
        // hd  0 -> [1] -> overwritten by [4]
        // hd  1 -> [3] -> overwritten by [5] -> overwritten by [7]
        // hd  2 -> [6]
        //
        // Expected Bottom View Output order (left to right): [2, 4, 7, 6]

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);
        root.right.left.right = new TreeNode(7);

        List<Integer> view = sol.bottomView(root);
        System.out.println("Bottom View Result: " + view);
        // Expected Console Output: Bottom View Result: [2, 4, 7, 6]
    }
}
```

**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + Last occurrence`

## 14. Vertical Order Traversal - Leetcode 987

Return nodes column by column from left to right.

### Java

```java

import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Structure: Map<Column, Map<Row, PriorityQueue<NodeValue>>>
    private TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        // Step 1: Traverse the tree and populate the nested map structure
        traverse(root, 0, 0);

        // Step 2: Extract data from the sorted map structure into the final result list
        for (int col : map.keySet()) {
            List<Integer> currentColumn = new ArrayList<>();
            TreeMap<Integer, PriorityQueue<Integer>> rows = map.get(col);

            for (int row : rows.keySet()) {
                PriorityQueue<Integer> pq = rows.get(row);
                // Pull values out of the PriorityQueue to guarantee value sorting
                while (!pq.isEmpty()) {
                    currentColumn.add(pq.poll());
                }
            }
            result.add(currentColumn);
        }

        return result;
    }

    private void traverse(TreeNode node, int row, int col) {
        if (node == null) {
            return;
        }

        // Ensure the inner structures exist for the current coordinate
        map.putIfAbsent(col, new TreeMap<>());
        map.get(col).putIfAbsent(row, new PriorityQueue<>());

        // Add the node value to the PriorityQueue at (col, row)
        map.get(col).get(row).add(node.val);

        // Move down the tree
        traverse(node.left, row + 1, col - 1);
        traverse(node.right, row + 1, col + 1);
    }
}

```

**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + TreeMap`

## 15. Boundary Traversal of Binary Tree — Very Important

Return the anti-clockwise boundary traversal: root, left boundary, leaves, right boundary reversed.

### Java

```java

import java.util.*;

// Definition for a binary tree node
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class Solution {
    public ArrayList<Integer> boundary(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<>();
        if (root == null) return res;

        // Step 1: Add root if it's not a leaf node
        if (!isLeaf(root)) {
            res.add(root.val);
        }

        // Step 2: Add left boundary (excluding leaves)
        addLeftBoundary(root.left, res);

        // Step 3: Add all leaf nodes
        addLeaves(root, res);

        // Step 4: Add right boundary (excluding leaves)
        addRightBoundary(root.right, res);

        return res;
    }

    private boolean isLeaf(TreeNode node) {
        return node.left == null && node.right == null;
    }

    private void addLeftBoundary(TreeNode node, ArrayList<Integer> res) {
        TreeNode curr = node;
        while (curr != null) {
            if (!isLeaf(curr)) {
                res.add(curr.val);
            }
            // Prioritize left child; if left is null, move to right child
            if (curr.left != null) {
                curr = curr.left;
            } else {
                curr = curr.right;
            }
        }
    }

    private void addRightBoundary(TreeNode node, ArrayList<Integer> res) {
        ArrayList<Integer> temp = new ArrayList<>();
        TreeNode curr = node;
        while (curr != null) {
            if (!isLeaf(curr)) {
                temp.add(curr.val);
            }
            // Prioritize right child; if right is null, move to left child
            if (curr.right != null) {
                curr = curr.right;
            } else {
                curr = curr.left;
            }
        }
        // Reverse to get bottom-up order for the right boundary
        Collections.reverse(temp);
        res.addAll(temp);
    }

    private void addLeaves(TreeNode node, ArrayList<Integer> res) {
        if (node == null) return;

        if (isLeaf(node)) {
            res.add(node.val);
            return;
        }
        // Standard pre-order/in-order traversal to collect leaves left-to-right
        addLeaves(node.left, res);
        addLeaves(node.right, res);
    }

    // Driver Code to test the implementation
    public static void main(String[] args) {
        Solution solver = new Solution();

        /* Constructed Binary Tree:
                 1
               /   \
              2     3
             / \   / \
            4   5 6   7
               / \
              8   9
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        root.left.right.left = new TreeNode(8);
        root.left.right.right = new TreeNode(9);

        ArrayList<Integer> boundaryOrder = solver.boundary(root);

        // Expected Output: [1, 2, 4, 8, 9, 6, 7, 3]
        System.out.println("Boundary Traversal: " + boundaryOrder);
    }
}

```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack + right-boundary temporary list  
**Pattern:** `Left Boundary + Leaves + Reversed Right Boundary`

## 16. Root to Leaf Path, Binary Tree Paths - Leetcode 257

Return all root-to-leaf paths.

### Java

```java
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root != null) {
            dfs(root, "", result);
        }
        return result;
    }

    private void dfs(TreeNode node, String path, List<String> result) {
        // Append the current node's value to the path string
        path += node.val;

        // If it's a leaf node, add the completed path to the results
        if (node.left == null && node.right == null) {
            result.add(path);
            return;
        }

        // If not a leaf, add the arrow separator and continue down the tree
        if (node.left != null) {
            dfs(node.left, path + "->", result);
        }
        if (node.right != null) {
            dfs(node.right, path + "->", result);
        }
    }
}

```

**Time:** `O(n × h)` in the worst case because each leaf path may be copied  
**Space:** `O(h)` recursion/path space, excluding output  
**Pattern:** `DFS + Path + Backtracking`

## 17. Flatten Binary Tree to Doubly Linked List

Convert a binary tree into a doubly linked list in inorder order using the same tree nodes.

### Java

```java
class Solution {

    TreeNode prev = null;
    TreeNode head = null;

    public TreeNode binaryTreeToDLL(TreeNode root) {

        inorder(root);

        return head;
    }

    private void inorder(TreeNode node) {

        if (node == null) {
            return;
        }

        // LEFT
        inorder(node.left);

        // NODE
        if (prev == null) {

            // First node of inorder becomes head
            head = node;
        }

        else {

            // Previous -> Current
            prev.right = node;

            // Current -> Previous
            node.left = prev;
        }

        // Move previous pointer
        prev = node;

        // RIGHT
        inorder(node.right);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack  
**Pattern:** `Inorder DFS + Previous Pointer`

## 18. Minimum Time to Burn Binary Tree from a Node — Very Important

Fire starts at a target node. In one second, fire spreads to the left child, right child, and parent.

### Java

```java
import java.util.*;

class Solution {

    public int minTime(TreeNode root, int target) {

        // Child -> Parent mapping
        Map<TreeNode, TreeNode> parentMap = new HashMap<>();

        TreeNode targetNode =
            createParentMap(root, parentMap, target);

        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();

        queue.offer(targetNode);
        visited.add(targetNode);

        int time = 0;

        while (!queue.isEmpty()) {

            int size = queue.size();

            boolean burnedNewNode = false;

            for (int i = 0; i < size; i++) {

                TreeNode node = queue.poll();

                // LEFT
                if (node.left != null &&
                    !visited.contains(node.left)) {

                    queue.offer(node.left);
                    visited.add(node.left);

                    burnedNewNode = true;
                }

                // RIGHT
                if (node.right != null &&
                    !visited.contains(node.right)) {

                    queue.offer(node.right);
                    visited.add(node.right);

                    burnedNewNode = true;
                }

                // PARENT
                TreeNode parent = parentMap.get(node);

                if (parent != null &&
                    !visited.contains(parent)) {

                    queue.offer(parent);
                    visited.add(parent);

                    burnedNewNode = true;
                }
            }

            // One second passed only if fire spread
            if (burnedNewNode) {
                time++;
            }
        }

        return time;
    }


    private TreeNode createParentMap(
        TreeNode root,
        Map<TreeNode, TreeNode> parentMap,
        int target
    ) {

        Queue<TreeNode> queue = new LinkedList<>();

        queue.offer(root);

        TreeNode targetNode = null;

        while (!queue.isEmpty()) {

            TreeNode node = queue.poll();

            if (node.val == target) {
                targetNode = node;
            }

            if (node.left != null) {

                parentMap.put(node.left, node);

                queue.offer(node.left);
            }

            if (node.right != null) {

                parentMap.put(node.right, node);

                queue.offer(node.right);
            }
        }

        return targetNode;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Parent Mapping + BFS + Visited Set`

## 19. Lowest Common Ancestor — LeetCode 236

Find the lowest node that has both `p` and `q` in its subtree.

### Java

```java
class Solution {

    public TreeNode lowestCommonAncestor(
        TreeNode root,
        TreeNode p,
        TreeNode q
    ) {

        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode left =
            lowestCommonAncestor(root.left, p, q);

        TreeNode right =
            lowestCommonAncestor(root.right, p, q);

        // p and q found on different sides
        if (left != null && right != null) {
            return root;
        }

        // Return whichever side found a node
        return left != null ? left : right;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Return information upward`

## 20. Print All Nodes at Distance K from Given Node — LeetCode 863 — VV Important

Return all nodes exactly `k` edges away from the target node.

### Java

```java
import java.util.*;

class Solution {

    public List<Integer> distanceK(
        TreeNode root,
        TreeNode target,
        int k
    ) {

        Map<TreeNode, TreeNode> parentMap =
            new HashMap<>();

        buildParentMap(root, parentMap);

        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();

        queue.offer(target);
        visited.add(target);

        int distance = 0;

        while (!queue.isEmpty()) {

            if (distance == k) {
                break;
            }

            int size = queue.size();

            for (int i = 0; i < size; i++) {

                TreeNode node = queue.poll();

                // LEFT
                if (node.left != null &&
                    !visited.contains(node.left)) {

                    visited.add(node.left);
                    queue.offer(node.left);
                }

                // RIGHT
                if (node.right != null &&
                    !visited.contains(node.right)) {

                    visited.add(node.right);
                    queue.offer(node.right);
                }

                // PARENT
                TreeNode parent = parentMap.get(node);

                if (parent != null &&
                    !visited.contains(parent)) {

                    visited.add(parent);
                    queue.offer(parent);
                }
            }

            distance++;
        }

        List<Integer> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            result.add(queue.poll().val);
        }

        return result;
    }


    private void buildParentMap(
        TreeNode root,
        Map<TreeNode, TreeNode> parentMap
    ) {

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            TreeNode node = queue.poll();

            if (node.left != null) {

                parentMap.put(node.left, node);
                queue.offer(node.left);
            }

            if (node.right != null) {

                parentMap.put(node.right, node);
                queue.offer(node.right);
            }
        }
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Parent Map + BFS + Visited`

## 21. Serialize and Deserialize Binary Tree — LeetCode 297

Serialize a binary tree into a string and deserialize that string back into the same tree.

### Java

```java
import java.util.*;

public class Codec {

    // Serialize tree -> String
    public String serialize(TreeNode root) {

        StringBuilder result = new StringBuilder();

        serializeDFS(root, result);

        return result.toString();
    }

    private void serializeDFS(
        TreeNode node,
        StringBuilder result
    ) {

        if (node == null) {

            result.append("#,");
            return;
        }

        // ROOT
        result.append(node.val).append(",");

        // LEFT
        serializeDFS(node.left, result);

        // RIGHT
        serializeDFS(node.right, result);
    }


    // Deserialize String -> Tree
    public TreeNode deserialize(String data) {

        Queue<String> values =
            new LinkedList<>(Arrays.asList(data.split(",")));

        return deserializeDFS(values);
    }

    private TreeNode deserializeDFS(
        Queue<String> values
    ) {

        String value = values.poll();

        if (value.equals("#")) {
            return null;
        }

        TreeNode root =
            new TreeNode(Integer.parseInt(value));

        root.left = deserializeDFS(values);

        root.right = deserializeDFS(values);

        return root;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Preorder DFS + Null Markers`

## 22. Connect Nodes at Same Level — LeetCode 116 / 117

Populate each node's `next` pointer so it points to the next node on the same level.

### Java — General BFS Solution

```java
import java.util.*;

class Solution {

    public Node connect(Node root) {

        if (root == null) {
            return null;
        }

        Queue<Node> queue = new LinkedList<>();

        queue.offer(root);

        while (!queue.isEmpty()) {

            int size = queue.size();

            Node previous = null;

            for (int i = 0; i < size; i++) {

                Node current = queue.poll();

                if (previous != null) {
                    previous.next = current;
                }

                previous = current;

                if (current.left != null) {
                    queue.offer(current.left);
                }

                if (current.right != null) {
                    queue.offer(current.right);
                }
            }

            // Last node
            previous.next = null;
        }

        return root;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Level Order BFS + Previous Node`

## 23. Morris Traversal — Optional

Perform inorder traversal without recursion or an explicit stack.

### Java

```java
import java.util.*;

class Solution {

    public List<Integer> inorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();

        TreeNode current = root;

        while (current != null) {

            // No left subtree
            if (current.left == null) {

                result.add(current.val);

                current = current.right;
            }

            else {

                // Find inorder predecessor
                TreeNode predecessor = current.left;

                while (predecessor.right != null &&
                       predecessor.right != current) {

                    predecessor = predecessor.right;
                }

                // Create temporary link
                if (predecessor.right == null) {

                    predecessor.right = current;

                    current = current.left;
                }

                // Temporary link already exists
                else {

                    predecessor.right = null;

                    result.add(current.val);

                    current = current.right;
                }
            }
        }

        return result;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`  
**Pattern:** `Temporary Threaded Links`

## 24. Path Sum — LeetCode 112

Determine whether the tree has a root-to-leaf path whose values sum to `targetSum`.

### Java

```java
class Solution {

    public boolean hasPathSum(
        TreeNode root,
        int targetSum
    ) {

        if (root == null) {
            return false;
        }

        // Leaf node
        if (root.left == null &&
            root.right == null) {

            return targetSum == root.val;
        }

        int remaining =
            targetSum - root.val;

        return hasPathSum(root.left, remaining)
            || hasPathSum(root.right, remaining);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Remaining Sum`

## 25. Path Sum II — LeetCode 113

Return all root-to-leaf paths whose sum equals `targetSum`.

### Java

```java
import java.util.*;

class Solution {

    public List<List<Integer>> pathSum(
        TreeNode root,
        int targetSum
    ) {

        List<List<Integer>> result =
            new ArrayList<>();

        List<Integer> path =
            new ArrayList<>();

        dfs(root, targetSum, path, result);

        return result;
    }

    private void dfs(
        TreeNode node,
        int remaining,
        List<Integer> path,
        List<List<Integer>> result
    ) {

        if (node == null) {
            return;
        }

        path.add(node.val);

        remaining -= node.val;

        // Valid root-to-leaf path
        if (node.left == null &&
            node.right == null &&
            remaining == 0) {

            result.add(new ArrayList<>(path));
        }

        dfs(node.left, remaining, path, result);

        dfs(node.right, remaining, path, result);

        // Backtrack
        path.remove(path.size() - 1);
    }
}
```

**Time:** `O(n × h)` worst case due to copying paths  
**Space:** `O(h)` excluding output  
**Pattern:** `DFS + Backtracking + Running Sum`

## 26. Path Sum III — LeetCode 437 — Important

Count the number of downward paths whose values sum to `targetSum`. The path does not need to start at root or end at leaf.

### Java — Prefix Sum

```java
import java.util.*;

class Solution {

    public int pathSum(TreeNode root, int targetSum) {

        Map<Long, Integer> prefixMap =
            new HashMap<>();

        prefixMap.put(0L, 1);

        return dfs(
            root,
            0L,
            targetSum,
            prefixMap
        );
    }

    private int dfs(
        TreeNode node,
        long currentSum,
        int target,
        Map<Long, Integer> prefixMap
    ) {

        if (node == null) {
            return 0;
        }

        currentSum += node.val;

        // Number of previous sums that create target
        int count =
            prefixMap.getOrDefault(
                currentSum - target,
                0
            );

        prefixMap.put(
            currentSum,
            prefixMap.getOrDefault(currentSum, 0) + 1
        );

        count += dfs(
            node.left,
            currentSum,
            target,
            prefixMap
        );

        count += dfs(
            node.right,
            currentSum,
            target,
            prefixMap
        );

        // Backtrack
        prefixMap.put(
            currentSum,
            prefixMap.get(currentSum) - 1
        );

        return count;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `DFS + Prefix Sum + HashMap + Backtracking`

## 27. Binary Tree Maximum Path Sum — LeetCode 124 — VV Important

Find the maximum possible path sum between any two nodes.

### Java

```java
class Solution {

    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {

        gain(root);

        return maxSum;
    }

    private int gain(TreeNode node) {

        if (node == null) {
            return 0;
        }

        // Ignore negative paths
        int leftGain =
            Math.max(0, gain(node.left));

        int rightGain =
            Math.max(0, gain(node.right));

        // Full path through current node
        int currentPath =
            node.val + leftGain + rightGain;

        maxSum =
            Math.max(maxSum, currentPath);

        // Return one side to parent
        return node.val
            + Math.max(leftGain, rightGain);
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `Postorder DFS + Global Maximum`

# BST

## 28. Kth Smallest Element in BST — LeetCode 230

Given a BST, return its `k`th smallest element.

### Java

```java
import java.util.*;

class Solution {

    public int kthSmallest(TreeNode root, int k) {

        Stack<TreeNode> stack =
            new Stack<>();

        TreeNode current = root;

        while (current != null ||
               !stack.isEmpty()) {

            // Go left
            while (current != null) {

                stack.push(current);

                current = current.left;
            }

            current = stack.pop();

            k--;

            if (k == 0) {
                return current.val;
            }

            current = current.right;
        }

        return -1;
    }
}
```

**Time:** `O(h + k)` approximately  
**Space:** `O(h)`  
**Pattern:** `BST + Inorder`

## 29. LCA in BST — LeetCode 235

Find the lowest common ancestor of two nodes in a BST.

### Java

```java
class Solution {

    public TreeNode lowestCommonAncestor(
        TreeNode root,
        TreeNode p,
        TreeNode q
    ) {

        TreeNode current = root;

        while (current != null) {

            // Both are smaller
            if (p.val < current.val &&
                q.val < current.val) {

                current = current.left;
            }

            // Both are larger
            else if (p.val > current.val &&
                     q.val > current.val) {

                current = current.right;
            }

            // Split happens here
            else {

                return current;
            }
        }

        return null;
    }
}
```

**Time:** `O(h)`  
**Space:** `O(1)`

## 30. Inorder Predecessor and Successor in BST

For a given key, find the largest value smaller than the key and the smallest value greater than the key.

### Java

```java
class Solution {

    public int[] predecessorSuccessor(
        TreeNode root,
        int key
    ) {

        int predecessor = -1;
        int successor = -1;

        TreeNode current = root;

        // Find predecessor
        while (current != null) {

            if (current.val < key) {

                predecessor = current.val;

                current = current.right;
            }

            else {

                current = current.left;
            }
        }

        current = root;

        // Find successor
        while (current != null) {

            if (current.val > key) {

                successor = current.val;

                current = current.left;
            }

            else {

                current = current.right;
            }
        }

        return new int[]{
            predecessor,
            successor
        };
    }
}
```

**Time:** `O(h)`  
**Space:** `O(1)`

## 31. Convert Sorted Array to BST — LeetCode 108

Given a sorted array, construct a height-balanced BST.

### Java

```java
class Solution {

    public TreeNode sortedArrayToBST(int[] nums) {

        return build(
            nums,
            0,
            nums.length - 1
        );
    }

    private TreeNode build(
        int[] nums,
        int left,
        int right
    ) {

        if (left > right) {
            return null;
        }

        int mid =
            left + (right - left) / 2;

        TreeNode root =
            new TreeNode(nums[mid]);

        root.left =
            build(nums, left, mid - 1);

        root.right =
            build(nums, mid + 1, right);

        return root;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(log n)` for balanced tree  
**Pattern:** `Divide & Conquer + Middle Element`

## 32. Validate Binary Search Tree — LeetCode 98

Determine whether a binary tree is a valid BST.

### Java

```java
class Solution {

    public boolean isValidBST(TreeNode root) {

        return validate(
            root,
            Long.MIN_VALUE,
            Long.MAX_VALUE
        );
    }

    private boolean validate(
        TreeNode node,
        long min,
        long max
    ) {

        if (node == null) {
            return true;
        }

        if (node.val <= min ||
            node.val >= max) {

            return false;
        }

        return validate(
                    node.left,
                    min,
                    node.val
               )
            &&
               validate(
                    node.right,
                    node.val,
                    max
               );
    }
}
```

**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Lower/Upper Bounds`

# Quick Revision Table

| Problem                   | Main Trick                            |
| ------------------------- | ------------------------------------- |
| Level Order               | BFS + Queue                           |
| Zigzag                    | BFS + Direction Flag                  |
| Height                    | `1 + max(left, right)`                |
| Mirror Tree               | Swap left/right                       |
| Symmetric Tree            | Cross comparison                      |
| Identical Tree            | Same-side comparison                  |
| Diameter                  | Return height, update `left + right`  |
| Preorder + Inorder Build  | Preorder root + inorder split         |
| Inorder + Postorder Build | Postorder root + build right first    |
| Right View                | Last node per level                   |
| Left View                 | First node per level                  |
| Top View                  | First node per HD                     |
| Bottom View               | Last node per HD                      |
| Vertical Printing         | All nodes per HD                      |
| Boundary Traversal        | Root + left + leaves + reversed right |
| Root-to-Leaf Paths        | DFS + Backtracking                    |
| Tree to DLL               | Inorder + `prev`                      |
| Burn Tree                 | Parent Map + BFS                      |
| Binary Tree LCA           | Left result + right result            |
| Nodes Distance K          | Parent Map + BFS                      |
| Serialization             | Preorder + `#`                        |
| Connect Same Level        | BFS + previous                        |
| Morris Traversal          | Temporary predecessor link            |
| Path Sum I                | Remaining sum                         |
| Path Sum II               | DFS + Backtracking                    |
| Path Sum III              | Prefix Sum + HashMap                  |
| Maximum Path Sum          | Return one side, update both          |
| BST Kth Smallest          | Inorder = sorted                      |
| BST LCA                   | Smaller / larger / split              |
| BST Predecessor           | Largest `< key`                       |
| BST Successor             | Smallest `> key`                      |
| Sorted Array → BST        | Middle = root                         |
| Validate BST              | Min/max allowed range                 |
