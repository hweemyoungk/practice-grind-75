# [3/15/2024]Time up
# 86%/59%
""" 
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
 """
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = len(intervals)
        if l == 1:
            return intervals
        
        def byStart(interval: List[int]) -> int:
            return interval[0]
        intervals.sort(key=byStart)
        ans=[]
        for i in range(l-1):
            curr = intervals[i]
            next = intervals[i+1]
            if next[0]<=curr[1]:
                intervals[i+1]=[min(curr[0],next[0]),max(curr[1],next[1])]
                continue
            ans.append(curr)
        ans.append(intervals[l-1])
        return ans
