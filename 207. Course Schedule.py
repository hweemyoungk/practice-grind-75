# [3/14/2024]27m out of 30m(90%)
# 53%/58%
""" 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
 """
from typing import List


class Solution:
    # Cycle detection
    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack = [False] * numCourses
        visited = [False] * numCourses
        outbounds = [[] for _ in range(numCourses)]
        for direction in prerequisites:
            outbounds[direction[0]].append(direction[1])

        for node in range(numCourses):
            if self.dfs(node, outbounds, stack, visited):
                return False
        return True
    
    # True if cycle detected
    def dfs(self, node: int, outbounds: List[List[int]], stack: List[bool], visited: List[bool]) -> bool:
        if stack[node]:
            return True
        # Not in stack
        if visited[node]:
            return False
        # Not fully processed
        
        # Add to stack
        stack[node] = True
        for outbound in outbounds[node]:
            if self.dfs(outbound, outbounds, stack, visited):
                return True
        # Set to fully processed
        visited[node] = True
        # Remove from stack
        stack[node] = False
        return False
