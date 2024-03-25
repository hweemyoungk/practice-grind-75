# [3/25/2024]34m out of 35m
# Editorial
# Not optimal
# 56%/58%
""" 
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300
 """
from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x==0 and y==0:
            return 0
        # Bidirectional BFS
        directions=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        coords1=[(0,0)]
        coords2=[(x,y)]
        numSteps1=-1
        numSteps2=-1
        visited1=set()
        visited2=set()
        while True:
            numSteps1+=1
            nextCoords1=[]
            for coord in coords1:
                if coord in visited2:
                    return numSteps1+numSteps2
                if coord in visited1:
                    continue
                visited1.add(coord)
                for i,j in directions:
                    nextCoords1.append((coord[0]+i,coord[1]+j))
            coords1=nextCoords1
            numSteps2+=1
            nextCoords2=[]
            for coord in coords2:
                if coord in visited1:
                    return numSteps1+numSteps2
                if coord in visited2:
                    continue
                visited2.add(coord)
                for i,j in directions:
                    nextCoords2.append((coord[0]+i,coord[1]+j))
            coords2=nextCoords2
