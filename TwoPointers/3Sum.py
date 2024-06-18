"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        j = 0
        k = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r = [nums[i], nums[j], nums[k]]
                        r.sort()
                        rt = tuple(r)
                        if rt not in ret:
                            ret.append(rt)
                    k += 1
                j += 1
            i += 1
            
        return [list(i) for i in ret]

s = Solution()

nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))

nums = [0,1,1]
print(s.threeSum(nums))

nums = [0,0,0]
print(s.threeSum(nums))
