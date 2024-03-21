# [3/20/2024]Time up
# Not optimal solution
# 76%/9%
""" 
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
 """
from typing import Dict, List, Tuple


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums=nums
        self.l=len(nums)
        self.dp=[None]*self.l
        self.dp[self.l-1]=1
        for i in range(self.l):
            self.dp[i]=self.lengthOfLISStartsAt(i)
        return max(self.dp)

    def lengthOfLISStartsAt(self, start: int) -> int:
        if self.dp[start]!=None:
            return self.dp[start]
        upper=None
        curr=self.nums[start]
        for i in range(start+1,self.l):
            if curr<self.nums[i]:
                upper=self.nums[i]
                break
        if upper==None:
            self.dp[start]=1
            return 1
        
        maxLength=1
        for j in range(i,self.l):
            target=self.nums[j]
            if upper<target or target<=curr:
                continue
            # Lower the upper
            upper=target
            maxLength=max(maxLength, self.lengthOfLISStartsAt(j)+1)
        self.dp[start]=maxLength
        return maxLength
        