"""

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.


Approach
    - Stack for Operations: We'll use a stack to manage the numbers and the results of sub-expressions enclosed in parentheses.
    - Current Number and Sign: We maintain a current number (num) and the current sign (+ or -).
    - Iterate through Characters: We iterate through the string character by character, performing actions based on the type of character (digit, operator, parenthesis).
    - Evaluate Expressions: When encountering a digit, we build the current number. When encountering an operator or a parenthesis, we evaluate the current number with the current sign and reset for the next number.

Detailed Steps
    - Initialization: Initialize a stack, num as 0, sign as 1 (which represents +), and result as 0.
    - Handling Digits: When a digit is encountered, update num.
    - Handling Operators: When + or - is encountered, update the result by adding num multiplied by sign to the result and update sign accordingly. Reset num to 0.
    - Handling Parentheses: When ( is encountered, push the current result and sign onto the stack, reset result to 0, and sign to 1. When ) is encountered, finalize the current sub-expression by adding num multiplied by sign to the result, then pop from the stack to update the result based on the values before the parentheses.
    - Final Calculation: At the end of the string, ensure to add the last num to the result.

"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 represents +, -1 represents -
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Push the result and the sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset the result and sign for the new sub-expression
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                num = 0
                # The result before the parenthesis
                result *= stack.pop()  # this is the sign before the parenthesis
                result += stack.pop()  # this is the result calculated before the parenthesis
                
        result += sign * num  # Add the last processed number
        
        return result
    
s = Solution()

# Example Usage
s1 = "1 + 1"
s2 = " 2-1 + 2 "
s3 = "(1+(4+5+2)-3)+(6+8)"

print(s.calculate(s1))  # Output: 2
print(s.calculate(s2))  # Output: 3
print(s.calculate(s3))  # Output: 23