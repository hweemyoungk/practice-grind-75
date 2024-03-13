# [3/12/2024]Time up: 40m out of 25m
# 160%
""" 
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
 """
from typing import List


class Solution:
    def __merge(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]
    

    # Bin insert
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Corner case
        if len(intervals) == 0:
            return [newInterval]
        
        left = 0  # Inclusive
        right = len(intervals)  # Exclusive
        while left < right:
            mid = (left+right)//2
            medium = intervals[mid]
            if newInterval[0] < medium[0]:
                index = mid
                right = mid
                continue
            if medium[0] < newInterval[0]:
                index = mid + 1
                left = mid + 1
                continue
            # Match: break
            index = mid
            break
        # Insert newInterval to mid
        # Check need merge
        merged = newInterval
        needMerge = False
        mergeStart = index
        mergeEnd = index-1
        # Check previous interval overlaps
        if 0 < index:
            prev = intervals[index-1]
            if newInterval[0] <= prev[1]:
                # Overlaps
                needMerge = True
                merged = self.__merge(prev, merged)
                mergeStart = index-1
        # Check next intervals overlap
        for i in range(index, len(intervals)):
            next = intervals[i]
            if next[0] <= newInterval[1]:
                # Overlaps
                needMerge = True
                merged = self.__merge(next, merged)
                mergeEnd = i
                continue
            break

        if needMerge:
            # Remove interval[mergeStart:mergeEnd(inclusive)]
            for i in range(mergeEnd-mergeStart+1):
                intervals.pop(mergeStart)
            # Insert merged at mergeStart
            intervals.insert(mergeStart, merged)
            return intervals
        
        # Merge not needed: just insert
        intervals.insert(index, newInterval)
        return intervals
        