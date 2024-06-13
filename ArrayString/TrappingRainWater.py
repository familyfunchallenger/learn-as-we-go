"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
 are being trapped.


Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return -1
        if len(height) < 3:
            return 0
        ret = 0
        left_max_wall_height = [0] * len(height)
        # Use this to track current known max wall height encountered
        # from left to right
        max_wall_height = 0
        for i, h in enumerate(height):
            if i == 0:
                left_max_wall_height[i] = 0
                max_wall_height = 0
            else:
                max_wall_height = max(max_wall_height, height[i - 1])
                left_max_wall_height[i] = max_wall_height
        print(left_max_wall_height)
        # Now use this to track current known max wall height encountered
        # from right to left
        max_wall_height = 0
        i = len(height) - 1
        while i > 0:
            # scan from right to left
            if i == len(height) - 1:
                max_wall_height = 0
            else:
                max_wall_height = max(max_wall_height, height[i + 1])
            
            if height[i] >= max_wall_height or height[i] >= left_max_wall_height[i]:
                # current bar is higher than either of the left/right wall
                # so it cannot trap any water at the current bar
                ret += 0
            else:
                ret += min(max_wall_height, left_max_wall_height[i]) - height[i]
            i -= 1
        return ret
    


s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))

height = [4,2,0,3,2,5]
print(s.trap(height))