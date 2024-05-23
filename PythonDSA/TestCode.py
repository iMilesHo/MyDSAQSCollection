from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

def shortestCellPath(grid, sr, sc, tr, tc):
  from collections import deque
  Rows = len(grid) # 3
  Columns = len(grid[0]) # 4
  bfs_queue = deque() 
  bfs_queue.append((sr,sc,0)) # [(0,0,0)]
  seen = set()
  seen.add((sr,sc)) # {(0, 0)}
  
  while len(bfs_queue) > 0:
    r, c, depth = bfs_queue.popleft()
    if r == tr and c == tc:
      return depth
    for (i_r, i_c) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]: # [(1, 0), (-1, 0), (0, 1), (0, -1)]
      if 0 <= i_r < Rows and 0 <= i_c < Columns and grid[i_r][i_c] == 1 and (i_r, i_c) not in seen:
        bfs_queue.append((i_r, i_c, depth+1))
  return -1

    

"""
[
[1, 1, 1, 1], 
[0, 0, 0, 1], 
[1, 1, 1, 1]
]
"""

# test
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print(shortestCellPath(grid, sr, sc, tr, tc)) # 8