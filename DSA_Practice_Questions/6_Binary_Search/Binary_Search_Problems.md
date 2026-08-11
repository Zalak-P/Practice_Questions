# Binary Search Problems

- Style A: The "Exact Target / Match" Style, Code: while low <= high (Striver's Binary Search Vidoes)
- Style B: The "Property / Convergence" Style, Code: while low < high (Codestory mik)

---

## 1. Lower and Upper Bound

**Core Trick**: Lower bound: arr[mid] >= target, Upper bound: arr[mid] > target

```python
def lower_bound(arr, target):
    low = 0
    ans = len(arr)
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # If mid element is greater than or equal to target
        if arr[mid] >= target:
            ans = mid
            high = mid - 1        # Look left; mid is still a candidate
        else:
            low = mid + 1     # Look right; mid is too small
    return ans

def upper_bound(arr, target):
    low = 0
    ans = len(arr)
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        # If mid element is strictly greater than target
        if arr[mid] > target:
            ans = mid
            high = mid - 1    # Look left; mid is still a candidate
        else:
            low = mid + 1     # Look right; mid is <= target, so discard it
    return ans

```

---

## 2. Search in an Infinitely Long Sorted Array

It first expands the search range exponentially and then applies binary search.

```python
def find_element_infinite_array(arr, target):
    # Phase 1: Exponential Backoff to find the search window
    low = 0
    high = 1

    # Expand high exponentially until arr[high] is >= target
    while arr[high] < target:
        low = high
        high *= 2  # Double the search space window

    # Phase 2: Standard Binary Search within the discovered window [low, high]
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid        # Target found, return its index
        elif arr[mid] > target:
            high = mid - 1    # Look left
        else:
            low = mid + 1     # Look right

    return -1  # Target is not present in the array

```

---

## 3. The N-th Root of an Integer

> **Core Trick**: In binary search on answer, you have to define left and right. It's usually on 1 to m.

```python
def multiply(number, n, target):
    """
    Helper function to calculate number^n safely.
    Returns:
     1 if number^n > target
     0 if number^n == target
    -1 if number^n < target
    """
    ans = 1
    for _ in range(n):
        ans *= number
        if ans > target:
            return 1  # Exceeded target early, prevent unnecessary loops
    if ans == target:
        return 0
    return -1

def nth_root(n, m):
    # Search space for the root is always between 1 and M
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2
        mid_power_status = multiply(mid, n, m)

        if mid_power_status == 0:
            return mid       # Exact N-th root found
        elif mid_power_status == 1:
            high = mid - 1   # mid^N is too big, search left
        else:
            low = mid + 1    # mid^N is too small, search right

    return -1  # Return -1 if M is not a perfect N-th power

```

---

## 4. Square Root of an Integer

**Core Trick:** Finding the Square Root of an Integer \(M\) is a specific case of the \(N\)-th root problem where \(N = 2\). If perfect square is not found then we look for floor value.

```python
def floor_sqrt(m):
    # Edge case for 0 and 1
    if m == 0 or m == 1:
        return m

    low = 1
    high = m
    ans = 0  # To track the closest floor square root

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared == m:
            return mid       # Exact perfect square found
        elif mid_squared < m:
            ans = mid        # mid is a potential floor answer, save it
            low = mid + 1    # Try to find a larger value on the right
        else:
            high = mid - 1   # Too big, look left

    return ans

```

---

## 5. Search in a Sorted and Rotated Array

![Search in a sorted and rotated array dry run](images/05_search_rotated_array.png)

> **Core Trick**: Identify which half is sorted: left/right.

```python
def search_rotated_sorted_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Condition 1: Target found
        if arr[mid] == target:
            return mid

        # Condition 2: Left half is normally sorted
        if arr[low] <= arr[mid]:
            # Check if target falls strictly within this left sorted range
            if arr[low] <= target < arr[mid]:
                high = mid - 1  # Search left
            else:
                low = mid + 1   # Search right

        # Condition 3: Right half is normally sorted
        else:
            # Check if target falls strictly within this right sorted range
            if arr[mid] < target <= arr[high]:
                low = mid + 1   # Search right
            else:
                high = mid - 1  # Search left

    return -1  # Target not found

    # Rotated II - Critical Edge Case: Cannot determine which half is sorted
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue  # Skip to the next iteration with reduced search space
```

---

## 6. Find Peak Element

Question: A peak element in an array is an element that is strictly greater than its **neighbors**.
If **multiple peaks** then return any of them. If peak at **either side** then assume the out-of-bounds neighbors are equal to negative infinity (-∞).

```python
def find_peak_element(arr):
    n = len(arr)

    # Handle single element edge case
    if n == 1:
        return 0

    # Check if the first or last element is a peak
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # Search space excludes the first and last elements since they were already checked
    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        # Condition 1: mid is a peak element
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        # Condition 2: We are on an upward slope to the right
        elif arr[mid] < arr[mid + 1]:
            low = mid + 1   # A peak must exist to the right

        # Condition 3: We are on a downward slope, or a local valley
        else:
            high = mid - 1  # A peak must exist to the left

    return -1

```

Style B: Instead of looking at both neighbors, you only look at one anchor: the neighbor directly to the right (nums[mid + 1]). This tells you which direction the mountain slope is going.Because low < high, mid can never equal high. This guarantees that mid + 1 is always a valid index inside the array. It will never crash.

```python
def find_peak_element(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # Compare mid with its immediate right neighbor
        if nums[mid] < nums[mid + 1]:
            low = mid + 1   # Upward slope: peak is to the right
        else:
            high = mid      # Downward slope: mid or left could be peak

    return low  # low and high converge perfectly on a peak
```

---

## 7. Find First and Last Position

```python
def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    first_idx = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            first_idx = mid
            high = mid - 1  # Keep looking left for the first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first_idx


def find_last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    last_idx = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            last_idx = mid
            low = mid + 1   # Keep looking right for the last occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last_idx


def first_and_last_position(arr, target):
    """
    Returns a list/tuple of [first_occurrence, last_occurrence].
    Returns [-1, -1] if the target is not found.
    """
    first = find_first_occurrence(arr, target)
    # If the first occurrence doesn't exist, the last won't either
    if first == -1:
        return [-1, -1]

    last = find_last_occurrence(arr, target)
    return [first, last]

```

---

## 8. Find Minimum in a Rotated Sorted Array

Style B: This version also handles duplicate values. With distinct values, the time complexity is `O(log n)`. With many duplicates, the worst case can become `O(n)`. Pointer-Convergence Style:

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        # Step 3: Continue until one minimum candidate remains.
        while low < high:
            mid = (low + high) // 2

            # Step 5: If nums[mid] is smaller than nums[high],the minimum is at mid or somewhere to its left.
            if nums[mid] < nums[high]:
                high = mid

            elif nums[mid] > nums[high]:
                low = mid + 1

            # Step 7: Equal values do not reveal the correct half.
            # Remove one duplicate safely from the right.
            else:
                high -= 1

        # Step 8: low points to the minimum element.
        return nums[low]
```

---

## 9. Koko Eating Bananas

```python
import math

def minEatingSpeed(piles, h):
    # Step 1: Define the search space for speed 'k'
    low = 1
    high = max(piles)
    ans = high  # Fallback answer tracking variable

    while low <= high:
        mid_speed = (low + high) // 2

        # Calculate total hours spent eating at 'mid_speed'
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / mid_speed)

        # Condition Check
        if total_hours <= h:
            ans = mid_speed   # mid_speed works! Save it as a candidate.
            high = mid_speed - 1  # Try to find a slower, more optimal speed.
        else:
            low = mid_speed + 1   # Too slow, Koko runs out of time. Look right.

    return ans

```

---

## 10. Allocation of Minimum Number of Pages

DSA_Practice_Questions/6_Binary_Search/images/image.png

```python
def count_students(arr, max_pages_allowed):
    """
    Helper function to count how many students are needed
    if no single student can read more than 'max_pages_allowed'.
    """
    students = 1
    current_pages = 0

    for pages in arr:
        if current_pages + pages <= max_pages_allowed:
            current_pages += pages
        else:
            students += 1
            current_pages = pages

    return students


def find_pages(arr, n, m):
    # Edge case: If there are more students than books, allocation is impossible
    if m > n:
        return -1

    # Step 1: Define the search space boundaries
    low = max(arr)     # Min possible answer: the biggest single book
    high = sum(arr)    # Max possible answer: one student reads all books
    ans = -1

    while low <= high:
        mid_pages = (low + high) // 2

        # Calculate how many students are required for this page limit
        required_students = count_students(arr, mid_pages)

        # Condition Check (Style A)
        if required_students <= m:
            ans = mid_pages        # This configuration is valid, save it.
            high = mid_pages - 1   # Try to find a smaller maximum page limit.
        else:
            low = mid_pages + 1    # Pages limit is too small, we need more students. Look right.

    return ans
```

---

## 11. Aggressive Cows

![Aggressive Cows dry run](images/11_aggressive_cows.png)

```python
def aggressive_cows(stalls, cows):
    # Step 1: Validate the input.
    if not stalls or cows <= 0 or cows > len(stalls):
        return -1

    # Step 2: With one cow, no distance between cows is required.
    if cows == 1:
        return 0

    # Step 3: Sort stall positions before greedy placement.
    stalls.sort()

    def can_place(minimum_distance):
        # Step 4: Place the first cow in the first stall.
        placed = 1
        last_position = stalls[0]

        # Step 5: Greedily place every next cow at the earliest
        # stall that maintains the required minimum distance.
        for position in stalls[1:]:
            if position - last_position >= minimum_distance:
                placed += 1
                last_position = position

                # Step 6: The candidate distance is feasible.
                if placed == cows:
                    return True

        # Step 7: Not enough cows could be placed.
        return False

    # Step 8: Search possible minimum distances.
    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0

    # Step 9: Binary-search for the largest feasible distance.
    while low <= high:
        distance = (low + high) // 2

        # Step 10: If feasible, save it and try a larger distance.
        if can_place(distance):
            answer = distance
            low = distance + 1

        # Step 11: Otherwise, try a smaller distance.
        else:
            high = distance - 1

    # Step 12: Return the maximum possible minimum distance.
    return answer
```

---

## 12. Painter's Partition Problem

![Painter's Partition Problem dry run](images/12_painter_partition.png)

```python
def painters_partition(boards, painters):
    # Step 1: Validate the input.
    if not boards or painters <= 0:
        return -1

    def painters_needed(time_limit):
        # Step 2: Start assigning boards to the first painter.
        used = 1
        current_work = 0

        # Step 3: Assign boards in contiguous order.
        for board in boards:
            # Step 4: Keep the board with the current painter
            # if the total work stays within time_limit.
            if current_work + board <= time_limit:
                current_work += board

            # Step 5: Otherwise, assign this board to a new painter.
            else:
                used += 1
                current_work = board

        # Step 6: Return the painters required for this limit.
        return used

    # Step 7: No valid answer can be below the largest board.
    low = max(boards)

    # Step 8: One painter doing all work gives the upper bound.
    high = sum(boards)
    answer = high

    # Step 9: Binary-search for the minimum feasible maximum workload.
    while low <= high:
        time_limit = (low + high) // 2

        # Step 10: If the work fits within the available painters,
        # save the limit and try a smaller one.
        if painters_needed(time_limit) <= painters:
            answer = time_limit
            high = time_limit - 1

        # Step 11: Otherwise, increase the time limit.
        else:
            low = time_limit + 1

    # Step 12: Return the minimum possible maximum painting time.
    return answer
```
