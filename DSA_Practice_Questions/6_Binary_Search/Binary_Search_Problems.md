# Binary Search Problems — Python Notes

---

## 1. Lower and Upper Bound

![Lower and Upper Bound dry run](images/01_lower_upper_bound.png)

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

![Search in an infinitely long sorted array dry run](images/02_infinite_sorted_array.png)

The following implementation uses a regular Python list to simulate the infinite-array problem. It first expands the search range exponentially and then applies binary search.

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

![The N-th root of an integer dry run](images/03_nth_root.png)

> **Correction to the image:** `531441 = 9⁶`, so for `n = 6` and `m = 531441`, the correct integer root is **9**, not 3.

```python
def compare_power(base, exponent, target):
    # Step 1: Start the multiplication result at 1.
    product = 1

    # Step 2: Multiply base exactly exponent times.
    for _ in range(exponent):
        # Step 3: Stop early when the next multiplication
        # would make the result greater than target.
        if product > target // base:
            return 1

        product *= base

    # Step 4: Report whether base ** exponent equals target.
    if product == target:
        return 0

    # Step 5: The calculated power is smaller than target.
    return -1


def integer_nth_root(n, m):
    # Step 1: Validate the input.
    if n <= 0 or m < 0:
        raise ValueError("n must be positive and m must be non-negative")

    # Step 2: Handle values whose answer is immediate.
    if m in (0, 1) or n == 1:
        return m

    # Step 3: Search for the root in the answer range [1, m].
    low = 1
    high = m

    # Step 4: Apply binary search.
    while low <= high:
        mid = (low + high) // 2

        # Step 5: Compare mid ** n with m safely.
        comparison = compare_power(mid, n, m)

        # Step 6: Exact power found.
        if comparison == 0:
            return mid

        # Step 7: mid ** n is too small, so try larger values.
        if comparison < 0:
            low = mid + 1

        # Step 8: mid ** n is too large, so try smaller values.
        else:
            high = mid - 1

    # Step 9: No exact integer N-th root exists.
    return -1
```

---

## 4. Square Root of an Integer

![Square root of an integer dry run](images/04_integer_square_root.png)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Step 1: Handle the smallest values directly.
        if x < 2:
            return x

        # Step 2: Initialize the answer search range.
        # For x >= 2, floor(sqrt(x)) cannot exceed x // 2.
        low = 1
        high = x // 2
        answer = 1

        # Step 3: Binary-search for the greatest valid integer.
        while low <= high:
            # Step 4: Calculate the middle candidate.
            mid = (low + high) // 2

            # Step 5: Check whether mid * mid <= x.
            # Using mid <= x // mid avoids overflow.
            if mid <= x // mid:
                # Step 6: mid is valid; save it and try a larger value.
                answer = mid
                low = mid + 1

            else:
                # Step 7: mid is too large; search the left half.
                high = mid - 1

        # Step 8: Return the greatest valid integer square root.
        return answer
```

---

## 5. Search in a Sorted and Rotated Array

![Search in a sorted and rotated array dry run](images/05_search_rotated_array.png)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Step 1: Initialize the binary-search range.
        low = 0
        high = len(nums) - 1

        # Step 2: Search while a valid range exists.
        while low <= high:
            # Step 3: Find the middle index.
            mid = (low + high) // 2

            # Step 4: Return immediately when target is found.
            if nums[mid] == target:
                return mid

            # Step 5: Check whether the left half is sorted.
            if nums[low] <= nums[mid]:
                # Step 6: If target lies inside the sorted left half,
                # discard the right half.
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Step 7: Otherwise, search the right half.
                else:
                    low = mid + 1

            # Step 8: Otherwise, the right half is sorted.
            else:
                # Step 9: If target lies inside the sorted right half,
                # discard the left half.
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # Step 10: Otherwise, search the left half.
                else:
                    high = mid - 1

        # Step 11: Target is not present.
        return -1
```

---

## 6. Find Peak Element

![Find peak element dry run](images/06_find_peak.png)

```python
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Step 1: Initialize the binary-search range.
        low = 0
        high = len(nums) - 1

        # Step 2: Continue until only one candidate remains.
        while low < high:
            # Step 3: Find the middle index.
            mid = (low + high) // 2

            # Step 4: If the slope rises from mid to mid + 1,
            # a peak must exist on the right side.
            if nums[mid] < nums[mid + 1]:
                low = mid + 1

            # Step 5: Otherwise, a peak exists at mid or to its left.
            else:
                high = mid

        # Step 6: low == high, so this index is a peak.
        return low
```

---

## 7. Find First and Last Position

![Find first and last position dry run](images/07_first_last_position.png)

```python
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first():
            # Step 1: Initialize the search range and default answer.
            low = 0
            high = len(nums) - 1
            answer = -1

            # Step 2: Run binary search.
            while low <= high:
                mid = (low + high) // 2

                # Step 3: When nums[mid] is target or larger,
                # continue searching toward the left.
                if nums[mid] >= target:
                    # Step 4: Store mid when target is found,
                    # but do not stop because an earlier copy may exist.
                    if nums[mid] == target:
                        answer = mid

                    high = mid - 1

                # Step 5: nums[mid] is smaller than target,
                # so move to the right half.
                else:
                    low = mid + 1

            # Step 6: Return the leftmost target index.
            return answer

        def find_last():
            # Step 1: Initialize the search range and default answer.
            low = 0
            high = len(nums) - 1
            answer = -1

            # Step 2: Run binary search.
            while low <= high:
                mid = (low + high) // 2

                # Step 3: When nums[mid] is target or smaller,
                # continue searching toward the right.
                if nums[mid] <= target:
                    # Step 4: Store mid when target is found,
                    # but continue because a later copy may exist.
                    if nums[mid] == target:
                        answer = mid

                    low = mid + 1

                # Step 5: nums[mid] is larger than target,
                # so move to the left half.
                else:
                    high = mid - 1

            # Step 6: Return the rightmost target index.
            return answer

        # Step 7: Run both searches and return the required range.
        return [find_first(), find_last()]
```

---

## 8. Find Minimum in a Rotated Sorted Array

![Find minimum in a rotated sorted array dry run](images/08_find_minimum_rotated.png)

This version also handles duplicate values. With distinct values, the time complexity is `O(log n)`. With many duplicates, the worst case can become `O(n)`.

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Step 1: Validate the input.
        if not nums:
            raise ValueError("nums must not be empty")

        # Step 2: Initialize the binary-search range.
        low = 0
        high = len(nums) - 1

        # Step 3: Continue until one minimum candidate remains.
        while low < high:
            # Step 4: Find the middle index.
            mid = (low + high) // 2

            # Step 5: If nums[mid] is smaller than nums[high],
            # the minimum is at mid or somewhere to its left.
            if nums[mid] < nums[high]:
                high = mid

            # Step 6: If nums[mid] is greater than nums[high],
            # the rotation point must be to the right of mid.
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

![Koko Eating Bananas dry run](images/09_koko_bananas.png)

> **Correction to the image:** for speed `k = 12`, the total time is **12 hours**, not 11. The final minimum speed of **12 bananas/hour** is correct.

```python
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Step 1: The minimum possible speed is 1.
        low = 1

        # Step 2: The maximum required speed is the largest pile.
        high = max(piles)
        answer = high

        # Step 3: Binary-search for the minimum feasible speed.
        while low <= high:
            # Step 4: Choose a candidate eating speed.
            speed = (low + high) // 2

            # Step 5: Calculate the total hours needed at this speed.
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed

            # Step 6: If Koko finishes within h hours,
            # save the speed and try a smaller one.
            if hours <= h:
                answer = speed
                high = speed - 1

            # Step 7: Otherwise, the speed is too slow.
            else:
                low = speed + 1

        # Step 8: Return the smallest feasible eating speed.
        return answer
```

---

## 10. Allocation of Minimum Number of Pages

![Allocation of minimum number of pages dry run](images/10_allocate_pages.png)

> **Correction to the image:** for books  
> `[12, 34, 67, 90, 26, 45, 89, 23, 11, 65]` and `4` students, the correct minimum possible maximum is **134**, not 113.  
> One optimal allocation is `[12,34,67] | [90,26] | [45,89] | [23,11,65]`.

```python
def allocate_minimum_pages(books, students):
    # Step 1: Validate the input.
    if not books or students <= 0 or students > len(books):
        return -1

    def students_needed(page_limit):
        # Step 2: Start by assigning books to the first student.
        used = 1
        current_pages = 0

        # Step 3: Allocate books in their original contiguous order.
        for pages in books:
            # Step 4: Keep the book with the current student
            # when it does not exceed the page limit.
            if current_pages + pages <= page_limit:
                current_pages += pages

            # Step 5: Otherwise, start allocation for a new student.
            else:
                used += 1
                current_pages = pages

        # Step 6: Return how many students this limit requires.
        return used

    # Step 7: The answer cannot be smaller than the largest book.
    low = max(books)

    # Step 8: One student reading every book gives the upper bound.
    high = sum(books)
    answer = high

    # Step 9: Binary-search for the minimum feasible page limit.
    while low <= high:
        page_limit = (low + high) // 2

        # Step 10: If the allocation uses at most the available students,
        # save the limit and try a smaller maximum.
        if students_needed(page_limit) <= students:
            answer = page_limit
            high = page_limit - 1

        # Step 11: Otherwise, increase the allowed page limit.
        else:
            low = page_limit + 1

    # Step 12: Return the minimum possible maximum pages.
    return answer
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
