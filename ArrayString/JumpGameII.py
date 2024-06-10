"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i],
 you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        stack = []
        arr_length = len(nums)
        if arr_length in [0, 1]:
            return 0
        if arr_length == 2:
            if nums[0] >= 1:
                return 1
            else:
                return arr_length + 1
        if nums[0] >= arr_length - 1:
            return 1
        # At this point the length of the array is at least two
        num_of_branches_left = nums[0]
        min_jumps = arr_length
        current_postion = 0
        while num_of_branches_left > 0:
            min_jumps = min(min_jumps, num_of_branches_left + self.jump(nums[num_of_branches_left:])) 
            num_of_branches_left -= 1
        return min_jumps
    


s = Solution()

nums = [2,3,1,1,4]
print(s.jump(nums))

nums = [2,3,0,1,4]
print(s.jump(nums))