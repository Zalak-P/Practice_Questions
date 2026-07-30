![alt text](image.png)

# Rule to Remember

```python
row = index // number_of_columns
col = index % number_of_columns
```

# Search in a 2D Sorted Matrix (LeetCode 74)

## Python Code

```python
class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            # Step 1: Find the middle index
            mid = (left + right) // 2

            # Step 2: Convert 1D index to 2D position
            row = mid // cols
            col = mid % cols

            # Step 3: Compare
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1      # Search right half

            else:
                right = mid - 1     # Search left half

        return False
```
