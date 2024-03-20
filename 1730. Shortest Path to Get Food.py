# [3/20/2024]14m out of 30m
# 93%/69%
""" 
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

 

Example 1:


Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.
Example 2:


Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.
Example 3:


Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.
 """
from typing import List, Tuple


class Solution:
    def findStart(self, grid) -> Tuple[int,int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='*':
                    return (i,j)

    # BFS+memoization
    def getFood(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False]*n for _ in range(m)]
        coords: List[Tuple[int,int]]=[self.findStart(grid)]
        dist=-1
        while coords:
            dist+=1
            nextCoords=[]
            for i,j in coords:
                if i<0 or i>m-1 or j<0 or j>n-1 or visited[i][j]:
                    continue
                visited[i][j]=True
                value = grid[i][j]
                if value=='#':
                    return dist
                if value=='X':
                    continue
                # value=='O'or'*'
                nextCoords.append((i-1,j))
                nextCoords.append((i+1,j))
                nextCoords.append((i,j-1))
                nextCoords.append((i,j+1))
            coords=nextCoords
        # Not found
        return -1
