# [3/12/2024]15m out of 20m
# 75%
""" 
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
 """
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distanceMat = [[0 for _ in range(n)] for _ in range(m)]
        checked = set()
        adjacents = set()
        # init adjacents with 0 cells
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    adjacents.add((i,j))
        checked = checked.union(adjacents)  # These are distance 0

        dist = 1
        while len(adjacents) != 0:
            coords = adjacents
            adjacents = set()
            for coord in coords:
                # Set adjacents to dist
                if 0 < coord[0]:
                    target = (coord[0]-1,coord[1])
                    if target not in checked:
                        checked.add(target)
                        distanceMat[target[0]][target[1]]=dist
                        adjacents.add(target)
                if coord[0] < m-1:
                    target = (coord[0]+1,coord[1])
                    if target not in checked:
                        checked.add(target)
                        distanceMat[target[0]][target[1]]=dist
                        adjacents.add(target)
                if 0 < coord[1]:
                    target = (coord[0],coord[1]-1)
                    if target not in checked:
                        checked.add(target)
                        distanceMat[target[0]][target[1]]=dist
                        adjacents.add(target)
                if coord[1] < n-1:
                    target = (coord[0],coord[1]+1)
                    if target not in checked:
                        checked.add(target)
                        distanceMat[target[0]][target[1]]=dist
                        adjacents.add(target)
            dist += 1
        
        return distanceMat