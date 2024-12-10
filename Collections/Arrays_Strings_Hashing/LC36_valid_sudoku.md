# 36. Valid Sudoku

## Python Solution

### My Solution

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets_list = [set() for _ in range(9)]
        col_sets_list = [set() for _ in range(9)]
        sub3t3_sets_list = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                temp = board[i][j]
                if temp == ".":
                    continue
                if temp not in row_sets_list[i]:
                    row_sets_list[i].add(temp)
                else:
                    return False
                if temp not in col_sets_list[j]:
                    col_sets_list[j].add(temp)
                else:
                    return False
                
                sub_3t3_index = int(i/3)*3 + int(j/3)
                if temp not in sub3t3_sets_list[sub_3t3_index]:
                    sub3t3_sets_list[sub_3t3_index].add(temp)
                else:
                    return False
        return True
```

### Leetcode Solution

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range (9):
                if board[r][c] == ".":
                    continue
                if (board [r][c] in rows [r] or
                    board [r][c] in cols [c] or
                    board [r][c] in squares [(r // 3, c //3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares [(r//3, c//3)].add(board[r][c])
        return True
                    
```


## Notes
```python
test_repeat_initialize_1 = [set()] * 9
test_repeat_initialize_2 = [set() for _ in range(9)]

for i in range(9):
    test_repeat_initialize_1[i].add(i)
    test_repeat_initialize_2[i].add(i)
print(test_repeat_initialize_1) 
print(test_repeat_initialize_2) 
# [{0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 3, 4, 5, 6, 7, 8}]
# [{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}]
```