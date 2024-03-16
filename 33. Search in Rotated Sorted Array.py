# [3/15/2024]Time up
# 40%/23%
""" 
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
 """
from collections import deque
from typing import List


class Solution:
    def binary_search(self, arr: List[int], num: int) -> int:
        # Corner case
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            if num == arr[0]:
                return 0
            return ~0 if num < arr[0] else ~1
        
        left = 0  # Inclusive
        right = len(arr)-1  # Inclusive
        while left <= right:
            mid = (left+right)//2
            medium = arr[mid]
            if num < medium:
                index = mid
                right = mid-1
                continue
            if medium < num:
                index = mid
                left = mid+1
                continue
            # Match: break
            return mid
        # Not found
        return ~index


    def search(self, nums: List[int], target: int) -> int:
        # Corner case
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        
        left=nums[0]
        right=nums[len(nums)-1]
        if left<right:
            # Whole array is ascending
            i=self.binary_search(nums, target)
            return max(-1,i)
        
        mid = len(nums)//2
        medium = nums[mid]
        if medium == target:
            return mid
        if mid==0 or left<medium:
            # Left half(mid inclusive) is ascending
            i=self.binary_search(nums[:mid+1], target)
            if 0<=i:
                return i
            i=self.search(nums[mid+1:], target)
            return -1 if i==-1 else mid+1+i
        if mid==len(nums)-1 or medium<right:
            # Right half(mid inclusive) is ascending
            i=self.binary_search(nums[mid:], target)
            if 0<=i:
                return mid+i
            return self.search(nums[:mid], target)
        return -1

            
