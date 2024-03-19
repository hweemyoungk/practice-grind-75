# [3/19/2024]Time up
# 69%/51%
""" 
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
 """
from typing import List, Tuple


class Solution:
    # def binary_search_leftmost(self, arr: List[Tuple[int,int]], target: int) -> int:
    #     l = len(arr)
    #     # Corner case
    #     if l == 0:
    #         return ~0
    #     if l == 1:
    #         if target == arr[0][1]:
    #             return 0
    #         return ~0 if target < arr[0][1] else ~1
        
    #     lo, hi = 0, len(arr)
    #     while lo < hi :
    #         m = (lo + hi) // 2
    #         if arr[m][1] < target:
    #             lo = m + 1
    #         else: 
    #             hi = m
    #     if lo==l:
    #         return ~l
    #     if arr[lo][1]!=target:
    #         return ~lo
    #     return lo
    
    # Monotonic stack
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        ans=[0]*l
        # Non-increasing stack
        stack: List[Tuple[int,int]]=[]
        for iCurr, tCurr in enumerate(temperatures):
            while stack:
                prev = stack.pop()
                if prev[1]<tCurr:
                    # Warmer
                    ans[prev[0]]=iCurr-prev[0]
                    continue
                # Not warmer
                stack.append(prev)
                break
            stack.append((iCurr,tCurr))
        return ans
        