class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # строки — идёшь по board[i]
        for i in range(9):
            row = [board[i][j] for j in range(9)]
            nums = [x for x in row if x != '.']
            if len(nums) != len(set(nums)):
                return False

        # колонки — идёшь по board[j][i]
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            nums = [x for x in col if x != '.']
            if len(nums) != len(set(nums)):
                return False

        # блоки 3x3 — вот хитрость:
        for box_row in range(3):
            for box_col in range(3):
                box = [board[box_row*3 + i][box_col*3 + j] 
                    for i in range(3) 
                    for j in range(3)]
                
                nums = [x for x in box if x != '.']
                if len(nums) != len(set(nums)):
                    return False

        return True