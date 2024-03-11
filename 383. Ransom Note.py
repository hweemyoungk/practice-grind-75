# [3/11/2024] 7m out of 15m
""" 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
 """

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        orda = ord('a')
        childCounter = [0] * 26
        for c in magazine:
            childCounter[ord(c) - orda] += 1
        for c in ransomNote:
            if (childCounter[ord(c) - orda] == 0):
                return False
            childCounter[ord(c) - orda] -= 1
        
        return True
