# 90° Clockwise
# Step 1: Transpose
# Step 2: Reverse each row

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()

        return matrix

# 90° Counter-Clockwise
# Step 1: Transpose
# Step 2: Reverse each column

class Solution:
    def rotateCounterClockwise(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each column
        for col in range(n):
            top = 0
            bottom = n - 1

            while top < bottom:
                matrix[top][col], matrix[bottom][col] = (
                    matrix[bottom][col],
                    matrix[top][col],
                )
                top += 1
                bottom -= 1

        return matrix