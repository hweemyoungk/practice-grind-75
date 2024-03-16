# [3/14/2024]Time up
# 13%/91%
""" 
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

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

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
 """
from typing import List, Optional

class TrieNode:
    def __init__(self, char: Optional[str], nextNodes: List, isEndOfKey: bool) -> None:
        self.char = char
        self.nextNodes = nextNodes
        self.isEndOfKey = isEndOfKey

class Trie:
    def __init__(self):
        self.root=TrieNode(None, [], False)

    def insert(self, word: str) -> None:
        currNode = self.root
        for i in range(len(word)):
            c = word[i]
            isLastChar = i == len(word)-1
            goToNextChar = False
            for nextNode in currNode.nextNodes:
                if nextNode.char != c:
                    continue
                # Char match
                if isLastChar:
                    nextNode.isEndOfKey = True
                    return
                # Not last char
                currNode = nextNode
                goToNextChar = True
                break
            if goToNextChar:
                continue
            # No match: create node
            newNode = TrieNode(c, [], isLastChar)
            currNode.nextNodes.append(newNode)
            currNode = newNode
            continue
        
        return

    def search(self, word: str) -> bool:
        currNode = self.root
        for i in range(len(word)):
            c = word[i]
            goToNextChar = False
            for nextNode in currNode.nextNodes:
                if nextNode.char != c:
                    continue
                # Char match
                currNode = nextNode
                goToNextChar = True
                break
            if goToNextChar:
                continue
            # No match
            return False
        # All chars match but last node must be end of key
        return currNode.isEndOfKey
        
    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            goToNextChar = False
            for nextNode in currNode.nextNodes:
                if nextNode.char != c:
                    continue
                # Char match
                currNode = nextNode
                goToNextChar = True
                break
            if goToNextChar:
                continue
            # No match
            return False
        # All chars match
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)