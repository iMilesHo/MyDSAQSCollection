# 766. Toeplitz Matrix

## My solution

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return False

        width, height = len(matrix[0]), len(matrix)
        if width == 1 or height == 1:
            return True

        # horizontal (first row)
        for i in range(width):
            row, col = 0, i
            while row < height and col < width:
                if matrix[0][i] != matrix[row][col]:
                    return False
                row += 1
                col += 1

        # vertical (first collumn)
        for j in range(1, height):
            row, col = j, 0
            while row < height and col < width:
                if matrix[j][0] != matrix[row][col]:
                    return False
                row += 1
                col += 1
        return True
```

## Optimized solution

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(columns):
                if r!=0 and c!=0 and matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True
```
