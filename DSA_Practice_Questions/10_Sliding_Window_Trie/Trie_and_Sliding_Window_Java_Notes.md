# Trie + Sliding Window Interview Problems — Java

## Trie

### 1. Implement Trie — Insert, Search, Delete

**Core Trick:** Each Trie node stores `children[26]` and `isEnd`.

```java
class Trie {

    static class TrieNode {

        TrieNode[] children = new TrieNode[26];

        boolean isEnd = false;
    }

    TrieNode root;

    public Trie() {

        root = new TrieNode();
    }


    public void insert(String word) {

        TrieNode current = root;

        for (char ch : word.toCharArray()) {

            int index = ch - 'a';

            if (current.children[index] == null) {

                current.children[index] =
                    new TrieNode();
            }

            current =
                current.children[index];
        }

        current.isEnd = true;
    }


    public boolean search(String word) {

        TrieNode node =
            searchPrefix(word);

        return node != null
            && node.isEnd;
    }


    public boolean startsWith(String prefix) {

        return searchPrefix(prefix) != null;
    }


    private TrieNode searchPrefix(
        String word
    ) {

        TrieNode current = root;

        for (char ch : word.toCharArray()) {

            int index = ch - 'a';

            if (current.children[index] == null) {
                return null;
            }

            current =
                current.children[index];
        }

        return current;
    }


    public void delete(String word) {

        delete(root, word, 0);
    }


    private boolean delete(
        TrieNode current,
        String word,
        int index
    ) {

        if (index == word.length()) {

            if (!current.isEnd) {
                return false;
            }

            current.isEnd = false;

            return hasNoChildren(current);
        }

        int childIndex =
            word.charAt(index) - 'a';

        TrieNode child =
            current.children[childIndex];

        if (child == null) {
            return false;
        }

        boolean shouldDeleteChild =
            delete(
                child,
                word,
                index + 1
            );

        if (shouldDeleteChild) {

            current.children[childIndex] =
                null;

            return !current.isEnd
                && hasNoChildren(current);
        }

        return false;
    }


    private boolean hasNoChildren(
        TrieNode node
    ) {

        for (TrieNode child : node.children) {

            if (child != null) {
                return false;
            }
        }

        return true;
    }
}
```

**Insert:** `O(L)`  
**Search:** `O(L)`  
**Delete:** `O(L × alphabet)` worst case  
**Space:** `O(total characters stored)`

### 2. Longest String With All Prefixes

**Core Trick:** Insert every word into a Trie. For each word, every node on its path must have `isEnd = true`.

```java
class Solution {

    static class TrieNode {

        TrieNode[] children =
            new TrieNode[26];

        boolean isEnd;
    }


    TrieNode root =
        new TrieNode();


    public String completeString(
        String[] words
    ) {

        for (String word : words) {
            insert(word);
        }

        String answer = "";

        for (String word : words) {

            if (allPrefixesExist(word)) {

                if (word.length() >
                    answer.length()) {

                    answer = word;
                }

                else if (
                    word.length() ==
                    answer.length()
                    &&
                    word.compareTo(answer) < 0
                ) {

                    answer = word;
                }
            }
        }

        return answer;
    }


    private void insert(String word) {

        TrieNode current = root;

        for (char ch : word.toCharArray()) {

            int index = ch - 'a';

            if (current.children[index] == null) {

                current.children[index] =
                    new TrieNode();
            }

            current =
                current.children[index];
        }

        current.isEnd = true;
    }


    private boolean allPrefixesExist(
        String word
    ) {

        TrieNode current = root;

        for (char ch : word.toCharArray()) {

            int index = ch - 'a';

            current =
                current.children[index];

            if (current == null ||
                !current.isEnd) {

                return false;
            }
        }

        return true;
    }
}
```

**Time:** `O(total characters)`  
**Space:** `O(total characters)`

## Sliding Window

### 3. Longest Substring Without Repeating Characters — LeetCode 3

**Core Trick:** Expand right. If duplicate appears, shrink from left until valid again.

```java
import java.util.*;

class Solution {

    public int lengthOfLongestSubstring(
        String s
    ) {

        Set<Character> window =
            new HashSet<>();

        int left = 0;
        int maxLength = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            char ch =
                s.charAt(right);

            while (window.contains(ch)) {

                window.remove(
                    s.charAt(left)
                );

                left++;
            }

            window.add(ch);

            maxLength =
                Math.max(
                    maxLength,
                    right - left + 1
                );
        }

        return maxLength;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(k)`

### 4. Longest Substring With At Most Two Distinct Characters

**Core Trick:** Keep `map.size() <= 2`.

```java
import java.util.*;

class Solution {

    public int lengthOfLongestSubstringTwoDistinct(
        String s
    ) {

        Map<Character, Integer> map =
            new HashMap<>();

        int left = 0;
        int maxLength = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            char ch =
                s.charAt(right);

            map.put(
                ch,
                map.getOrDefault(ch, 0) + 1
            );

            while (map.size() > 2) {

                char leftChar =
                    s.charAt(left);

                map.put(
                    leftChar,
                    map.get(leftChar) - 1
                );

                if (map.get(leftChar) == 0) {
                    map.remove(leftChar);
                }

                left++;
            }

            maxLength =
                Math.max(
                    maxLength,
                    right - left + 1
                );
        }

        return maxLength;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)` practically

### 5. Longest Substring With At Most K Distinct Characters

**Core Trick:** Keep `map.size() <= k`.

```java
import java.util.*;

class Solution {

    public int lengthOfLongestSubstringKDistinct(
        String s,
        int k
    ) {

        Map<Character, Integer> map =
            new HashMap<>();

        int left = 0;
        int maxLength = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            char ch =
                s.charAt(right);

            map.put(
                ch,
                map.getOrDefault(ch, 0) + 1
            );

            while (map.size() > k) {

                char leftChar =
                    s.charAt(left);

                map.put(
                    leftChar,
                    map.get(leftChar) - 1
                );

                if (map.get(leftChar) == 0) {
                    map.remove(leftChar);
                }

                left++;
            }

            maxLength =
                Math.max(
                    maxLength,
                    right - left + 1
                );
        }

        return maxLength;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(k)`

### 6. Find K-Length Substrings With No Repeated Characters

**Core Trick:** Fixed-size window. Valid when window length is `k` and distinct-character count is also `k`.

```java
import java.util.*;

class Solution {

    public int numKLenSubstrNoRepeats(
        String s,
        int k
    ) {

        if (k > s.length()) {
            return 0;
        }

        Map<Character, Integer> map =
            new HashMap<>();

        int left = 0;
        int count = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            char ch =
                s.charAt(right);

            map.put(
                ch,
                map.getOrDefault(ch, 0) + 1
            );

            if (right - left + 1 > k) {

                char leftChar =
                    s.charAt(left);

                map.put(
                    leftChar,
                    map.get(leftChar) - 1
                );

                if (map.get(leftChar) == 0) {
                    map.remove(leftChar);
                }

                left++;
            }

            if (right - left + 1 == k
                && map.size() == k) {

                count++;
            }
        }

        return count;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(k)`

### 7. Longest Repeating Character Replacement — LeetCode 424

**Core Trick:** `windowSize - maxFrequency <= k`.

```java
class Solution {

    public int characterReplacement(
        String s,
        int k
    ) {

        int[] frequency =
            new int[26];

        int left = 0;
        int maxFrequency = 0;
        int maxLength = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            int index =
                s.charAt(right) - 'A';

            frequency[index]++;

            maxFrequency =
                Math.max(
                    maxFrequency,
                    frequency[index]
                );

            while (
                right - left + 1
                - maxFrequency
                > k
            ) {

                frequency[
                    s.charAt(left) - 'A'
                ]--;

                left++;
            }

            maxLength =
                Math.max(
                    maxLength,
                    right - left + 1
                );
        }

        return maxLength;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

### 8. Sliding Window Maximum — LeetCode 239 — Very Important

**Core Trick:** Use a monotonic decreasing deque of indices. The front always gives the current maximum.

```java
import java.util.*;

class Solution {

    public int[] maxSlidingWindow(
        int[] nums,
        int k
    ) {

        int[] result =
            new int[nums.length - k + 1];

        Deque<Integer> deque =
            new ArrayDeque<>();

        int index = 0;

        for (int right = 0;
             right < nums.length;
             right++) {

            while (
                !deque.isEmpty()
                &&
                nums[deque.peekLast()]
                <= nums[right]
            ) {

                deque.pollLast();
            }

            deque.offerLast(right);

            if (
                deque.peekFirst()
                <= right - k
            ) {

                deque.pollFirst();
            }

            if (right >= k - 1) {

                result[index++] =
                    nums[deque.peekFirst()];
            }
        }

        return result;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(k)`

### 9. Minimum Window Substring — LeetCode 76 — VV Important

**Core Trick:** Expand until valid, then shrink while valid to find the minimum window.

```java
import java.util.*;

class Solution {

    public String minWindow(
        String s,
        String t
    ) {

        if (t.length() > s.length()) {
            return "";
        }

        Map<Character, Integer> need =
            new HashMap<>();

        for (char ch : t.toCharArray()) {

            need.put(
                ch,
                need.getOrDefault(ch, 0) + 1
            );
        }

        Map<Character, Integer> window =
            new HashMap<>();

        int required = need.size();
        int formed = 0;

        int left = 0;

        int minLength =
            Integer.MAX_VALUE;

        int start = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            char ch =
                s.charAt(right);

            window.put(
                ch,
                window.getOrDefault(ch, 0) + 1
            );

            if (
                need.containsKey(ch)
                &&
                window.get(ch)
                    .intValue()
                ==
                need.get(ch)
                    .intValue()
            ) {

                formed++;
            }

            while (
                left <= right
                &&
                formed == required
            ) {

                if (
                    right - left + 1
                    < minLength
                ) {

                    minLength =
                        right - left + 1;

                    start = left;
                }

                char leftChar =
                    s.charAt(left);

                window.put(
                    leftChar,
                    window.get(leftChar) - 1
                );

                if (
                    need.containsKey(leftChar)
                    &&
                    window.get(leftChar)
                    < need.get(leftChar)
                ) {

                    formed--;
                }

                left++;
            }
        }

        if (minLength == Integer.MAX_VALUE) {
            return "";
        }

        return s.substring(
            start,
            start + minLength
        );
    }
}
```

**Time:** `O(n + m)`  
**Space:** `O(character set)`

### 10. Find All Anagrams in a String — LeetCode 438

**Core Trick:** Fixed-size window equal to `p.length()` and compare frequency arrays.

```java
import java.util.*;

class Solution {

    public List<Integer> findAnagrams(
        String s,
        String p
    ) {

        List<Integer> result =
            new ArrayList<>();

        if (p.length() > s.length()) {
            return result;
        }

        int[] need =
            new int[26];

        int[] window =
            new int[26];

        for (char ch : p.toCharArray()) {

            need[ch - 'a']++;
        }

        int left = 0;

        for (int right = 0;
             right < s.length();
             right++) {

            window[
                s.charAt(right) - 'a'
            ]++;

            if (
                right - left + 1
                > p.length()
            ) {

                window[
                    s.charAt(left) - 'a'
                ]--;

                left++;
            }

            if (
                right - left + 1
                == p.length()
                &&
                Arrays.equals(
                    need,
                    window
                )
            ) {

                result.add(left);
            }
        }

        return result;
    }
}
```

**Time:** `O(n)` effectively  
**Space:** `O(1)`

### 11. Max Consecutive Ones III — LeetCode 1004

**Core Trick:** Window is valid while `zeroCount <= k`.

```java
class Solution {

    public int longestOnes(
        int[] nums,
        int k
    ) {

        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;

        for (int right = 0;
             right < nums.length;
             right++) {

            if (nums[right] == 0) {
                zeroCount++;
            }

            while (zeroCount > k) {

                if (nums[left] == 0) {
                    zeroCount--;
                }

                left++;
            }

            maxLength =
                Math.max(
                    maxLength,
                    right - left + 1
                );
        }

        return maxLength;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

### 12. Longest Subarray of 1s After Deleting One Element — LeetCode 1493

**Core Trick:** Keep at most one zero in the window. Since one element must be deleted, answer is `right - left`, not `right - left + 1`.

```java
class Solution {

    public int longestSubarray(
        int[] nums
    ) {

        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;

        for (int right = 0;
             right < nums.length;
             right++) {

            if (nums[right] == 0) {
                zeroCount++;
            }

            while (zeroCount > 1) {

                if (nums[left] == 0) {
                    zeroCount--;
                }

                left++;
            }

            maxLength =
                Math.max(
                    maxLength,
                    right - left
                );
        }

        return maxLength;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

## Sliding Window Pattern Map

| Problem | Main Trick |
|---|---|
| Longest substring without repeat | Window contains unique chars |
| At most 2 distinct | `map.size() <= 2` |
| At most K distinct | `map.size() <= k` |
| K-length unique substring | Fixed window + unique chars |
| Character Replacement | `window - maxFreq <= k` |
| Sliding Window Maximum | Monotonic deque |
| Minimum Window Substring | Expand valid → shrink to minimum |
| Find All Anagrams | Fixed window + frequency |
| Max Consecutive Ones III | `zeros <= k` |
| Delete One Element | `zeros <= 1`, answer `window - 1` |
