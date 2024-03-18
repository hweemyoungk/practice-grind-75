# [3/18/2024]20m out of 30m(67%)
# 95%/63%
""" 
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
 """
from typing import List


class Solution:
    # Two pointers
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        lp=len(p)
        ls=len(s)
        if ls < lp:
            return []
        
        orda=ord('a')
        pCounts=[0]*26
        for c in p:
            pCounts[ord(c)-orda]+=1
        ptr2=-1
        subStrCounts=[0]*26
        # init subStrCounts
        for ptr2 in range(lp-1):
            subStrCounts[ord(s[ptr2])-orda]+=1
        ptr2+=1
        ptr1=0

        while ptr2<ls:
            subStrCounts[ord(s[ptr2])-orda]+=1
            if pCounts==subStrCounts:
                ans.append(ptr1)
            subStrCounts[ord(s[ptr1])-orda]-=1
            ptr1+=1
            ptr2+=1
        
        return ans
            