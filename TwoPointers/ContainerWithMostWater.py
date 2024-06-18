"""
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.


Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        i = 0
        j = 0
        print('[i, j] - ', i, ':', j)
        while i < len(height) - 1:
            j = i + 1
            while j < len(height):
                print('[i, j] - ', i, ':', j)
                print(height[i])
                print(height[j])
                # if i and j are immediate neighbors, the volume is 0
                area = min(height[i], height[j]) * (j - i) 
                print('area - ', area)
                if area > ret:
                    ret = area            
                j += 1
            i += 1
        return ret
    
  
s = Solution()
    
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))

height = [1, 1]
print(s.maxArea(height))