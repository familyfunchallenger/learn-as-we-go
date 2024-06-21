"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note: --> This is important

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


from typing import List


class Solution:
    
    def _isSubmatrixValid(self, board: List[List[str]], start: int) -> bool:
        ret = True
        i = start
        j = start
        digits = []
        while i < start + 3:
            print('i - ', i)
            while j < start + 3:
                print('j - ', j)
                if board[i][j].isnumeric():
                    if board[i][j] not in digits:
                        digits.append(board[i][j])
                    else:
                        print('submatrix - start - i - j - c - digits -result - ',
                               start, i, j, board[i][j], digits, False)
                        return False
                j += 1
            i += 1
        return ret
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ret = True
        # Three rules:
        # 1. every row shall not have repeated digits
        for row in board:
            # check if there is repeated digits
            digits = []
            for c in row:
                if c.isnumeric():
                    if c not in digits:
                        digits.append(c)
                    else:
                        print('row - result', row, False)
                        return False
        # 2. every column shall not have repeated digits
        column = 0
        while column < len(board): # assuming it is guaranteed to be a nxn matrix
            digits_in_column = []
            for row in board:
                if row[column].isnumeric():
                    if row[column] not in digits_in_column:
                        digits_in_column.append(row[column])
                    else:
                        print('column - result - ', column, False)
                        return False
            column += 1
        # 3. each of the 9 3x3 sub-matrix shall not have repeated digits
        i = 0
        while i < 3:
            ret = ret and self._isSubmatrixValid(board, i * 3)
            if not ret:
                return False
            i += 1
        return ret
    

s = Solution()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))
