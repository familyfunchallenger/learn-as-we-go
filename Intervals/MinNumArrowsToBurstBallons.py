"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= x-start < x-end <= 2^31 - 1
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Approach
            - Sort the Balloons: First, sort the array of balloons by their end coordinates. This ensures that when we shoot an arrow, it covers the most balloons that end first, thus minimizing the number of arrows.

            - Iterate and Shoot Arrows: Start with the first balloon's end coordinate and shoot an arrow there. Then, continue to the next balloon that starts after this arrow's position. Repeat this process until all balloons are covered.

            - Count the Arrows: Keep a count of how many arrows are used.

        Explanation
            - Sorting: The balloons are sorted by their end coordinates to allow a greedy approach where each arrow shot is positioned optimally to cover the maximum number of balloons.
            - Iterating: By iterating through the sorted list, we track the end of the last balloon burst by an arrow. If the start of the next balloon is beyond this end, a new arrow is needed.
            - Counting: The variable arrows keeps track of the number of arrows used.
            
            Complexity
            Time Complexity: Sorting the list takes O(nlogn) time, and the subsequent iteration through the list takes O(n) time. Thus, the overall time complexity is O(nlogn).
            
            Space Complexity: The space complexity is O(1) additional space, not counting the input space.
        """
        if not points:
            return 0

        # Sort the points by the end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for x_start, x_end in points:
            # If the start of the current balloon is after the end of the last burst balloon,
            # we need a new arrow
            if x_start > current_end:
                arrows += 1
                current_end = x_end
        
        return arrows
    

s = Solution()


points = [[10,16],[2,8],[1,6],[7,12]]


points = [[1,2],[3,4],[5,6],[7,8]]


points = [[1,2],[2,3],[3,4],[4,5]]