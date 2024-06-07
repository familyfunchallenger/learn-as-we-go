"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that
the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3


Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given the value range of nums[i] is limited, we can have a dict {nums[i]: # of occurrences}
        as we go through the list, update the dict and check if the # of occurrences of nums[i]
        have exceeded n/2 times, if so, return nums[i]
        """
        keys = list(range(-109, 110))
        occurrences = dict()
        for i in keys:
            occurrences[i] = 0
        for i in nums:
            occurrences[i] += 1
            if occurrences[i] > len(nums) / 2:
                return i
        return -1
    

s = Solution()

nums = [3,2,3]
print(s.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))