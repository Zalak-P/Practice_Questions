## 1. Jump Game I — LeetCode 55

You are given an array where `nums[i]` tells you the **maximum distance you can jump from index `i`**.

Example:

```text
nums = [2,3,1,1,4]

Index:  0 1 2 3 4
Value:  2 3 1 1 4
```

From index `0`, you can jump at most `2` positions. So keep looking.

The key idea is to keep track of the **farthest index reachable so far**.

```java
class Solution {
    public boolean canJump(int[] nums) {

        int maxReach = 0;

        for (int i = 0; i < nums.length; i++) {

            // Cannot even reach this index
            if (i > maxReach) {
                return false;
            }

            // Farthest position reachable from here
            maxReach = Math.max(maxReach, i + nums[i]);

            // End is reachable
            if (maxReach >= nums.length - 1) {
                return true;
            }
        }

        return true;
    }
}
```

For:

```text
maxReach >= lastIndex
4 >= 4
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 2. Jump Game II — LeetCode 45

Here, reaching the end is guaranteed.
Now the question is: What is the **minimum number of jumps** needed?

Example:

```text
Input: nums = [2,3,1,1,4]
Output: 2
Possible path:
0 → 1 → 4
```

```java
class Solution {
    public int jump(int[] nums) {

        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;

        // No need to jump from the last index
        for (int i = 0; i < nums.length - 1; i++) {

            // Farthest point reachable for next jump
            farthest = Math.max(farthest, i + nums[i]);

            // Finished current jump's range
            if (i == currentEnd) {
                jumps++;
                // Next range boundary
                currentEnd = farthest;
            }
        }
        return jumps;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 3. Minimum Add to Make Parentheses Valid — LeetCode 921

You are given a string `s` containing only `'('` and `')'`.

Return the **minimum number of parentheses you must add** to make the string valid.

A parentheses string is valid if:

- Every opening `'('` has a matching closing `')'`.
- A closing `')'` cannot appear before its matching opening `'('`.

### Example 1

```text
Input: s = "())"
Output: 1
```

Explanation:

```text
())
  ↑
Need one '('
```

For example:

```text
(())
```

### Example 2

```text
Input: s = "((("
Output: 3
```

You need three closing parentheses:

```text
((()))
```

### Example 3

```text
Input: s = "()"
Output: 0
```

The string is already valid.

### Java

```java
class Solution {
    public int minAddToMakeValid(String s) {

        int open = 0; // Unmatched '('
        int add = 0;  // '(' we need to add

        for (char ch : s.toCharArray()) {

            if (ch == '(') {
                open++;
            } else {
                if (open > 0) {
                    open--; // Match ')' with an existing '('
                } else {
                    add++;  // No '(' available, so add one
                }
            }
        }

        // add = missing '('
        // open = missing ')'
        return add + open;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 4. Merge Intervals — LeetCode 56

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

```text
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

```java
import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {

        // Sort by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> result = new ArrayList<>();

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {

            // Overlap
            if (intervals[i][0] <= end) {
                end = Math.max(end, intervals[i][1]);
            }
            // No overlap
            else {
                result.add(new int[]{start, end});

                start = intervals[i][0];
                end = intervals[i][1];
            }
        }

        // Add last interval
        result.add(new int[]{start, end});

        return result.toArray(new int[result.size()][]);
    }
}
```

**Key condition:**

```java
intervals[i][0] <= end
```

If the next interval starts before the current interval ends → **overlap**.

**Time:** `O(n log n)`  
**Space:** `O(n)`

---

## 5. Meeting Rooms I — LeetCode 252

Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, determine whether a person could attend **all meetings**.

```text
Input:  [[0,30],[5,10],[15,20]]
Output: false
```

```text
Input:  [[7,10],[2,4]]
Output: true
```

```java
import java.util.*;

class Solution {
    public boolean canAttendMeetings(int[][] intervals) {

        // Sort by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        for (int i = 1; i < intervals.length; i++) {

            // Current starts before previous ends
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }

        return true;
    }
}
```

Example:

```text
[[0,30], [5,10], [15,20]]

0------30
     5---10
          15---20

Overlap → false
```

The entire problem comes down to:

```java
currentStart < previousEnd
```

**Time:** `O(n log n)`  
**Space:** `O(1)` apart from sorting overhead.

---

## 6. Meeting Rooms II — LeetCode 253

Given an array of meeting time intervals, return the **minimum number of conference rooms required**.

```text
Input:  [[0,30],[5,10],[15,20]]
Output: 2
```

```text
Input:  [[7,10],[2,4]]
Output: 1
```

A clean interview solution is **sorting + min heap**.

The heap stores the **end times of meetings currently using rooms**.

```java
import java.util.*;

class Solution {
    public int minMeetingRooms(int[][] intervals) {

        if (intervals.length == 0) {
            return 0;
        }

        // Sort meetings by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        // Stores room end times
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int[] meeting : intervals) {

            int start = meeting[0];
            int end = meeting[1];

            // Earliest room is free
            if (!minHeap.isEmpty() && start >= minHeap.peek()) {
                minHeap.poll();
            }

            // Use a room for current meeting
            minHeap.offer(end);
        }

        return minHeap.size();
    }
}
```

For:

```text
[[0,30], [5,10], [15,20]]
```

Conceptually:

```text
Meeting       Heap

[0,30]        [30]

[5,10]        [10,30]

[15,20]
10 <= 15
remove 10
add 20

               [20,30]
```

Two rooms are required.

**Time:** `O(n log n)`  
**Space:** `O(n)`

---

## 7. Gas Station — LeetCode 134

There are `n` gas stations arranged in a circle.

`gas[i]` represents the amount of gas available at station `i`.

`cost[i]` represents the amount of gas required to travel from station `i` to station `i + 1`.

You start with an empty tank.

Return the **starting gas station index** from which you can travel around the entire circuit clockwise.

If it is impossible, return `-1`.

```text
Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3
```

This is a classic **greedy** problem.

```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {

        int totalGas = 0;
        int currentGas = 0;
        int start = 0;

        for (int i = 0; i < gas.length; i++) {

            int gain = gas[i] - cost[i];

            totalGas += gain;
            currentGas += gain;

            // Cannot reach next station
            if (currentGas < 0) {

                // Try starting after current station
                start = i + 1;
                currentGas = 0;
            }
        }

        // Overall trip impossible
        if (totalGas < 0) {
            return -1;
        }

        return start;
    }
}
```

There are **two important variables**:

```text
totalGas
    ↓
Can the entire journey happen?


currentGas
    ↓
Can my current starting position work?
```

For:

```text
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
```

Differences:

```text
gas - cost

[-2, -2, -2, +3, +3]
```

Whenever:

```java
currentGas < 0
```

the current starting point cannot work.

So:

```java
start = i + 1;
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 8. Minimum Number of Railway Platforms

Given the arrival and departure times of all trains reaching a railway station, find the **minimum number of platforms required** so that no train has to wait.

```text
Arrival   = [900, 940, 950, 1100, 1500, 1800]
Departure = [910, 1200, 1120, 1130, 1900, 2000]

Output: 3
```

At the busiest point, three trains are at the station simultaneously, so `3` platforms are required.

This is essentially **Meeting Rooms II using two pointers**.

```java
import java.util.*;

class Solution {
    public static int findPlatform(int[] arrival, int[] departure) {

        Arrays.sort(arrival);
        Arrays.sort(departure);

        int i = 0; // Next arrival
        int j = 0; // Next departure

        int platforms = 0;
        int maxPlatforms = 0;

        while (i < arrival.length && j < departure.length) {

            // Train arrives before/equal to departure
            if (arrival[i] <= departure[j]) {

                platforms++;

                maxPlatforms = Math.max(maxPlatforms, platforms);

                i++;
            }
            // Train leaves
            else {

                platforms--;

                j++;
            }
        }

        return maxPlatforms;
    }
}
```

Example:

```text
Arrival:
900  940  950  1100  1500  1800

Departure:
910  1120  1130  1200  1900  2000
```

Think:

```text
Arrival   → +1 platform
Departure → -1 platform
```

Then track:

```java
maxPlatforms = Math.max(maxPlatforms, platforms);
```

**Time:** `O(n log n)`  
**Space:** `O(1)` apart from sorting overhead.

---

## 9. Insert Interval — LeetCode 57

You are given an array of **non-overlapping intervals**, sorted by their starting times.

You are also given:

```text
newInterval = [start, end]
```

Insert `newInterval` into the intervals while ensuring that the resulting intervals are still sorted and non-overlapping.

Merge intervals if necessary.

```text
Input:
intervals   = [[1,3],[6,9]]
newInterval = [2,5]

Output:
[[1,5],[6,9]]
```

Another example:

```text
Input:
intervals   = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

Output:
[[1,2],[3,10],[12,16]]
```

There are **3 stages**:

```text
1. Before new interval
2. Overlapping with new interval
3. After new interval
```

Code:

```java
import java.util.*;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {

        List<int[]> result = new ArrayList<>();

        int i = 0;
        int n = intervals.length;

        // 1. Add intervals completely before newInterval
        while (i < n && intervals[i][1] < newInterval[0]) {

            result.add(intervals[i]);
            i++;
        }

        // 2. Merge overlapping intervals
        while (i < n && intervals[i][0] <= newInterval[1]) {

            newInterval[0] =
                Math.min(newInterval[0], intervals[i][0]);

            newInterval[1] =
                Math.max(newInterval[1], intervals[i][1]);

            i++;
        }

        result.add(newInterval);

        // 3. Add remaining intervals
        while (i < n) {

            result.add(intervals[i]);
            i++;
        }

        return result.toArray(new int[result.size()][]);
    }
}
```

Example:

```text
intervals:

[1,2] [3,5] [6,7] [8,10] [12,16]

newInterval:

[4,8]
```

Think of three sections:

```text
BEFORE       OVERLAP                    AFTER

[1,2]       [3,5] [6,7] [8,10]        [12,16]
                 ↑
               [4,8]

                    ↓ merge

[1,2]       [3,10]                     [12,16]
```

Output:

```text
[[1,2], [3,10], [12,16]]
```

**Time:** `O(n)`  
**Space:** `O(n)`
