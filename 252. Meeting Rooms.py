# [3/12/2024]13m out of 20m
""" 
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti < endi <= 10^6
 """
from typing import List


class Solution:
    # Sorting
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        l = len(intervals)
        if l < 2:
            return True
        
        # Sort by starting time
        def byStartTime(e: List[int]):
            return e[0]
        intervals.sort(key=byStartTime)

        for i in range(l-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True
