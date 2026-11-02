# Sliding Window and Trie — Python

Basic sum/product windows rely on nonnegative/positive inputs as specified. Negative-number sum problems may require prefix sums or monotonic deques.

## Sliding Window

**Pattern: Fixed-size window**

### 1. ★ Maximum Average Subarray I

[LeetCode 643 Link](https://leetcode.com/problems/maximum-average-subarray-i/)

Return the maximum average of any contiguous subarray of length k. Assume 1 <= k <= len(nums).

**Input/Output**

```text
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
```

**Code**

Keep a running sum of exactly k elements; add the incoming value and subtract the outgoing value.

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = sum(nums[i] for i in range(k))
        best = total
        for right in range(k, len(nums)):
            total += nums[right] - nums[right - k]
            best = max(best, total)
        return best / k
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 2. ★ Maximum Number of Vowels in a Substring of Given Length

[LeetCode 1456 Link](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

Return the largest number of lowercase English vowels in any substring of length k.

**Input/Output**

```text
Input: s = "abciiidef", k = 3
Output: 3
```

**Code**

Track the vowel count in a fixed-size window.

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = best = 0
        for r, ch in enumerate(s):
            count += ch in vowels
            if r >= k:
                count -= s[r - k] in vowels
            if r >= k - 1:
                best = max(best, count)
        return best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 3. ★ Permutation in String

[LeetCode 567 Link](https://leetcode.com/problems/permutation-in-string/)

Return whether s2 contains a permutation of s1. Both strings contain lowercase English letters.

**Input/Output**

```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
```

**Code**

Compare 26-letter frequency arrays for windows of length len(s1).

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need, window = [0] * 26, [0] * 26
        for ch in s1:
            need[ord(ch) - 97] += 1
        for r, ch in enumerate(s2):
            window[ord(ch) - 97] += 1
            if r >= len(s1):
                window[ord(s2[r - len(s1)]) - 97] -= 1
            if r >= len(s1) - 1 and window == need:
                return True
        return False
```

**Time / Space Complexity**

Time: O(m + 26n) = O(m + n), where m = len(s1), n = len(s2). Auxiliary space: O(26) = O(1).

### 4. Find All Anagrams in a String

[LeetCode 438 Link](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Return the starting indices of all substrings of s that are anagrams of p. Inputs contain lowercase English letters.

**Input/Output**

```text
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
```

**Code**

Use a fixed-size frequency window of length len(p).

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        need, window = [0] * 26, [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1
        answer = []
        for r, ch in enumerate(s):
            window[ord(ch) - 97] += 1
            if r >= len(p):
                window[ord(s[r - len(p)]) - 97] -= 1
            if r >= len(p) - 1 and window == need:
                answer.append(r - len(p) + 1)
        return answer
```

**Time / Space Complexity**

Time: O(m + 26n) = O(m + n). Auxiliary space: O(1), excluding O(n) worst-case output.

### 5. Maximum Sum of Distinct Subarrays With Length K

[LeetCode 2461 Link](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)

Return the largest sum of a length-k subarray whose elements are all distinct. Return 0 if none exists; nums contains positive integers.

**Input/Output**

```text
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
```

**Code**

Maintain the sum and a frequency map. A length-k window is valid when the map has k keys.

```python
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        total = best = 0
        for r, x in enumerate(nums):
            total += x
            freq[x] = freq.get(x, 0) + 1
            if r >= k:
                old = nums[r - k]
                total -= old
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
            if r >= k - 1 and len(freq) == k:
                best = max(best, total)
        return best
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(k).

**Pattern: Longest valid window**

### 6. ★ Longest Substring Without Repeating Characters

[LeetCode 3 Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Return the length of the longest substring containing no repeated characters.

**Input/Output**

```text
Input: s = "abcabcbb"
Output: 3
```

**Code**

Store each character's most recent index. Move left past a duplicate only when it lies inside the current window.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = best = 0
        for r, ch in enumerate(s):
            left = max(left, last.get(ch, -1) + 1)
            last[ch] = r
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(min(n, A)), where A is the character alphabet size.

### 7. ★ Max Consecutive Ones III

[LeetCode 1004 Link](https://leetcode.com/problems/max-consecutive-ones-iii/)

In a binary array, return the longest run of ones achievable by flipping at most k zeros.

**Input/Output**

```text
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
```

**Code**

Shrink whenever the window contains more than k zeros.

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zeros = best = 0
        for r, x in enumerate(nums):
            zeros += x == 0
            while zeros > k:
                zeros -= nums[left] == 0
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 8. ★ Fruit Into Baskets

[LeetCode 904 Link](https://leetcode.com/problems/fruit-into-baskets/)

Return the longest contiguous subarray containing at most two distinct fruit types.

**Input/Output**

```text
Input: fruits = [1,2,3,2,2]
Output: 4
```

**Code**

Count fruit types; shrink from the left whenever a third distinct type appears.

```python
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        left = best = 0
        for r, x in enumerate(fruits):
            freq[x] = freq.get(x, 0) + 1
            while len(freq) > 2:
                old = fruits[left]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(1), since the map holds at most three types.

### 9. ★ Longest Repeating Character Replacement

[LeetCode 424 Link](https://leetcode.com/problems/longest-repeating-character-replacement/)

Return the longest substring that can become one repeated uppercase English character using at most k replacements.

**Input/Output**

```text
Input: s = "AABABBA", k = 1
Output: 4
```

**Code**

Track a historical maximum character frequency. If window length minus that frequency exceeds k, shrink. The historical maximum can stay stale: it prevents a larger answer unless a sufficient frequency has actually been reached.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = max_freq = best = 0
        for r, ch in enumerate(s):
            i = ord(ch) - ord('A')
            freq[i] += 1
            max_freq = max(max_freq, freq[i])
            while r - left + 1 - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(26) = O(1).

### 10. Longest Subarray of 1's After Deleting One Element

[LeetCode 1493 Link](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

Delete exactly one element from a binary array and return the longest remaining run of ones.

**Input/Output**

```text
Input: nums = [1,1,0,1]
Output: 3
```

**Code**

Keep at most one zero. Subtract one from the window length because deletion is mandatory, including for an all-ones array.

```python
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = zeros = best = 0
        for r, x in enumerate(nums):
            zeros += x == 0
            while zeros > 1:
                zeros -= nums[left] == 0
                left += 1
            best = max(best, r - left)
        return best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 11. Get Equal Substrings Within Budget

[LeetCode 1208 Link](https://leetcode.com/problems/get-equal-substrings-within-budget/)

For equal-length strings s and t, changing position i costs abs(ord(s[i]) - ord(t[i])). Return the longest substring with total cost at most maxCost.

**Input/Output**

```text
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
```

**Code**

Expand while adding conversion costs; shrink while the budget is exceeded.

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = best = 0
        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

**Pattern: Smallest valid window**

### 12. ★ Minimum Size Subarray Sum

[LeetCode 209 Link](https://leetcode.com/problems/minimum-size-subarray-sum/)

For positive integers nums and a positive target, return the minimum subarray length with sum at least target. Return 0 if none exists.

**Input/Output**

```text
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
```

**Code**

Expand to reach the target, then shrink while the sum remains large enough. Positivity makes this monotonic.

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = total = 0
        best = len(nums) + 1
        for r, x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best, r - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best > len(nums) else best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 13. ★ Minimum Window Substring

[LeetCode 76 Link](https://leetcode.com/problems/minimum-window-substring/)

Return the shortest substring of s containing every character of t with its required multiplicity. Return an empty string if impossible.

**Input/Output**

```text
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Code**

Count missing characters. Expand until none are missing; then repeatedly shrink while recording the shortest valid window.

```python
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        need = Counter(t)
        missing = len(t)
        left = start = 0
        best = len(s) + 1
        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if r - left + 1 < best:
                    start, best = left, r - left + 1
                old = s[left]
                need[old] += 1
                if need[old] > 0:
                    missing += 1
                left += 1
        return '' if best > len(s) else s[start:start + best]
```

**Time / Space Complexity**

Time: O(n + m) expected. Auxiliary space: O(A) for character counts, plus O(n) worst-case returned substring.

### 14. Minimum Operations to Reduce X to Zero

[LeetCode 1658 Link](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

Remove values from either end of a positive-integer array until their sum equals x. Return the fewest removals, or -1 if impossible.

**Input/Output**

```text
Input: nums = [1,1,4,2,3], x = 5
Output: 2
```

**Code**

Keep the longest middle subarray with sum total - x. Answer = n minus its length.

```python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left = total = 0
        best = -1
        for r, value in enumerate(nums):
            total += value
            while total > target:
                total -= nums[left]
                left += 1
            if total == target:
                best = max(best, r - left + 1)
        return -1 if best == -1 else len(nums) - best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

**Pattern: Counting windows**

### 15. ★ Subarray Product Less Than K

[LeetCode 713 Link](https://leetcode.com/problems/subarray-product-less-than-k/)

Count contiguous nonempty subarrays with product strictly less than k. Every array value is a positive integer.

**Input/Output**

```text
Input: nums = [10,5,2,6], k = 100
Output: 8
```

**Code**

Shrink while product >= k. Once valid, every suffix ending at right is valid, giving right - left + 1 new subarrays.

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = answer = 0
        product = 1
        for r, x in enumerate(nums):
            product *= x
            while product >= k:
                product //= nums[left]
                left += 1
            answer += r - left + 1
        return answer
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1), under fixed-width integer constraints.

### 16. ★ Binary Subarrays With Sum

[LeetCode 930 Link](https://leetcode.com/problems/binary-subarrays-with-sum/)

Count nonempty subarrays of a binary array with sum exactly goal.

**Input/Output**

```text
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
```

**Code**

Exactly(goal) = atMost(goal) - atMost(goal - 1). The helper returns 0 for a negative bound, handling goal = 0 correctly.

```python
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def at_most(bound):
            if bound < 0:
                return 0
            left = total = count = 0
            for r, x in enumerate(nums):
                total += x
                while total > bound:
                    total -= nums[left]
                    left += 1
                count += r - left + 1
            return count
        return at_most(goal) - at_most(goal - 1)
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 17. ★ Count Number of Nice Subarrays

[LeetCode 1248 Link](https://leetcode.com/problems/count-number-of-nice-subarrays/)

Count contiguous subarrays containing exactly k odd numbers.

**Input/Output**

```text
Input: nums = [1,1,2,1,1], k = 3
Output: 2
```

**Code**

Treat odd numbers as 1 and even numbers as 0. Subtract the counts with at most k - 1 odds from those with at most k.

```python
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def at_most(bound):
            if bound < 0:
                return 0
            left = odds = count = 0
            for r, x in enumerate(nums):
                odds += x % 2
                while odds > bound:
                    odds -= nums[left] % 2
                    left += 1
                count += r - left + 1
            return count
        return at_most(k) - at_most(k - 1)
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 18. ★ Subarrays with K Different Integers

[LeetCode 992 Link](https://leetcode.com/problems/subarrays-with-k-different-integers/)

Count contiguous subarrays containing exactly k distinct integer values.

**Input/Output**

```text
Input: nums = [1,2,1,2,3], k = 2
Output: 7
```

**Code**

Exactly k distinct = at most k distinct minus at most k - 1 distinct. Remove map keys when their counts reach zero.

```python
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def at_most(bound):
            if bound < 0:
                return 0
            freq = {}
            left = count = 0
            for r, x in enumerate(nums):
                freq[x] = freq.get(x, 0) + 1
                while len(freq) > bound:
                    old = nums[left]
                    freq[old] -= 1
                    if freq[old] == 0:
                        del freq[old]
                    left += 1
                count += r - left + 1
            return count
        return at_most(k) - at_most(k - 1)
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(k) for k >= 1.

### 19. Number of Substrings Containing All Three Characters

[LeetCode 1358 Link](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

For a string containing only a, b, and c, count substrings containing at least one of each.

**Input/Output**

```text
Input: s = "abcabc"
Output: 10
```

**Code**

While all three counts are positive, shrink the left edge. Afterwards exactly left starting positions produce valid substrings ending at right.

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0, 0, 0]
        left = answer = 0
        for ch in s:
            freq[ord(ch) - 97] += 1
            while all(freq):
                freq[ord(s[left]) - 97] -= 1
                left += 1
            answer += left
        return answer
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 20. Count Subarrays Where Max Element Appears at Least K Times

[LeetCode 2962 Link](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)

Count subarrays containing at least k occurrences of the maximum value of the entire array; k >= 1.

**Input/Output**

```text
Input: nums = [1,3,2,3,3], k = 2
Output: 6
```

**Code**

Count global-maximum occurrences. Shrink until fewer than k remain; then left is the number of valid starts for this right endpoint.

```python
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maximum = max(nums)
        left = count = answer = 0
        for x in nums:
            count += x == maximum
            while count >= k:
                count -= nums[left] == maximum
                left += 1
            answer += left
        return answer
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

**Pattern: Supporting data structures**

### 21. ★ Sliding Window Maximum

[LeetCode 239 Link](https://leetcode.com/problems/sliding-window-maximum/)

Return the maximum value in each contiguous window of length k.

**Input/Output**

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Code**

Keep indices in a deque with values in decreasing order. Remove expired indices from the front and dominated indices from the back.

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        answer = []
        for r, x in enumerate(nums):
            while q and q[0] <= r - k:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(r)
            if r >= k - 1:
                answer.append(nums[q[0]])
        return answer
```

**Time / Space Complexity**

Time: O(n), since each index enters and leaves once. Auxiliary space: O(k), excluding O(n - k + 1) output.

### 22. ★ Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

[LeetCode 1438 Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

Return the longest subarray whose maximum minus minimum is at most limit.

**Input/Output**

```text
Input: nums = [8,2,4,7], limit = 4
Output: 2
```

**Code**

Use decreasing and increasing deques for the current maximum and minimum. Shrink while their difference exceeds limit.

```python
from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        high, low = deque(), deque()
        left = best = 0
        for r, x in enumerate(nums):
            while high and nums[high[-1]] <= x:
                high.pop()
            while low and nums[low[-1]] >= x:
                low.pop()
            high.append(r)
            low.append(r)
            while nums[high[0]] - nums[low[0]] > limit:
                if high[0] == left:
                    high.popleft()
                if low[0] == left:
                    low.popleft()
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(n) worst case.

### 23. Frequency of the Most Frequent Element

[LeetCode 1838 Link](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

Using at most k increments, maximize the frequency of any value. Each operation increases one array element by 1.

**Input/Output**

```text
Input: nums = [1,2,4], k = 5
Output: 3
```

**Code**

Sort. The cost of raising a window to its rightmost value is value \* length - window sum. Shrink when cost exceeds k.

```python
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = total = best = 0
        for r, x in enumerate(nums):
            total += x
            while x * (r - left + 1) - total > k:
                total -= nums[left]
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n log n). Auxiliary space: Python O(n), Java O(log n) sorting stack. The input array is sorted in place.

### 24. Maximum Points You Can Obtain from Cards

[LeetCode 1423 Link](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

Take exactly k cards, each from either end of the array. Return the largest total score.

**Input/Output**

```text
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
```

**Code**

The cards left behind form one window of length n - k. Subtract its minimum sum from the total.

```python
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        size = len(cardPoints) - k
        total = sum(cardPoints)
        if size == 0:
            return total
        window = sum(cardPoints[i] for i in range(size))
        smallest = window
        for r in range(size, len(cardPoints)):
            window += cardPoints[r] - cardPoints[r - size]
            smallest = min(smallest, window)
        return total - smallest
```

**Time / Space Complexity**

Time: O(n). Auxiliary space: O(1).

### 25. Sliding Window Median

[LeetCode 480 Link](https://leetcode.com/problems/sliding-window-median/)

Return the median of every contiguous window of length k. For even k, average the two middle values.

**Input/Output**

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
```

**Code**

Python: maintain a max-heap for the lower half and a min-heap for the upper half, with lazy removal and logical sizes. Buried stale entries may accumulate. Java: maintain two TreeMap multisets with immediate removal. Keep the lower half equal in size to the upper half or larger by one.

```python
import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        low, high = [], []
        delayed = Counter()
        low_size = high_size = 0

        def prune(heap, sign):
            while heap and delayed[sign * heap[0]]:
                value = sign * heapq.heappop(heap)
                delayed[value] -= 1
                if delayed[value] == 0:
                    del delayed[value]

        def balance():
            nonlocal low_size, high_size
            if low_size > high_size + 1:
                heapq.heappush(high, -heapq.heappop(low))
                low_size -= 1
                high_size += 1
                prune(low, -1)
            elif low_size < high_size:
                heapq.heappush(low, -heapq.heappop(high))
                high_size -= 1
                low_size += 1
                prune(high, 1)

        def add(value):
            nonlocal low_size, high_size
            if not low or value <= -low[0]:
                heapq.heappush(low, -value)
                low_size += 1
            else:
                heapq.heappush(high, value)
                high_size += 1
            balance()

        def remove(value):
            nonlocal low_size, high_size
            delayed[value] += 1
            if value <= -low[0]:
                low_size -= 1
                if value == -low[0]:
                    prune(low, -1)
            else:
                high_size -= 1
                if high and value == high[0]:
                    prune(high, 1)
            balance()

        for i in range(k):
            add(nums[i])
        answer = []
        for start in range(len(nums) - k + 1):
            answer.append(float(-low[0]) if k % 2 else (-low[0] + high[0]) / 2)
            if start + k < len(nums):
                add(nums[start + k])
                remove(nums[start])
        return answer
```

**Time / Space Complexity**

Python: O(n log n) time and O(n) auxiliary space worst case for these lazy heaps. Java: O(n log(k + 1)) time and O(k) auxiliary space. Both exclude O(n - k + 1) output.

## Trie

Trie notation: L = word length, P = prefix length, S = total dictionary characters, N = number of words, A = alphabet size. Hash-map bounds assume expected constant-time operations. Output space is excluded only where explicitly stated.

**Pattern: Implementation and prefix basics**

### 26. ★ Implement Trie (Prefix Tree)

[LeetCode 208 Link](https://leetcode.com/problems/implement-trie-prefix-tree/)

Implement insert, exact search, and prefix search for lowercase English words. A delete extension from the earlier Java notes is retained: it removes the word and prunes unused nodes.

**Input/Output**

```text
Operations: insert("apple"), search("apple"), search("app"), startsWith("app"), insert("app"), delete("apple"), search("apple"), search("app")
Output: null, true, false, true, null, null, false, true
```

**Code**

Each node stores children and a word-end flag. Deletion unmarks the terminal node, then removes unused nodes backwards without recursion.

```python
class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.end = True

    def _walk(self, text):
        node = self.root
        for ch in text:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def delete(self, word: str) -> None:
        node = self.root
        path = []
        for ch in word:
            if ch not in node.children:
                return
            path.append((node, ch))
            node = node.children[ch]
        if not node.end:
            return
        node.end = False
        for parent, ch in reversed(path):
            child = parent.children[ch]
            if child.end or child.children:
                break
            del parent.children[ch]
```

**Time / Space Complexity**

Insert/search/startsWith: O(L) time. Delete: O(L) time and O(L) temporary path space. Trie storage: O(S), where S is total inserted characters. Searches use O(1) auxiliary space.

### 27. Implement Trie II (Prefix Tree)

[LeetCode 1804 Link](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)

Support insert, countWordsEqualTo, countWordsStartingWith, and erase, including duplicate words. This LeetCode problem may require Premium access. Erase removes one occurrence.

**Input/Output**

```text
Operations: insert("apple"), insert("apple"), countWordsEqualTo("apple"), countWordsStartingWith("app"), erase("apple"), countWordsEqualTo("apple")
Output: null, null, 2, 2, null, 1
```

**Code**

Store pass counts at every node and an end count at terminal nodes. Decrement the path on erase; prune nodes whose pass count reaches zero.

```python
class Node:
    def __init__(self):
        self.children = {}
        self.passed = 0
        self.ends = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        node.passed += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            node.passed += 1
        node.ends += 1

    def _walk(self, text):
        node = self.root
        for ch in text:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def countWordsEqualTo(self, word: str) -> int:
        node = self._walk(word)
        return node.ends if node else 0

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._walk(prefix)
        return node.passed if node else 0

    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word) == 0:
            return
        node = self.root
        node.passed -= 1
        path = []
        for ch in word:
            path.append((node, ch))
            node = node.children[ch]
            node.passed -= 1
        node.ends -= 1
        for parent, ch in reversed(path):
            if parent.children[ch].passed != 0:
                break
            del parent.children[ch]
```

**Time / Space Complexity**

Each operation: O(L) expected time. Storage: O(S). Erase uses O(L) temporary path space; other operations use O(1) auxiliary space.

### 28. ★ Replace Words

[LeetCode 648 Link](https://leetcode.com/problems/replace-words/)

Replace each sentence word by its shortest dictionary root, if any. Words contain lowercase English letters and are separated by single spaces.

**Input/Output**

```text
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

**Code**

Build a trie of roots. Stop at the first terminal node while reading each sentence word.

```python
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = {}
        for word in dictionary:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True

        def replace(word):
            node = root
            for i, ch in enumerate(word):
                if ch not in node:
                    return word
                node = node[ch]
                if '#' in node:
                    return word[:i + 1]
            return word
        return ' '.join(replace(word) for word in sentence.split())
```

**Time / Space Complexity**

Time: O(S + T), where S is total dictionary characters and T is sentence length. Space: O(S + T), including split words and output.

### 29. Longest Word in Dictionary

[LeetCode 720 Link](https://leetcode.com/problems/longest-word-in-dictionary/)

Return the longest word whose every nonempty prefix is also a dictionary word. Break ties lexicographically; return an empty string if none exists. This also covers the earlier notes' Longest String With All Prefixes exercise.

**Input/Output**

```text
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

**Code**

Insert all words. Check that every node on each candidate path is terminal; select by length, then alphabetical order.

```python
class Solution:
    def longestWord(self, words: list[str]) -> str:
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True
        best = ''
        for word in words:
            node = root
            valid = True
            for ch in word:
                node = node[ch]
                if '#' not in node:
                    valid = False
                    break
            if valid and (len(word) > len(best) or
                          (len(word) == len(best) and word < best)):
                best = word
        return best
```

**Time / Space Complexity**

Time: O(S), where S is total word characters, including tie comparisons. Space: O(S) for the trie.

### 30. Map Sum Pairs

[LeetCode 677 Link](https://leetcode.com/problems/map-sum-pairs/)

Implement insert(key, val) and sum(prefix). Reinserting an existing key replaces its value.

**Input/Output**

```text
Operations: insert("apple",3), sum("ap"), insert("app",2), sum("ap"), insert("apple",2), sum("ap")
Output: null, 3, null, 5, null, 4
```

**Code**

Keep previous key values. Add only the value difference to each prefix node's stored sum.

```python
class Node:
    def __init__(self):
        self.children = {}
        self.total = 0

class MapSum:
    def __init__(self):
        self.root = Node()
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.values.get(key, 0)
        self.values[key] = val
        node = self.root
        node.total += delta
        for ch in key:
            if ch not in node.children:
                node.children[ch] = Node()
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

**Time / Space Complexity**

Insert: O(L). Sum: O(P). Storage: O(S) for trie nodes and stored keys.

**Pattern: Searching and prefix aggregation**

### 31. ★ Design Add and Search Words Data Structure

[LeetCode 211 Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

Implement addWord and search. A dot in a search pattern matches exactly one lowercase English letter.

**Input/Output**

```text
Operations: addWord("bad"), addWord("dad"), addWord("mad"), search("pad"), search("bad"), search(".ad"), search("b..")
Output: null, null, null, false, true, true, true
```

**Code**

Insert normally. During search, follow one edge for a literal and branch over children for a dot. An explicit stack avoids recursion depth limits.

```python
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if '#' in node:
                    return True
            elif word[i] == '.':
                for ch, child in node.items():
                    if ch != '#':
                        stack.append((child, i + 1))
            elif word[i] in node:
                stack.append((node[word[i]], i + 1))
        return False
```

**Time / Space Complexity**

Add: O(L). Search: O(min(V, L \* 26^d)) worst-case upper bound, where V is trie nodes and d is number of dots. Search stack: O(26L) = O(L). Storage: O(S).

### 32. ★ Search Suggestions System

[LeetCode 1268 Link](https://leetcode.com/problems/search-suggestions-system/)

For every successive prefix of searchWord, return up to three lexicographically smallest matching products.

**Input/Output**

```text
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

**Code**

Insert products in sorted order. Each node stores references to its first three products. Follow the query one character at a time.

```python
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        root = {'children': {}, 'top': []}
        for word in sorted(products):
            node = root
            for ch in word:
                if ch not in node['children']:
                    node['children'][ch] = {'children': {}, 'top': []}
                node = node['children'][ch]
                if len(node['top']) < 3:
                    node['top'].append(word)
        answer = []
        node = root
        for ch in searchWord:
            node = node['children'].get(ch) if node else None
            answer.append(list(node['top']) if node else [])
        return answer
```

**Time / Space Complexity**

Time: O(N log N \* L + S + Q), including worst-case string comparisons in sorting; N products, max product length L, total product characters S, query length Q. Space: O(S + N + Q), including trie, sorting and output references.

### 33. Implement Magic Dictionary

[LeetCode 676 Link](https://leetcode.com/problems/implement-magic-dictionary/)

Build a dictionary. Search returns true only if replacing exactly one character of the query produces a dictionary word. Insertion and deletion are not allowed.

**Input/Output**

```text
Operations: buildDict(["hello","leetcode"]), search("hello"), search("hhllo"), search("hell"), search("leetcoded")
Output: null, false, true, false, false
```

**Code**

Traverse states (node, position, edits). Explore alternative letters only while no edit has been used; accept a terminal word with exactly one edit.

```python
class MagicDictionary:
    def __init__(self):
        self.root = {}

    def buildDict(self, dictionary: list[str]) -> None:
        self.root = {}
        for word in dictionary:
            node = self.root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True

    def search(self, searchWord: str) -> bool:
        stack = [(self.root, 0, 0)]
        while stack:
            node, i, edits = stack.pop()
            if i == len(searchWord):
                if edits == 1 and '#' in node:
                    return True
                continue
            if edits:
                if searchWord[i] in node:
                    stack.append((node[searchWord[i]], i + 1, 1))
            else:
                for ch, child in node.items():
                    if ch != '#':
                        stack.append((child, i + 1, int(ch != searchWord[i])))
        return False
```

**Time / Space Complexity**

Build: O(S). Search: O(min(V, 26L^2)) upper bound; V trie nodes, L query length. Search stack: O(26L) = O(L). Trie storage: O(S).

### 34. Sum of Prefix Scores of Strings

[LeetCode 2416 Link](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/)

A prefix score is the number of input words starting with that prefix. For each word, sum the scores of all its nonempty prefixes.

**Input/Output**

```text
Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
```

**Code**

Increment a pass count at every visited node during insertion. Sum those counts on a second traversal of each word.

```python
class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        root = Node()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
                node.count += 1
        answer = []
        for word in words:
            node = root
            score = 0
            for ch in word:
                node = node.children[ch]
                score += node.count
            answer.append(score)
        return answer
```

**Time / Space Complexity**

Time: O(S). Auxiliary space: O(S), excluding O(N) output.

**Pattern: Trie + DFS / backtracking**

### 35. ★ Word Search II

[LeetCode 212 Link](https://leetcode.com/problems/word-search-ii/)

Find dictionary words on a lowercase-letter board using horizontal or vertical neighbors. A cell may be used only once within one word. Return each found word once, in any order.

**Input/Output**

```text
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["oath","eat"] (order may vary)
```

**Code**

Build a word trie; start DFS from each board cell. Stop immediately if the path is not a trie prefix. Mark visited cells temporarily, restore them on return, and clear a found terminal to avoid duplicates.

```python
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word
        if not board or not board[0]:
            return []
        rows, cols = len(board), len(board[0])
        answer = []

        def dfs(r, c, parent):
            ch = board[r][c]
            if ch not in parent:
                return
            node = parent[ch]
            word = node.pop('#', None)
            if word is not None:
                answer.append(word)
            board[r][c] = '!'
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '!':
                    dfs(nr, nc, node)
            board[r][c] = ch
            if not node:
                del parent[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return answer
```

**Time / Space Complexity**

Time: O(S + R*C*4*3^(D-1)) worst-case upper bound, D = min(max word length, R*C). Auxiliary space: O(S + D), excluding output. S is total dictionary characters.

### 36. Concatenated Words

[LeetCode 472 Link](https://leetcode.com/problems/concatenated-words/)

Return dictionary words that can be formed by concatenating at least two shorter dictionary words. Components may be reused; output order is unrestricted.

**Input/Output**

```text
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
```

**Code**

Build one trie. For each word, DP tracks the maximum number of pieces reaching each position. Trie walks enumerate dictionary words beginning at reachable positions; require at least two pieces to exclude the word itself.

```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        root = {}
        for word in words:
            if not word:
                continue
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True
        answer = []
        for word in words:
            pieces = [-1] * (len(word) + 1)
            pieces[0] = 0
            for start in range(len(word)):
                if pieces[start] < 0:
                    continue
                node = root
                for end in range(start, len(word)):
                    node = node.get(word[end])
                    if node is None:
                        break
                    if '#' in node:
                        pieces[end + 1] = max(pieces[end + 1], pieces[start] + 1)
            if pieces[-1] >= 2:
                answer.append(word)
        return answer
```

**Time / Space Complexity**

Time: O(S + sum(L_i^2)). Auxiliary space: O(S + Lmax), excluding output.

**Pattern: Binary trie / XOR**

### 37. ★ Maximum XOR of Two Numbers in an Array

[LeetCode 421 Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

Return the largest XOR of any two array values. Values are nonnegative signed 32-bit integers.

**Input/Output**

```text
Input: nums = [3,10,5,25,2,8]
Output: 28
```

**Code**

Store bits 30 down to 0 in a binary trie. For each query bit, prefer the opposite bit to maximize the most significant remaining XOR bit.

```python
class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        root = {}
        for value in nums:
            node = root
            for bit in range(30, -1, -1):
                node = node.setdefault((value >> bit) & 1, {})
        best = 0
        for value in nums:
            node = root
            score = 0
            for bit in range(30, -1, -1):
                digit = (value >> bit) & 1
                if 1 - digit in node:
                    score |= 1 << bit
                    node = node[1 - digit]
                else:
                    node = node[digit]
            best = max(best, score)
        return best
```

**Time / Space Complexity**

Time: O(nB). Space: O(nB), with B = 31, hence linear for fixed-width integers.

### 38. Maximum XOR With an Element From Array

[LeetCode 1707 Link](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

Each query [x, m] asks for the maximum x XOR value using an array value <= m. Return -1 when no value qualifies, preserving original query order. Values are nonnegative signed 32-bit integers.

**Input/Output**

```text
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
```

**Code**

Sort values and queries by their limit m. Insert newly eligible values before answering each query with a greedy binary-trie walk.

```python
class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        values = sorted(nums)
        ordered = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        root = {}
        answer = [-1] * len(queries)
        inserted = 0
        for limit, x, index in ordered:
            while inserted < len(values) and values[inserted] <= limit:
                node = root
                for bit in range(30, -1, -1):
                    node = node.setdefault((values[inserted] >> bit) & 1, {})
                inserted += 1
            if inserted == 0:
                continue
            node = root
            score = 0
            for bit in range(30, -1, -1):
                digit = (x >> bit) & 1
                if 1 - digit in node:
                    score |= 1 << bit
                    node = node[1 - digit]
                else:
                    node = node[digit]
            answer[index] = score
        return answer
```

**Time / Space Complexity**

Time: O(n log n + q log q + (n + q)B). Auxiliary space: O(nB + n + q); B = 31. Inputs are copied before sorting.

### 39. Count Pairs With XOR in a Range

[LeetCode 1803 Link](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/)

Count index pairs i < j such that low <= (nums[i] XOR nums[j]) <= high. Values and bounds are nonnegative signed 32-bit integers.

**Input/Output**

```text
Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6
```

**Code**

Query earlier values before inserting the current one. Count XOR < high + 1 minus XOR < low. Store subtree counts; include bit 31 so high + 1 is representable even at the signed-int boundary.

```python
class Node:
    def __init__(self):
        self.child = [None, None]
        self.count = 0

class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        root = Node()

        def less(value, limit):
            if limit <= 0:
                return 0
            node = root
            total = 0
            for bit in range(31, -1, -1):
                if node is None:
                    break
                digit = (value >> bit) & 1
                if (limit >> bit) & 1:
                    same = node.child[digit]
                    if same is not None:
                        total += same.count
                    node = node.child[1 - digit]
                else:
                    node = node.child[digit]
            return total

        answer = 0
        for value in nums:
            answer += less(value, high + 1) - less(value, low)
            node = root
            for bit in range(31, -1, -1):
                digit = (value >> bit) & 1
                if node.child[digit] is None:
                    node.child[digit] = Node()
                node = node.child[digit]
                node.count += 1
        return answer
```

**Time / Space Complexity**

Time: O(nB). Auxiliary space: O(nB), B = 32. The LeetCode answer fits int; Java uses long internally for bounds and counts.

**Pattern: Advanced design**

### 40. Stream of Characters

[LeetCode 1032 Link](https://leetcode.com/problems/stream-of-characters/)

Construct with a word list. Each query adds one lowercase letter to a stream; return whether any nonempty stream suffix is a dictionary word.

**Input/Output**

```text
Input: words = ["cd","f","kl"], queries = ["a","b","c","d","e","f","g","h","i","j","k","l"]
Output: [false,false,false,true,false,true,false,false,false,false,false,true]
```

**Code**

Insert words backwards. Retain only the last Lmax stream characters and walk them from newest to oldest through the reversed trie.

```python
from collections import deque

class StreamChecker:
    def __init__(self, words: list[str]):
        self.root = {}
        maximum = max((len(word) for word in words), default=0)
        self.stream = deque(maxlen=maximum)
        for word in words:
            node = self.root
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node['#'] = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.root
        for ch in reversed(self.stream):
            node = node.get(ch)
            if node is None:
                return False
            if '#' in node:
                return True
        return False
```

**Time / Space Complexity**

Build: O(S). Each query: O(Lmax) worst case. Storage: O(S + Lmax).

## Additional practice retained

**Pattern: Distinct-character windows**

### 41. Longest Substring with At Most Two Distinct Characters

[LeetCode 159 Link](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

Return the longest substring containing at most two distinct characters. This LeetCode problem may require Premium access.

**Input/Output**

```text
Input: s = "eceba"
Output: 3
```

**Code**

Count characters in the window. Shrink until the number of nonzero frequency entries is within the allowed limit.

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        freq = {}
        left = best = 0
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            while len(freq) > k:
                old = s[left]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(1), at most three map entries.

### 42. Longest Substring with At Most K Distinct Characters

[LeetCode 340 Link](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

Return the longest substring containing at most k distinct characters. This LeetCode problem may require Premium access.

**Input/Output**

```text
Input: s = "eceba", k = 2
Output: 3
```

**Code**

Count characters in the window. Shrink until the number of nonzero frequency entries is within the allowed limit.

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k <= 0:
            return 0
        freq = {}
        left = best = 0
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            while len(freq) > k:
                old = s[left]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
                left += 1
            best = max(best, r - left + 1)
        return best
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(min(n, k + 1)) for nonnegative k.

**Pattern: Fixed-size unique window**

### 43. Find K-Length Substrings With No Repeated Characters

[LeetCode 1100 Link](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/)

Count length-k substrings whose characters are all distinct. This LeetCode problem may require Premium access.

**Input/Output**

```text
Input: s = "havefunonleetcode", k = 5
Output: 6
```

**Code**

Maintain a length-k frequency window and count it when the number of distinct characters equals k.

```python
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k <= 0 or k > len(s):
            return 0
        freq = {}
        answer = 0
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            if r >= k:
                old = s[r - k]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
            if r >= k - 1 and len(freq) == k:
                answer += 1
        return answer
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(min(n, k + 1)).
