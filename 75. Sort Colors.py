""" 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
 """
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        # Cocktail sort
        lo=0
        hi=l-1
        while lo<hi:
            left = nums[lo]
            right = nums[hi]
            if left == 0:
                lo+=1
                continue
            if right == 2:
                hi-=1
                continue
            # left:1 or 2 and right is 0 or 1
            if left == 2:
                nums[lo], nums[hi-1] = nums[hi-1], 2
                hi-=1
                continue
            if right == 0:
                nums[lo+1], nums[hi] = 0, nums[lo+1]
                lo+=1
                continue
            # left==1 and right==1
            iNonOne=lo+1
            while iNonOne<hi:
                n = nums[iNonOne]
                if n == 1:
                    iNonOne+=1
                    continue
                if n == 0:
                    nums[lo], nums[iNonOne] = 0, 1
                    lo+=1
                    iNonOne+=1
                    continue
                nums[iNonOne], nums[hi] = 1, 2
                hi-=1
                iNonOne+=1
                
            return
            

