#  74. Search a 2D Matrix
36_74_search_a_2d_matrix.md

## Solution
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n * m - 1
        mid = int((left + right) / 2)

        while left <= right:
            h_target = matrix[int(mid/n)][mid%n]
            if h_target == target:
                return True
            elif h_target < target:
                left = mid + 1
                mid = int((left + right) / 2)
            else:
                right = mid - 1
                mid = int((left + right) / 2)
        return False
```
