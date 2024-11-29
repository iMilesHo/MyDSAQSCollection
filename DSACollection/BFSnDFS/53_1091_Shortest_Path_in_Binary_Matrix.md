# 1091. Shortest Path in Binary Matrix

file name: 1091_Shortest_Path_in_Binary_Matrix.md

## My solution

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        from collections import deque
        Rows = len(grid) # 3
        Columns = len(grid[0]) # 4
        sr,sc,tr,tc = 0, 0, Rows - 1, Columns - 1
        bfs_queue = deque()
        bfs_queue.append((sr,sc,1)) # [(0,0,1)]
        seen = set()
        seen.add((sr,sc)) # {(0, 0)}

        while len(bfs_queue) > 0:
            r, c, depth = bfs_queue.popleft()
            if r == tr and c == tc:
                return depth
            for (i_r, i_c) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1,c+1), (r-1,c+1), (r+1,c-1),(r-1,c-1)]: # [(1, 0), (-1, 0), (0, 1), (0, -1)]
                if 0 <= i_r < Rows and 0 <= i_c < Columns and grid[i_r][i_c] == 0 and (i_r, i_c) not in seen:
                    bfs_queue.append((i_r, i_c, depth+1))
                    seen.add((i_r, i_c))
        return -1
```

## Notes:

- breadth first search (BFS) algorithm
