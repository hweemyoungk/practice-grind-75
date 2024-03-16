# [3/16/2024]25m out of 25m(100%)
# 68%/64%
""" 
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
 """
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        # n=len(matrix[0])
        isIncreasing=True
        isHorizontal=True
        iMin=0
        iMax=m-1
        i=0
        ans=[]
        while iMin<=iMax:
            if isHorizontal:
                if isIncreasing:
                    # horizontally increasing
                    ans.extend(matrix[i])
                    i+=1
                    iMin+=1
                    isHorizontal=False
                    continue
                # horizontally decreasing
                ans.extend(reversed(matrix[i]))
                i-=1
                iMax-=1
                isHorizontal=False
                continue
            # vertically increasing
            if isIncreasing:
                if len(matrix[iMin])==0:
                    break
                for k in range(iMin,iMax+1):
                    ans.append(matrix[k].pop())
                i=iMax
                isIncreasing=False
                isHorizontal=True
                continue
            # vertically decreasing
            if len(matrix[iMax])==0:
                break
            for k in reversed(range(iMin,iMax+1)):
                ans.append(matrix[k].pop(0))
            i=iMin
            isIncreasing=True
            isHorizontal=True
            continue

        return ans

