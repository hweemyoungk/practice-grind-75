# [3/14/2024]Time up
# 14%/70%
""" 
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
 """
from collections import deque
from typing import List


class Solution:
    # BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # Scan rotten oranges
        targets = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    targets.append((i-1,j))
                    targets.append((i+1,j))
                    targets.append((i,j-1))
                    targets.append((i,j+1))
                    continue
                if grid[i][j] == 0:
                    visited[i][j] = True
        if all([all([visit for visit in row]) for row in visited]):
            # Every cell is either rotten or empty
            return 0
        
        # If any unvisited cell, that is fresh orange
        time=0
        while targets:
            nextTargets = []
            for target in targets:
                i=target[0]
                j=target[1]
                if i<0 or i>m-1 or j<0 or j>n-1:
                    continue
                if visited[i][j]:
                    # Already rotten or empty
                    continue
                # Fresh orange
                visited[i][j]=True
                nextTargets.append((i-1,j))
                nextTargets.append((i+1,j))
                nextTargets.append((i,j-1))
                nextTargets.append((i,j+1))
            if len(nextTargets) == 0:
                # Nothing has been newly rotten
                break
            targets = nextTargets
            time+=1
        
        if any([any([not visit for visit in row]) for row in visited]):
            return -1
        return time
                
                