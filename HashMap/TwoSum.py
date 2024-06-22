"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        # Easiy solution is to traverse the list in the n * (n - 1) / 2 way to find the first two indexes
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return ret
    
    def twoSumWithTwoHashMaps(self, nums: List[int], target: int) -> List[int]:
        ret = []
        pos_map = {}
        for i in range(0, len(nums)):
            if nums[i] not in pos_map:
                pos_map[nums[i]] = [i]
            else:
                pos_map[nums[i]].append(i)
        for i in range(0, len(nums)):
            complement_value = target - nums[i]
            next_index = -1
            if complement_value in pos_map:
                for j in pos_map[complement_value]:
                    if j != i:
                        next_index = j
                        break
                if next_index != -1:
                    return [i, next_index]
        return ret

s = Solution()

nums = [2,7,11,15]
target = 9
print(s.twoSumWithTwoHashMaps(nums, target))

nums = [3,2,4]
target = 6
print(s.twoSumWithTwoHashMaps(nums, target))

nums = [3,3]
target = 6
print(s.twoSumWithTwoHashMaps(nums, target))
