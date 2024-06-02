from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque



"""
grid = [
        [1,2],
        [3,4]
    ]
possible path:
[1,2]
[1,2,4]
[1,3]
[1,3,4]
[2,4]
[3,4]
"""
def find_increasing_sequences(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    # explore direction
    explore_dir = [(1,0), (-1,0), (0,1), (0,-1)]
    res = 0

    def exploreable(r,c):
        return 0 <= r < ROWS and 0 <= c < COLS

    def dfs(r, c, psn): # 1, 1, 3
        nonlocal res
        if psn >= 2: 
            res += 1 # 2
        for ar, ac in explore_dir:
            nr, nc = r+ar,c+ac # 
            if exploreable(nr, nc) and grid[nr][nc] > grid[r][c]:
                dfs(nr,nc,psn+1) # 1, 1, 3
        return
    for i in range(ROWS):
        for j in range(COLS):
            dfs(i, j, 1)
    return res



# Define the grid
grid = [
    [1, 2],
    [3, 4]
]

# Find all increasing sequences
print("Found sequences:", find_increasing_sequences(grid))

