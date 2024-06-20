"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1


Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

# O(n * log(n)) is done with sliding window and binary-search
class Solution {
public:

    bool func(int mid, int k, vector<int>& v) {
        int n = v.size();
        int sum = 0;
        for (int i = 0; i < mid; i++) {
            sum += v[i];
        }
        if (sum >= k) return true;

        for (int i = mid; i < n; i++) {
            sum += v[i] - v[i - mid];
            if (sum >= k) return true;
        }
        return false;
    }

    int minSubArrayLen(int t, vector<int>& v) {
        int n=v.size();
        int s=0;
        int ans=s;
        int e=n;
        while(s<=e){
            int mid=(s+e)/2;
            if(func(mid,t,v)){
                ans=mid;
                e=mid-1;
            }
            else s=mid+1;
        }
        return ans;
    }
};

!!! Dynamic window size by moving the window start pos and the window end pos while ensure the required condition still be met
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #return self._solution1(target, nums)
        return self._solutionBigON(target, nums)
    
    def _solution1(self, target: int, nums: List[int]) -> int:
        # Time complexity of O(n^2) [n*(n-1)/2]
        ret = 0
        if len(nums) == 0:
            return ret
        if len(nums) == 1:
            return 1 if nums[0] == target else 0
        # now we have a list with at least 2 elements
        window_size = 1
        starting_pos = 0
        while window_size < len(nums):
            # The window size will increase till either a subarray is found or the size exceeds the length of the array
            # The window will slide towards the end of the list if allowed, i.e. starting_pos + window_size <= len(nums)
            starting_pos = 0
            while window_size + starting_pos <= len(nums):
                if sum(nums[starting_pos:starting_pos + window_size]) >= target:
                    return window_size
                starting_pos += 1
            # out of the above loop without returning a valid subarray length, it means the window size needs to be increased
            window_size += 1
        return ret
    
    def _solutionBigON(self, target: int, nums: List[int]) -> int:
        # Complexity of big O(n)
        ret = 0
        window_start = 0
        window_end = 0
        current_sum = 0
        min_length = len(nums) + 1
        while window_end < len(nums):
            current_sum += nums[window_end]
            while (current_sum >= target):
                current_sum -= nums[window_start]
                min_length = min(window_end - window_start + 1, min_length)
                window_start += 1
            window_end += 1
        if min_length != len(nums) + 1:
            ret = min_length
        return ret
    

s = Solution()


target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))

target = 4
nums = [1,4,4]
print(s.minSubArrayLen(target, nums))

target = 11
nums = [1,1,1,1,1,1,1,1]
print(s.minSubArrayLen(target, nums))
