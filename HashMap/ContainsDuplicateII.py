"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        The bruteforce way is to do a traverse to see if any i,j idex pair satisfy the requirement.

        If to use a dict/map, maybe have a mapp of the {value: [indexes]} and then traverse the dict/map to see if any meets the requirement.

        I do not see a real different at the Big O complexity
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

s = Solution()

nums = [1,2,3,1]
k = 3
print(s.containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))