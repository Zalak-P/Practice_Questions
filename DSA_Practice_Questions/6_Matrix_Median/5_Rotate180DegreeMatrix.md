![alt text](image-2.png)

# Matrix Rotation - 180° (Python)

```python
class Solution:
    def rotate180(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n):

                ni = n - 1 - i
                nj = n - 1 - j

                if (i < ni) or (i == ni and j < nj):
                    matrix[i][j], matrix[ni][nj] = matrix[ni][nj], matrix[i][j]

        return matrix
```
