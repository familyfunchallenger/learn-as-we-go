"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


chatGPT provides a DFS based solution

def numIslands(grid):
    if not grid:
        return 0

    def dfs(grid, i, j):
        # If out of bounds or at a water cell, return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        # Mark the cell as visited
        grid[i][j] = '0'
        # Explore all four possible directions
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                # Found an island
                count += 1
                # Use DFS to mark all parts of the island
                dfs(grid, i, j)
    
    return count
"""

from doctest import TestResults
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        def startOfNewIsland(i: int, j: int) -> bool:
            val = grid[i][j]
            if val in ['0', '-1']:
                return False
            if i == 0 and j == 0:
                if (grid[1][0] in ['0', '1']
                    and grid[0][1] in ['0', '1']):
                    return True
            elif i == 0 and j == len(grid[0]) - 1:
                if (grid[0][len(grid[0]) - 2] in ['0', '1']
                    and grid[1][len(grid[0]) - 1] in ['0', '1']):
                    return True
            elif i == len(grid) - 1 and j == 0:
                if (grid[len(grid) - 1][1] in ['0', '1']
                    and grid[len(grid) - 2][0] in ['0', '1']):
                    return True
            elif i == len(grid) - 1 and j == len(grid[0]) -1:
                if (grid[len(grid) - 1][len(grid[0]) - 2] in ['0', '1']
                    and grid[len(grid) - 2][len(grid[0]) - 1]) in ['0', '1']:
                    return True
            elif i == 0 and 0 < j < len(grid[0]) - 1:
                if (grid[i + 1][j] in ['0', '1']
                    and grid[i][j - 1] in ['0', '1']
                    and grid[i][j + 1] in ['0', '1']):
                    return True
            elif i == len(grid) - 1 and 0 < j < len(grid[0]) - 1:
                if (grid[i - 1][j] in ['0', '1']
                    and grid[i][j - 1] in ['0', '1']
                    and grid[i][j + 1] in ['0', '1']):
                    return True
            elif 0 < i < len(grid) - 1 and j == 0:
                if (grid[i + 1][j] in ['0', '1']
                    and grid[i - 1][j] in ['0', '1']
                    and grid[i][j + 1] in ['0', '1']):
                    return True
            elif 0 < i < len(grid) - 1 and j == len(grid[0]) - 1:
                if (grid[i + 1][j] in ['0', '1']
                    and grid[i - 1][j] in ['0', '1']
                    and grid[i][j - 1] in ['0', '1']):
                    return True
            else:
                if (val == '1'
                    and grid[i - 1][j] in ['0', '1']
                    and grid[i + 1][j] in ['0', '1']
                    and grid[i][j - 1] in ['0', '1']
                    and grid[i][j + 1] in ['0', '1']):
                    return True
            return False
        
        def partOfIsland(i: int, j: int) -> bool:
            val = grid[i][j]
            if val == '0':
                return False
            if val == '-1':
                return True
            if i == 0 and j == 0:
                if (grid[1][0] == '-1'
                    or grid[0][1] == '-1'):
                    return True
            elif i == 0 and j == len(grid[0]) - 1:
                if (grid[0][len(grid[0]) - 2] == '-1'
                    or grid[1][len(grid[0]) - 1] == '-1'):
                    return True
            elif i == len(grid) - 1 and j == 0:
                if (grid[len(grid) - 1][1] == '-1'
                    or grid[len(grid) - 2][0] == '-1'):
                    return True
            elif i == len(grid) - 1 and j == len(grid[0]) -1:
                if (grid[len(grid) - 1][len(grid[0]) - 2] == '-1'
                    or grid[len(grid) - 2][len(grid[0]) - 1] == '-1'):
                    return True
            elif i == 0 and 0 < j < len(grid[0]) - 1:
                if (grid[i + 1][j] == '-1'
                    or grid[i][j - 1] == '-1'
                    or grid[i][j + 1] == '-1'):
                    return True
            elif i == len(grid) - 1 and 0 < j < len(grid[0]) - 1:
                if (grid[i - 1][j] == '-1'
                    or grid[i][j - 1] == '-1'
                    or grid[i][j + 1] == '-1'):
                    return True
            elif 0 < i < len(grid) - 1 and j == 0:
                if (grid[i + 1][j] == '-1'
                    or grid[i - 1][j] == '-1'
                    or grid[i][j + 1] == '-1'):
                    return True
            elif 0 < i < len(grid) - 1 and j == len(grid[0]) - 1:
                if (grid[i + 1][j] == '-1'
                    or grid[i - 1][j] == '-1'
                    or grid[i][j - 1] == '-1'):
                    return True
            else:
                if (grid[i - 1][j] == '-1'
                    or grid[i + 1][j] == '-1'
                    or grid[i][j - 1] == '-1'
                    or grid[i][j + 1] == '-1'):
                    return True
            return False
        
        i = 0
        j = 0
        #print('len(grid) - ', len(grid))
        while i < len(grid):
            #print('processing row ', i)
            j = 0
            while j < len(grid[0]):
                print()
                print('Checking at ', i, ', ', j)
                if grid[i][j] == '1':
                    if startOfNewIsland(i, j):
                        print('find new island at ', i, ', ', j)
                        num_islands += 1
                        grid[i][j] = '-1'
                    elif partOfIsland(i, j):
                        print('part of island at ', i, ', ', j)
                        grid[i][j] = '-1'
                j += 1
            i += 1
        return num_islands
    

s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
#print(s.numIslands(grid))


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))
