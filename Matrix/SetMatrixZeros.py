"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(m*n) space is probably a bad idea.
# O(m * n) ==> use another matrix to store the result
A simple improvement uses O(m + n) space, but still not the best solution.
# O(m + n) ==> use two arrays, one for rows and the other for columns to store which rows/columns to mark as zeors
Could you devise a constant space solution?
# O(1) ==> mark the rows/columns as something out of the valid range, e.g. 231

"""

from typing import List

class Solution:
    
    def _setValue(self, matrix: List[List[int]],
                   row: int, column: int, val: int) -> None:
        # If an item is already zero, do not change it
        # First set the row
        i = 0
        while i < len(matrix[0]):
            if matrix[row][i] != 0:
                matrix[row][i] = val 
            i += 1
        # Now set the column
        i = 0
        while i < len(matrix):
            if matrix[i][column] != 0:
                matrix[i][column] = val
            i += 1
        print('matrix after finding a zero - ', matrix)
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        j = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                print('[i, j] - ', i, '-', j, ':', matrix[i][j])
                if matrix[i][j] == 0:
                    # mark row i and column j as special values
                    print('find a zero')
                    self._setValue(matrix, i, j, 231)
                j += 1
            i += 1
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == 231:
                    # mark row i and column j as special values
                    matrix[i][j] = 0
                j += 1
            i += 1
        print(matrix)
        return
    

s = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)