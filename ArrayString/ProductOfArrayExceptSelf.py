"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        p = 1
        num_of_zeros = 0
        for n in nums:
            if n != 0:
                p = p * n
            else:
                num_of_zeros += 1
        for (i, n) in enumerate(nums):
            if n != 0:
                if num_of_zeros == 0:
                    products.append(p // n)
                else:
                    products.append(0)
            else:
                if num_of_zeros == 1:
                    # only one 0
                    products.append(p)
                else:
                    products.append(0)
                
        return products
    


s = Solution()

nums = [1,2,3,4]
print(s.productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))

nums = [-1,1,0,-3, 0, 3]
print(s.productExceptSelf(nums))