# [3/11/2024]10.5min
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # count-map
        sMap = {}
        for c in s:
            if c not in sMap:
                sMap[c] = 1
                continue
            sMap[c] = sMap[c] + 1
        for c in t:
            if c not in sMap:
                return False
            if sMap[c] == 0:
                return False
            sMap[c] = sMap[c] - 1
        return True
            
