"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        window_start = 0
        window_size = sum([len(i) for i in words])
        if len(s) < window_size:
            return ret
        while window_start <= len(s) - window_size:
            #print('window_start - ', window_start)
            #print('substr - ', s[window_start:window_size])
            all_in = True
            substr = s[window_start:window_start + window_size]
            for i in words:
                # this check only handles that all words are unique in the list
                if i not in substr:
                    all_in = False
                    break
                else:
                    # Remove the current word from the current substr and let the loop continue
                    substr = substr.replace(i, '', 1)
            if all_in:
                ret.append(window_start)
            window_start += 1
        return ret
    

so = Solution()


s = "barfoothefoobarman"
words = ["foo","bar"]
print(so.findSubstring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(so.findSubstring(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(so.findSubstring(s, words))