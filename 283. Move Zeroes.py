# [3/12/2024]Retired: Couldn't implement optimal solution
# 30%
""" 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Could you minimize the total number of operations done?
 """
from typing import List


class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     i=0
    #     l=len(nums)
    #     while i < l:
    #         n = nums[i]
    #         if n != 0:
    #             i+=1
    #             continue
    #         nums.pop(i)
    #         nums.append(n)
    #         l-=1
    # Swap operations with 2 pointers
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        
        curNonZeroPtr = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                curNonZeroPtr = i
                break
        if curNonZeroPtr == -1:
            # Zeros only
            return
        
        # Init lastNonZeroPtr
        lastNonZeroPtr = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                lastNonZeroPtr = i-1
                break
        
        if lastNonZeroPtr == len(nums) - 1:
            # Non zeros only
            return

        while lastNonZeroPtr != len(nums) and curNonZeroPtr != len(nums):
            if nums[curNonZeroPtr] == 0 or lastNonZeroPtr == curNonZeroPtr:
                curNonZeroPtr += 1
                continue

            nonZero = nums[curNonZeroPtr]
            nums[lastNonZeroPtr+1] = nonZero
            nums[curNonZeroPtr] = 0
            lastNonZeroPtr += 1
