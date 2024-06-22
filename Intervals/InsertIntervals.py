"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the i-th interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

from typing import List

class Solution:
    def _append(
            self, intervals: List[List[int]],
            newInterval: List[int]) -> None:
        if (newInterval[0] >= intervals[-1][0]
            and newInterval[0] <= intervals[-1][1]):
            # completely within, no op
            intervals[-1][1] = max(intervals[-1][1], newInterval[1])
        elif newInterval[0] > intervals[-1][1]:
            # extend the last interval
            intervals.append(newInterval)

    def insert(self,
            intervals: List[List[int]], newInterval: List[int]
            ) -> List[List[int]]:
        ret = []
        if len(intervals) == 0:
            ret.append(newInterval)
            return ret
        # we have at least one interval in the intervals list
        # copy the first element into the ret and then check if new intervals
        # couldbe somehow added (direct copy, merge with the one in the ret)
        # after that keep checking if merge is needed
        ret.append(intervals[0])
        current_interval = 0
        new_interval_added = False
        while current_interval < len(intervals) - 1:
            current_interval += 1
            print('current_interval : ret - ',
                   current_interval, intervals[current_interval], ' : ', ret)
            
            # if newInterval[0] is between ret[-1][0] and intervals[current_interval][0], process the newInterval, otherwise, process the intervals in the list
            if (newInterval[0] >= ret[-1][0] 
                and newInterval[0] <= intervals[current_interval][0]):
                print('can process newInterval')
                self._append(ret, newInterval)
                new_interval_added = True
            self._append(ret, intervals[current_interval])
        if not new_interval_added:
            # the new interval has not been added, append here
            ret.append(newInterval)
        return ret
    

s = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(s.insert(intervals, newInterval))


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(s.insert(intervals, newInterval))