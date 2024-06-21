"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ''
        if len(s) < len(t):
            return ret
        # need dynamically adjust the window start and end to detect the minimum window
        window_start = 0
        window_end = 0
        current_substr = ''
        min_window_len = len(s) + 1
        while window_end < len(s):
            current_substr = s[window_start:window_end + 1]
            while (self._windowHasAll(current_substr, t)):
                print('current_substr - in inner while loop - ', current_substr)
                ret = current_substr
                current_substr = s[window_start + 1:window_end + 1]
                min_window_len = min(
                    window_end - window_start + 1, min_window_len)
                window_start += 1
            window_end += 1
            #current_sum += s[window_end]
            #while (current_sum >= target):
            #    current_sum -= nums[window_start]
            #    min_length = min(window_end - window_start + 1, min_length)
            #    window_start += 1
            #window_end += 1
        #if min_window_len != len(s) + 1:
        return ret
    
    def _windowHasAll(self, w: str, t: str) -> bool:
        ret = True
        # w is the window, t is the target
        if len(w) < len(t):
            return False
        copyW = w
        for c in t:
            if c in copyW:
                # remove c from w and then continue the loop
                copyW = copyW.replace(c, '', 1)
            else:
                return False
        return ret
    

so = Solution()

s = "ADOBECODEBANC"
t = "ABC"
print(so.minWindow(s, t))

s = "a"
t = "a"
print(so.minWindow(s, t))


s = "a"
t = "aa"
print(so.minWindow(s, t))
