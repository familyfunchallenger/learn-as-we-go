"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].


Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        The approach is to compare the last element of each array, the larger is copied to the
        end of the first array (the end of the first array will move towards the head each time
        a copy is made). The pointers to each array will move accordingly.
        """
        # if array 2 is empty, it's done
        if n == 0:
            return
        # if array 1 is empty, copy array 2 to array 1, and it's done
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        # now both array 1 and array 2 are not empty
        index_copy_to = m + n -1
        index1 = m - 1
        index2 = n - 1
        while index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index_copy_to] = nums1[index1]
                index1 -= 1
            else:
                nums1[index_copy_to] = nums2[index2]
                index2 -= 1
            index_copy_to -= 1

# Now test it
s = Solution()

# TC 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
                
nums1 = [1]
m = 1
nums2 =[]
n = 0
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 =[1]
n = 1
s.merge(nums1, m, nums2, n)
print(nums1)