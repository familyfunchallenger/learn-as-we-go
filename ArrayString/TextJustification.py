"""

Given an array of strings words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in
each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth 
characters.

Extra spaces between words should be distributed as evenly as possible. If the number of 
spaces on a line does not divide evenly between words, the empty slots on the left will be
assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between
words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]


Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        i = 0
        current_line_width = 0
        current_line = []
        lines = []
        while i < len(words):
            if current_line_width + len(current_line) + len(words[i]) - 1 <= maxWidth :
                # add to current line 
                current_line.append(words[i])
                current_line_width += len(words[i])
            else:
                lines.append(current_line)
                # re-initialize
                current_line = [words[i]]
                current_line_width = len(words[i])
            i += 1
            print('current_line - ', current_line)
            print('current_line_width - ', current_line_width)
        if current_line:
            lines.append(current_line)
        print(lines)
        # Above can give the right lines, without padding
        # Below is to do the padding
        m = 0
        while m < len(lines):
            # For each line in lines, do the padding needed
            baseSpaces = 1
            needsForExtraSpaces = 0
            current_line_width = sum([len(i) for i in lines[m]])
            current_line = lines[m]
            numWords = len(current_line)
            if numWords > 1:
                baseSpaces = (maxWidth - current_line_width) // (numWords - 1)
                needsForExtraSpaces = (maxWidth - current_line_width) % (numWords - 1)
            print()
            print('current_line - ', current_line)
            print('maxWidth - ', maxWidth)
            print('numWords - ', numWords)
            print('baseSpaces - ', baseSpaces)
            print('needsForExtraSpaces - ', needsForExtraSpaces)
            print('current_line_width - ', current_line_width)
            lineStr = ''
            if numWords == 1:
                if len(current_line[0]) < maxWidth:
                    lineStr = current_line[0] + ' ' * (maxWidth - len(current_line[0]))
                else:
                    lineStr = current_line[0]
            else:
                j = 0
                while j < numWords - 1:
                    if j < needsForExtraSpaces:
                        lineStr += current_line[j] + (' ' * (baseSpaces + 1))
                    else:
                        lineStr += current_line[j] + (' ' * baseSpaces)
                    j += 1
                lineStr += ' ' * (maxWidth - len(lineStr) - len(current_line[numWords - 1])) + current_line[numWords - 1]
            m += 1
            ret.append(lineStr)
                
        return ret
    
    
s = Solution()

# TC1
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(s.fullJustify(words, maxWidth))

# TC2
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

# TC3
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20