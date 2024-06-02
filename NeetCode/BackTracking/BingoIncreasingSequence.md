# Bingo Increasing Sequence

## Problem Statement

Given a 2D grid of size m x n. You need to find the number of strictly increasing sequences of consecutive numbers in the grid. The sequence should have length >= 2. The sequence should be increasing in row-wise or column-wise in the grid.

## Example

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

the output should be 6

## Solution

### Record the increasing sequences

```python
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
```

### Just count the increasing sequences

Notes: so this is just a dfs search, no backtracking is needed

```python
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
```
