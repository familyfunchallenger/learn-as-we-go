"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

If using sorting first, it could be O(n * log(n) + n) where O(n * log(n)) is for the sorting, and the O(n) is to traverse the sorted list to find the longest sequece.

To do it in O(n) time, we will have to traverse the list only constant times.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Approach
            - Convert the List to a Set: This allows for O(1) average time complexity for checking the existence of elements.

            -  Iterate Through the Array: For each element, check if it is the start of a sequence by seeing if the previous element (num - 1) exists in the set. If it doesn't, then this element is the beginning of a new sequence.

            - Count the Length of the Sequence: From the starting element, count the number of consecutive elements by incrementing a counter until the next element in the sequence is no longer in the set.

            - Keep Track of the Maximum Length: Update a variable to store the maximum length of consecutive sequences found.

        Explanation
            - Set Conversion: Converting the list to a set allows us to quickly check if an element exists.
            - Sequence Start Detection: By checking if num - 1 is not in the set, we ensure that we only start counting a sequence from its smallest element.
            - Counting the Sequence: By incrementing from the starting element and checking for the next elements in the set, we count the length of the current sequence.
            - Max Length Tracking: We keep updating the maximum length found during the iterations.
            
        This approach ensures that each element is processed in constant time, resulting in an overall time complexity of O(n).
        """
        if not nums:
            return 0
    
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
    

s = Solution()

nums = [100,4,200,1,3,2]
print(s.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(s.longestConsecutive(nums))
