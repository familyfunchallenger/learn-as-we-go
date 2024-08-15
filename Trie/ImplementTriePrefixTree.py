"""_summary_

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
* Trie() Initializes the trie object.
* void insert(String word) Inserts the string word into the trie.
* boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
* boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:
* 1 <= word.length, prefix.length <= 2000
* word and prefix consist only of lowercase English letters.
* At most 3 * 10^04 calls in total will be made to insert, search, and startsWith.

Thoughts:
Each node is a data structure like below:
struct TrieNode {
    char val;
    List[TrieNode] childrenNodes;  ==> Dictionary/Map here is much better than list
}

Operation "insert" will start from searching the Trie structure character by character till the next character cannot be found. At that point, start the actual insert.

class TrieNode:
    def __init__(self):
        # Dictionary to hold child nodes
        self.children = {}
        # Boolean flag to indicate if the node represents the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        # Start from the root node
        node = self.root
        # Traverse through the word
        for char in word:
            # If the character is not in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        # Start from the root node
        node = self.root
        # Traverse through the word
        for char in word:
            # If the character is not in the current node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if the current node marks the end of a word
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        node = self.root
        # Traverse through the prefix
        for char in prefix:
            # If the character is not in the current node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if the prefix is found
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True

"""