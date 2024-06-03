from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        explore_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        path = set()
        ROWS, COLS = len(board), len(board[0])

        def valide(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, idx):
            if idx == len(word) - 1:
                return True
            
            flag = False
            for (ar, ac) in explore_dir:
                nr, nc = r + ar, c + ac
                print(path)
                if valide(nr,nc) and (nr,nc) not in path and board[nr][nc] == word[idx+1]:
                    path.add((nr,nc))
                    flag = dfs(nr,nc,idx+1)
                    path.remove((nr,nc))
            
            return flag
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    path.add((i,j))
                    if dfs(i,j,0):
                        return True
                    path.remove((i,j))
        return False




