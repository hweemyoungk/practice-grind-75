# [3/21/2024]Time up
# 41%/92%
""" 
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
 """
from typing import Tuple


class Solution:
    # DFS(stack)
    def decodeString(self, s: str) -> str:
        self.s=s
        self.l=len(s)
        self.digits='0123456789'
        self.opening = '['
        self.closing = ']'
        return self.decode(0)[0]
    
    def decode(self, start: int) -> Tuple[str, int]:
        ans=''
        lastNumber=''
        i=start
        while i<self.l:
            c=self.s[i]
            if c==self.closing:
                return ans,i+1
            if c==self.opening:
                res,newStart=self.decode(i+1)
                ans+=int(lastNumber)*res
                i=newStart
                lastNumber=''
                continue
            if c in self.digits:
                lastNumber+=c
                i+=1
                continue
            ans+=c
            i+=1
        return ans,i
                