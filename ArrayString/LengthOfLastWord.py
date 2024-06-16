"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s.split())
        return len(s.split()[-1])
    
    def lengthOfLastWord2(self, s: str) -> int:
        #x = s.strip()
        x = s
        t = ''
        i = 0
        need_reset = True
        while i < len(x):
            # Traverse and update t till we see a whitespace
            if x[i] != ' ':
                if need_reset:
                    t = x[i]
                else:
                    t += x[i]
                need_reset = False
            else:
                need_reset = True            
            i += 1
        return len(t)
    


s = Solution()

print(s.lengthOfLastWord2('Hello World'))

print(s.lengthOfLastWord2('   fly me   to   the moon  '))


print(s.lengthOfLastWord2('luffy is still joyboy'))