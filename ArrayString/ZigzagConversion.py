"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        ret = ''
        c = (len(s) // (numRows + numRows - 2)) * (1 + numRows - 2) + 1
        print('len of s: ', len(s))
        print('num of columns: ', c)
        print('num of rows: ', numRows)
        arr = [''] * (c * numRows)
        trend = -1 # -1: going down; 1: going zigzap up
        i = 0
        curr_row = 0
        curr_col = 0
        while i < len(s):
            arr[curr_row * c + curr_col] = s[i]
            print('s[i] - ', s[i])
            
            print('curr_row - ', curr_row)
            print('curr_col - ', curr_col)
            print(arr)
            i += 1
            if trend == -1:
                # going down, update the row index
                curr_row += 1
                # check if next move should be going zigzag up
                if curr_row == numRows:
                    # need to back off one step up, and move one column forward
                    trend = 1
                    curr_row = numRows - 2
                    curr_col += 1
            else:
                # going zigzag up now, update the row index first
                curr_row -= 1
                if curr_row < 0:
                    curr_row = 1
                    trend = -1
                else:
                    curr_col += 1
        ret = ''.join(arr)
        return ret


so = Solution()
    
s = "PAYPALISHIRING"
numRows = 3
print(so.convert(s, numRows))

s = "PAYPALISHIRING"
numRows = 4
print(so.convert(s, numRows))

s = "A"
numRows = 1
print(so.convert(s, numRows))