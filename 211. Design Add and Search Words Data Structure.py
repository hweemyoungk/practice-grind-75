# [3/20/2024]Passes debug, fails run... wtf? 19m out of 35m
""" 
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 10^4 calls will be made to addWord and search.
 """
from typing import Dict, Optional


class WordDictionary:

    def __init__(self):
        self.startNodes: Dict[str, 'TrieNode']={}
        

    def addWord(self, word: str) -> None:
        # Constraint: len(word)>=1
        initial = word[0]
        if initial not in self.startNodes:
            self.startNodes[initial]=TrieNode(initial)
        self.startNodes[initial].appendWord(word[1:])
        

    def search(self, word: str) -> bool:
        initial = word[0]
        if initial == '.':
            for node in self.startNodes.values():
                if node.hasWord(word[1:]):
                    return True
            return False
        # Not wildcard
        if initial not in self.startNodes:
            return False
        return self.startNodes[initial].hasWord(word[1:])
        
class TrieNode:
    def __init__(self, char: str, isEndOfWord: bool=False, nextNodes: Dict[str, 'TrieNode']={}) -> None:
        self.char=char
        self.isEndOfWord=isEndOfWord
        self.nextNodes=nextNodes
    
    def appendWord(self, word: str) -> None:
        if word=="":
            self.isEndOfWord=True
            return
        
        initial = word[0]
        if initial not in self.nextNodes:
            self.nextNodes[initial]=TrieNode(initial)
        nextNode=self.nextNodes[initial]
        nextNode.appendWord(word[1:])
        return

    def hasWord(self, word: str) -> bool:
        if word=="":
            return self.isEndOfWord
        initial = word[0]
        restWord = word[1:]
        if initial == '.':
            for node in self.nextNodes.values():
                if node.hasWord(restWord):
                    return True
            return False
        # Not wildcard
        if initial not in self.nextNodes:
            return False
        return self.nextNodes[initial].hasWord(restWord)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)