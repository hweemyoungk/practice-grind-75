# [3/20/2024]Retire
""" 
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
 """
from collections import deque
from typing import List, Optional, Tuple


class Solution:
    # Memoization
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights=heights
        self.m=len(heights)
        self.n=len(heights[0])
        self.pacific: List[List[Optional[bool]]] = [[True]*self.n]+[[True]+[None for _ in range(self.n-1)] for _ in range(self.m-1)]
        self.atlantic: List[List[Optional[bool]]] = [[None for _ in range(self.n-1)]+[True] for _ in range(self.m-1)]+[[True]*self.n]
        ans: List[List[int]]=[]
        for i in range(self.m):
            for j in range(self.n):
                if self.flowToPacific(i,j,set()) and self.flowToAtlantic(i,j,set()):
                    ans.append([i,j])
                    
        return ans
    
    def flowToPacific(self, i: int, j: int, prevs: set[Tuple[int,int]]) -> bool:
        if self.pacific[i][j]!=None:
            return self.pacific[i][j]
        
        currHeight=self.heights[i][j]
        for direction in [-1,1]:
            if 0<=i+direction and i+direction<=self.m-1 and (i+direction,j) not in prevs and self.heights[i+direction][j]<=currHeight:
                curr = (i+direction,j)
                prevs.add(curr)
                if self.flowToPacific(i+direction,j,prevs):
                    self.pacific[i][j]=True
                    prevs.remove(curr)
                    return True
                prevs.remove(curr)
            if 0<=j+direction and j+direction<=self.n-1 and (i,j+direction) not in prevs and self.heights[i][j+direction]<=currHeight:
                curr = (i,j+direction)
                prevs.add(curr)
                if self.flowToPacific(i,j+direction,prevs):
                    self.pacific[i][j]=True
                    prevs.remove(curr)
                    return True
                prevs.remove(curr)
                
        self.pacific[i][j]=False
        return False
    
    def flowToAtlantic(self, i: int, j: int, prevs: set[Tuple[int,int]]) -> bool:
        if self.atlantic[i][j]!=None:
            return self.atlantic[i][j]
        
        currHeight=self.heights[i][j]
        for direction in [-1,1]:
            if 0<=i+direction and i+direction<=self.m-1 and (i+direction,j) not in prevs and self.heights[i+direction][j]<=currHeight:
                curr = (i+direction,j)
                prevs.add(curr)
                if self.flowToAtlantic(i+direction,j,prevs):
                    self.atlantic[i][j]=True
                    prevs.remove(curr)
                    return True
                prevs.remove(curr)
            if 0<=j+direction and j+direction<=self.n-1 and (i,j+direction) not in prevs and self.heights[i][j+direction]<=currHeight:
                curr = (i,j+direction)
                prevs.add(curr)
                if self.flowToAtlantic(i,j+direction,prevs):
                    self.atlantic[i][j]=True
                    prevs.remove(curr)
                    return True
                prevs.remove(curr)
                
        self.atlantic[i][j]=False
        return False