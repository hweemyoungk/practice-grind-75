# [3/14/2024]Time up
# 65%/85%
""" 
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
 """
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        m = len(grid)
        self.m = m
        n = len(grid[0])
        self.n = n
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if self.visited[i][j]:
                    continue
                target = grid[i][j]
                if target == '1':
                    # Unvisited land
                    ans+=1
                self.dfs(i,j)
        return ans
    
    def dfs(self, i: int, j: int) -> bool:
        # out of range
        if i < 0 or i > self.m-1 or j < 0 or j > self.n-1:
            return False
        
        if self.visited[i][j]:
            return False
        
        self.visited[i][j] = True
        val = self.grid[i][j]
        if val != '1':
            return False
        
        # Propagate
        self.dfs(i-1,j)
        self.dfs(i+1,j)
        self.dfs(i,j-1)
        self.dfs(i,j+1)
        return True
