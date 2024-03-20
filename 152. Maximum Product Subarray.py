# [3/19/2024]Time up
# 79%/86%
""" 
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 """
import math
from typing import List, Tuple


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMin=nums[0]
        localMax=nums[0]
        globalMax=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            localMin,localMax=min(n,localMin*n,localMax*n),max(n,localMin*n,localMax*n)
            globalMax=max(globalMax,localMax)
        return globalMax