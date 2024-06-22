"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        construct a dictionary from magazine {charactor in magazine: number of occurrences in magazine}, then traverse the ransomeNote to see if (1) the charactor in ransomeNote is in the dictionary and (2) the available occurrences are greater than 0 and (3) if true, reduce the number of occurrences; otherwise return False
        """
        char_in_magazine = {}
        for i in magazine:
            if i not in char_in_magazine:
                char_in_magazine[i] = 1
            else:
                char_in_magazine[i] += 1
        for i in ransomNote:
            if i not in char_in_magazine or char_in_magazine[i] == 0:
                return False
            else:
                char_in_magazine[i] -= 1
        return True
    

s = Solution()

ransomNote = "a"
magazine = "b"
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote, magazine))
