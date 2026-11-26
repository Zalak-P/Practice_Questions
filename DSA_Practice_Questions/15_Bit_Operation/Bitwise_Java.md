# Bitwise Problems — Java

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

```java
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= n - 1;
            count++;
        }
        return count;
    }
}
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

```java
class Solution {
    public int[] countBits(int n) {
        int[] answer = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            answer[i] = answer[i >>> 1] + (i & 1);
        }
        return answer;
    }
}
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

```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
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

```java
class Solution {
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>>= 1;
        }
        return result;
    }
}
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

```java
class Solution {
    public int findComplement(int num) {
        int mask = 0;
        int value = num;
        while (value != 0) {
            mask = (mask << 1) | 1;
            value >>>= 1;
        }
        return num ^ mask;
    }
}
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

```java
class Solution {
    public int minBitFlips(int start, int goal) {
        int difference = start ^ goal;
        int count = 0;
        while (difference != 0) {
            difference &= difference - 1;
            count++;
        }
        return count;
    }
}
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

```java
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int value : nums) result ^= value;
        return result;
    }
}
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

```java
class Solution {
    public int missingNumber(int[] nums) {
        int result = nums.length;
        for (int i = 0; i < nums.length; i++) result ^= i ^ nums[i];
        return result;
    }
}
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

```java
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int bit = 0; bit < 32; bit++) {
            int count = 0;
            for (int value : nums) count += (value >>> bit) & 1;
            if (count % 3 != 0) result |= 1 << bit;
        }
        return result;
    }
}
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

```java
class Solution {
    public int[] singleNumber(int[] nums) {
        int combined = 0;
        for (int value : nums) combined ^= value;
        int distinguishingBit = Integer.lowestOneBit(combined);
        int first = 0, second = 0;
        for (int value : nums) {
            if ((value & distinguishingBit) != 0) first ^= value;
            else second ^= value;
        }
        return new int[]{first, second};
    }
}
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

```java
class Solution {
    public int[] findArray(int[] pref) {
        int[] result = new int[pref.length];
        result[0] = pref[0];
        for (int i = 1; i < pref.length; i++) result[i] = pref[i - 1] ^ pref[i];
        return result;
    }
}
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

```java
class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int shifts = 0;
        while (left != right) {
            left >>>= 1;
            right >>>= 1;
            shifts++;
        }
        return left << shifts;
    }
}
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

```java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
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

```java
class Solution {
    public int minFlips(int a, int b, int c) {
        int flips = 0;
        for (int bit = 0; bit < 32; bit++) {
            int x = (a >>> bit) & 1, y = (b >>> bit) & 1, z = (c >>> bit) & 1;
            if (z == 0) flips += x + y;
            else if (x == 0 && y == 0) flips++;
        }
        return flips;
    }
}
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

```java
import java.util.*;
class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        Set<Integer> current = new HashSet<>(), seen = new HashSet<>();
        for (int value : arr) {
            Set<Integer> next = new HashSet<>();
            next.add(value);
            for (int previous : current) next.add(previous | value);
            seen.addAll(next);
            current = next;
        }
        return seen.size();
    }
}
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

```java
import java.util.*;
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        for (int mask = 0; mask < (1 << nums.length); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                if ((mask & (1 << i)) != 0) subset.add(nums[i]);
            }
            result.add(subset);
        }
        return result;
    }
}
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

```java
class Solution {
    public int maxProduct(String[] words) {
        int[] masks = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            for (char c : words[i].toCharArray()) masks[i] |= 1 << (c - 'a');
        }
        int best = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < i; j++) {
                if ((masks[i] & masks[j]) == 0)
                    best = Math.max(best, words[i].length() * words[j].length());
            }
        }
        return best;
    }
}
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

```java
import java.util.*;
class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < (1 << n); i++) result.add(i ^ (i >>> 1));
        return result;
    }
}
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

```java
import java.util.*;
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int value : nums) total += value;
        if (k > nums.length || total % k != 0) return false;
        int target = total / k;
        for (int value : nums) if (value > target) return false;
        int[] dp = new int[1 << nums.length];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int mask = 0; mask < dp.length; mask++) {
            if (dp[mask] == -1) continue;
            for (int i = 0; i < nums.length; i++) {
                if ((mask & (1 << i)) == 0 && dp[mask] + nums[i] <= target)
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target;
            }
        }
        return dp[dp.length - 1] == 0;
    }
}
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

```java
import java.util.*;
class Solution {
    public long subarrayXor(int[] arr, int k) {
        Map<Integer, Long> frequencies = new HashMap<>();
        frequencies.put(0, 1L);
        int prefix = 0;
        long answer = 0;
        for (int value : arr) {
            prefix ^= value;
            answer += frequencies.getOrDefault(prefix ^ k, 0L);
            frequencies.put(prefix, frequencies.getOrDefault(prefix, 0L) + 1);
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Solution {
    public int countTriplets(int[] arr) {
        Map<Integer, Integer> counts = new HashMap<>(), positions = new HashMap<>();
        counts.put(0, 1);
        positions.put(0, 0);
        int prefix = 0, answer = 0;
        for (int q = 1; q <= arr.length; q++) {
            prefix ^= arr[q - 1];
            answer += counts.getOrDefault(prefix, 0) * (q - 1)
                    - positions.getOrDefault(prefix, 0);
            counts.put(prefix, counts.getOrDefault(prefix, 0) + 1);
            positions.put(prefix, positions.getOrDefault(prefix, 0) + q);
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Solution {
    public int findTheLongestSubstring(String s) {
        int[] first = new int[32];
        Arrays.fill(first, -2);
        first[0] = -1;
        int mask = 0, best = 0;
        for (int i = 0; i < s.length(); i++) {
            int bit = "aeiou".indexOf(s.charAt(i));
            if (bit >= 0) mask ^= 1 << bit;
            if (first[mask] == -2) first[mask] = i;
            else best = Math.max(best, i - first[mask]);
        }
        return best;
    }
}
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

```java
class Solution {

    private static class Node {
        Node[] child = new Node[2];
    }
    private void insert(Node root, int value) {
        Node node = root;
        for (int bit = 30; bit >= 0; bit--) {
            int digit = (value >>> bit) & 1;
            if (node.child[digit] == null) node.child[digit] = new Node();
            node = node.child[digit];
        }
    }
    private int maximumXor(Node root, int value) {
        Node node = root;
        int answer = 0;
        for (int bit = 30; bit >= 0; bit--) {
            int digit = (value >>> bit) & 1;
            if (node.child[digit ^ 1] != null) {
                answer |= 1 << bit;
                node = node.child[digit ^ 1];
            } else node = node.child[digit];
        }
        return answer;
    }

    public int findMaximumXOR(int[] nums) {
        Node root = new Node();
        for (int value : nums) insert(root, value);
        int best = 0;
        for (int value : nums) best = Math.max(best, maximumXor(root, value));
        return best;
    }
}
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

```java
import java.util.*;
class Solution {

    private static class Node {
        Node[] child = new Node[2];
    }
    private void insert(Node root, int value) {
        Node node = root;
        for (int bit = 30; bit >= 0; bit--) {
            int digit = (value >>> bit) & 1;
            if (node.child[digit] == null) node.child[digit] = new Node();
            node = node.child[digit];
        }
    }
    private int maximumXor(Node root, int value) {
        Node node = root;
        int answer = 0;
        for (int bit = 30; bit >= 0; bit--) {
            int digit = (value >>> bit) & 1;
            if (node.child[digit ^ 1] != null) {
                answer |= 1 << bit;
                node = node.child[digit ^ 1];
            } else node = node.child[digit];
        }
        return answer;
    }

    public int[] maximizeXor(int[] nums, int[][] queries) {
        int[] values = nums.clone();
        Arrays.sort(values);
        Integer[] order = new Integer[queries.length];
        for (int i = 0; i < order.length; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> queries[i][1]));
        int[] answer = new int[queries.length];
        Arrays.fill(answer, -1);
        Node root = new Node();
        int inserted = 0;
        for (int index : order) {
            while (inserted < values.length && values[inserted] <= queries[index][1])
                insert(root, values[inserted++]);
            if (inserted > 0) answer[index] = maximumXor(root, queries[index][0]);
        }
        return answer;
    }
}
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

```java
class Solution {
    private static class Node {
        Node[] child = new Node[2];
        int count;
    }
    private void insert(Node root, int value) {
        Node node = root;
        for (int bit = 30; bit >= 0; bit--) {
            int digit = (value >>> bit) & 1;
            if (node.child[digit] == null) node.child[digit] = new Node();
            node = node.child[digit];
            node.count++;
        }
    }
    private int countLess(Node root, int value, int limit) {
        Node node = root;
        int answer = 0;
        for (int bit = 30; bit >= 0 && node != null; bit--) {
            int digit = (value >>> bit) & 1;
            if (((limit >>> bit) & 1) != 0) {
                if (node.child[digit] != null) answer += node.child[digit].count;
                node = node.child[digit ^ 1];
            } else node = node.child[digit];
        }
        return answer;
    }
    public int countPairs(int[] nums, int low, int high) {
        Node root = new Node();
        int answer = 0;
        for (int value : nums) {
            answer += countLess(root, value, high + 1) - countLess(root, value, low);
            insert(root, value);
        }
        return answer;
    }
}
```

**Time Space Complexity**

Time: O(nb). Space: O(nb), where b = 31. The linked constraints keep high + 1 within these bits.
