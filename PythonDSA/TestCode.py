from typing import List
from traitlets import Int

def findInMonotonic(matrix: List[List[Int]], k: Int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0

    while row >= 0 and col < cols:
        if matrix[row][col] == k:
            return True
        elif matrix[row][col] > k:
            row -= 1
        else:
            col += 1
    return False

matrix = [[1, 2, 3], 
          [4, 6, 7], 
          [5, 8, 9]]
print(findInMonotonic(matrix, 6))  # True