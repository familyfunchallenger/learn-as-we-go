"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


Example 2:

Input: strs = [""]
Output: [[""]]


Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List


class Solution:

    def _getSortedStr(self, s: str) -> str:
        s1 = list(s)
        s1.sort()
        return ''.join(s1)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        mapping = {}
        for i in range(0, len(strs)):
            sorted_str = self._getSortedStr(strs[i])
            if sorted_str not in mapping:
                mapping[sorted_str] = [strs[i]]
            else:
                mapping[sorted_str].append(strs[i])
        for _, v in mapping.items():
            ret.append(v)
        return ret


s = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))

strs = [""]
print(s.groupAnagrams(strs))

strs = ["a"]
print(s.groupAnagrams(strs))