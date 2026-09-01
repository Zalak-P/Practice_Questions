# Array and Math Problems — Java Notes

---

## 1. Two Sum

[LeetCode 1](https://leetcode.com/problems/two-sum/)

![Two Sum dry run](images/TwoSum.png)

```java
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;

            if (hashmap.containsKey(diff)) {
                return new int[]{hashmap.get(diff), i};
            }

            hashmap.put(num, i);
        }

        return new int[]{};
    }
}
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 2. 3Sum

[LeetCode 15](https://leetcode.com/problems/3sum/)

![3Sum dry run](images/ThreeSum.png)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) {
                break;
            }

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];

                if (total == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;

                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }

                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }

                else if (total < 0) {
                    left++;
                }

                else {
                    right--;
                }
            }
        }

        return result;
    }
}
```

**Time:** `O(n²)`  
**Space:** `O(1)` excluding the output and sorting space

---

## 3. Container With Most Water

[LeetCode 11](https://leetcode.com/problems/container-with-most-water/)

![Container With Most Water dry run](images/ContainerWithMostWater.png)

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int currentArea = Math.min(height[left], height[right]) * width;

            maxArea = Math.max(maxArea, currentArea);

            if (height[left] < height[right]) {
                left++;
            }

            else {
                right--;
            }
        }

        return maxArea;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 4. Sort Colors

[LeetCode 75](https://leetcode.com/problems/sort-colors/)

![Sort Colors dry run](images/SortColors.png)

```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;

                low++;
                mid++;
            }

            else if (nums[mid] == 1) {
                mid++;
            }

            else {
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;

                high--;
            }
        }
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 5. Product of Array Except Self

[LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/)

![Product of Array Except Self dry run](images/ProductOfArrayExceptSelf.png)

```java
import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);

        int prefix = 1;

        for (int i = 0; i < nums.length; i++) {
            answer[i] = prefix;
            prefix *= nums[i];
        }

        int suffix = 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }

        return answer;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)` excluding the output array

---

## 6. Next Permutation

[LeetCode 31](https://leetcode.com/problems/next-permutation/)

![Next Permutation dry run](images/NextPermutation.png)

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int pivot = nums.length - 2;

        while (pivot >= 0 && nums[pivot] >= nums[pivot + 1]) {
            pivot--;
        }

        if (pivot >= 0) {
            int successor = nums.length - 1;

            while (nums[successor] <= nums[pivot]) {
                successor--;
            }

            int temp = nums[pivot];
            nums[pivot] = nums[successor];
            nums[successor] = temp;
        }

        int left = pivot + 1;
        int right = nums.length - 1;

        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;

            left++;
            right--;
        }
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 7. Majority Element

[LeetCode 169](https://leetcode.com/problems/majority-element/)

![Majority Element dry run](images/MajorityElement.png)

```java
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }

            if (num == candidate) {
                count++;
            }

            else {
                count--;
            }
        }

        return candidate;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

## 8. Find Missing and Repeating Number

![Find Missing and Repeating Number dry run](images/FindMissingRepeating.png)

```java
class Solution {
    public int[] findMissingRepeating(int[] nums) {
        int repeating = -1;
        int missing = -1;

        for (int num : nums) {
            int index = Math.abs(num) - 1;

            if (nums[index] < 0) {
                repeating = Math.abs(num);
            }

            else {
                nums[index] *= -1;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missing = i + 1;
                break;
            }
        }

        return new int[]{repeating, missing};
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`

> This solution modifies the input array.

---

## 9. Pow(x, n)

[LeetCode 50](https://leetcode.com/problems/powx-n/)

![Pow(x, n) dry run](images/PowXN.png)

```java
class Solution {
    public double myPow(double x, int n) {
        long exponent = n;

        if (exponent < 0) {
            x = 1 / x;
            exponent = -exponent;
        }

        double result = 1.0;

        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result *= x;
            }

            x *= x;
            exponent /= 2;
        }

        return result;
    }
}
```

**Time:** `O(log |n|)`  
**Space:** `O(1)`

---

## 10. Sqrt(x)

[LeetCode 69](https://leetcode.com/problems/sqrtx/)

![Sqrt(x) dry run](images/SqrtX.png)

```java
class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 1;
        int right = x;
        int answer = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long square = (long) mid * mid;

            if (square == x) {
                return mid;
            }

            if (square < x) {
                answer = mid;
                left = mid + 1;
            }

            else {
                right = mid - 1;
            }
        }

        return answer;
    }
}
```

**Time:** `O(log x)`  
**Space:** `O(1)`

---

## 11. Maximum Subarray

[LeetCode 53](https://leetcode.com/problems/maximum-subarray/)

![Maximum Subarray dry run](images/MaximumSubarray.png)

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
```

**Time:** `O(n)`  
**Space:** `O(1)`
