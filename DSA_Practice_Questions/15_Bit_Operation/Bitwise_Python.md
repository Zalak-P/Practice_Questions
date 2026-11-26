# Bitwise Problems — Python

## Bit manipulation fundamentals

### 1. ★ Number of 1 Bits

[LeetCode Link](https://leetcode.com/problems/number-of-1-bits/)

Return the number of set bits in a nonnegative integer. Clear the lowest set bit on each iteration.

**Input/Output**

```text
Input: n = 11
Output: 3
```

**Code**

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
```

**Time Space Complexity**

Time: O(s), where s is the number of set bits. Space: O(1) for a fixed-width integer.

### 2. ★ Counting Bits

[LeetCode Link](https://leetcode.com/problems/counting-bits/)

Return the set-bit count for every integer from 0 through n. Reuse the answer for n shifted right by one bit.

**Input/Output**

```text
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
```

**Code**

```python
class Solution:
    def countBits(self, n: int) -> list[int]:
        answer = [0] * (n + 1)
        for i in range(1, n + 1):
            answer[i] = answer[i >> 1] + (i & 1)
        return answer
```

**Time Space Complexity**

Time: O(n). Auxiliary space: O(1), excluding the O(n) output.

### 3. ★ Power of Two

[LeetCode Link](https://leetcode.com/problems/power-of-two/)

Return whether n is a positive power of two. Such a number has exactly one set bit.

**Input/Output**

```text
Input: n = 16
Output: true
```

**Code**

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
```

**Time Space Complexity**

Time: O(1). Space: O(1), under fixed-width input constraints.

### 4. Reverse Bits

[LeetCode Link](https://leetcode.com/problems/reverse-bits/)

Reverse all 32 bits of an unsigned 32-bit integer. In Java, int stores the same bit pattern as a signed value; use an unsigned right shift.

**Input/Output**

```text
Input: n = 43261596
Output: 964176192
```

**Code**

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
```

**Time Space Complexity**

Time: O(32) = O(1). Space: O(1).

### 5. Number Complement

[LeetCode Link](https://leetcode.com/problems/number-complement/)

Flip the bits of a positive integer only through its most significant set bit. Build an all-ones mask of the same width.

**Input/Output**

```text
Input: num = 5
Output: 2
```

**Code**

```python
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        value = num
        while value:
            mask = (mask << 1) | 1
            value >>= 1
        return num ^ mask
```

**Time Space Complexity**

Time: O(b), where b is the significant bit width. Space: O(1) under 32-bit constraints.

### 6. ★ Minimum Bit Flips to Convert Number

[LeetCode Link](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)

Count the differing bits between start and goal by counting set bits in their XOR.

**Input/Output**

```text
Input: start = 10, goal = 7
Output: 3
```

**Code**

```python
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        difference = start ^ goal
        count = 0
        while difference:
            difference &= difference - 1
            count += 1
        return count
```

**Time Space Complexity**

Time: O(s), where s is the number of differing bits. Space: O(1).

## XOR patterns

### 7. ★ Single Number

[LeetCode Link](https://leetcode.com/problems/single-number/)

Every value appears twice except one. XOR all values to cancel the pairs.

**Input/Output**

```text
Input: nums = [4, 1, 2, 1, 2]
Output: 4
```

**Code**

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for value in nums:
            result ^= value
        return result
```

**Time Space Complexity**

Time: O(n). Space: O(1).

### 8. ★ Missing Number

[LeetCode Link](https://leetcode.com/problems/missing-number/)

Find the missing number from the range 0 through n. XOR all indices and values with n.

**Input/Output**

```text
Input: nums = [3, 0, 1]
Output: 2
```

**Code**

```python
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)
        for i, value in enumerate(nums):
            result ^= i ^ value
        return result
```

**Time Space Complexity**

Time: O(n). Space: O(1).

### 9. ★ Single Number II

[LeetCode Link](https://leetcode.com/problems/single-number-ii/)

Every value appears three times except one. Count each of the 32 bit positions modulo three and reconstruct the signed result.

**Input/Output**

```text
Input: nums = [2, 2, 3, 2]
Output: 3
```

**Code**

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for bit in range(32):
            count = sum((value >> bit) & 1 for value in nums)
            if count % 3:
                result |= 1 << bit
        return result if result < (1 << 31) else result - (1 << 32)
```

**Time Space Complexity**

Time: O(32n) = O(n). Space: O(1).

### 10. ★ Single Number III

[LeetCode Link](https://leetcode.com/problems/single-number-iii/)

Exactly two values appear once; all others appear twice. Isolate a set bit in the combined XOR to divide the two unique values into different groups. Either output order is valid.

**Input/Output**

```text
Input: nums = [1, 2, 1, 3, 2, 5]
Output: [3, 5]
```

**Code**

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        combined = 0
        for value in nums:
            combined ^= value
        distinguishing_bit = combined & -combined
        first = second = 0
        for value in nums:
            if value & distinguishing_bit:
                first ^= value
            else:
                second ^= value
        return [first, second]
```

**Time Space Complexity**

Time: O(n). Space: O(1), excluding output.

### 11. Find the Original Array of Prefix XOR

[LeetCode Link](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/)

Recover the original array. Its first value equals pref[0]; each subsequent value is the XOR of adjacent prefix values.

**Input/Output**

```text
Input: pref = [5, 2, 0, 3, 1]
Output: [5, 7, 2, 3, 2]
```

**Code**

```python
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        result = [pref[0]]
        for i in range(1, len(pref)):
            result.append(pref[i - 1] ^ pref[i])
        return result
```

**Time Space Complexity**

Time: O(n). Auxiliary space: O(1), excluding the O(n) output.

## Bitwise AND, OR, and arithmetic

### 12. ★ Bitwise AND of Numbers Range

[LeetCode Link](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

Return the AND of every integer in the inclusive range [left, right]. Keep only the common binary prefix.

**Input/Output**

```text
Input: left = 5, right = 7
Output: 4
```

**Code**

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left != right:
            left >>= 1
            right >>= 1
            shifts += 1
        return left << shifts
```

**Time Space Complexity**

Time: O(b), where b is the input bit width. Space: O(1).

### 13. ★ Sum of Two Integers

[LeetCode Link](https://leetcode.com/problems/sum-of-two-integers/)

Add two signed integers without + or -. XOR computes the sum without carry; shifted AND computes the carry. Python requires a 32-bit mask and signed conversion.

**Input/Output**

```text
Input: a = -2, b = 3
Output: 1
```

**Code**

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
```

**Time Space Complexity**

Time: O(b), with b = 32. Space: O(1).

### 14. Minimum Flips to Make a OR b Equal to c

[LeetCode Link](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

For each bit, if c is zero, clear every set bit in a and b. If c is one and both input bits are zero, set one bit.

**Input/Output**

```text
Input: a = 2, b = 6, c = 5
Output: 3
```

**Code**

```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for bit in range(32):
            x, y, z = (a >> bit) & 1, (b >> bit) & 1, (c >> bit) & 1
            if z == 0:
                flips += x + y
            elif x == 0 and y == 0:
                flips += 1
        return flips
```

**Time Space Complexity**

Time: O(32) = O(1). Space: O(1).

### 15. Bitwise ORs of Subarrays

[LeetCode Link](https://leetcode.com/problems/bitwise-ors-of-subarrays/)

Count distinct OR results across all nonempty contiguous subarrays. Maintain the distinct OR values of subarrays ending at the current index.

**Input/Output**

```text
Input: arr = [1, 2, 4]
Output: 6
```

**Code**

```python
class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        current = set()
        seen = set()
        for value in arr:
            current = {value} | {previous | value for previous in current}
            seen.update(current)
        return len(seen)
```

**Time Space Complexity**

Expected time: O(nb). Space: O(nb) including all distinct results; the current set uses O(b). Here b is the nonnegative input bit width, at most 30.

## Bitmasking and subsets

### 16. ★ Subsets

[LeetCode Link](https://leetcode.com/problems/subsets/)

Generate every subset of an array of distinct integers. Each bit in a mask decides whether to include one element. Output order may vary.

**Input/Output**

```text
Input: nums = [1, 2]
Output: [[], [1], [2], [1, 2]]
```

**Code**

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        for mask in range(1 << len(nums)):
            subset = []
            for i, value in enumerate(nums):
                if mask & (1 << i):
                    subset.append(value)
            result.append(subset)
        return result
```

**Time Space Complexity**

Time: O(n × 2^n). Auxiliary space: O(n) for a current subset; output space: O(n × 2^n).

### 17. ★ Maximum Product of Word Lengths

[LeetCode Link](https://leetcode.com/problems/maximum-product-of-word-lengths/)

Find the largest product of lengths of two lowercase English words with no shared letter. Encode each word as a 26-bit character mask.

**Input/Output**

```text
Input: words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Output: 16
```

**Code**

```python
class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for character in word:
                mask |= 1 << (ord(character) - ord('a'))
            masks.append(mask)
        best = 0
        for i in range(len(words)):
            for j in range(i):
                if masks[i] & masks[j] == 0:
                    best = max(best, len(words[i]) * len(words[j]))
        return best
```

**Time Space Complexity**

Time: O(L + n²), where L is the total character count and n is the word count. Space: O(n).

### 18. Gray Code

[LeetCode Link](https://leetcode.com/problems/gray-code/)

Generate an n-bit Gray code sequence starting at zero. Adjacent values, including the last and first, differ in exactly one bit.

**Input/Output**

```text
Input: n = 2
Output: [0, 1, 3, 2]
```

**Code**

```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
```

**Time Space Complexity**

Time: O(2^n). Auxiliary space: O(1), excluding the O(2^n) output.

### 19. Partition to K Equal Sum Subsets

[LeetCode Link](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

Partition positive integers into k nonempty groups of equal sum. A reachable mask stores the sum in the current unfinished group; reaching the target starts a new group.

**Input/Output**

```text
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: true
```

**Code**

```python
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if k > len(nums) or total % k:
            return False
        target = total // k
        if max(nums) > target:
            return False
        dp = [-1] * (1 << len(nums))
        dp[0] = 0
        for mask in range(len(dp)):
            if dp[mask] == -1:
                continue
            for i, value in enumerate(nums):
                if not (mask & (1 << i)) and dp[mask] + value <= target:
                    dp[mask | (1 << i)] = (dp[mask] + value) % target
        return dp[-1] == 0
```

**Time Space Complexity**

Time: O(n × 2^n). Space: O(2^n).

## Prefix XOR and counting

### 20. ★ Count Subarrays with Given XOR

[GFG Link](https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1)

Count contiguous subarrays whose XOR equals k. If the current prefix is p, count earlier prefixes equal to p XOR k. The method returns the count; adapt its name to the judge template if necessary.

**Input/Output**

```text
Input: arr = [4, 2, 2, 6, 4], k = 6
Output: 4
```

**Code**

```python
class Solution:
    def subarrayXor(self, arr: list[int], k: int) -> int:
        frequencies = {0: 1}
        prefix = answer = 0
        for value in arr:
            prefix ^= value
            answer += frequencies.get(prefix ^ k, 0)
            frequencies[prefix] = frequencies.get(prefix, 0) + 1
        return answer
```

**Time Space Complexity**

Expected time: O(n). Space: O(n). Java uses long for the count to avoid overflow.

### 21. Count Triplets That Can Form Two Arrays of Equal XOR

[LeetCode Link](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

Count triplets i < j <= k where XOR(arr[i..j-1]) equals XOR(arr[j..k]). Equal prefix XOR values at positions p and q contribute q - p - 1 choices of the split. Track prefix counts and position sums.

**Input/Output**

```text
Input: arr = [2, 3, 1, 6, 7]
Output: 4
```

**Code**

```python
class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        counts = {0: 1}
        positions = {0: 0}
        prefix = answer = 0
        for q, value in enumerate(arr, 1):
            prefix ^= value
            answer += counts.get(prefix, 0) * (q - 1) - positions.get(prefix, 0)
            counts[prefix] = counts.get(prefix, 0) + 1
            positions[prefix] = positions.get(prefix, 0) + q
        return answer
```

**Time Space Complexity**

Expected time: O(n). Space: O(n).

### 22. Find the Longest Substring Containing Vowels in Even Counts

[LeetCode Link](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)

Track odd/even counts of the five vowels with a 5-bit mask. Repeated masks identify a substring in which all vowel counts are even. Keep the earliest position of every mask.

**Input/Output**

```text
Input: s = "eleetminicoworoep"
Output: 13
```

**Code**

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = [-2] * 32
        first[0] = -1
        vowel_bits = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mask = best = 0
        for i, character in enumerate(s):
            if character in vowel_bits:
                mask ^= 1 << vowel_bits[character]
            if first[mask] == -2:
                first[mask] = i
            else:
                best = max(best, i - first[mask])
        return best
```

**Time Space Complexity**

Time: O(n). Space: O(32) = O(1).

## XOR with a binary trie

### 23. ★ Maximum XOR of Two Numbers in an Array

[LeetCode Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

Find the maximum XOR of any two array values. Insert all numbers into a binary trie, then greedily choose the opposite bit during each query. Values are nonnegative 31-bit integers.

**Input/Output**

```text
Input: nums = [3, 10, 5, 25, 2, 8]
Output: 28
```

**Code**

```python
class BinaryTrie:
    def __init__(self):
        self.children = [[-1, -1]]

    def insert(self, value: int) -> None:
        node = 0
        for bit in range(30, -1, -1):
            digit = (value >> bit) & 1
            if self.children[node][digit] == -1:
                self.children[node][digit] = len(self.children)
                self.children.append([-1, -1])
            node = self.children[node][digit]

    def maximum_xor(self, value: int) -> int:
        node = answer = 0
        for bit in range(30, -1, -1):
            digit = (value >> bit) & 1
            opposite = digit ^ 1
            if self.children[node][opposite] != -1:
                answer |= 1 << bit
                node = self.children[node][opposite]
            else:
                node = self.children[node][digit]
        return answer

class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        trie = BinaryTrie()
        for value in nums:
            trie.insert(value)
        return max(trie.maximum_xor(value) for value in nums)
```

**Time Space Complexity**

Time: O(nb). Space: O(nb), where b = 31.

### 24. Maximum XOR With an Element From Array

[LeetCode Link](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

For every query [x, m], maximize x XOR value over array values at most m; return -1 if none qualifies. Sort the queries by m and incrementally insert eligible numbers. Restore original query order.

**Input/Output**

```text
Input: nums = [0, 1, 2, 3, 4], queries = [[3, 1], [1, 3], [5, 6]]
Output: [3, 3, 7]
```

**Code**

```python
class BinaryTrie:
    def __init__(self):
        self.children = [[-1, -1]]

    def insert(self, value: int) -> None:
        node = 0
        for bit in range(30, -1, -1):
            digit = (value >> bit) & 1
            if self.children[node][digit] == -1:
                self.children[node][digit] = len(self.children)
                self.children.append([-1, -1])
            node = self.children[node][digit]

    def maximum_xor(self, value: int) -> int:
        node = answer = 0
        for bit in range(30, -1, -1):
            digit = (value >> bit) & 1
            opposite = digit ^ 1
            if self.children[node][opposite] != -1:
                answer |= 1 << bit
                node = self.children[node][opposite]
            else:
                node = self.children[node][digit]
        return answer

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        values = sorted(nums)
        ordered = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        trie = BinaryTrie()
        answer = [-1] * len(queries)
        inserted = 0
        for limit, value, index in ordered:
            while inserted < len(values) and values[inserted] <= limit:
                trie.insert(values[inserted])
                inserted += 1
            if inserted:
                answer[index] = trie.maximum_xor(value)
        return answer
```

**Time Space Complexity**

Time: O(n log n + q log q + (n + q)b). Space: O(nb + n + q), including sorting copies, query order, and output; b = 31.

### 25. Count Pairs With XOR in a Range

[LeetCode Link](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/)

Count pairs i < j whose XOR is in [low, high]. Before inserting each value, query the trie for counts with XOR below high + 1 and below low, then subtract. Counts stored at trie nodes allow whole branches to be added at once.

**Input/Output**

```text
Input: nums = [1, 4, 2, 7], low = 2, high = 6
Output: 6
```

**Code**

```python
class CountingTrie:
    def __init__(self):
        self.children = [[-1, -1]]
        self.counts = [0]

    def insert(self, value: int) -> None:
        node = 0
        for bit in range(30, -1, -1):
            digit = (value >> bit) & 1
            if self.children[node][digit] == -1:
                self.children[node][digit] = len(self.children)
                self.children.append([-1, -1])
                self.counts.append(0)
            node = self.children[node][digit]
            self.counts[node] += 1

    def count_less(self, value: int, limit: int) -> int:
        node = answer = 0
        for bit in range(30, -1, -1):
            if node == -1:
                break
            digit = (value >> bit) & 1
            if (limit >> bit) & 1:
                same = self.children[node][digit]
                if same != -1:
                    answer += self.counts[same]
                node = self.children[node][digit ^ 1]
            else:
                node = self.children[node][digit]
        return answer

class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        trie = CountingTrie()
        answer = 0
        for value in nums:
            answer += trie.count_less(value, high + 1) - trie.count_less(value, low)
            trie.insert(value)
        return answer
```

**Time Space Complexity**

Time: O(nb). Space: O(nb), where b = 31. The linked constraints keep high + 1 within these bits.
