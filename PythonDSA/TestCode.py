from typing import List
from traitlets import Int


"""
1 2 3 4
5 1 2 3
6 5 1 2
7 6 5 1
"""
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


# Test
solution = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[6,5,1,2],[7,6,5,1]]
print(solution.isToeplitzMatrix(matrix))  # True

matrix = [[11,74,0,93],[40,11,74,7]]
print(solution.isToeplitzMatrix(matrix))  # False