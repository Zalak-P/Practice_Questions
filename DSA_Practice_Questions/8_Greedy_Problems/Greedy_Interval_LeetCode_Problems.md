# Greedy & Interval Problems

## 1. Jump Game I --- LeetCode 55

You are given an array where `nums[i]` tells you the **maximum distance
you can jump from index `i`**.

Return `true` if you can reach the last index, otherwise return `false`.

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

Time: O(n log n)
Space: O(n)

## 2. Jump Game II --- LeetCode 45

You are given a 0-indexed array of integers `nums` of length `n`. You
are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump
from index `i`.

Return the **minimum number of jumps** required to reach `nums[n - 1]`.

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

## 3. Minimum Add to Make Parentheses Valid --- LeetCode 921

You are given a string `s` containing only `'('` and `')'`.

In one move, you can insert either `'('` or `')'` anywhere in the
string.

Return the **minimum number of parentheses you must add** to make the
string valid.

A parentheses string is valid if:

- Every opening `'('` has a matching closing `')'`.
- A closing `')'` cannot appear before its matching opening `'('`.

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

## 4. Merge Intervals --- LeetCode 56

Given an array of intervals where `intervals[i] = [starti, endi]`, merge
all overlapping intervals and return an array of the non-overlapping
intervals that cover all the intervals in the input.

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

## 5. Meeting Rooms I --- LeetCode 252

Given an array of meeting time intervals where
`intervals[i] = [starti, endi]`, determine whether a person could attend
**all meetings**.

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

## 6. Meeting Rooms II --- LeetCode 253

Given an array of meeting time intervals, return the **minimum number of
conference rooms required**.

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

## 7. Gas Station --- LeetCode 134

There are `n` gas stations arranged in a circle.

`gas[i]` represents the amount of gas available at station `i`.

`cost[i]` represents the amount of gas required to travel from station
`i` to station `i + 1`.

You start with an empty tank.

Return the **starting gas station index** from which you can travel
around the entire circuit clockwise.

If it is impossible, return `-1`.

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

## 8. Minimum Number of Railway Platforms

Given the arrival and departure times of all trains reaching a railway
station, find the **minimum number of platforms required** so that no
train has to wait.

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

## 9. Insert Interval --- LeetCode 57

You are given an array of **non-overlapping intervals**, sorted by their
starting times.

You are also given `newInterval = [start, end]`.

Insert `newInterval` into the intervals while ensuring that the
resulting intervals are still sorted and non-overlapping.

Merge intervals if necessary.

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
