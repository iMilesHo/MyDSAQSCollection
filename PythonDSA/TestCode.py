from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        from collections import deque        

        for i in range(rows):
            for j in range(cols):
                queue = deque()
                seen = set()
                queue.append((i,j,0))
                while len(queue) > 0: 
                    print("queue", queue)
                    r, c, idx = queue.popleft() 
                    if not (idx < len(word) and 0 <= r < rows and 0 <=c < cols and board[r][c] == word[idx]):
                        continue
                    if idx == len(word) - 1: 
                        return True
                    seen.add((r,c,idx)) 
                    print("seen", seen)
                    if 0 <= r + 1 < rows and 0 <= c < cols and (r+1, c, idx+1) not in seen:
                        queue.append((r+1, c, idx+1))
                    if 0 <= r < rows and 0 <= c + 1 < cols and (r, c+1, idx+1) not in seen:
                        queue.append((r, c+1, idx+1))
                    if 0 <= r - 1 < rows and 0 <= c < cols and (r-1, c, idx+1) not in seen:
                        queue.append((r-1, c, idx+1))
                    if 0 <= r < rows and 0 <= c - 1 < cols and (r, c-1, idx+1) not in seen:
                        queue.append((r, c-1, idx+1))
        return False

board = [["a","a"]]
word = "aaa"

sol = Solution()
print(sol.exist(board, word))

"""
[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
ABCESEEEFS
"""