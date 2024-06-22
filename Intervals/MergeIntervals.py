"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from curses.ascii import SO
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # assuming the list of intervals are sorted by the start of the interval
        ret = []
        if len(intervals) == 0:
            return ret
        if len(intervals) == 1:
            return intervals
        range_start = intervals[0][0]
        range_end = intervals[0][1]
        current_interval = 0
        while current_interval < len(intervals) - 1:
            if (intervals[current_interval + 1][0] <= range_end 
                and intervals[current_interval + 1][0] >= range_start):
                # we can increase the range
                range_end = intervals[current_interval + 1][1]
            else:
                ret.append([range_start, range_end])
                range_start = intervals[current_interval + 1][0]
                range_end = intervals[current_interval + 1][1]
            current_interval += 1
        ret.append([range_start, range_end])
        return ret
    

s= Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))

intervals = [[1,4],[4,5]]
print(s.merge(intervals))
