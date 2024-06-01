from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

"""
Grid = [
    [1,2],
    [3,4]
]

consecutive increasing numbers sequence of length >= 2:
[1,2]
[1,2,4]
[1,3]
[1,3,4]
[2,4]
[3,4]
so the answer is 6
"""

def find_increasing_sequences(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    result = []
    res_count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, path):
        nonlocal res_count
        if len(path) > 1:
            result.append(path.copy())
            res_count += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and grid[nx][ny] > grid[x][y]:
                path.append(grid[nx][ny])
                dfs(nx, ny, path)
                path.pop()

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, [grid[i][j]])

    return result, res_count

# Define the grid
grid = [
    [1, 2],
    [3, 4]
]

# Find all increasing sequences
sequences = find_increasing_sequences(grid)
print("Found sequences:", sequences[1])
# print("Number of sequences:", len(sequences))
