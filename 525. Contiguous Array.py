# [3/21/2024]Editorial
# 82%/89%
""" 
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 """
from typing import Dict, List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        globalMax=0
        countToLeftmostIdx:Dict[int,int]={0:-1}
        for i,n in enumerate(nums):
            if n==0:
                count-=1
            else:
                count+=1
            if count not in countToLeftmostIdx:
                countToLeftmostIdx[count]=i
                continue
            # count in countToLeftmostIdx
            globalMax=max(globalMax,i-countToLeftmostIdx[count])
        return globalMax