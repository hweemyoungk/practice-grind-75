# [3/11/2024]Time up: 16m out of 15m
""" 
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
 """
from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLength = max(len(a), len(b))
        a = a.zfill(maxLength)
        b = b.zfill(maxLength)
        ord0 = ord('0')
        curDigit = 0
        over = 0
        result = ''
        while curDigit < maxLength:
            curDigit += 1
            digit, over = self.__addDigit(ord(a[len(a) - 1 - curDigit]) - ord0, ord(b[len(b) - 1 - curDigit]) - ord0 + over)
            result = chr(ord0 + digit) + result
        if over == 1:
            result = '1' + result

        return result
        
    
    def __addDigit(self, a: int, b: int) -> Tuple[int, int]:
        return (a+b)%2, (a+b)//2

