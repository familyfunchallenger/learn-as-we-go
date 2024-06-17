"""
Given two strings needle and haystack, return the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle) or (
            len(haystack) == len(needle) and haystack != needle):
            return -1
        i = -1
        while i <= len(haystack) - len(needle):
            print('part of hay - ', haystack[i: i + len(needle)])
            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1
        return -1
    
    
s = Solution()

haystack = "sadbutsad"
needle = "sad"
print(s.strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(s.strStr(haystack, needle))