"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


from curses import window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print('s - ', s)
        ret = 0
        if len(s) == 1:
            return 1
        window_start = 0
        window_end = 1
        current_substr = [s[0]]
        max_length = 1
        while window_end < len(s):
            print('window_end - outter while block - ', window_end)
            if s[window_end] not in current_substr:
                # if next character is not in the current window/substr, increase the window by moving the window_end towards end by 1
                current_substr.append(s[window_end])
                window_end += 1
                max_length = max(len(current_substr), max_length)
                print('current_substr - in if block - ', current_substr)
            else:
                # Now the next character is in the current  window/substr,
                # Current max substr length has been recorded before the execution gets here
                # move the window_start to the character that's next to the value of 's[window_end]'
                while window_start < window_end and s[window_start] != s[window_end]:
                        # keep moving window_start till we find the index of the character same as s[window_end]
                        window_start += 1
                        print('current_substr - ', current_substr)
                        del current_substr[0]
                # after the while loop above, window_start is the index of the element that has the same value as s[window_end]
                # we move the window_start by 1 to start a new window
                window_start += 1
            if window_start == window_end:
                window_end += 1
        if max_length >= 1:
            ret = max_length
        return ret
    

so = Solution()

s = "abcabcbb"
print(so.lengthOfLongestSubstring(s))

s = "bbbbb"
print(so.lengthOfLongestSubstring(s))

s = "pwwkew"
print(so.lengthOfLongestSubstring(s))
