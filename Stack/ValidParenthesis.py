"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true


Example 2:

Input: s = "()[]{}"
Output: true


Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
                
            if c in (')', ']', '}') and len(stack) > 0:
                # pop the stack
                if (stack[-1] == '(' and c == ')') or (
                    stack[-1] == '[' and c == ']') or (
                    stack[-1] == '{' and c == '}'):
                    del stack[-1]
    
        return len(stack) == 0
    

so = Solution()

s = "()"
print(so.isValid(s))

s = "()[]{}"
print(so.isValid(s))

s = "(]"
print(so.isValid(s))
