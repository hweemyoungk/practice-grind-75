# [3/16/2024]Time up
# 51%/19%
""" 
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
 """
from typing import List, Tuple


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum&1 != 0:
            return False
        subSetSum = totalSum>>1
        self.nums=nums
        self.l = len(nums)
        self.memo: set[Tuple[int, int]] = set()  # Impossible (target, iIncluding) pairs
        return self.dfs(0, subSetSum)
    
    def dfs(self, iIncluding: int, target: int) -> bool:
        if (target, iIncluding) in self.memo:
            return False
        
        # Corner case
        if target==0:
            return True
        if target<0:
            self.memo.add((target, iIncluding))
            return False
        if iIncluding==self.l:
            # All num excluded but still positive target
            return False
        
        # With/Without iIncluding
        if self.dfs(iIncluding+1, target-self.nums[iIncluding]) or self.dfs(iIncluding+1, target):
            return True
        self.memo.add((target, iIncluding))
        return False
        