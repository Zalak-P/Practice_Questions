![alt text](image-2.png)

# Matrix Rotation - 180° (Python)

```python
class Solution:
    def rotate180(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n):

                newrow = n - 1 - i
                newcol = n - 1 - j

                if (i < newrow) or (i == newrow and j < newcol):
                    matrix[i][j], matrix[newrow][newcol] = matrix[newrow][newcol], matrix[i][j]

        return matrix
```
