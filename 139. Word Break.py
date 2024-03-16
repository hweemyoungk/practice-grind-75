# [3/16/2024]11m out of 30m
# 29%/35%
""" 
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
 """
from typing import List


class Solution:
    # Backtracking
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BCT~O(n2)
        # wordDict.sort()
        self.visited = set()
        return self.backtrack(s, wordDict)
    
    def backtrack(self, s: str, wordDict: List[str]) -> bool:
        if s in self.visited:
            return False
        for word in wordDict:
            if s.startswith(word):
                s=s[len(word):]
                if s=="":
                    return True
                if self.backtrack(s, wordDict):
                    return True
                s=word+s
        self.visited.add(s)
        return False
