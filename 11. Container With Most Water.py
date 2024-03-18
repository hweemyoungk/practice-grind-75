# [3/18/2024]19m out of 35m
# 72%/67%
# Need to prove by this algorithm, answer reflects global optimal: https://leetcode.com/problems/container-with-most-water/solutions/6089/Anyone-who-has-a-O(N)-algorithm/comments/7268/
""" 
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
 """
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        ptr1=0
        ptr2=n-1
        ans=0
        w=n-1
        while ptr1<ptr2:
            h1=height[ptr1]
            h2=height[ptr2]
            h=min(h1,h2)
            area=w*h
            ans=max(ans,area)
            if h1<h2:
                ptr1+=1
            else:
                ptr2-=1
            w-=1
        return ans