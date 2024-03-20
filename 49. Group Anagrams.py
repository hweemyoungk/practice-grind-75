# [3/19/2024]6m out of 25m
# 17%/28%
""" 
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 """
from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[List[int],List[str]]={}
        orda = ord('a')
        for s in strs:
            charCounter=[0]*26
            for c in s:
                charCounter[ord(c)-orda]+=1
            charCounterTup = tuple(charCounter)
            if charCounterTup in groups:
                groups[charCounterTup].append(s)
                continue
            groups[charCounterTup]=[s]
        return list(groups.values())