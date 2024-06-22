"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true


Example 2:

Input: s = "foo", t = "bar"
Output: false


Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Establish two maps, one for each string.
        Each map has key as the character in the string, and value as the number of occurrences of that character.
        Then compare the two maps to see if the number of characters with same number of occurrences in s is the same with those in t.
        """
        if len(s) != len(t):
            return False
        map_for_s = {}
        map_for_t = {}
        for i in range(0, len(s)):
            if s[i] not in map_for_s:
                map_for_s[s[i]] = 1
            else:
                map_for_s[s[i]] += 1
           
            if t[i] not in map_for_t:
                map_for_t[t[i]] = 1
            else:
                map_for_t[t[i]] += 1
        list_for_s = [map_for_s[k] for k in map_for_s]
        list_for_t = [map_for_t[k] for k in map_for_t]
        list_for_s.sort()
        list_for_t.sort()
        print('s - t', list_for_s, list_for_t)
        return list_for_s == list_for_t
    

so = Solution()

s = "egg"
t = "add"
print(so.isIsomorphic(s, t))

s = "foo"
t = "bar"
print(so.isIsomorphic(s, t))

s = "paper"
t = "title"
print(so.isIsomorphic(s, t))
