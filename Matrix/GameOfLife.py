"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
Answer: need to know the number of neighbors as well as its previous value. Number of neibours is the sum of 'live' cells. The previous value could be represented by '+' and '-' signs, i.e. if the value updated afterwards is positive, it means it was 1 otherwise it was 0 

In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

"""


from typing import List


class Solution:
    def _originalValue(self, i: int) -> int:
        if i > 0:
            return 1
        return 0
    
    def _numOfLiveNeighbors(
            self, board: List[List[int]], i: int, j: int) -> int:
        num_of_live_neighbors = 0 
        # up left
        if i > 0 and j > 0:
            num_of_live_neighbors += self._originalValue(board[i - 1][j - 1])
        # up
        if i > 0:
            num_of_live_neighbors += self._originalValue(board[i - 1][j])
        # up right
        if i > 0 and j < len(board[i]) - 1:
            num_of_live_neighbors += self._originalValue(board[i - 1][j + 1])
        # left
        if j > 0:
            num_of_live_neighbors += self._originalValue(board[i][j - 1])
        # right
        if j < len(board[i]) - 1:
            num_of_live_neighbors += self._originalValue(board[i][j + 1])
        # down left
        if i < len(board) - 1 and j > 0:
            num_of_live_neighbors += self._originalValue(board[i + 1][j - 1])
        # down right
        if i < len(board) - 1 and j < len(board[i]) - 1:
            num_of_live_neighbors += self._originalValue(board[i + 1][j + 1])
        # down
        if i < (len(board)) - 1:
            num_of_live_neighbors += self._originalValue(board[i + 1][j])
        # print('i - j - neighobrs : ', i, ' - ', j, ' - ', num_of_live_neighbors)
        return num_of_live_neighbors
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # First pass to mark the to-be ones
        for i in (range(0, len(board))):
            for j in (range(0, len(board[i]))):
                num_of_neighbors = self._numOfLiveNeighbors(board, i, j)
                if board[i][j] == 1:
                    board[i][j] = num_of_neighbors
                else:
                    board[i][j] = -num_of_neighbors
                
        # Second pass to change the marked ones to 0 or 1 respectively
        for i in (range(0, len(board))):
            for j in (range(0, len(board[i]))):
                val = board[i][j]
                if val > 0 and val < 2:
                    board[i][j] = 0
                elif val == 2 or val == 3:
                    board[i][j] = 1
                elif val > 3:
                    board[i][j] = 0
                elif val < 0 and abs(val) == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        print(board)
        

s = Solution()

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)

board = [[1,1],[1,0]]
s.gameOfLife(board)