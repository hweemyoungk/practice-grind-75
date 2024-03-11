# [3/1/2024]13m
""" 
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
 """
from typing import List


class Solution:
    # # Recursive
    # def search(self, nums: List[int], target: int) -> int:
    #     if nums[len(nums) - 1] < target or target < nums[0]:
    #         return -1
        
    #     medIdx = len(nums) // 2
    #     medium = nums[medIdx]
    #     if target == medium:
    #         return medIdx
    #     if target < medium:
    #         return self.search(nums[:medIdx], target)
    #     i = self.search(nums[medIdx:], target)
    #     if i == -1:
    #         return -1
    #     return medIdx + i
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0  # Inclusive
        right = len(nums)  # Exclusive
        while True:
            if nums[right - 1] < target or target < nums[left]:
                return -1
            mid = (left + right) // 2
            medium = nums[mid]
            if target == medium:
                return mid
            if target < medium:
                right = mid
                continue
            left = mid + 1
        
