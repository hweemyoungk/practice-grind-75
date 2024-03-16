# [3/15/2024]15m out of 30m
# 42%/79%
""" 
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
 """
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.l = len(nums)
        self.backtrack([], nums)
        return self.ans

    def backtrack(self, arr: List[int], remains: List[int]):
        none=True
        for i in range(self.l):
            n = remains[i]
            if n == None:
                continue
            none=False
            arr.append(n)
            remains[i]=None
            self.backtrack(arr, remains)
            arr.pop()
            remains[i]=n
        
        if none:
            self.ans.append(arr[:])
