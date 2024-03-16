# [3/16/2024]11m out of 30m
# 24%/36%
""" 
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
 """
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # DFS
        self.l=len(nums)
        self.nums=nums
        return self.dfs(0)
    
    def dfs(self, i: int) -> List[List[int]]:
        # Merge array of subsets with/without nums[iStart]
        if i == self.l:
            return [[]]
        n = self.nums[i]
        arrs = self.dfs(i+1)
        # Clone elements
        arrs.extend([[n] + arr[:] for arr in arrs])
        return arrs