# Binary Tree & BST Interview Problems — Java

## 1. Level Order Traversal — LeetCode 102
**Question:** Return the level-order traversal of a binary tree from left to right.
**Example:**
```text
        3
       / \
      9   20
         /  \
        15   7
Output: [[3],[9,20],[15,7]]
```
**Java:**
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
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
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
**Question:** Return level-order traversal while alternating direction at every level.
**Example:**
```text
        3
       / \
      9   20
         /  \
        15   7
Output: [[3],[20,9],[15,7]]
```
**Java:**
```java
import java.util.*;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            LinkedList<Integer> currentLevel = new LinkedList<>();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (leftToRight) currentLevel.addLast(node.val);
                else currentLevel.addFirst(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(currentLevel);
            leftToRight = !leftToRight;
        }
        return result;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Queue + Direction Flag`

## 3. Height / Maximum Depth of Binary Tree — LeetCode 104
**Question:** Return the height / maximum depth of a binary tree.
**Java:**
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int leftHeight = maxDepth(root.left);
        int rightHeight = maxDepth(root.right);
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Recursion`

## 4. Mirror Tree / Invert Binary Tree — LeetCode 226
**Question:** Swap the left and right child of every node and return the mirrored tree.
**Java:**
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
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
**Question:** Check whether a binary tree is a mirror of itself.
**Core Trick:** Compare `left.left ↔ right.right` and `left.right ↔ right.left`.
**Java:**
```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isMirror(root.left, root.right);
    }
    private boolean isMirror(TreeNode left, TreeNode right) {
        if (left == null && right == null) return true;
        if (left == null || right == null) return false;
        if (left.val != right.val) return false;
        return isMirror(left.left, right.right)
                && isMirror(left.right, right.left);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Mirror Comparison`

## 6. Identical Tree / Same Tree — LeetCode 100
**Question:** Check whether two trees have the same structure and the same values.
**Java:**
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left)
                && isSameTree(p.right, q.right);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Compare Two Trees`

## 7. Diameter of Binary Tree — LeetCode 543
**Question:** Return the longest path between any two nodes. LeetCode measures diameter in number of edges.
**Core Trick:** `UPDATE = leftHeight + rightHeight`, `RETURN = 1 + max(leftHeight, rightHeight)`.
**Java:**
```java
class Solution {
    int diameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        height(root);
        return diameter;
    }
    private int height(TreeNode node) {
        if (node == null) return 0;
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);
        diameter = Math.max(diameter, leftHeight + rightHeight);
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Height + Global Maximum`

## 8. Construct Binary Tree from Preorder and Inorder — LeetCode 105
**Question:** Build a binary tree using preorder and inorder traversals.
**Core Trick:** `Preorder = ROOT → LEFT → RIGHT`, `Inorder = LEFT → ROOT → RIGHT`.
**Java:**
```java
import java.util.*;

class Solution {
    int preorderIndex = 0;
    Map<Integer, Integer> inorderMap = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) inorderMap.put(inorder[i], i);
        return build(preorder, 0, inorder.length - 1);
    }
    private TreeNode build(int[] preorder, int left, int right) {
        if (left > right) return null;
        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);
        int rootIndex = inorderMap.get(rootValue);
        root.left = build(preorder, left, rootIndex - 1);
        root.right = build(preorder, rootIndex + 1, right);
        return root;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Preorder finds ROOT + Inorder splits LEFT/RIGHT`

## 9. Construct Binary Tree from Inorder and Postorder — LeetCode 106
**Question:** Build a binary tree using inorder and postorder traversals.
**Core Trick:** `Postorder = LEFT → RIGHT → ROOT`; reading backwards gives `ROOT → RIGHT → LEFT`, so build right first.
**Java:**
```java
import java.util.*;

class Solution {
    int postorderIndex;
    Map<Integer, Integer> inorderMap = new HashMap<>();
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        postorderIndex = postorder.length - 1;
        for (int i = 0; i < inorder.length; i++) inorderMap.put(inorder[i], i);
        return build(postorder, 0, inorder.length - 1);
    }
    private TreeNode build(int[] postorder, int left, int right) {
        if (left > right) return null;
        int rootValue = postorder[postorderIndex--];
        TreeNode root = new TreeNode(rootValue);
        int rootIndex = inorderMap.get(rootValue);
        root.right = build(postorder, rootIndex + 1, right);
        root.left = build(postorder, left, rootIndex - 1);
        return root;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Postorder finds ROOT + Inorder split + Build RIGHT first`

## 10. Right View of Binary Tree
**Question:** Return the nodes visible from the right side.
**Core Trick:** Last node of each BFS level.
**Java:**
```java
import java.util.*;

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) result.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Last Node of Every Level`

## 11. Left View of Binary Tree
**Question:** Return the nodes visible from the left side.
**Core Trick:** First node of each BFS level.
**Java:**
```java
import java.util.*;

class Solution {
    public List<Integer> leftView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == 0) result.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + First Node of Every Level`

## 12. Top View of Binary Tree
**Question:** Return nodes visible from the top.
**Core Trick:** First node encountered at each horizontal distance. `Left → HD-1`, `Right → HD+1`.
**Java:**
```java
import java.util.*;

class Solution {
    static class Pair {
        TreeNode node;
        int hd;
        Pair(TreeNode node, int hd) {
            this.node = node;
            this.hd = hd;
        }
    }
    public List<Integer> topView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Map<Integer, Integer> map = new TreeMap<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 0));
        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            TreeNode node = current.node;
            int hd = current.hd;
            map.putIfAbsent(hd, node.val);
            if (node.left != null) queue.offer(new Pair(node.left, hd - 1));
            if (node.right != null) queue.offer(new Pair(node.right, hd + 1));
        }
        result.addAll(map.values());
        return result;
    }
}
```
**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + First Occurrence`

## 13. Bottom View of Binary Tree — Important
**Question:** Return nodes visible from the bottom.
**Core Trick:** Last node encountered at each horizontal distance.
**Java:**
```java
import java.util.*;

class Solution {
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
        if (root == null) return result;
        Map<Integer, Integer> map = new TreeMap<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 0));
        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            TreeNode node = current.node;
            int hd = current.hd;
            map.put(hd, node.val);
            if (node.left != null) queue.offer(new Pair(node.left, hd - 1));
            if (node.right != null) queue.offer(new Pair(node.right, hd + 1));
        }
        result.addAll(map.values());
        return result;
    }
}
```
**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + Last Occurrence`

## 14. Vertical Order Traversal / Vertical Printing
**Question:** Print nodes column by column from left to right.
**Core Trick:** Group all nodes by horizontal distance.
**Java:**
```java
import java.util.*;

class Solution {
    static class Pair {
        TreeNode node;
        int hd;
        Pair(TreeNode node, int hd) {
            this.node = node;
            this.hd = hd;
        }
    }
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Map<Integer, List<Integer>> map = new TreeMap<>();
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 0));
        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            TreeNode node = current.node;
            int hd = current.hd;
            map.putIfAbsent(hd, new ArrayList<>());
            map.get(hd).add(node.val);
            if (node.left != null) queue.offer(new Pair(node.left, hd - 1));
            if (node.right != null) queue.offer(new Pair(node.right, hd + 1));
        }
        for (List<Integer> column : map.values()) result.add(column);
        return result;
    }
}
```
**Time:** `O(n log n)`  
**Space:** `O(n)`  
**Pattern:** `BFS + Horizontal Distance + TreeMap`

## 15. Boundary Traversal — Very Important
**Question:** Return the anti-clockwise boundary traversal.
**Order:** `ROOT → LEFT BOUNDARY → LEAVES → RIGHT BOUNDARY REVERSED`
**Java:**
```java
import java.util.*;

class Solution {
    public List<Integer> boundaryTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        if (!isLeaf(root)) result.add(root.val);
        addLeftBoundary(root, result);
        addLeaves(root, result);
        addRightBoundary(root, result);
        return result;
    }
    private boolean isLeaf(TreeNode node) {
        return node.left == null && node.right == null;
    }
    private void addLeftBoundary(TreeNode root, List<Integer> result) {
        TreeNode current = root.left;
        while (current != null) {
            if (!isLeaf(current)) result.add(current.val);
            if (current.left != null) current = current.left;
            else current = current.right;
        }
    }
    private void addLeaves(TreeNode node, List<Integer> result) {
        if (node == null) return;
        if (isLeaf(node)) {
            result.add(node.val);
            return;
        }
        addLeaves(node.left, result);
        addLeaves(node.right, result);
    }
    private void addRightBoundary(TreeNode root, List<Integer> result) {
        TreeNode current = root.right;
        List<Integer> temp = new ArrayList<>();
        while (current != null) {
            if (!isLeaf(current)) temp.add(current.val);
            if (current.right != null) current = current.right;
            else current = current.left;
        }
        for (int i = temp.size() - 1; i >= 0; i--) result.add(temp.get(i));
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)` recursion stack + temporary right-boundary list  
**Pattern:** `Left Boundary + Leaves + Reversed Right Boundary`

## 16. Root-to-Leaf Path Printing
**Question:** Return all root-to-leaf paths.
**Java:**
```java
import java.util.*;

class Solution {
    public List<List<Integer>> rootToLeafPaths(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(root, path, result);
        return result;
    }
    private void dfs(TreeNode node, List<Integer> path, List<List<Integer>> result) {
        if (node == null) return;
        path.add(node.val);
        if (node.left == null && node.right == null) {
            result.add(new ArrayList<>(path));
        } else {
            dfs(node.left, path, result);
            dfs(node.right, path, result);
        }
        path.remove(path.size() - 1);
    }
}
```
**Time:** `O(n × h)` worst case due to path copying  
**Space:** `O(h)` excluding output  
**Pattern:** `DFS + Path + Backtracking`

## 17. Binary Tree to Doubly Linked List
**Question:** Convert a binary tree into a DLL using inorder order.
**Core Trick:** `node.left → previous`, `node.right → next`.
**Java:**
```java
class Solution {
    TreeNode prev = null;
    TreeNode head = null;
    public TreeNode binaryTreeToDLL(TreeNode root) {
        inorder(root);
        return head;
    }
    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev == null) {
            head = node;
        } else {
            prev.right = node;
            node.left = prev;
        }
        prev = node;
        inorder(node.right);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `Inorder DFS + Previous Pointer`

## 18. Minimum Time to Burn Binary Tree from a Node — Very Important
**Question:** Fire starts at a target node and spreads every second to left, right, and parent. Return minimum time to burn the whole tree.
**Core Trick:** Create `child → parent` mapping, then BFS from target.
**Java:**
```java
import java.util.*;

class Solution {
    public int minTime(TreeNode root, int target) {
        Map<TreeNode, TreeNode> parentMap = new HashMap<>();
        TreeNode targetNode = createParentMap(root, parentMap, target);
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
                if (node.left != null && !visited.contains(node.left)) {
                    queue.offer(node.left);
                    visited.add(node.left);
                    burnedNewNode = true;
                }
                if (node.right != null && !visited.contains(node.right)) {
                    queue.offer(node.right);
                    visited.add(node.right);
                    burnedNewNode = true;
                }
                TreeNode parent = parentMap.get(node);
                if (parent != null && !visited.contains(parent)) {
                    queue.offer(parent);
                    visited.add(parent);
                    burnedNewNode = true;
                }
            }
            if (burnedNewNode) time++;
        }
        return time;
    }
    private TreeNode createParentMap(TreeNode root, Map<TreeNode, TreeNode> parentMap, int target) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        TreeNode targetNode = null;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.val == target) targetNode = node;
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
**Question:** Find the lowest node that has both `p` and `q` in its subtree.
**Java:**
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Return Information Upward`

## 20. All Nodes at Distance K from Target — LeetCode 863 — VV Important
**Question:** Return all nodes exactly `k` edges away from a target node.
**Core Trick:** Same as Burn Tree: `Parent Map + BFS + Visited`.
**Java:**
```java
import java.util.*;

class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, TreeNode> parentMap = new HashMap<>();
        buildParentMap(root, parentMap);
        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();
        queue.offer(target);
        visited.add(target);
        int distance = 0;
        while (!queue.isEmpty()) {
            if (distance == k) break;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null && !visited.contains(node.left)) {
                    visited.add(node.left);
                    queue.offer(node.left);
                }
                if (node.right != null && !visited.contains(node.right)) {
                    visited.add(node.right);
                    queue.offer(node.right);
                }
                TreeNode parent = parentMap.get(node);
                if (parent != null && !visited.contains(parent)) {
                    visited.add(parent);
                    queue.offer(parent);
                }
            }
            distance++;
        }
        List<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) result.add(queue.poll().val);
        return result;
    }
    private void buildParentMap(TreeNode root, Map<TreeNode, TreeNode> parentMap) {
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
**Question:** Convert a tree into a string and rebuild the exact same tree from that string.
**Core Trick:** Preorder traversal + null marker `#`.
**Java:**
```java
import java.util.*;

public class Codec {
    public String serialize(TreeNode root) {
        StringBuilder result = new StringBuilder();
        serializeDFS(root, result);
        return result.toString();
    }
    private void serializeDFS(TreeNode node, StringBuilder result) {
        if (node == null) {
            result.append("#,");
            return;
        }
        result.append(node.val).append(",");
        serializeDFS(node.left, result);
        serializeDFS(node.right, result);
    }
    public TreeNode deserialize(String data) {
        Queue<String> values = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserializeDFS(values);
    }
    private TreeNode deserializeDFS(Queue<String> values) {
        String value = values.poll();
        if (value.equals("#")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(value));
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
**Question:** Populate each node's `next` pointer to point to the next node on the same level.
**Java:**
```java
import java.util.*;

class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            Node previous = null;
            for (int i = 0; i < size; i++) {
                Node current = queue.poll();
                if (previous != null) previous.next = current;
                previous = current;
                if (current.left != null) queue.offer(current.left);
                if (current.right != null) queue.offer(current.right);
            }
            previous.next = null;
        }
        return root;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `Level Order BFS + Previous Node`

## 23. Morris Inorder Traversal — Optional
**Question:** Perform inorder traversal without recursion or an explicit stack.
**Core Trick:** Temporarily connect inorder predecessor's right pointer to current node.
**Java:**
```java
import java.util.*;

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        TreeNode current = root;
        while (current != null) {
            if (current.left == null) {
                result.add(current.val);
                current = current.right;
            } else {
                TreeNode predecessor = current.left;
                while (predecessor.right != null && predecessor.right != current) {
                    predecessor = predecessor.right;
                }
                if (predecessor.right == null) {
                    predecessor.right = current;
                    current = current.left;
                } else {
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
**Question:** Determine whether a root-to-leaf path has sum equal to `targetSum`.
**Java:**
```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) return targetSum == root.val;
        int remaining = targetSum - root.val;
        return hasPathSum(root.left, remaining)
                || hasPathSum(root.right, remaining);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Remaining Sum`

## 25. Path Sum II — LeetCode 113
**Question:** Return all root-to-leaf paths whose sum equals `targetSum`.
**Java:**
```java
import java.util.*;

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(root, targetSum, path, result);
        return result;
    }
    private void dfs(TreeNode node, int remaining, List<Integer> path, List<List<Integer>> result) {
        if (node == null) return;
        path.add(node.val);
        remaining -= node.val;
        if (node.left == null && node.right == null && remaining == 0) {
            result.add(new ArrayList<>(path));
        }
        dfs(node.left, remaining, path, result);
        dfs(node.right, remaining, path, result);
        path.remove(path.size() - 1);
    }
}
```
**Time:** `O(n × h)` worst case due to path copying  
**Space:** `O(h)` excluding output  
**Pattern:** `DFS + Backtracking + Running Sum`

## 26. Path Sum III — LeetCode 437 — Important
**Question:** Count downward paths whose values sum to `targetSum`. The path may start and end anywhere.
**Core Trick:** `currentPrefix - oldPrefix = target` ⇒ `oldPrefix = currentPrefix - target`.
**Java:**
```java
import java.util.*;

class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> prefixMap = new HashMap<>();
        prefixMap.put(0L, 1);
        return dfs(root, 0L, targetSum, prefixMap);
    }
    private int dfs(TreeNode node, long currentSum, int target, Map<Long, Integer> prefixMap) {
        if (node == null) return 0;
        currentSum += node.val;
        int count = prefixMap.getOrDefault(currentSum - target, 0);
        prefixMap.put(currentSum, prefixMap.getOrDefault(currentSum, 0) + 1);
        count += dfs(node.left, currentSum, target, prefixMap);
        count += dfs(node.right, currentSum, target, prefixMap);
        prefixMap.put(currentSum, prefixMap.get(currentSum) - 1);
        return count;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(n)`  
**Pattern:** `DFS + Prefix Sum + HashMap + Backtracking`

## 27. Binary Tree Maximum Path Sum — LeetCode 124 — VV Important
**Question:** Return the maximum path sum between any two nodes.
**Core Trick:** `UPDATE GLOBAL = node + left + right`, `RETURN = node + max(left, right)`.
**Java:**
```java
class Solution {
    int maxSum = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        gain(root);
        return maxSum;
    }
    private int gain(TreeNode node) {
        if (node == null) return 0;
        int leftGain = Math.max(0, gain(node.left));
        int rightGain = Math.max(0, gain(node.right));
        int currentPath = node.val + leftGain + rightGain;
        maxSum = Math.max(maxSum, currentPath);
        return node.val + Math.max(leftGain, rightGain);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `Postorder DFS + Global Maximum`

# BST Problems

## 28. Kth Smallest Element in BST — LeetCode 230
**Question:** Return the `k`th smallest value in a BST.
**Core Trick:** Inorder traversal of BST gives sorted order.
**Java:**
```java
import java.util.*;

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            current = stack.pop();
            k--;
            if (k == 0) return current.val;
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
**Question:** Find the lowest common ancestor of two nodes in a BST.
**Core Trick:** `Both smaller → LEFT`, `Both bigger → RIGHT`, otherwise current is LCA.
**Java:**
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode current = root;
        while (current != null) {
            if (p.val < current.val && q.val < current.val) {
                current = current.left;
            } else if (p.val > current.val && q.val > current.val) {
                current = current.right;
            } else {
                return current;
            }
        }
        return null;
    }
}
```
**Time:** `O(h)`  
**Space:** `O(1)`  
**Pattern:** `BST Property + Direction Choice`

## 30. Inorder Predecessor and Successor in BST
**Question:** Find `Predecessor = largest value < key` and `Successor = smallest value > key`.
**Java:**
```java
class Solution {
    public int[] predecessorSuccessor(TreeNode root, int key) {
        int predecessor = -1;
        int successor = -1;
        TreeNode current = root;
        while (current != null) {
            if (current.val < key) {
                predecessor = current.val;
                current = current.right;
            } else {
                current = current.left;
            }
        }
        current = root;
        while (current != null) {
            if (current.val > key) {
                successor = current.val;
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return new int[]{predecessor, successor};
    }
}
```
**Time:** `O(h)`  
**Space:** `O(1)`  
**Pattern:** `BST Search`

## 31. Convert Sorted Array to BST — LeetCode 108
**Question:** Construct a height-balanced BST from a sorted array.
**Core Trick:** Pick middle element as root.
**Java:**
```java
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }
    private TreeNode build(int[] nums, int left, int right) {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = build(nums, left, mid - 1);
        root.right = build(nums, mid + 1, right);
        return root;
    }
}
```
**Time:** `O(n)`  
**Space:** `O(log n)` for a balanced tree  
**Pattern:** `Divide & Conquer + Middle Element`

## 32. Validate Binary Search Tree — LeetCode 98
**Question:** Determine whether a binary tree satisfies BST rules.
**Important:** Every node must stay within its allowed `(min, max)` range; checking only immediate children is not enough.
**Java:**
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    private boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return validate(node.left, min, node.val)
                && validate(node.right, node.val, max);
    }
}
```
**Time:** `O(n)`  
**Space:** `O(h)`  
**Pattern:** `DFS + Lower/Upper Bounds`

# Quick Revision Table
| Problem | Main Trick |
|---|---|
| Level Order | BFS + Queue |
| Zigzag | BFS + Direction Flag |
| Height | `1 + max(left, right)` |
| Mirror Tree | Swap left/right |
| Symmetric Tree | Cross comparison |
| Identical Tree | Same-side comparison |
| Diameter | Return height, update `left + right` |
| Preorder + Inorder Build | Preorder root + inorder split |
| Inorder + Postorder Build | Postorder root + build right first |
| Right View | Last node per level |
| Left View | First node per level |
| Top View | First node per HD |
| Bottom View | Last node per HD |
| Vertical Printing | All nodes per HD |
| Boundary Traversal | Root + left + leaves + reversed right |
| Root-to-Leaf Paths | DFS + Backtracking |
| Tree to DLL | Inorder + `prev` |
| Burn Tree | Parent Map + BFS |
| Binary Tree LCA | Left result + right result |
| Nodes Distance K | Parent Map + BFS |
| Serialization | Preorder + `#` |
| Connect Same Level | BFS + previous |
| Morris Traversal | Temporary predecessor link |
| Path Sum I | Remaining sum |
| Path Sum II | DFS + Backtracking |
| Path Sum III | Prefix Sum + HashMap |
| Maximum Path Sum | Return one side, update both |
| BST Kth Smallest | Inorder = sorted |
| BST LCA | Smaller / larger / split |
| BST Predecessor | Largest `< key` |
| BST Successor | Smallest `> key` |
| Sorted Array → BST | Middle = root |
| Validate BST | Min/max allowed range |
