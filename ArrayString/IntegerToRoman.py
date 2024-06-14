"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
 Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
 append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, 
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms 
are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.
 You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places


Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII

 
 Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV

Constraints:
1 <= num <= 3999
"""


from operator import ne


class Solution:

    def __init__(self):
        self.i2r = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:
            return 'Out of Range'
        ret = ''    
        rem = num
        i = 1
        while rem > 0:
            q = rem % 10
            actual_rem = q * (10 ** (i - 1))
            rem = rem // 10
            new_sub_str = ''
            #print('mb - ', mb)
            print('q - ', q)
            print('rem - ', rem)
            print('acutal_rem - ', actual_rem)
            if actual_rem in self.i2r:
                new_sub_str = self.i2r[actual_rem]   # add the new sub-str at the beginning
            else:
                # need to compute 
                if actual_rem > 0 and actual_rem < 5:
                    while actual_rem > 0:
                        new_sub_str += 'I'
                        actual_rem -= 1
                elif actual_rem > 5 and actual_rem < 10:
                    actual_rem -= 5
                    new_sub_str = 'V'
                    while actual_rem > 0:
                        new_sub_str += 'I'
                        actual_rem -= 1
                elif actual_rem > 10 and actual_rem < 50:
                    while actual_rem > 0:
                        new_sub_str += 'X'
                        actual_rem -= 10 ** (i - 1)
                elif actual_rem > 50 and actual_rem < 100:
                    new_sub_str = 'L'
                    actual_rem -= 50
                    while actual_rem > 0:
                        new_sub_str += 'X'
                        actual_rem -= 10 ** (i - 1)
                elif actual_rem > 100 and actual_rem < 500:
                    while actual_rem > 0:
                        new_sub_str += 'C'
                        actual_rem -= 10 ** (i - 1)
                elif actual_rem > 500 and actual_rem < 1000:
                     new_sub_str = 'D'
                     actual_rem -= 500
                     while actual_rem > 0:
                         new_sub_str += 'C'
                         actual_rem -= 10 ** (i -1)
                else:
                    # between 1000 and 3999
                    while actual_rem > 0:
                        new_sub_str += 'M'
                        actual_rem -= 10 ** (i -1)
            ret = new_sub_str + ret
            i += 1
        return ret
    


s = Solution()

num = 3749
print(s.intToRoman(num))


print(s.intToRoman(58))


print(s.intToRoman(1994))