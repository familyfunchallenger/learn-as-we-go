"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Example 1:
Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [
    ["X"]]
Output: [
    ["X"]]

 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

From chatGPT:
Approach:
Identify Border-Connected 'O's:

Traverse the border of the board and use DFS/BFS to mark all 'O's that are connected to the border.
Mark these cells temporarily with a different character (e.g., 'E' for "escape") to distinguish them from the surrounded 'O's.
Replace Remaining 'O's:

Traverse the entire board again.
Replace all 'O' cells with 'X' (these are the surrounded regions).
Replace all 'E' cells back to 'O' (these were connected to the border and should not be captured).

"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
    
        rows, cols = len(board), len(board[0])
        
        def dfs(board, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = 'E'  # Mark this cell as escaped
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)
        
        # Step 1: Mark all 'O's connected to the border as 'E'
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and board[i][j] == 'O':
                    dfs(board, i, j)
        
        # Step 2: Replace all 'O' with 'X' and 'E' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'


s = Solution()

board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

s.solve(board)
print(board)

board = [
    ["X"]]
