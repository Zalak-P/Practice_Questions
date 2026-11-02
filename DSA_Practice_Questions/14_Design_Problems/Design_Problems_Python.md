# Design Problems for DSA Interviews — Python

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

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
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

```python
class MyQueue:
    def __init__(self):
        self.incoming = []
        self.outgoing = []

    def push(self, x: int) -> None:
        self.incoming.append(x)

    def _transfer(self):
        if not self.outgoing:
            while self.incoming:
                self.outgoing.append(self.incoming.pop())

    def pop(self) -> int:
        self._transfer()
        return self.outgoing.pop()

    def peek(self) -> int:
        self._transfer()
        return self.outgoing[-1]

    def empty(self) -> bool:
        return not self.incoming and not self.outgoing
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

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
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

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.front = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[(self.front + self.size) % len(self.data)] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[(self.front + self.size - 1) % len(self.data)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.data)
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

```python
class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [0] * k
        self.front = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[(self.front + self.size) % len(self.data)] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.data[(self.front + self.size - 1) % len(self.data)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.data)
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

```python
class CustomStack:
    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.values = []
        self.pending = []

    def push(self, x: int) -> None:
        if len(self.values) < self.capacity:
            self.values.append(x)
            self.pending.append(0)

    def pop(self) -> int:
        if not self.values:
            return -1
        extra = self.pending.pop()
        if self.pending:
            self.pending[-1] += extra
        return self.values.pop() + extra

    def increment(self, k: int, val: int) -> None:
        index = min(k, len(self.values)) - 1
        if index >= 0:
            self.pending[index] += val
```

**Time Space Complexity**

Each operation: O(1). Stored space: O(m), where m is current size, at most maxSize. Dynamic-array pushes are amortized O(1).

## Hash Map and Set Design

### 7. ★ Design HashMap

[LeetCode 706](https://leetcode.com/problems/design-hashmap/)

Implement integer-key put, get, and remove without a built-in hash map. Use separate chaining: each bucket holds entries whose keys share a hash. This teaching implementation uses a fixed bucket count.

**Input/Output**

```text
MyHashMap(); put(7,40); get(7) → 40; put(7,90); get(7) → 90; remove(7); get(7) → -1
```

**Code**

```python
class MyHashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(2069)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        for k, value in self.buckets[key % len(self.buckets)]:
            if k == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                return
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

```python
class MyHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(2069)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % len(self.buckets)]
        for i, value in enumerate(bucket):
            if value == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                return

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % len(self.buckets)]
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

```python
import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        i = self.index[val]
        last = self.values[-1]
        self.values[i] = last
        self.index[last] = i
        self.values.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
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

```python
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.positions = defaultdict(set)

    def insert(self, val: int) -> bool:
        first = not self.positions[val]
        self.positions[val].add(len(self.values))
        self.values.append(val)
        return first

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        i = self.positions[val].pop()
        last_index = len(self.values) - 1
        last = self.values[-1]
        if i != last_index:
            self.values[i] = last
            self.positions[last].remove(last_index)
            self.positions[last].add(i)
        self.values.pop()
        if not self.positions[val]:
            del self.positions[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
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

```python
class _Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head, self.tail = _Node(), _Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._remove(node)
        else:
            node = _Node(key, value)
            self.nodes[key] = node
        self._add_front(node)
        if len(self.nodes) > self.capacity:
            victim = self.tail.prev
            self._remove(victim)
            del self.nodes[victim.key]
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

```python
from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = {}  # key -> (value, frequency)
        self.buckets = {}  # frequency -> oldest-to-newest keys
        self.minimum = 0

    def _touch(self, key):
        value, frequency = self.items[key]
        del self.buckets[frequency][key]
        if not self.buckets[frequency]:
            del self.buckets[frequency]
            if self.minimum == frequency:
                self.minimum += 1
        self.items[key] = (value, frequency + 1)
        self.buckets.setdefault(frequency + 1, OrderedDict())[key] = None

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        self._touch(key)
        return self.items[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.items:
            _, frequency = self.items[key]
            self.items[key] = (value, frequency)
            self._touch(key)
            return
        if len(self.items) == self.capacity:
            bucket = self.buckets[self.minimum]
            victim, _ = bucket.popitem(last=False)
            del self.items[victim]
            if not bucket:
                del self.buckets[self.minimum]
        self.items[key] = (value, 1)
        self.buckets.setdefault(1, OrderedDict())[key] = None
        self.minimum = 1
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

```python
class _ListNode:
    def __init__(self, value=0, next_node=None):
        self.value, self.next = value, next_node

class MyLinkedList:
    def __init__(self):
        self.head = _ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
        return node.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        previous = self.head
        for _ in range(index):
            previous = previous.next
        previous.next = _ListNode(val, previous.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        previous = self.head
        for _ in range(index):
            previous = previous.next
        previous.next = previous.next.next
        self.size -= 1
```

**Time Space Complexity**

addAtHead: O(1). get/addAtIndex/deleteAtIndex/addAtTail: O(n) worst case. Space: O(n).

Python 3. NestedInteger for problem 341 and the underlying Iterator for problem 284 are supplied by LeetCode.

### 14. ★ Flatten Nested List Iterator

[LeetCode 341](https://leetcode.com/problems/flatten-nested-list-iterator/)

Lazily iterate through integers inside nested lists. Keep a stack of list iterators and one cached integer. The judge supplies NestedInteger with isInteger(), getInteger(), and getList().

**Input/Output**

```text
Nested input: [[1,1],2,[1,1]]. Repeated next() while hasNext() is true → [1,1,2,1,1]. Empty nested lists produce no values.
```

**Code**

```python
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [iter(nestedList)]
        self.ready = False
        self.cached = None

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        self.ready = False
        return self.cached

    def hasNext(self) -> bool:
        if self.ready:
            return True
        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue
            if item.isInteger():
                self.cached = item.getInteger()
                self.ready = True
                return True
            self.stack.append(iter(item.getList()))
        return False
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

```python
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.ready = False
        self.cached = None

    def peek(self):
        if not self.ready:
            self.cached = self.iterator.next()
            self.ready = True
        return self.cached

    def next(self):
        if self.ready:
            self.ready = False
            return self.cached
        return self.iterator.next()

    def hasNext(self):
        return self.ready or self.iterator.hasNext()
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

```python
class _Page:
    def __init__(self, url):
        self.url = url
        self.prev = self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = _Page(homepage)

    def visit(self, url: str) -> None:
        page = _Page(url)
        page.prev = self.current
        self.current.next = page
        self.current = page

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url
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

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.terminal = True

    def _walk(self, text):
        node = self
        for ch in text:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.terminal

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
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

```python
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if "$" in node:
                    return True
                continue
            ch = word[i]
            if ch == ".":
                for letter, child in node.items():
                    if letter != "$":
                        stack.append((child, i + 1))
            elif ch in node:
                stack.append((node[ch], i + 1))
        return False
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

```python
class _SumNode:
    def __init__(self):
        self.children = {}
        self.total = 0

class MapSum:
    def __init__(self):
        self.root = _SumNode()
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.values.get(key, 0)
        self.values[key] = val
        node = self.root
        node.total += delta
        for ch in key:
            if ch not in node.children:
                node.children[ch] = _SumNode()
            node = node.children[ch]
            node.total += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return 0
        return node.total
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

```python
class _AutoNode:
    def __init__(self):
        self.children = {}
        self.best = []

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = _AutoNode()
        self.counts = {}
        self.buffer = []
        self.current = self.root
        for sentence, count in zip(sentences, times):
            self._add(sentence, count)

    def _add(self, sentence, count):
        self.counts[sentence] = self.counts.get(sentence, 0) + count
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = _AutoNode()
            node = node.children[ch]
            if sentence not in node.best:
                node.best.append(sentence)
            node.best.sort(key=lambda s: (-self.counts[s], s))
            del node.best[3:]

    def input(self, c: str):
        if c == "#":
            if self.buffer:
                self._add("".join(self.buffer), 1)
            self.buffer = []
            self.current = self.root
            return []
        self.buffer.append(c)
        if self.current is not None:
            self.current = self.current.children.get(c)
        return list(self.current.best) if self.current else []
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

```python
class TimeMap:
    def __init__(self):
        self.history = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        items = self.history.get(key, [])
        low, high = 0, len(items)
        while low < high:
            mid = (low + high) // 2
            if items[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid
        return items[low - 1][1] if low else ""
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

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []  # Negated values simulate a max heap.
        self.upper = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0
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

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.heap = []
        for value in nums:
            self.add(value)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
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

```python
import heapq

class StockPrice:
    def __init__(self):
        self.prices = {}
        self.latest = -1
        self.minimum_heap = []
        self.maximum_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.minimum_heap, (price, timestamp))
        heapq.heappush(self.maximum_heap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest]

    def maximum(self) -> int:
        while self.prices[self.maximum_heap[0][1]] != -self.maximum_heap[0][0]:
            heapq.heappop(self.maximum_heap)
        return -self.maximum_heap[0][0]

    def minimum(self) -> int:
        while self.prices[self.minimum_heap[0][1]] != self.minimum_heap[0][0]:
            heapq.heappop(self.minimum_heap)
        return self.minimum_heap[0][0]
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

```python
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
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

```python
import heapq

class Twitter:
    def __init__(self):
        self.clock = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.clock, tweetId))
        self.clock += 1

    def getNewsFeed(self, userId: int):
        users = self.following.get(userId, set()) | {userId}
        heap = []
        for user in users:
            items = self.tweets.get(user, [])
            if items:
                i = len(items) - 1
                time, tweet = items[i]
                heapq.heappush(heap, (-time, tweet, user, i))
        result = []
        while heap and len(result) < 10:
            _, tweet, user, i = heapq.heappop(heap)
            result.append(tweet)
            if i > 0:
                time, previous_tweet = self.tweets[user][i - 1]
                heapq.heappush(heap, (-time, previous_tweet, user, i - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
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

```python
class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, check_in_time = self.active.pop(id)
        key = (start, stationName)
        total, count = self.routes.get(key, (0, 0))
        self.routes[key] = (total + t - check_in_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.routes[(startStation, endStation)]
        return total / count
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

```python
class ATM:
    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.counts = [0] * 5

    def deposit(self, banknotesCount) -> None:
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount: int):
        used = [0] * 5
        for i in range(4, -1, -1):
            used[i] = min(self.counts[i], amount // self.denominations[i])
            amount -= used[i] * self.denominations[i]
        if amount:
            return [-1]
        for i in range(5):
            self.counts[i] -= used[i]
        return used
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

```python
import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foods = {}
        self.heaps = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (cuisine, rating)
            heapq.heappush(self.heaps.setdefault(cuisine, []), (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foods[food]
        self.foods[food] = (cuisine, newRating)
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while -heap[0][0] != self.foods[heap[0][1]][1]:
            heapq.heappop(heap)
        return heap[0][1]
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

```python
from collections import OrderedDict

class _Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = OrderedDict()
        self.prev = self.next = None

class AllOne:
    def __init__(self):
        self.head, self.tail = _Bucket(0), _Bucket(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.location = {}

    def _insert_after(self, previous, node):
        node.prev, node.next = previous, previous.next
        previous.next.prev = node
        previous.next = node

    def _remove_if_empty(self, node):
        if node is not self.head and node is not self.tail and not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        old = self.location.get(key, self.head)
        count = old.count + 1
        target = old.next
        if target is self.tail or target.count != count:
            target = _Bucket(count)
            self._insert_after(old, target)
        target.keys[key] = None
        self.location[key] = target
        if old is not self.head:
            del old.keys[key]
            self._remove_if_empty(old)

    def dec(self, key: str) -> None:
        old = self.location[key]
        if old.count == 1:
            del self.location[key]
        else:
            target = old.prev
            if target is self.head or target.count != old.count - 1:
                target = _Bucket(old.count - 1)
                self._insert_after(old.prev, target)
            target.keys[key] = None
            self.location[key] = target
        del old.keys[key]
        self._remove_if_empty(old)

    def getMaxKey(self) -> str:
        return "" if self.tail.prev is self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next is self.tail else next(iter(self.head.next.keys))
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

```python
class NumArray:
    def __init__(self, nums):
        self.values = [0] * len(nums)
        self.tree = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self.update(i, value)

    def update(self, index: int, val: int) -> None:
        delta = val - self.values[index]
        self.values[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def _prefix(self, end):
        total = 0
        while end > 0:
            total += self.tree[end]
            end -= end & -end
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)
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

```python
class SnapshotArray:
    def __init__(self, length: int):
        self.snapshot = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        items = self.history[index]
        if items[-1][0] == self.snapshot:
            items[-1] = (self.snapshot, val)
        else:
            items.append((self.snapshot, val))

    def snap(self) -> int:
        result = self.snapshot
        self.snapshot += 1
        return result

    def get(self, index: int, snap_id: int) -> int:
        items = self.history[index]
        low, high = 0, len(items)
        while low < high:
            mid = (low + high) // 2
            if items[mid][0] <= snap_id:
                low = mid + 1
            else:
                high = mid
        return items[low - 1][1]
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

```python
class _FileNode:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.chunks = []

class FileSystem:
    def __init__(self):
        self.root = _FileNode()

    def _walk(self, path, create=False):
        node = self.root
        for part in path.split("/"):
            if not part:
                continue
            if create and part not in node.children:
                node.children[part] = _FileNode()
            node = node.children[part]
        return node

    def ls(self, path: str):
        node = self._walk(path)
        return [path.rsplit("/", 1)[-1]] if node.is_file else sorted(node.children)

    def mkdir(self, path: str) -> None:
        self._walk(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath, True)
        node.is_file = True
        node.chunks.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        return "".join(self._walk(filePath).chunks)
```

**Time Space Complexity**

Let P be path characters, D children in the listed directory, C appended text length, and F full file length. mkdir: expected O(P). ls(directory): O(P + D log D) name comparisons; file listing O(P). read: O(P+F). Python append: O(P) plus amortized O(1) chunk-reference append; Java append: O(P+C) amortized, with occasional copying of prior content. Space: O(total path/name data + file content + chunk metadata). String-comparison costs depend on name lengths.
