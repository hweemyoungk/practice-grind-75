# [3/16/2024]Time up
# 22%/10%
""" 
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
 """
from typing import List


class Solution:
    # Backtracking
    def longestPalindrome(self, s: str) -> str:
        self.s=s
        self.l=len(s)
        self.visited: List[List[bool]] = [[None]*self.l for _ in range(self.l)]
        self.ans=""
        self.ansLength=0
        for i in range(self.l):
            for j in range(i,self.l):
                length = j-i+1
                if length<=self.ansLength:
                    continue
                if self.isPalindrom(i,j):
                    if self.ansLength<length:
                        self.ansLength=length
                        self.ans=s[i:j+1]
        return self.ans
    
    def isPalindrom(self, start: int, end: int) -> bool:
        if self.visited[start][end]!=None:
            return self.visited[start][end]
        if start<0 or self.l-1<start or end<0 or self.l-1<end:
            # Out of index range
            return False
        if end<start:
            return False
        if start==end:
            self.visited[start][start]=True
            return True
        
        cStart = self.s[start]
        cEnd = self.s[end]
        if cStart!=cEnd:
            self.visited[start][end]=False
            return False
        if start+1==end:
            # Adjacent
            self.visited[start][end]=True
            return True
        # More than 3 chars: must be palindrom between start and end
        if self.isPalindrom(start+1,end-1):
            self.visited[start][end]=True
            return True
        self.visited[start][end]=False
        return False
        