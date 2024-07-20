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