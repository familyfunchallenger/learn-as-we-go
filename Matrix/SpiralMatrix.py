"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

from typing import List


class Solution:
    def _initExtraMatrix(
            self, num_rows: int, num_colums: int) -> List[List[bool]]:
        extra_matrix = []
        extra_matrix.append([True] * num_colums)
        extra_matrix.extend([ [False] * num_colums for _ in range(num_rows - 2)])
        extra_matrix.append([True] * num_colums)
        i = 0
        while i < num_rows:
            extra_matrix[i][0] = True
            extra_matrix[i][num_colums - 1] = True
            i += 1
        return extra_matrix
    
    def _isDoneAt(self, visited: List[List[bool]], i: int, j: int) -> bool:
        # i and j are the coordinates in the original matrix, to check within the visited matrix, we need to increase i and j by 1 respectively
        i += 1
        j += 1
        return visited[i - 1][j] and visited[i + 1][j] and visited[
            i][j - 1] and visited[i][j + 1] 

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        The directions to traverse a m*n matrix is a loop of [Right, Down, Left, Up].

        The traverse starts at [0, 0] with direction Right.

        Conditions where the next move shall change direction:
        * Reaches the boundary of the matrix
          * Reaches the column (n - 1)
          * Reaches the row (m - 1)
          * If continues at current direct, the next element has been visited already

        How to decide which direction the next move shall take:
        * current direction is Right, after finishing this move, 
          * the position on the right is already visited (or not visitable), change direction to Down
        * current direction is Down, after finishing this move,
          * the position below is already visited (or not visitable), change direction to Left
        * current direction is Left, after finishing this move,
          * the position on the left is already visited (or not visitable), change direction to Up
        * current direction is Up, after finishing this move,
          * the poistion above is already visited, change direction to Right

        Condition to end the traverse:
        All positions around (up, down, left, right) have been visited already

        Extra matrix to remember if a position is visited: a (m + 2) * (n + 2) matrix where row 0, row m + 1, column 0, column n + 1 are all initilized to "visited"/True while other positions are initialized as False/"not visited".
        """
        ret = []
        num_rows = len(matrix)
        num_columns = len(matrix[0])
        right = 1
        down = 2
        left = 3
        up = 4
        current_direction = right
        i = 0
        j = 0
        visited = self._initExtraMatrix(num_rows + 2, num_columns + 2)
        
        while not self._isDoneAt(visited, i, j):
            # mark current position visited
            ret.append(matrix[i][j])
            visited[i + 1][j + 1] = True
            print('[i, j] - ', i, ' , ', j)
            if current_direction == right:
                if visited[i + 1][j + 2]:
                    current_direction = down
                    i += 1
                else:
                    j += 1
            elif current_direction == down:
                if visited[i + 2][j + 1]:
                    current_direction = left
                    j -= 1
                else:
                    i += 1
            elif current_direction == left:
                if visited[i + 1][j]:
                    current_direction = up
                    i -= 1
                else:
                    j -= 1
            elif current_direction == up:
                if visited[i][j + 1]:
                    current_direction = right
                    j += 1
                else:
                    i -= 1
            else:
                print("something is wrong.")
        ret.append(matrix[i][j])
        return ret
    

s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))