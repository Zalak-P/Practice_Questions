![alt text](image-4.png)

Set Matrix Zeroes

Code Trick: Use the first row and first column as markers.

class Solution:
def setZeroes(self, matrix: List[List[int]]) -> None:
rows = len(matrix)
cols = len(matrix[0])

        firstRowZero = any(matrix[0][j] == 0 for j in range(cols))
        firstColZero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows and columns using the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Apply markers to the inner matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Update the first row
        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        # Update the first column
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0
