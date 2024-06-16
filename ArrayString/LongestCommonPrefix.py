"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letterfor i, c in enumerate(s):
                if s.
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ret = ''
        last_prefix = strs[0]
        for s in strs:
            curr_prefix = ''
            i = 0
            while i < min(len(s), len(last_prefix)):
                if s[i] == last_prefix[i]:
                    curr_prefix += s[i]
                i += 1
            if len(curr_prefix) < len(last_prefix):
                last_prefix = curr_prefix
        return last_prefix
    

s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))

print(s.longestCommonPrefix(["dog","racecar","car"]))