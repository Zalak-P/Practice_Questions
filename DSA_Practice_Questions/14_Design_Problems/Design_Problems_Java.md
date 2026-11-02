# Design Problems for DSA Interviews — Java

Hash-map bounds assume average-case hashing. Dynamic-array append is amortized. Space includes the designed data structure. String costs are called out where relevant.

## Stack and Queue Design

### 1. ★ Min Stack

[LeetCode 155](https://leetcode.com/problems/min-stack/)

Support push, pop, top, and minimum lookup. Store the minimum so far alongside each value.

**Input/Output**

```text
MinStack(); push(4); push(2); push(2); getMin() → 2; pop(); getMin() → 2; top() → 2
```

**Code**

```java
import java.util.*;

class MinStack {
    private final Deque<int[]> stack = new ArrayDeque<>();

    public void push(int val) {
        int minimum = stack.isEmpty() ? val : Math.min(val, stack.peek()[1]);
        stack.push(new int[]{val, minimum});
    }
    public void pop() { stack.pop(); }
    public int top() { return stack.peek()[0]; }
    public int getMin() { return stack.peek()[1]; }
}
```

**Time Space Complexity**

Each operation: O(1). Space: O(n) for n stored values.

### 2. ★ Implement Queue using Stacks

[LeetCode 232](https://leetcode.com/problems/implement-queue-using-stacks/)

Implement a FIFO queue using two stacks. Move incoming elements only when the outgoing stack is empty.

**Input/Output**

```text
MyQueue(); push(7); push(9); peek() → 7; pop() → 7; empty() → false
```

**Code**

```java
import java.util.*;

class MyQueue {
    private final Deque<Integer> incoming = new ArrayDeque<>();
    private final Deque<Integer> outgoing = new ArrayDeque<>();

    public void push(int x) { incoming.push(x); }
    private void transfer() {
        if (outgoing.isEmpty()) {
            while (!incoming.isEmpty()) outgoing.push(incoming.pop());
        }
    }
    public int pop() { transfer(); return outgoing.pop(); }
    public int peek() { transfer(); return outgoing.peek(); }
    public boolean empty() { return incoming.isEmpty() && outgoing.isEmpty(); }
}
```

**Time Space Complexity**

push/empty: O(1). pop/peek: O(1) amortized, O(n) worst case during a transfer. Space: O(n).

### 3. Implement Stack using Queues

[LeetCode 225](https://leetcode.com/problems/implement-stack-using-queues/)

Implement a LIFO stack using a queue. Rotate the existing elements after each insertion so the newest element reaches the front.

**Input/Output**

```text
MyStack(); push(7); push(9); top() → 9; pop() → 9; empty() → false
```

**Code**

```java
import java.util.*;

class MyStack {
    private final Queue<Integer> queue = new ArrayDeque<>();
    public void push(int x) {
        queue.offer(x);
        for (int i = queue.size() - 1; i > 0; i--) queue.offer(queue.remove());
    }
    public int pop() { return queue.remove(); }
    public int top() { return queue.element(); }
    public boolean empty() { return queue.isEmpty(); }
}
```

**Time Space Complexity**

push: O(n). pop/top/empty: O(1). Space: O(n).

### 4. Design Circular Queue

[LeetCode 622](https://leetcode.com/problems/design-circular-queue/)

Build a bounded FIFO queue with an array, a front index, and a size counter. Use modulo arithmetic to wrap around.

**Input/Output**

```text
MyCircularQueue(2); enQueue(5) → true; enQueue(8) → true; enQueue(9) → false; deQueue() → true; enQueue(9) → true; Front() → 8; Rear() → 9
```

**Code**

```java
class MyCircularQueue {
    private final int[] data;
    private int front = 0, size = 0;
    public MyCircularQueue(int k) { data = new int[k]; }
    public boolean enQueue(int value) {
        if (isFull()) return false;
        data[(front + size) % data.length] = value;
        size++;
        return true;
    }
    public boolean deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % data.length;
        size--;
        return true;
    }
    public int Front() { return isEmpty() ? -1 : data[front]; }
    public int Rear() { return isEmpty() ? -1 : data[(front + size - 1) % data.length]; }
    public boolean isEmpty() { return size == 0; }
    public boolean isFull() { return size == data.length; }
}
```

**Time Space Complexity**

Construction: O(k). Each operation: O(1). Space: O(k) for capacity k.

### 5. Design Circular Deque

[LeetCode 641](https://leetcode.com/problems/design-circular-deque/)

Build a bounded deque supporting insertion and deletion at both ends. Track the front position and current size in a circular array.

**Input/Output**

```text
MyCircularDeque(2); insertFront(5) → true; insertLast(8) → true; getRear() → 8; deleteFront() → true; getFront() → 8
```

**Code**

```java
class MyCircularDeque {
    private final int[] data;
    private int front = 0, size = 0;
    public MyCircularDeque(int k) { data = new int[k]; }
    public boolean insertFront(int value) {
        if (isFull()) return false;
        front = (front - 1 + data.length) % data.length;
        data[front] = value;
        size++;
        return true;
    }
    public boolean insertLast(int value) {
        if (isFull()) return false;
        data[(front + size) % data.length] = value;
        size++;
        return true;
    }
    public boolean deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % data.length;
        size--;
        return true;
    }
    public boolean deleteLast() {
        if (isEmpty()) return false;
        size--;
        return true;
    }
    public int getFront() { return isEmpty() ? -1 : data[front]; }
    public int getRear() { return isEmpty() ? -1 : data[(front + size - 1) % data.length]; }
    public boolean isEmpty() { return size == 0; }
    public boolean isFull() { return size == data.length; }
}
```

**Time Space Complexity**

Construction: O(k). Each operation: O(1). Space: O(k).

### 6. Design a Stack With Increment Operation

[LeetCode 1381](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

Support a capacity-limited stack and increment the bottom k elements. Defer increments at their boundary and propagate them downward during pop.

**Input/Output**

```text
CustomStack(3); push(1); push(2); increment(2,10); pop() → 12; pop() → 11; pop() → -1
```

**Code**

```java
class CustomStack {
    private final int[] values, pending;
    private int size = 0;
    public CustomStack(int maxSize) {
        values = new int[maxSize];
        pending = new int[maxSize];
    }
    public void push(int x) {
        if (size == values.length) return;
        values[size] = x;
        pending[size++] = 0;
    }
    public int pop() {
        if (size == 0) return -1;
        int index = --size;
        if (index > 0) pending[index - 1] += pending[index];
        return values[index] + pending[index];
    }
    public void increment(int k, int val) {
        int index = Math.min(k, size) - 1;
        if (index >= 0) pending[index] += val;
    }
}
```

**Time Space Complexity**

Construction: O(maxSize). Each operation: O(1). Space: O(maxSize) for the two preallocated arrays.

## Hash Map and Set Design

### 7. ★ Design HashMap

[LeetCode 706](https://leetcode.com/problems/design-hashmap/)

Implement integer-key put, get, and remove without a built-in hash map. Use separate chaining: each bucket holds entries whose keys share a hash. This teaching implementation uses a fixed bucket count.

**Input/Output**

```text
MyHashMap(); put(7,40); get(7) → 40; put(7,90); get(7) → 90; remove(7); get(7) → -1
```

**Code**

```java
import java.util.*;

class MyHashMap {
    private final List<List<int[]>> buckets = new ArrayList<>();
    public MyHashMap() {
        for (int i = 0; i < 2069; i++) buckets.add(new ArrayList<>());
    }
    private List<int[]> bucket(int key) { return buckets.get(Math.floorMod(key, buckets.size())); }
    public void put(int key, int value) {
        for (int[] entry : bucket(key)) {
            if (entry[0] == key) { entry[1] = value; return; }
        }
        bucket(key).add(new int[]{key, value});
    }
    public int get(int key) {
        for (int[] entry : bucket(key)) if (entry[0] == key) return entry[1];
        return -1;
    }
    public void remove(int key) {
        List<int[]> list = bucket(key);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i)[0] == key) {
                list.set(i, list.get(list.size() - 1));
                list.remove(list.size() - 1);
                return;
            }
        }
    }
}
```

**Time Space Complexity**

With B fixed buckets and n entries, expected operation time is O(1 + n/B) under uniform hashing; worst case O(n). Space: O(B+n). Expected O(1) requires a bounded load factor; a resizable production table would rehash.

### 8. Design HashSet

[LeetCode 705](https://leetcode.com/problems/design-hashset/)

Implement add, remove, and contains without a built-in hash set. Use fixed buckets with separate chaining.

**Input/Output**

```text
MyHashSet(); add(7); add(7); contains(7) → true; remove(7); contains(7) → false
```

**Code**

```java
import java.util.*;

class MyHashSet {
    private final List<List<Integer>> buckets = new ArrayList<>();
    public MyHashSet() {
        for (int i = 0; i < 2069; i++) buckets.add(new ArrayList<>());
    }
    private List<Integer> bucket(int key) { return buckets.get(Math.floorMod(key, buckets.size())); }
    public void add(int key) {
        List<Integer> list = bucket(key);
        if (!list.contains(key)) list.add(key);
    }
    public void remove(int key) {
        List<Integer> list = bucket(key);
        int index = list.indexOf(key);
        if (index < 0) return;
        list.set(index, list.get(list.size() - 1));
        list.remove(list.size() - 1);
    }
    public boolean contains(int key) { return bucket(key).contains(key); }
}
```

**Time Space Complexity**

With B buckets: expected O(1+n/B) per operation under uniform hashing, worst O(n). Space: O(B+n). Rehashing is needed to maintain expected O(1) as n grows without bound.

### 9. ★ Insert Delete GetRandom O(1)

[LeetCode 380](https://leetcode.com/problems/insert-delete-getrandom-o1/)

Support unique values with average constant-time insertion, deletion, and uniform random selection. Combine an array with a value-to-index map; delete by swapping with the last element.

**Input/Output**

```text
RandomizedSet(); insert(4) → true; insert(4) → false; insert(8) → true; remove(4) → true; getRandom() → 8
```

**Code**

```java
import java.util.*;

class RandomizedSet {
    private final List<Integer> values = new ArrayList<>();
    private final Map<Integer, Integer> index = new HashMap<>();
    private final Random random = new Random();
    public boolean insert(int val) {
        if (index.containsKey(val)) return false;
        index.put(val, values.size());
        values.add(val);
        return true;
    }
    public boolean remove(int val) {
        if (!index.containsKey(val)) return false;
        int i = index.get(val), last = values.get(values.size() - 1);
        values.set(i, last);
        index.put(last, i);
        values.remove(values.size() - 1);
        index.remove(val);
        return true;
    }
    public int getRandom() { return values.get(random.nextInt(values.size())); }
}
```

**Time Space Complexity**

insert/remove/getRandom: average O(1), including amortized array growth. Space: O(n). getRandom is called only when nonempty.

### 10. Insert Delete GetRandom O(1) – Duplicates allowed

[LeetCode 381](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)

Allow repeated values while retaining average constant-time operations. Map each value to its set of array positions. Random selection is uniform over occurrences, so duplicates increase selection probability.

**Input/Output**

```text
RandomizedCollection(); insert(4) → true; insert(4) → false; insert(8) → true; remove(4) → true; remove(4) → true; getRandom() → 8
```

**Code**

```java
import java.util.*;

class RandomizedCollection {
    private final List<Integer> values = new ArrayList<>();
    private final Map<Integer, Set<Integer>> positions = new HashMap<>();
    private final Random random = new Random();
    public boolean insert(int val) {
        boolean first = !positions.containsKey(val);
        positions.computeIfAbsent(val, x -> new HashSet<>()).add(values.size());
        values.add(val);
        return first;
    }
    public boolean remove(int val) {
        Set<Integer> set = positions.get(val);
        if (set == null) return false;
        int i = set.iterator().next();
        set.remove(i);
        int lastIndex = values.size() - 1, last = values.get(lastIndex);
        if (i != lastIndex) {
            values.set(i, last);
            positions.get(last).remove(lastIndex);
            positions.get(last).add(i);
        }
        values.remove(lastIndex);
        if (set.isEmpty()) positions.remove(val);
        return true;
    }
    public int getRandom() { return values.get(random.nextInt(values.size())); }
}
```

**Time Space Complexity**

insert/remove/getRandom: average O(1). Space: O(n) for n occurrences. Random selection requires a nonempty collection.

## Cache Design

### 11. ★ LRU Cache

[LeetCode 146](https://leetcode.com/problems/lru-cache/)

Evict the least recently used key when capacity is exceeded. A hash map locates nodes; a doubly linked list maintains recency, with the most recent node just after the head sentinel.

**Input/Output**

```text
LRUCache(2); put(1,10); put(2,20); get(1) → 10; put(3,30); get(2) → -1
```

**Code**

```java
import java.util.*;

class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;
        Node(int k, int v) { key = k; value = v; }
    }
    private final int capacity;
    private final Map<Integer, Node> nodes = new HashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0);
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    private void addFront(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }
    public int get(int key) {
        Node node = nodes.get(key);
        if (node == null) return -1;
        remove(node);
        addFront(node);
        return node.value;
    }
    public void put(int key, int value) {
        if (capacity == 0) return;
        Node node = nodes.get(key);
        if (node == null) {
            node = new Node(key, value);
            nodes.put(key, node);
        } else {
            node.value = value;
            remove(node);
        }
        addFront(node);
        if (nodes.size() > capacity) {
            Node victim = tail.prev;
            remove(victim);
            nodes.remove(victim.key);
        }
    }
}
```

**Time Space Complexity**

get/put: average O(1). Space: O(capacity).

### 12. ★ LFU Cache

[LeetCode 460](https://leetcode.com/problems/lfu-cache/)

Evict the least frequently used key, breaking frequency ties by least recent use. Maintain ordered buckets by frequency and track the minimum frequency. A successful get or an update through put increases frequency.

**Input/Output**

```text
LFUCache(2); put(1,10); put(2,20); get(1) → 10; put(3,30); get(2) → -1; get(3) → 30
```

**Code**

```java
import java.util.*;

class LFUCache {
    private final int capacity;
    private int minimum = 0;
    private final Map<Integer, int[]> items = new HashMap<>();
    private final Map<Integer, LinkedHashSet<Integer>> buckets = new HashMap<>();
    public LFUCache(int capacity) { this.capacity = capacity; }
    private void touch(int key) {
        int[] item = items.get(key);
        int frequency = item[1];
        LinkedHashSet<Integer> bucket = buckets.get(frequency);
        bucket.remove(key);
        if (bucket.isEmpty()) {
            buckets.remove(frequency);
            if (minimum == frequency) minimum++;
        }
        item[1]++;
        buckets.computeIfAbsent(item[1], x -> new LinkedHashSet<>()).add(key);
    }
    public int get(int key) {
        if (!items.containsKey(key)) return -1;
        touch(key);
        return items.get(key)[0];
    }
    public void put(int key, int value) {
        if (capacity == 0) return;
        if (items.containsKey(key)) {
            items.get(key)[0] = value;
            touch(key);
            return;
        }
        if (items.size() == capacity) {
            LinkedHashSet<Integer> bucket = buckets.get(minimum);
            int victim = bucket.iterator().next();
            bucket.remove(victim);
            items.remove(victim);
            if (bucket.isEmpty()) buckets.remove(minimum);
        }
        items.put(key, new int[]{value, 1});
        buckets.computeIfAbsent(1, x -> new LinkedHashSet<>()).add(key);
        minimum = 1;
    }
}
```

**Time Space Complexity**

get/put: average O(1). Space: O(capacity). Empty frequency buckets are deleted.

## Linked List and Iterator Design

### 13. Design Linked List

[LeetCode 707](https://leetcode.com/problems/design-linked-list/)

Implement an indexed singly linked list with a sentinel head. Support get and insertion/deletion at the head, tail, or an index. Invalid indices leave the list unchanged or return -1 for get.

**Input/Output**

```text
MyLinkedList(); addAtHead(1); addAtTail(3); addAtIndex(1,2); get(1) → 2; deleteAtIndex(1); get(1) → 3
```

**Code**

```java
class MyLinkedList {
    private static class Node {
        int value;
        Node next;
        Node(int value, Node next) { this.value = value; this.next = next; }
    }
    private final Node head = new Node(0, null);
    private int size = 0;
    public int get(int index) {
        if (index < 0 || index >= size) return -1;
        Node node = head.next;
        for (int i = 0; i < index; i++) node = node.next;
        return node.value;
    }
    public void addAtHead(int val) { addAtIndex(0, val); }
    public void addAtTail(int val) { addAtIndex(size, val); }
    public void addAtIndex(int index, int val) {
        if (index > size) return;
        index = Math.max(0, index);
        Node previous = head;
        for (int i = 0; i < index; i++) previous = previous.next;
        previous.next = new Node(val, previous.next);
        size++;
    }
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        Node previous = head;
        for (int i = 0; i < index; i++) previous = previous.next;
        previous.next = previous.next.next;
        size--;
    }
}
```

**Time Space Complexity**

addAtHead: O(1). get/addAtIndex/deleteAtIndex/addAtTail: O(n) worst case. Space: O(n).

### 14. ★ Flatten Nested List Iterator

[LeetCode 341](https://leetcode.com/problems/flatten-nested-list-iterator/)

Lazily iterate through integers inside nested lists. Keep a stack of list iterators and one cached integer. The judge supplies NestedInteger with isInteger(), getInteger(), and getList().

**Input/Output**

```text
Nested input: [[1,1],2,[1,1]]. Repeated next() while hasNext() is true → [1,1,2,1,1]. Empty nested lists produce no values.
```

**Code**

```java
import java.util.*;

// NestedInteger is supplied by the judge.
class NestedIterator implements Iterator<Integer> {
    private final Deque<Iterator<NestedInteger>> stack = new ArrayDeque<>();
    private Integer cached = null;
    private boolean ready = false;
    public NestedIterator(List<NestedInteger> nestedList) { stack.push(nestedList.iterator()); }
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        ready = false;
        return cached;
    }
    public boolean hasNext() {
        if (ready) return true;
        while (!stack.isEmpty()) {
            if (!stack.peek().hasNext()) { stack.pop(); continue; }
            NestedInteger item = stack.peek().next();
            if (item.isInteger()) {
                cached = item.getInteger();
                ready = true;
                return true;
            }
            stack.push(item.getList().iterator());
        }
        return false;
    }
}
```

**Time Space Complexity**

Let T be all integer/list objects visited and D maximum nesting depth. A full traversal takes O(T); an individual hasNext/next may traverse many empty lists, up to O(T). Auxiliary space: O(D). Repeated hasNext with a cached value is O(1).

### 15. Peeking Iterator

[LeetCode 284](https://leetcode.com/problems/peeking-iterator/)

Add peek to an existing iterator without advancing its logical position. Cache one item. Python uses the judge-supplied Iterator API next()/hasNext(); Java uses java.util.Iterator<Integer>.

**Input/Output**

```text
Underlying values: [4,7]. PeekingIterator(iterator); peek() → 4; peek() → 4; next() → 4; next() → 7; hasNext() → false
```

**Code**

```java
import java.util.*;

class PeekingIterator implements Iterator<Integer> {
    private final Iterator<Integer> iterator;
    private boolean ready = false;
    private Integer cached;
    public PeekingIterator(Iterator<Integer> iterator) { this.iterator = iterator; }
    public Integer peek() {
        if (!ready) { cached = iterator.next(); ready = true; }
        return cached;
    }
    public Integer next() {
        if (ready) { ready = false; return cached; }
        return iterator.next();
    }
    public boolean hasNext() { return ready || iterator.hasNext(); }
}
```

**Time Space Complexity**

Each operation: O(1), assuming the underlying iterator operations are O(1). Extra space: O(1).

### 16. Design Browser History

[LeetCode 1472](https://leetcode.com/problems/design-browser-history/)

Maintain browser history with a doubly linked list and a current node. Visiting a page discards forward history; back and forward stop at the ends.

**Input/Output**

```text
BrowserHistory("home"); visit("a"); visit("b"); back(1) → "a"; visit("c"); forward(1) → "c"; back(2) → "home"
```

**Code**

```java
class BrowserHistory {
    private static class Page {
        String url;
        Page prev, next;
        Page(String url) { this.url = url; }
    }
    private Page current;
    public BrowserHistory(String homepage) { current = new Page(homepage); }
    public void visit(String url) {
        Page page = new Page(url);
        page.prev = current;
        current.next = page;
        current = page;
    }
    public String back(int steps) {
        while (steps-- > 0 && current.prev != null) current = current.prev;
        return current.url;
    }
    public String forward(int steps) {
        while (steps-- > 0 && current.next != null) current = current.next;
        return current.url;
    }
}
```

**Time Space Complexity**

visit: O(1) pointer work; back/forward: O(min(steps, traversable pages)). Space: O(H) for H retained pages. Memory reclamation of discarded nodes can add runtime-dependent work.

## Trie and Dictionary Design

### 17. ★ Implement Trie (Prefix Tree)

[LeetCode 208](https://leetcode.com/problems/implement-trie-prefix-tree/)

Insert words and check exact words or prefixes. A terminal flag distinguishes complete words from prefixes; inputs use lowercase English letters.

**Input/Output**

```text
Trie(); insert("apple"); search("apple") → true; search("app") → false; startsWith("app") → true; insert("app"); search("app") → true
```

**Code**

```java
class Trie {
    private final Trie[] children = new Trie[26];
    private boolean terminal = false;
    public void insert(String word) {
        Trie node = this;
        for (char ch : word.toCharArray()) {
            int i = ch - 'a';
            if (node.children[i] == null) node.children[i] = new Trie();
            node = node.children[i];
        }
        node.terminal = true;
    }
    private Trie walk(String text) {
        Trie node = this;
        for (int j = 0; j < text.length(); j++) {
            node = node.children[text.charAt(j) - 'a'];
            if (node == null) return null;
        }
        return node;
    }
    public boolean search(String word) {
        Trie node = walk(word);
        return node != null && node.terminal;
    }
    public boolean startsWith(String prefix) { return walk(prefix) != null; }
}
```

**Time Space Complexity**

insert/search/startsWith: O(L) for input length L. Space: O(S), where S is total inserted characters, with shared prefixes reusing nodes.

### 18. ★ Design Add and Search Words Data Structure

[LeetCode 211](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

Store lowercase words and search patterns where a dot matches any single letter. Traverse a trie and branch only at wildcard positions. The Python implementation uses an explicit stack.

**Input/Output**

```text
WordDictionary(); addWord("bad"); addWord("dad"); search("pad") → false; search(".ad") → true; search("b..") → true
```

**Code**

```java
class WordDictionary {
    private static class Node {
        Node[] children = new Node[26];
        boolean terminal;
    }
    private final Node root = new Node();
    public void addWord(String word) {
        Node node = root;
        for (char ch : word.toCharArray()) {
            int i = ch - 'a';
            if (node.children[i] == null) node.children[i] = new Node();
            node = node.children[i];
        }
        node.terminal = true;
    }
    public boolean search(String word) { return dfs(root, word, 0); }
    private boolean dfs(Node node, String word, int i) {
        if (i == word.length()) return node.terminal;
        char ch = word.charAt(i);
        if (ch != '.') {
            Node child = node.children[ch - 'a'];
            return child != null && dfs(child, word, i + 1);
        }
        for (Node child : node.children) {
            if (child != null && dfs(child, word, i + 1)) return true;
        }
        return false;
    }
}
```

**Time Space Complexity**

addWord: O(L). Search: O(V) visited trie states, bounded by O(1+26+...+26^L); no-wildcard search is O(L). Storage: O(S) inserted characters. Search auxiliary space: O(26L) explicit-stack bound in Python, O(L) recursion in Java.

### 19. Map Sum Pairs

[LeetCode 677](https://leetcode.com/problems/map-sum-pairs/)

Associate values with string keys and return the sum for a prefix. When replacing a key, propagate only the value difference through trie prefix totals.

**Input/Output**

```text
MapSum(); insert("apple",3); sum("ap") → 3; insert("app",2); sum("ap") → 5; insert("apple",4); sum("ap") → 6
```

**Code**

```java
import java.util.*;

class MapSum {
    private static class Node {
        Node[] children = new Node[26];
        int total;
    }
    private final Node root = new Node();
    private final Map<String, Integer> values = new HashMap<>();
    public void insert(String key, int val) {
        int delta = val - values.getOrDefault(key, 0);
        values.put(key, val);
        Node node = root;
        node.total += delta;
        for (char ch : key.toCharArray()) {
            int i = ch - 'a';
            if (node.children[i] == null) node.children[i] = new Node();
            node = node.children[i];
            node.total += delta;
        }
    }
    public int sum(String prefix) {
        Node node = root;
        for (int j = 0; j < prefix.length(); j++) {
            node = node.children[prefix.charAt(j) - 'a'];
            if (node == null) return 0;
        }
        return node.total;
    }
}
```

**Time Space Complexity**

insert: O(L); sum: O(P) for prefix length P. Space: O(S) for distinct keys and their trie nodes.

### 20. Design Search Autocomplete System

[LeetCode 642](https://leetcode.com/problems/design-search-autocomplete-system/)

Return up to three matching sentences after each character, ranked by descending historical frequency and then lexicographic order. A # commits the current sentence and resets input. Cache only the best three sentence references at each trie node. LeetCode Premium.

**Input/Output**

```text
AutocompleteSystem(["hello","help","hey"],[3,2,1]); input("h") → ["hello","help","hey"]; input("e") → ["hello","help","hey"]; input("#") → []
```

**Code**

```java
import java.util.*;

class AutocompleteSystem {
    private static class Node {
        Map<Character, Node> children = new HashMap<>();
        List<String> best = new ArrayList<>();
    }
    private final Node root = new Node();
    private final Map<String, Integer> counts = new HashMap<>();
    private final StringBuilder buffer = new StringBuilder();
    private Node current = root;
    public AutocompleteSystem(String[] sentences, int[] times) {
        for (int i = 0; i < sentences.length; i++) add(sentences[i], times[i]);
    }
    private void add(String sentence, int count) {
        counts.put(sentence, counts.getOrDefault(sentence, 0) + count);
        Node node = root;
        for (char ch : sentence.toCharArray()) {
            node = node.children.computeIfAbsent(ch, x -> new Node());
            if (!node.best.contains(sentence)) node.best.add(sentence);
            node.best.sort((a, b) -> {
                int cmp = Integer.compare(counts.get(b), counts.get(a));
                return cmp != 0 ? cmp : a.compareTo(b);
            });
            if (node.best.size() > 3) node.best.remove(3);
        }
    }
    public List<String> input(char c) {
        if (c == '#') {
            if (buffer.length() > 0) add(buffer.toString(), 1);
            buffer.setLength(0);
            current = root;
            return new ArrayList<>();
        }
        buffer.append(c);
        if (current != null) current = current.children.get(c);
        return current == null ? new ArrayList<>() : new ArrayList<>(current.best);
    }
}
```

**Time Space Complexity**

Let S be total historical sentence characters, L maximum sentence length, and P current input length. Construction: O(S·L) conservative bound including string comparisons. Ordinary input: O(1) trie work plus O(3) output references; committing #: O(P·L) worst-case ranking/string work. Space: O(S) trie nodes, sentence storage, and constant-size top-three lists; current input O(P). Counts only increase, so updating the changed sentence plus the old top three is sufficient.

## Time-Based and Streaming Structures

### 21. ★ Time Based Key-Value Store

[LeetCode 981](https://leetcode.com/problems/time-based-key-value-store/)

Store timestamped values and return the value at the greatest timestamp no later than a query. The problem guarantees strictly increasing set timestamps, so each key history can be appended and binary-searched.

**Input/Output**

```text
TimeMap(); set("key","old",2); set("key","new",5); get("key",1) → ""; get("key",4) → "old"; get("key",5) → "new"
```

**Code**

```java
import java.util.*;

class TimeMap {
    private static class Entry {
        int time;
        String value;
        Entry(int time, String value) { this.time = time; this.value = value; }
    }
    private final Map<String, List<Entry>> history = new HashMap<>();
    public void set(String key, String value, int timestamp) {
        history.computeIfAbsent(key, x -> new ArrayList<>()).add(new Entry(timestamp, value));
    }
    public String get(String key, int timestamp) {
        List<Entry> list = history.get(key);
        if (list == null) return "";
        int low = 0, high = list.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (list.get(mid).time <= timestamp) low = mid + 1;
            else high = mid;
        }
        return low == 0 ? "" : list.get(low - 1).value;
    }
}
```

**Time Space Complexity**

set: amortized O(1); get: O(log m), where m is versions for that key. Space: O(N) records, plus stored string contents. Hashing a fresh key also depends on key length.

### 22. ★ Find Median from Data Stream

[LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/)

Maintain a max heap for the lower half and a min heap for the upper half. The lower half has either the same size or one extra element. Median is queried only after at least one insertion.

**Input/Output**

```text
MedianFinder(); addNum(2); addNum(8); findMedian() → 5.0; addNum(4); findMedian() → 4.0
```

**Code**

```java
import java.util.*;

class MedianFinder {
    private final PriorityQueue<Integer> lower = new PriorityQueue<>(Collections.reverseOrder());
    private final PriorityQueue<Integer> upper = new PriorityQueue<>();
    public void addNum(int num) {
        lower.offer(num);
        upper.offer(lower.poll());
        if (upper.size() > lower.size()) lower.offer(upper.poll());
    }
    public double findMedian() {
        if (lower.size() > upper.size()) return lower.peek();
        return ((long) lower.peek() + upper.peek()) / 2.0;
    }
}
```

**Time Space Complexity**

addNum: O(log n); findMedian: O(1). Space: O(n).

### 23. ★ Kth Largest Element in a Stream

[LeetCode 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

Keep only the k largest values in a min heap. Its root is the kth largest once at least k values have been seen, as guaranteed for valid add queries.

**Input/Output**

```text
KthLargest(3,[4,5,8,2]); add(3) → 4; add(5) → 5; add(10) → 5; add(9) → 8
```

**Code**

```java
import java.util.*;

class KthLargest {
    private final int k;
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();
    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int value : nums) add(value);
    }
    public int add(int val) {
        if (heap.size() < k) heap.offer(val);
        else if (val > heap.peek()) { heap.poll(); heap.offer(val); }
        return heap.peek();
    }
}
```

**Time Space Complexity**

Construction: O(n log(k+1)) with repeated insertions. add: O(log(k+1)). Space: O(k).

### 24. Stock Price Fluctuation

[LeetCode 2034](https://leetcode.com/problems/stock-price-fluctuation/)

Accept price updates and corrections at arbitrary timestamps. Track the latest timestamp, and use min/max heaps with lazy deletion: discard a heap entry when it differs from the timestamp’s current price.

**Input/Output**

```text
StockPrice(); update(1,10); update(2,5); current() → 5; maximum() → 10; update(1,3); maximum() → 5; minimum() → 3
```

**Code**

```java
import java.util.*;

class StockPrice {
    private final Map<Integer, Integer> prices = new HashMap<>();
    private int latest = -1;
    private final PriorityQueue<int[]> minHeap = new PriorityQueue<>((a,b) -> Integer.compare(a[0],b[0]));
    private final PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> Integer.compare(b[0],a[0]));
    public void update(int timestamp, int price) {
        prices.put(timestamp, price);
        latest = Math.max(latest, timestamp);
        minHeap.offer(new int[]{price, timestamp});
        maxHeap.offer(new int[]{price, timestamp});
    }
    public int current() { return prices.get(latest); }
    public int maximum() {
        while (prices.get(maxHeap.peek()[1]).intValue() != maxHeap.peek()[0]) maxHeap.poll();
        return maxHeap.peek()[0];
    }
    public int minimum() {
        while (prices.get(minHeap.peek()[1]).intValue() != minHeap.peek()[0]) minHeap.poll();
        return minHeap.peek()[0];
    }
}
```

**Time Space Complexity**

For U updates and T distinct timestamps: update O(log U), current O(1), maximum/minimum O((r+1) log U) when r stale entries are removed. Each inserted heap entry is removed at most once, so cleanup costs amortize across updates. Space: O(U+T), including stale entries. Queries follow at least one update.

### 25. Online Stock Span

[LeetCode 901](https://leetcode.com/problems/online-stock-span/)

For each daily price, count consecutive days ending today whose prices are no greater than today’s. Maintain decreasing prices with aggregated spans in a monotonic stack.

**Input/Output**

```text
StockSpanner(); next prices [100,80,60,70,60,75,85] → spans [1,1,1,2,1,4,6]
```

**Code**

```java
import java.util.*;

class StockSpanner {
    private final Deque<int[]> stack = new ArrayDeque<>();
    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) span += stack.pop()[1];
        stack.push(new int[]{price, span});
        return span;
    }
}
```

**Time Space Complexity**

next: O(1) amortized, O(n) worst case for a single call. Space: O(n). Each price group is pushed and popped at most once.

## Application-Style Design

### 26. ★ Design Twitter

[LeetCode 355](https://leetcode.com/problems/design-twitter/)

Implement posting, following, unfollowing, and a feed of the ten most recent tweets from the user and their followees. Merge per-user chronological tweet lists with a heap; always include the user’s own tweets.

**Input/Output**

```text
Twitter(); postTweet(1,5); follow(1,2); postTweet(2,6); getNewsFeed(1) → [6,5]; unfollow(1,2); getNewsFeed(1) → [5]
```

**Code**

```java
import java.util.*;

class Twitter {
    private long clock = 0;
    private final Map<Integer, List<long[]>> tweets = new HashMap<>();
    private final Map<Integer, Set<Integer>> following = new HashMap<>();
    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, x -> new ArrayList<>()).add(new long[]{clock++, tweetId});
    }
    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> users = new HashSet<>(following.getOrDefault(userId, Collections.emptySet()));
        users.add(userId);
        // Entry: timestamp, tweet ID, user ID, index in that user's list.
        PriorityQueue<long[]> heap = new PriorityQueue<>((a,b) -> Long.compare(b[0],a[0]));
        for (int user : users) {
            List<long[]> list = tweets.get(user);
            if (list != null && !list.isEmpty()) {
                int i = list.size() - 1;
                long[] tweet = list.get(i);
                heap.offer(new long[]{tweet[0], tweet[1], user, i});
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!heap.isEmpty() && result.size() < 10) {
            long[] item = heap.poll();
            result.add((int) item[1]);
            int user = (int) item[2], i = (int) item[3];
            if (i > 0) {
                long[] tweet = tweets.get(user).get(i - 1);
                heap.offer(new long[]{tweet[0], tweet[1], user, i - 1});
            }
        }
        return result;
    }
    public void follow(int followerId, int followeeId) {
        if (followerId != followeeId)
            following.computeIfAbsent(followerId, x -> new HashSet<>()).add(followeeId);
    }
    public void unfollow(int followerId, int followeeId) {
        Set<Integer> users = following.get(followerId);
        if (users != null) users.remove(followeeId);
    }
}
```

**Time Space Complexity**

For F followed users plus self and K=10: postTweet/follow/unfollow average amortized O(1); feed O(F log(F+1) + K log(F+1)) in this repeated-heap-insertion implementation. Feed extra space O(F+K); total storage O(tweets + users + follow relationships).

### 27. Design Underground System

[LeetCode 1396](https://leetcode.com/problems/design-underground-system/)

Record active check-ins and aggregate total duration and trip count for each directed station pair. Routes A→B and B→A are distinct; valid checkout and average queries are guaranteed.

**Input/Output**

```text
UndergroundSystem(); checkIn(1,"A",3); checkOut(1,"B",13); checkIn(2,"A",20); checkOut(2,"B",34); getAverageTime("A","B") → 12.0
```

**Code**

```java
import java.util.*;

class UndergroundSystem {
    private static class CheckIn {
        String station;
        int time;
        CheckIn(String station, int time) { this.station = station; this.time = time; }
    }
    private final Map<Integer, CheckIn> active = new HashMap<>();
    private final Map<String, Map<String, long[]>> routes = new HashMap<>();
    public void checkIn(int id, String stationName, int t) {
        active.put(id, new CheckIn(stationName, t));
    }
    public void checkOut(int id, String stationName, int t) {
        CheckIn start = active.remove(id);
        long[] stats = routes.computeIfAbsent(start.station, x -> new HashMap<>())
            .computeIfAbsent(stationName, x -> new long[2]);
        stats[0] += (long) t - start.time;
        stats[1]++;
    }
    public double getAverageTime(String startStation, String endStation) {
        long[] stats = routes.get(startStation).get(endStation);
        return (double) stats[0] / stats[1];
    }
}
```

**Time Space Complexity**

Each operation: expected O(1) excluding station-name hashing/comparison. Space: O(A+R), with A active passengers and R distinct directed routes, plus station strings.

### 28. Design an ATM Machine

[LeetCode 2241](https://leetcode.com/problems/design-an-atm-machine/)

Store counts of 20, 50, 100, 200, and 500 notes. Withdrawal must greedily prioritize larger denominations according to the problem’s rule. If that greedy attempt fails, return [-1] without changing inventory; do not search for another combination.

**Input/Output**

```text
ATM(); deposit([0,0,0,3,1]); withdraw(600) → [-1] because greedy takes 500 and cannot finish, even though 3×200 exists. withdraw(500) → [0,0,0,0,1].
```

**Code**

```java
class ATM {
    private final int[] denominations = {20, 50, 100, 200, 500};
    private final long[] counts = new long[5];
    public void deposit(int[] banknotesCount) {
        for (int i = 0; i < 5; i++) counts[i] += banknotesCount[i];
    }
    public int[] withdraw(int amount) {
        int[] used = new int[5];
        long remaining = amount;
        for (int i = 4; i >= 0; i--) {
            used[i] = (int) Math.min(counts[i], remaining / denominations[i]);
            remaining -= (long) used[i] * denominations[i];
        }
        if (remaining != 0) return new int[]{-1};
        for (int i = 0; i < 5; i++) counts[i] -= used[i];
        return used;
    }
}
```

**Time Space Complexity**

deposit/withdraw: O(5)=O(1). Space: O(5)=O(1). Java uses long for accumulated note counts.

### 29. Design a Food Rating System

[LeetCode 2353](https://leetcode.com/problems/design-a-food-rating-system/)

Update a food’s rating and return the highest-rated food in a cuisine, using lexicographically smallest name for ties. Python uses lazy heaps; Java uses ordered sets and removes the old immutable entry before inserting the new one.

**Input/Output**

```text
FoodRatings(["ramen","sushi"],["japanese","japanese"],[12,12]); highestRated("japanese") → "ramen"; changeRating("sushi",15); highestRated("japanese") → "sushi"
```

**Code**

```java
import java.util.*;

class FoodRatings {
    private static class Entry {
        String food;
        int rating;
        Entry(String food, int rating) { this.food = food; this.rating = rating; }
    }
    private final Map<String, String> cuisineOf = new HashMap<>();
    private final Map<String, Entry> entries = new HashMap<>();
    private final Map<String, TreeSet<Entry>> cuisines = new HashMap<>();
    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; i++) {
            Entry entry = new Entry(foods[i], ratings[i]);
            cuisineOf.put(foods[i], cuisines[i]);
            entries.put(foods[i], entry);
            this.cuisines.computeIfAbsent(cuisines[i], x -> new TreeSet<>((a,b) -> {
                int cmp = Integer.compare(b.rating, a.rating);
                return cmp != 0 ? cmp : a.food.compareTo(b.food);
            })).add(entry);
        }
    }
    public void changeRating(String food, int newRating) {
        TreeSet<Entry> set = cuisines.get(cuisineOf.get(food));
        set.remove(entries.get(food));
        Entry entry = new Entry(food, newRating);
        entries.put(food, entry);
        set.add(entry);
    }
    public String highestRated(String cuisine) { return cuisines.get(cuisine).first().food; }
}
```

**Time Space Complexity**

Python: construction O(N log(N+1)); changeRating O(log(N+U)); highestRated O((r+1)log(N+U)) when removing r stale entries; total stale cleanup amortizes over updates. Space O(N+U). Java: construction O(N log(N+1)); changeRating O(log C); highestRated O(log C) worst-case tree descent; space O(N), with C foods in the cuisine. Bounds exclude food-name comparison cost.

## Advanced Data Structure Design

### 30. All O`one Data Structure

[LeetCode 432](https://leetcode.com/problems/all-oone-data-structure/)

Maintain string counts with increment, decrement, and min/max key retrieval. Link nonempty frequency buckets in sorted order; a key moves only to an adjacent frequency. Any tied key is acceptable. dec is called only for existing keys.

**Input/Output**

```text
AllOne(); inc("a"); inc("a"); inc("b"); getMaxKey() → "a"; getMinKey() → "b"; dec("a"); getMaxKey() → either "a" or "b"
```

**Code**

```java
import java.util.*;

class AllOne {
    private static class Bucket {
        int count;
        LinkedHashSet<String> keys = new LinkedHashSet<>();
        Bucket prev, next;
        Bucket(int count) { this.count = count; }
    }
    private final Bucket head = new Bucket(0), tail = new Bucket(0);
    private final Map<String, Bucket> location = new HashMap<>();
    public AllOne() { head.next = tail; tail.prev = head; }
    private void insertAfter(Bucket previous, Bucket node) {
        node.prev = previous;
        node.next = previous.next;
        previous.next.prev = node;
        previous.next = node;
    }
    private void removeIfEmpty(Bucket node) {
        if (node != head && node != tail && node.keys.isEmpty()) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
    }
    public void inc(String key) {
        Bucket old = location.getOrDefault(key, head), target = old.next;
        int count = old.count + 1;
        if (target == tail || target.count != count) {
            target = new Bucket(count);
            insertAfter(old, target);
        }
        target.keys.add(key);
        location.put(key, target);
        if (old != head) { old.keys.remove(key); removeIfEmpty(old); }
    }
    public void dec(String key) {
        Bucket old = location.get(key);
        if (old.count == 1) location.remove(key);
        else {
            Bucket target = old.prev;
            if (target == head || target.count != old.count - 1) {
                target = new Bucket(old.count - 1);
                insertAfter(old.prev, target);
            }
            target.keys.add(key);
            location.put(key, target);
        }
        old.keys.remove(key);
        removeIfEmpty(old);
    }
    public String getMaxKey() {
        return tail.prev == head ? "" : tail.prev.keys.iterator().next();
    }
    public String getMinKey() {
        return head.next == tail ? "" : head.next.keys.iterator().next();
    }
}
```

**Time Space Complexity**

Each operation: average O(1) excluding key hashing. Space: O(K), with K distinct live keys. Ordered key containers allow constant-time access to a representative without scanning empty hash slots.

### 31. Range Sum Query – Mutable

[LeetCode 307](https://leetcode.com/problems/range-sum-query-mutable/)

Support point updates and inclusive range-sum queries. Use a Fenwick tree storing partial sums; update propagates the difference from the previous value.

**Input/Output**

```text
NumArray([1,3,5]); sumRange(0,2) → 9; update(1,2); sumRange(0,2) → 8
```

**Code**

```java
class NumArray {
    private final int[] values, tree;
    public NumArray(int[] nums) {
        values = new int[nums.length];
        tree = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) update(i, nums[i]);
    }
    public void update(int index, int val) {
        int delta = val - values[index];
        values[index] = val;
        for (int i = index + 1; i < tree.length; i += i & -i) tree[i] += delta;
    }
    private int prefix(int end) {
        int total = 0;
        for (int i = end; i > 0; i -= i & -i) total += tree[i];
        return total;
    }
    public int sumRange(int left, int right) { return prefix(right + 1) - prefix(left); }
}
```

**Time Space Complexity**

This construction inserts each value: O(n log(n+1)). update/sumRange: O(log(n+1)). Space: O(n).

### 32. Snapshot Array

[LeetCode 1146](https://leetcode.com/problems/snapshot-array/)

Store version history separately for each array index. Repeated sets before the next snapshot overwrite the current version. Binary search finds the last update at or before the requested snapshot.

**Input/Output**

```text
SnapshotArray(3); set(0,5); snap() → 0; set(0,6); get(0,0) → 5; snap() → 1; get(0,1) → 6
```

**Code**

```java
import java.util.*;

class SnapshotArray {
    private int snapshot = 0;
    private final List<List<int[]>> history = new ArrayList<>();
    public SnapshotArray(int length) {
        for (int i = 0; i < length; i++) {
            List<int[]> list = new ArrayList<>();
            list.add(new int[]{0, 0});
            history.add(list);
        }
    }
    public void set(int index, int val) {
        List<int[]> list = history.get(index);
        int[] last = list.get(list.size() - 1);
        if (last[0] == snapshot) last[1] = val;
        else list.add(new int[]{snapshot, val});
    }
    public int snap() { return snapshot++; }
    public int get(int index, int snap_id) {
        List<int[]> list = history.get(index);
        int low = 0, high = list.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (list.get(mid)[0] <= snap_id) low = mid + 1;
            else high = mid;
        }
        return list.get(low - 1)[1];
    }
}
```

**Time Space Complexity**

Construction: O(length). set: amortized O(1); snap: O(1); get: O(log h), where h is stored versions at the index. Space: O(length+V) for retained version entries.

### 33. Design In-Memory File System

[LeetCode 588](https://leetcode.com/problems/design-in-memory-file-system/)

Implement ls, mkdir, content append, and file reads using a trie of path components. Directory listings are lexicographically sorted; ls on a file returns only its basename. Paths are absolute and valid under the problem’s constraints. LeetCode Premium.

**Input/Output**

```text
FileSystem(); mkdir("/a/b"); addContentToFile("/a/b/note","hello"); ls("/") → ["a"]; ls("/a/b/note") → ["note"]; addContentToFile("/a/b/note"," world"); readContentFromFile("/a/b/note") → "hello world"
```

**Code**

```java
import java.util.*;

class FileSystem {
    private static class Node {
        Map<String, Node> children = new HashMap<>();
        boolean isFile;
        StringBuilder content = new StringBuilder();
    }
    private final Node root = new Node();
    private Node walk(String path, boolean create) {
        Node node = root;
        for (String part : path.split("/")) {
            if (part.isEmpty()) continue;
            if (create) node = node.children.computeIfAbsent(part, x -> new Node());
            else node = node.children.get(part);
        }
        return node;
    }
    public List<String> ls(String path) {
        Node node = walk(path, false);
        if (node.isFile) return Collections.singletonList(path.substring(path.lastIndexOf('/') + 1));
        List<String> names = new ArrayList<>(node.children.keySet());
        Collections.sort(names);
        return names;
    }
    public void mkdir(String path) { walk(path, true); }
    public void addContentToFile(String filePath, String content) {
        Node node = walk(filePath, true);
        node.isFile = true;
        node.content.append(content);
    }
    public String readContentFromFile(String filePath) { return walk(filePath, false).content.toString(); }
}
```

**Time Space Complexity**

Let P be path characters, D children in the listed directory, C appended text length, and F full file length. mkdir: expected O(P). ls(directory): O(P + D log D) name comparisons; file listing O(P). read: O(P+F). Python append: O(P) plus amortized O(1) chunk-reference append; Java append: O(P+C) amortized, with occasional copying of prior content. Space: O(total path/name data + file content + chunk metadata). String-comparison costs depend on name lengths.
