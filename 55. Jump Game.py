# [3/25/2024]18m out of 20m
# Not optimal solution
# Note: Jump distance can be 1,...,jump
# 13%/6% (...)
""" 
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
 """
from collections import deque
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        visited=[False]*l
        queue=deque([0])
        queueDistinct=set([0])
        while queue:
            iCurr = queue.popleft()
            queueDistinct.remove(iCurr)
            if l-1==iCurr:
                return True
            if visited[iCurr]:
                continue
            visited[iCurr]=True
            curr = nums[iCurr]
            if curr==0:
                continue
            for iNext in reversed(range(iCurr+1, min(l,iCurr+curr+1))):
                if visited[iNext] or iNext in queueDistinct:
                    continue
                queue.append(iNext)
                queueDistinct.add(iNext)
        return False