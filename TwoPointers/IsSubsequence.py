"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9,
and you want to check one by one to see if t has its subsequence. In this scenario,
how would you change your code?
# mutli-threading

Dynamic Programming Approach:
For the dynamic programming solution, the idea is to preprocess string t to understand
the next occurrence of every character after each position. This approach is particularly
useful when there are numerous subsequences to be checked against t, as it can check each
subsequence in linear time.

Key Data Structures:
nxt: A list of dictionaries to store the next occurrence of every character after each
position in t.

Enhanced Breakdown:
Preprocess string t:

Create a list of dictionaries nxt to store the next occurrence of every character after
each position in t.
Traverse string t in reverse. For each position, copy the next position's dictionary and
update the current character's next occurrence.

Check Subsequence:

Traverse string s and for each character, check its next occurrence in t using the nxt list.
If any character of s doesn't have a next occurrence in t, return False. Otherwise, continue.

Complexity Analysis:
Time Complexity (for checking one subsequence s):

The algorithm traverses the string s once, resulting in a time complexity of
O(len(s))O(\text{len}(s))O(len(s)).
Space Complexity:

The algorithm creates a list of dictionaries nxt of size len(t)\text{len}(t)len(t),
leading to a space complexity of O(len(t))O(\text{len}(t))O(len(t)).

Code Dynamic Programming

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        nxt = [{} for _ in range(len(t) + 1)]
        for i in range(len(t) - 1, -1, -1):
            nxt[i] = nxt[i + 1].copy()
            nxt[i][t[i]] = i + 1
        
        i = 0
        for c in s:
            if c in nxt[i]:
                i = nxt[i][c]
            else:
                return False
        return True

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == len(t):
            return s == t
        i = 0
        j = 0
        while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    j += 1
                else:
                    i += 1
        if j == len(t):
            return False
        return True
    
 
so = Solution()
    
s = "abc"
t = "ahbgdc"
print(so.isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(so.isSubsequence(s, t))