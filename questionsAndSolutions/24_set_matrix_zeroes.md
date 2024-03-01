# 73. Set Matrix Zeroes


## constraints:
- do it in place
- m, n: [1, 200]
- value of element: 32-bit integer

## ideas:
- two sets, to store which row and column needed to be set into 0
- if the row and column is already encoencountered, which is in these two sets, we do not need to set it again
- if not, we set it

## test cases:
- 


## Python Solution

### My Method

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_zeros = set()
        column_zeros = set()

        for row_i in range(len(matrix)):
            for column_i in range(len(matrix[0])):
                if matrix[row_i][column_i] == 0:
                    rows_zeros.add(row_i)
                    column_zeros.add(column_i)
        for row_i in range(len(matrix)):
            for column_i in range(len(matrix[0])):
                if row_i in rows_zeros or column_i in column_zeros:
                    matrix[row_i][column_i] = 0
```

### Method 1: Using two lists

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_zeros = [False] * len(matrix)
        column_zeros = [False] * len(matrix[0])

        for row_i in range(len(matrix)):
            for column_i in range(len(matrix[0])):
                if matrix[row_i][column_i] == 0:
                    rows_zeros[row_i] = True
                    column_zeros[column_i] = True
        for row_i in range(len(matrix)):
            for column_i in range(len(matrix[0])):
                if rows_zeros[row_i] or column_zeros[column_i]:
                    matrix[row_i][column_i] = 0
```

### Method 2: Using first row and first column as the flags

```python
