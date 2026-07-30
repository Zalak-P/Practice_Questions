![alt text](image-4.png)

# Set Matrix Zeroes (LeetCode 73)

**Code Trick:** Use the first row and first column as markers.

```python

class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRowZero = True

        # Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                firstColZero = True

        # Mark rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeroes
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero first row
        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero first column
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0
```

## Complexity

- **Time:** `O(m × n)`
- **Space:** `O(1)`
