# [3/12/2024]Time up: 25m out of 15m
""" 
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
 """
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        numBits = 1
        div = n
        while True:
            div = div // 2
            if div == 0:
                break
            numBits+=1
        
        bitCounts = [0]
        
        num = 1
        prev = ''.zfill(numBits)
        prevCount = 0
        while num < n + 1:
            carry = True
            for i in range(len(prev)):
                if not carry:
                    break
                bit = prev[i]
                # Carry exists
                if bit == '0':
                    carry = False
                    prev = prev[:i] + '1' + prev[i+1:]
                    prevCount += 1
                    continue
                # bit == '1'
                carry = True
                prev = prev[:i] + '0' + prev[i+1:]
                prevCount -= 1

            # bitCounts.append(prev.count('1'))
            bitCounts.append(prevCount)
            num += 1
        
        return bitCounts
