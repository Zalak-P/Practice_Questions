# String Problems

## 1. String Miss

Given two strings where the second string contains the same characters
as the first string except for one missing character, find the **missing
character**.

Example:

``` text
Input:
s1 = "abcdef"
s2 = "abdef"

Output:
c
```

``` java
class Solution {
    public char findMissingCharacter(String s1, String s2) {

        char result = 0;

        // XOR all characters from first string
        for (char ch : s1.toCharArray()) {
            result ^= ch;
        }

        // XOR all characters from second string
        for (char ch : s2.toCharArray()) {
            result ^= ch;
        }

        // Matching characters cancel out
        return result;
    }
}
```

## 2. Count and Say --- LeetCode 38

The **count-and-say** sequence is a sequence of digit strings defined
recursively:

-   `countAndSay(1) = "1"`
-   To generate the next string, read the previous string and describe
    consecutive groups of the same digit.

Return the `n`th term of the count-and-say sequence.

Example:

``` text
n = 4

1
11
21
1211

Output: "1211"
```

``` java
class Solution {
    public String countAndSay(int n) {

        String result = "1";

        for (int i = 2; i <= n; i++) {

            StringBuilder next = new StringBuilder();

            int count = 1;

            for (int j = 1; j < result.length(); j++) {

                // Same consecutive character
                if (result.charAt(j) == result.charAt(j - 1)) {
                    count++;
                } else {

                    // Add count and character
                    next.append(count);
                    next.append(result.charAt(j - 1));

                    count = 1;
                }
            }

            // Add last group
            next.append(count);
            next.append(result.charAt(result.length() - 1));

            result = next.toString();
        }

        return result;
    }
}
```

## 3. Decode String --- LeetCode 394

Given an encoded string, return its decoded string.

The encoding rule is:

``` text
k[encoded_string]
```

where the `encoded_string` inside the square brackets is repeated
exactly `k` times.

Example:

``` text
Input: "3[a]2[bc]"

Output: "aaabcbc"
```

Another example:

``` text
Input: "3[a2[c]]"

Output: "accaccacc"
```

``` java
import java.util.*;

class Solution {
    public String decodeString(String s) {

        Stack<Integer> countStack = new Stack<>();
        Stack<StringBuilder> stringStack = new Stack<>();

        StringBuilder current = new StringBuilder();
        int number = 0;

        for (char ch : s.toCharArray()) {

            // Build multi-digit number
            if (Character.isDigit(ch)) {
                number = number * 10 + (ch - '0');
            }

            // Start new encoded section
            else if (ch == '[') {

                countStack.push(number);
                stringStack.push(current);

                number = 0;
                current = new StringBuilder();
            }

            // Finish encoded section
            else if (ch == ']') {

                int repeat = countStack.pop();
                StringBuilder previous = stringStack.pop();

                for (int i = 0; i < repeat; i++) {
                    previous.append(current);
                }

                current = previous;
            }

            // Normal character
            else {
                current.append(ch);
            }
        }

        return current.toString();
    }
}
```

## 4. First Non-Repeating Character

Given a string, find the **first character that occurs only once**.

If no non-repeating character exists, return an appropriate value such
as `'\0'`.

Example:

``` text
Input: "aabbcddee"

Output: 'c'
```

``` java
import java.util.*;

class Solution {
    public char firstNonRepeatingCharacter(String s) {

        Map<Character, Integer> frequency = new LinkedHashMap<>();

        // Count frequency
        for (char ch : s.toCharArray()) {
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }

        // Find first character occurring once
        for (char ch : s.toCharArray()) {

            if (frequency.get(ch) == 1) {
                return ch;
            }
        }

        return '\0';
    }
}
```

## 5. String Compression --- Very Important

Given a string containing consecutive repeating characters, compress it
by replacing each group with the character followed by its count.

Example:

``` text
Input:
"aaabbffr"

Output:
"a3b2f2r1"
```

``` java
class Solution {
    public String compress(String s) {

        if (s == null || s.length() == 0) {
            return "";
        }

        StringBuilder result = new StringBuilder();

        int count = 1;

        for (int i = 1; i < s.length(); i++) {

            // Same consecutive character
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            }

            // Character changed
            else {

                result.append(s.charAt(i - 1));
                result.append(count);

                count = 1;
            }
        }

        // Add last character group
        result.append(s.charAt(s.length() - 1));
        result.append(count);

        return result.toString();
    }
}
```
