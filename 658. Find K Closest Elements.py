# [3/23/2024]24m out of 30m
# Not optimal solution
# 40%/33%
""" 
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
 """
from collections import deque


class Solution:
    from typing import List

    # Returns index of num if found or complement of index for num to be inserted at.
    # Array must already been sorted in ascending order.
    def binary_search(self, arr: List[int], num: int) -> int:
        l = len(arr)
        # Corner case
        if l == 0:
            return ~0
        if l == 1:
            if num == arr[0]:
                return 0
            return ~0 if num < arr[0] else ~1
        
        lo = 0  # Inclusive
        hi = l-1  # Inclusive
        while lo <= hi:
            mid = (lo+hi+1)//2
            medium = arr[mid]
            if num < medium:
                index = mid-1
                hi = mid-1
                continue
            if medium < num:
                index = mid+1
                lo = mid+1
                continue
            # Match: break
            return mid
        # Not found
        if index==-1:
            return ~0
        # if index==l:
        #     return ~l
        return ~index

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans=deque()
        queue=deque()
        iLeft=None
        iRight=None
        index=self.binary_search(arr, x)
        # what if ~index==len(arr)
        if index<0:
            iLeft=~index-1
            iRight=~index
            index=~index
            count=0
        else:
            iLeft=index-1
            iRight=index+1
            ans.append(arr[index])
            count=1
        l = len(arr)
        while count!=k:
            dLeft=None
            dRight=None
            if 0<=iLeft and iLeft<=l-1:
                dLeft=x-arr[iLeft]
            if 0<=iRight and iRight<=l-1:
                dRight=arr[iRight]-x
            if dLeft==None and dRight==None:
                break
            elif dLeft==None:
                queue.append(iRight)
                iRight+=1
            elif dRight==None:
                queue.append(iLeft)
                iLeft-=1
            elif dLeft<=dRight:
                queue.append(iLeft)
                iLeft-=1
            else:
                queue.append(iRight)
                iRight+=1
            iTarget=queue.popleft()
            if iTarget<index:
                ans.appendleft(arr[iTarget])
            else:
                ans.append(arr[iTarget])
            count+=1
            continue
        return ans