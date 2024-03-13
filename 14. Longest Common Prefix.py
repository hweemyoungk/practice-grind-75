# [3/12/2024]6m out of 20m
# 30%
""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
 """
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = ''
        for i in range(min(*[len(s) for s in strs])):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    return prefix
            prefix = prefix + c
        return prefix