# Sliding Window and Trie — Java

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

```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        long sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        long best = sum;
        for (int r = k; r < nums.length; r++) {
            sum += nums[r] - nums[r - k];
            best = Math.max(best, sum);
        }
        return (double) best / k;
    }
}
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

```java
class Solution {
    public int maxVowels(String s, int k) {
        int count = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            if (isVowel(s.charAt(r))) count++;
            if (r >= k && isVowel(s.charAt(r - k))) count--;
            if (r >= k - 1) best = Math.max(best, count);
        }
        return best;
    }
    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) >= 0;
    }
}
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

```java
import java.util.Arrays;
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] need = new int[26], window = new int[26];
        for (int i = 0; i < s1.length(); i++) need[s1.charAt(i) - 'a']++;
        for (int r = 0; r < s2.length(); r++) {
            window[s2.charAt(r) - 'a']++;
            if (r >= s1.length()) window[s2.charAt(r - s1.length()) - 'a']--;
            if (r >= s1.length() - 1 && Arrays.equals(need, window)) return true;
        }
        return false;
    }
}
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

```java
import java.util.*;
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] need = new int[26], window = new int[26];
        for (int i = 0; i < p.length(); i++) need[p.charAt(i) - 'a']++;
        List<Integer> answer = new ArrayList<>();
        for (int r = 0; r < s.length(); r++) {
            window[s.charAt(r) - 'a']++;
            if (r >= p.length()) window[s.charAt(r - p.length()) - 'a']--;
            if (r >= p.length() - 1 && Arrays.equals(need, window))
                answer.add(r - p.length() + 1);
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        long sum = 0, best = 0;
        for (int r = 0; r < nums.length; r++) {
            int x = nums[r];
            sum += x;
            freq.put(x, freq.getOrDefault(x, 0) + 1);
            if (r >= k) {
                int old = nums[r - k];
                sum -= old;
                freq.put(old, freq.get(old) - 1);
                if (freq.get(old) == 0) freq.remove(old);
            }
            if (r >= k - 1 && freq.size() == k) best = Math.max(best, sum);
        }
        return best;
    }
}
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

```java
import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> last = new HashMap<>();
        int left = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            left = Math.max(left, last.getOrDefault(c, -1) + 1);
            last.put(c, r);
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, best = 0;
        for (int r = 0; r < nums.length; r++) {
            if (nums[r] == 0) zeros++;
            while (zeros > k) if (nums[left++] == 0) zeros--;
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
import java.util.*;
class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> freq = new HashMap<>();
        int left = 0, best = 0;
        for (int r = 0; r < fruits.length; r++) {
            int x = fruits[r];
            freq.put(x, freq.getOrDefault(x, 0) + 1);
            while (freq.size() > 2) {
                int old = fruits[left++];
                freq.put(old, freq.get(old) - 1);
                if (freq.get(old) == 0) freq.remove(old);
            }
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int left = 0, maxFreq = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            maxFreq = Math.max(maxFreq, ++freq[s.charAt(r) - 'A']);
            while (r - left + 1 - maxFreq > k) freq[s.charAt(left++) - 'A']--;
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0, zeros = 0, best = 0;
        for (int r = 0; r < nums.length; r++) {
            if (nums[r] == 0) zeros++;
            while (zeros > 1) if (nums[left++] == 0) zeros--;
            best = Math.max(best, r - left);
        }
        return best;
    }
}
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

```java
class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int left = 0, cost = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            cost += Math.abs(s.charAt(r) - t.charAt(r));
            while (cost > maxCost) {
                cost -= Math.abs(s.charAt(left) - t.charAt(left));
                left++;
            }
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, best = nums.length + 1;
        long sum = 0;
        for (int r = 0; r < nums.length; r++) {
            sum += nums[r];
            while (sum >= target) {
                best = Math.min(best, r - left + 1);
                sum -= nums[left++];
            }
        }
        return best > nums.length ? 0 : best;
    }
}
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

```java
import java.util.*;
class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";
        Map<Character, Integer> need = new HashMap<>();
        for (int i = 0; i < t.length(); i++)
            need.merge(t.charAt(i), 1, Integer::sum);
        int missing = t.length(), left = 0, start = 0, best = s.length() + 1;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            if (need.getOrDefault(c, 0) > 0) missing--;
            need.put(c, need.getOrDefault(c, 0) - 1);
            while (missing == 0) {
                if (r - left + 1 < best) { start = left; best = r - left + 1; }
                char old = s.charAt(left++);
                need.put(old, need.get(old) + 1);
                if (need.get(old) > 0) missing++;
            }
        }
        return best > s.length() ? "" : s.substring(start, start + best);
    }
}
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

```java
class Solution {
    public int minOperations(int[] nums, int x) {
        long target = -x;
        for (int value : nums) target += value;
        if (target < 0) return -1;
        if (target == 0) return nums.length;
        int left = 0, best = -1;
        long sum = 0;
        for (int r = 0; r < nums.length; r++) {
            sum += nums[r];
            while (sum > target) sum -= nums[left++];
            if (sum == target) best = Math.max(best, r - left + 1);
        }
        return best == -1 ? -1 : nums.length - best;
    }
}
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

```java
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        int left = 0, answer = 0;
        long product = 1;
        for (int r = 0; r < nums.length; r++) {
            product *= nums[r];
            while (product >= k) product /= nums[left++];
            answer += r - left + 1;
        }
        return answer;
    }
}
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

```java
class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        return atMost(nums, goal) - atMost(nums, goal - 1);
    }
    private int atMost(int[] nums, int bound) {
        if (bound < 0) return 0;
        int left = 0, sum = 0, count = 0;
        for (int r = 0; r < nums.length; r++) {
            sum += nums[r];
            while (sum > bound) sum -= nums[left++];
            count += r - left + 1;
        }
        return count;
    }
}
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

```java
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
    private int atMost(int[] nums, int bound) {
        if (bound < 0) return 0;
        int left = 0, odds = 0, count = 0;
        for (int r = 0; r < nums.length; r++) {
            odds += nums[r] & 1;
            while (odds > bound) odds -= nums[left++] & 1;
            count += r - left + 1;
        }
        return count;
    }
}
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

```java
import java.util.*;
class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
    private int atMost(int[] nums, int bound) {
        if (bound < 0) return 0;
        Map<Integer, Integer> freq = new HashMap<>();
        int left = 0, count = 0;
        for (int r = 0; r < nums.length; r++) {
            freq.merge(nums[r], 1, Integer::sum);
            while (freq.size() > bound) {
                int old = nums[left++];
                freq.put(old, freq.get(old) - 1);
                if (freq.get(old) == 0) freq.remove(old);
            }
            count += r - left + 1;
        }
        return count;
    }
}
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

```java
class Solution {
    public int numberOfSubstrings(String s) {
        int[] freq = new int[3];
        int left = 0, answer = 0;
        for (int r = 0; r < s.length(); r++) {
            freq[s.charAt(r) - 'a']++;
            while (freq[0] > 0 && freq[1] > 0 && freq[2] > 0)
                freq[s.charAt(left++) - 'a']--;
            answer += left;
        }
        return answer;
    }
}
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

```java
class Solution {
    public long countSubarrays(int[] nums, int k) {
        int maximum = nums[0];
        for (int x : nums) maximum = Math.max(maximum, x);
        int left = 0, count = 0;
        long answer = 0;
        for (int r = 0; r < nums.length; r++) {
            if (nums[r] == maximum) count++;
            while (count >= k) if (nums[left++] == maximum) count--;
            answer += left;
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        int[] answer = new int[nums.length - k + 1];
        for (int r = 0; r < nums.length; r++) {
            while (!q.isEmpty() && q.peekFirst() <= r - k) q.pollFirst();
            while (!q.isEmpty() && nums[q.peekLast()] <= nums[r]) q.pollLast();
            q.offerLast(r);
            if (r >= k - 1) answer[r - k + 1] = nums[q.peekFirst()];
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> high = new ArrayDeque<>(), low = new ArrayDeque<>();
        int left = 0, best = 0;
        for (int r = 0; r < nums.length; r++) {
            while (!high.isEmpty() && nums[high.peekLast()] <= nums[r]) high.pollLast();
            while (!low.isEmpty() && nums[low.peekLast()] >= nums[r]) low.pollLast();
            high.offerLast(r);
            low.offerLast(r);
            while ((long) nums[high.peekFirst()] - nums[low.peekFirst()] > limit) {
                if (high.peekFirst() == left) high.pollFirst();
                if (low.peekFirst() == left) low.pollFirst();
                left++;
            }
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

Sort. The cost of raising a window to its rightmost value is value * length - window sum. Shrink when cost exceeds k.

```java
import java.util.Arrays;
class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, best = 0;
        long sum = 0;
        for (int r = 0; r < nums.length; r++) {
            sum += nums[r];
            while ((long) nums[r] * (r - left + 1) - sum > k) sum -= nums[left++];
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int size = cardPoints.length - k, total = 0;
        for (int x : cardPoints) total += x;
        if (size == 0) return total;
        int window = 0;
        for (int i = 0; i < size; i++) window += cardPoints[i];
        int smallest = window;
        for (int r = size; r < cardPoints.length; r++) {
            window += cardPoints[r] - cardPoints[r - size];
            smallest = Math.min(smallest, window);
        }
        return total - smallest;
    }
}
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

```java
import java.util.*;
class Solution {
    private final TreeMap<Integer, Integer> low = new TreeMap<>();
    private final TreeMap<Integer, Integer> high = new TreeMap<>();
    private int lowSize, highSize;

    private void put(TreeMap<Integer, Integer> map, int x) {
        map.merge(x, 1, Integer::sum);
    }
    private void erase(TreeMap<Integer, Integer> map, int x) {
        int count = map.get(x);
        if (count == 1) map.remove(x);
        else map.put(x, count - 1);
    }
    private void balance() {
        while (lowSize > highSize + 1) {
            int x = low.lastKey();
            erase(low, x); put(high, x);
            lowSize--; highSize++;
        }
        while (lowSize < highSize) {
            int x = high.firstKey();
            erase(high, x); put(low, x);
            highSize--; lowSize++;
        }
    }
    private void add(int x) {
        if (low.isEmpty() || x <= low.lastKey()) { put(low, x); lowSize++; }
        else { put(high, x); highSize++; }
        balance();
    }
    private void remove(int x) {
        if (low.containsKey(x)) { erase(low, x); lowSize--; }
        else { erase(high, x); highSize--; }
        balance();
    }
    public double[] medianSlidingWindow(int[] nums, int k) {
        low.clear(); high.clear(); lowSize = highSize = 0;
        for (int i = 0; i < k; i++) add(nums[i]);
        double[] answer = new double[nums.length - k + 1];
        for (int start = 0; start < answer.length; start++) {
            answer[start] = k % 2 == 1 ? low.lastKey()
                : ((long) low.lastKey() + high.firstKey()) / 2.0;
            if (start + k < nums.length) {
                remove(nums[start]);
                add(nums[start + k]);
            }
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Trie {
    static class Node {
        Node[] child = new Node[26];
        boolean end;
    }
    private final Node root = new Node();
    public Trie() {}
    public void insert(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            int c = word.charAt(i) - 'a';
            if (node.child[c] == null) node.child[c] = new Node();
            node = node.child[c];
        }
        node.end = true;
    }
    private Node walk(String text) {
        Node node = root;
        for (int i = 0; i < text.length(); i++) {
            node = node.child[text.charAt(i) - 'a'];
            if (node == null) return null;
        }
        return node;
    }
    public boolean search(String word) {
        Node node = walk(word);
        return node != null && node.end;
    }
    public boolean startsWith(String prefix) { return walk(prefix) != null; }
    public void delete(String word) {
        Node[] path = new Node[word.length() + 1];
        path[0] = root;
        for (int i = 0; i < word.length(); i++) {
            path[i + 1] = path[i].child[word.charAt(i) - 'a'];
            if (path[i + 1] == null) return;
        }
        Node terminal = path[word.length()];
        if (!terminal.end) return;
        terminal.end = false;
        for (int i = word.length() - 1; i >= 0; i--) {
            Node child = path[i + 1];
            if (child.end || hasChildren(child)) break;
            path[i].child[word.charAt(i) - 'a'] = null;
        }
    }
    private boolean hasChildren(Node node) {
        for (Node child : node.child) if (child != null) return true;
        return false;
    }
}
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

```java
class Trie {
    static class Node {
        Node[] child = new Node[26];
        int passed, ends;
    }
    private final Node root = new Node();
    public Trie() {}
    public void insert(String word) {
        Node node = root;
        node.passed++;
        for (int i = 0; i < word.length(); i++) {
            int c = word.charAt(i) - 'a';
            if (node.child[c] == null) node.child[c] = new Node();
            node = node.child[c];
            node.passed++;
        }
        node.ends++;
    }
    private Node walk(String text) {
        Node node = root;
        for (int i = 0; i < text.length(); i++) {
            node = node.child[text.charAt(i) - 'a'];
            if (node == null) return null;
        }
        return node;
    }
    public int countWordsEqualTo(String word) {
        Node node = walk(word);
        return node == null ? 0 : node.ends;
    }
    public int countWordsStartingWith(String prefix) {
        Node node = walk(prefix);
        return node == null ? 0 : node.passed;
    }
    public void erase(String word) {
        if (countWordsEqualTo(word) == 0) return;
        Node[] path = new Node[word.length() + 1];
        Node node = root;
        path[0] = node;
        node.passed--;
        for (int i = 0; i < word.length(); i++) {
            node = node.child[word.charAt(i) - 'a'];
            path[i + 1] = node;
            node.passed--;
        }
        node.ends--;
        for (int i = word.length() - 1; i >= 0; i--) {
            if (path[i + 1].passed != 0) break;
            path[i].child[word.charAt(i) - 'a'] = null;
        }
    }
}
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

```java
import java.util.*;
class Solution {
    static class Node { Node[] child = new Node[26]; boolean end; }
    public String replaceWords(List<String> dictionary, String sentence) {
        Node root = new Node();
        for (String word : dictionary) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
            }
            node.end = true;
        }
        String[] words = sentence.split(" ");
        for (int w = 0; w < words.length; w++) {
            Node node = root;
            for (int i = 0; i < words[w].length(); i++) {
                node = node.child[words[w].charAt(i) - 'a'];
                if (node == null) break;
                if (node.end) { words[w] = words[w].substring(0, i + 1); break; }
            }
        }
        return String.join(" ", words);
    }
}
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

```java
class Solution {
    static class Node { Node[] child = new Node[26]; boolean end; }
    public String longestWord(String[] words) {
        Node root = new Node();
        for (String word : words) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
            }
            node.end = true;
        }
        String best = "";
        for (String word : words) {
            Node node = root;
            boolean valid = true;
            for (int i = 0; i < word.length(); i++) {
                node = node.child[word.charAt(i) - 'a'];
                if (!node.end) { valid = false; break; }
            }
            if (valid && (word.length() > best.length() ||
                (word.length() == best.length() && word.compareTo(best) < 0))) best = word;
        }
        return best;
    }
}
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

```java
import java.util.*;
class MapSum {
    static class Node { Node[] child = new Node[26]; int total; }
    private final Node root = new Node();
    private final Map<String, Integer> values = new HashMap<>();
    public MapSum() {}
    public void insert(String key, int val) {
        int delta = val - values.getOrDefault(key, 0);
        values.put(key, val);
        Node node = root;
        node.total += delta;
        for (int i = 0; i < key.length(); i++) {
            int c = key.charAt(i) - 'a';
            if (node.child[c] == null) node.child[c] = new Node();
            node = node.child[c];
            node.total += delta;
        }
    }
    public int sum(String prefix) {
        Node node = root;
        for (int i = 0; i < prefix.length(); i++) {
            node = node.child[prefix.charAt(i) - 'a'];
            if (node == null) return 0;
        }
        return node.total;
    }
}
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

```java
import java.util.*;
class WordDictionary {
    static class Node { Node[] child = new Node[26]; boolean end; }
    static class State {
        Node node; int index;
        State(Node node, int index) { this.node = node; this.index = index; }
    }
    private final Node root = new Node();
    public WordDictionary() {}
    public void addWord(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            int c = word.charAt(i) - 'a';
            if (node.child[c] == null) node.child[c] = new Node();
            node = node.child[c];
        }
        node.end = true;
    }
    public boolean search(String word) {
        Deque<State> stack = new ArrayDeque<>();
        stack.push(new State(root, 0));
        while (!stack.isEmpty()) {
            State state = stack.pop();
            Node node = state.node;
            int i = state.index;
            if (i == word.length()) { if (node.end) return true; }
            else if (word.charAt(i) == '.') {
                for (Node child : node.child)
                    if (child != null) stack.push(new State(child, i + 1));
            } else {
                Node child = node.child[word.charAt(i) - 'a'];
                if (child != null) stack.push(new State(child, i + 1));
            }
        }
        return false;
    }
}
```

**Time / Space Complexity**

Add: O(L). Search: O(min(V, L * 26^d)) worst-case upper bound, where V is trie nodes and d is number of dots. Search stack: O(26L) = O(L). Storage: O(S).

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

```java
import java.util.*;
class Solution {
    static class Node {
        Node[] child = new Node[26];
        List<String> top = new ArrayList<>();
    }
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        String[] sorted = products.clone();
        Arrays.sort(sorted);
        Node root = new Node();
        for (String word : sorted) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
                if (node.top.size() < 3) node.top.add(word);
            }
        }
        List<List<String>> answer = new ArrayList<>();
        Node node = root;
        for (int i = 0; i < searchWord.length(); i++) {
            node = node == null ? null : node.child[searchWord.charAt(i) - 'a'];
            answer.add(node == null ? new ArrayList<>() : new ArrayList<>(node.top));
        }
        return answer;
    }
}
```

**Time / Space Complexity**

Time: O(N log N * L + S + Q), including worst-case string comparisons in sorting; N products, max product length L, total product characters S, query length Q. Space: O(S + N + Q), including trie, sorting and output references.

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

```java
import java.util.*;
class MagicDictionary {
    static class Node { Node[] child = new Node[26]; boolean end; }
    static class State {
        Node node; int index, edits;
        State(Node n, int i, int e) { node = n; index = i; edits = e; }
    }
    private Node root = new Node();
    public MagicDictionary() {}
    public void buildDict(String[] dictionary) {
        root = new Node();
        for (String word : dictionary) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
            }
            node.end = true;
        }
    }
    public boolean search(String word) {
        Deque<State> stack = new ArrayDeque<>();
        stack.push(new State(root, 0, 0));
        while (!stack.isEmpty()) {
            State s = stack.pop();
            if (s.index == word.length()) {
                if (s.edits == 1 && s.node.end) return true;
                continue;
            }
            int expected = word.charAt(s.index) - 'a';
            if (s.edits == 1) {
                if (s.node.child[expected] != null)
                    stack.push(new State(s.node.child[expected], s.index + 1, 1));
            } else {
                for (int c = 0; c < 26; c++) if (s.node.child[c] != null)
                    stack.push(new State(s.node.child[c], s.index + 1, c == expected ? 0 : 1));
            }
        }
        return false;
    }
}
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

```java
class Solution {
    static class Node { Node[] child = new Node[26]; int count; }
    public int[] sumPrefixScores(String[] words) {
        Node root = new Node();
        for (String word : words) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
                node.count++;
            }
        }
        int[] answer = new int[words.length];
        for (int w = 0; w < words.length; w++) {
            Node node = root;
            for (int i = 0; i < words[w].length(); i++) {
                node = node.child[words[w].charAt(i) - 'a'];
                answer[w] += node.count;
            }
        }
        return answer;
    }
}
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

```java
import java.util.*;
class Solution {
    static class Node { Node[] child = new Node[26]; String word; }
    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String word : words) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
            }
            node.word = word;
        }
        List<String> answer = new ArrayList<>();
        if (board.length == 0 || board[0].length == 0) return answer;
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, answer);
        return answer;
    }
    private void dfs(char[][] board, int r, int c, Node parent, List<String> answer) {
        char ch = board[r][c];
        if (ch == '!') return;
        Node node = parent.child[ch - 'a'];
        if (node == null) return;
        if (node.word != null) { answer.add(node.word); node.word = null; }
        board[r][c] = '!';
        if (r > 0) dfs(board, r - 1, c, node, answer);
        if (r + 1 < board.length) dfs(board, r + 1, c, node, answer);
        if (c > 0) dfs(board, r, c - 1, node, answer);
        if (c + 1 < board[0].length) dfs(board, r, c + 1, node, answer);
        board[r][c] = ch;
    }
}
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

```java
import java.util.*;
class Solution {
    static class Node { Node[] child = new Node[26]; boolean end; }
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Node root = new Node();
        for (String word : words) {
            if (word.isEmpty()) continue;
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
            }
            node.end = true;
        }
        List<String> answer = new ArrayList<>();
        for (String word : words) {
            int[] pieces = new int[word.length() + 1];
            Arrays.fill(pieces, -1);
            pieces[0] = 0;
            for (int start = 0; start < word.length(); start++) {
                if (pieces[start] < 0) continue;
                Node node = root;
                for (int end = start; end < word.length(); end++) {
                    node = node.child[word.charAt(end) - 'a'];
                    if (node == null) break;
                    if (node.end) pieces[end + 1] = Math.max(pieces[end + 1], pieces[start] + 1);
                }
            }
            if (pieces[word.length()] >= 2) answer.add(word);
        }
        return answer;
    }
}
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

```java
class Solution {
    static class Node { Node[] child = new Node[2]; }
    public int findMaximumXOR(int[] nums) {
        Node root = new Node();
        for (int value : nums) {
            Node node = root;
            for (int bit = 30; bit >= 0; bit--) {
                int digit = (value >>> bit) & 1;
                if (node.child[digit] == null) node.child[digit] = new Node();
                node = node.child[digit];
            }
        }
        int best = 0;
        for (int value : nums) {
            Node node = root;
            int score = 0;
            for (int bit = 30; bit >= 0; bit--) {
                int digit = (value >>> bit) & 1;
                if (node.child[digit ^ 1] != null) {
                    score |= 1 << bit;
                    node = node.child[digit ^ 1];
                } else node = node.child[digit];
            }
            best = Math.max(best, score);
        }
        return best;
    }
}
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

```java
import java.util.*;
class Solution {
    static class Node { Node[] child = new Node[2]; }
    public int[] maximizeXor(int[] nums, int[][] queries) {
        int[] values = nums.clone();
        Arrays.sort(values);
        int[][] ordered = new int[queries.length][3];
        for (int i = 0; i < queries.length; i++)
            ordered[i] = new int[]{queries[i][1], queries[i][0], i};
        Arrays.sort(ordered, Comparator.comparingInt(a -> a[0]));
        int[] answer = new int[queries.length];
        Arrays.fill(answer, -1);
        Node root = new Node();
        int inserted = 0;
        for (int[] query : ordered) {
            while (inserted < values.length && values[inserted] <= query[0]) {
                Node node = root;
                int value = values[inserted++];
                for (int bit = 30; bit >= 0; bit--) {
                    int digit = (value >>> bit) & 1;
                    if (node.child[digit] == null) node.child[digit] = new Node();
                    node = node.child[digit];
                }
            }
            if (inserted == 0) continue;
            Node node = root;
            int score = 0;
            for (int bit = 30; bit >= 0; bit--) {
                int digit = (query[1] >>> bit) & 1;
                if (node.child[digit ^ 1] != null) {
                    score |= 1 << bit;
                    node = node.child[digit ^ 1];
                } else node = node.child[digit];
            }
            answer[query[2]] = score;
        }
        return answer;
    }
}
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

```java
class Solution {
    static class Node { Node[] child = new Node[2]; int count; }
    private long less(Node node, int value, long limit) {
        if (limit <= 0) return 0;
        long total = 0;
        for (int bit = 31; bit >= 0 && node != null; bit--) {
            int digit = (value >>> bit) & 1;
            if (((limit >>> bit) & 1L) != 0) {
                if (node.child[digit] != null) total += node.child[digit].count;
                node = node.child[digit ^ 1];
            } else node = node.child[digit];
        }
        return total;
    }
    public int countPairs(int[] nums, int low, int high) {
        Node root = new Node();
        long answer = 0;
        for (int value : nums) {
            answer += less(root, value, (long) high + 1) - less(root, value, low);
            Node node = root;
            for (int bit = 31; bit >= 0; bit--) {
                int digit = (value >>> bit) & 1;
                if (node.child[digit] == null) node.child[digit] = new Node();
                node = node.child[digit];
                node.count++;
            }
        }
        return (int) answer;
    }
}
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

```java
import java.util.*;
class StreamChecker {
    static class Node { Node[] child = new Node[26]; boolean end; }
    private final Node root = new Node();
    private final Deque<Character> stream = new ArrayDeque<>();
    private int maximum;
    public StreamChecker(String[] words) {
        for (String word : words) {
            maximum = Math.max(maximum, word.length());
            Node node = root;
            for (int i = word.length() - 1; i >= 0; i--) {
                int c = word.charAt(i) - 'a';
                if (node.child[c] == null) node.child[c] = new Node();
                node = node.child[c];
            }
            node.end = true;
        }
    }
    public boolean query(char letter) {
        stream.offerFirst(letter);
        if (stream.size() > maximum) stream.pollLast();
        Node node = root;
        for (char ch : stream) {
            node = node.child[ch - 'a'];
            if (node == null) return false;
            if (node.end) return true;
        }
        return false;
    }
}
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

```java
import java.util.*;
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int k = 2;
        Map<Character, Integer> freq = new HashMap<>();
        int left = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            freq.merge(s.charAt(r), 1, Integer::sum);
            while (freq.size() > k) {
                char old = s.charAt(left++);
                freq.put(old, freq.get(old) - 1);
                if (freq.get(old) == 0) freq.remove(old);
            }
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
import java.util.*;
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k <= 0) return 0;
        Map<Character, Integer> freq = new HashMap<>();
        int left = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            freq.merge(s.charAt(r), 1, Integer::sum);
            while (freq.size() > k) {
                char old = s.charAt(left++);
                freq.put(old, freq.get(old) - 1);
                if (freq.get(old) == 0) freq.remove(old);
            }
            best = Math.max(best, r - left + 1);
        }
        return best;
    }
}
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

```java
import java.util.*;
class Solution {
    public int numKLenSubstrNoRepeats(String s, int k) {
        if (k <= 0 || k > s.length()) return 0;
        Map<Character, Integer> freq = new HashMap<>();
        int answer = 0;
        for (int r = 0; r < s.length(); r++) {
            freq.merge(s.charAt(r), 1, Integer::sum);
            if (r >= k) {
                char old = s.charAt(r - k);
                freq.put(old, freq.get(old) - 1);
                if (freq.get(old) == 0) freq.remove(old);
            }
            if (r >= k - 1 && freq.size() == k) answer++;
        }
        return answer;
    }
}
```

**Time / Space Complexity**

Time: O(n) expected. Auxiliary space: O(min(n, k + 1)).
