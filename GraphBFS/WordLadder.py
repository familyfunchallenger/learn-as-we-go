"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:
* 1 <= beginWord.length <= 10
* endWord.length == beginWord.length
* 1 <= wordList.length <= 5000
* wordList[i].length == beginWord.length
* beginWord, endWord, and wordList[i] consist of lowercase English letters.
* beginWord != endWord
* All the words in wordList are unique.

A DFS could be solve the problem by tracking two conditions to end a path and current least depth:
* All words in the dictionary has been used, and if a word can not be used again in the same path because it will cause a loop
* or the end word is found

BFS is to track the current word and the current depth at the same time using a tuple. Also, if a word is used, it will not be used again to find a valid path. So a "visited" check works.

from collections import deque

def wordLadderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    
    # Check if endWord is in wordList
    if endWord not in wordSet:
        return 0
    
    # Initialize BFS queue and visited set
    queue = deque([(beginWord, 1)])  # (current_word, transformation_count)
    visited = set()
    visited.add(beginWord)
    
    while queue:
        current_word, level = queue.popleft()
        
        # Generate all possible transformations
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                
                if next_word == endWord:
                    return level + 1  # Return the length of the sequence including endWord
                
                if next_word in wordSet and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))
    
    return 0  # If no sequence found
"""

from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return 0
    



s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]