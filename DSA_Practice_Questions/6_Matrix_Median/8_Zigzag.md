```python
from typing import List

class Solution:
    def zigzagTraversal(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        for i in range(rows):

            # Even row -> Left to Right
            if i % 2 == 0:
                for j in range(cols):
                    result.append(matrix[i][j])

            # Odd row -> Right to Left
            else:
                for j in range(cols - 1, -1, -1):
                    result.append(matrix[i][j])

        return result
```

### Complexity

- **Time:** `O(m × n)`
- **Space:** `O(1)` *(excluding output array)*

### Code Trick

- Even row → `range(cols)`
- Odd row → `range(cols - 1, -1, -1)`