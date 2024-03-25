# [3/25/2024]13m out of 30m
# 98%/53%
""" 
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
 """
from collections import deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Draw graph
        neighbors: List[List[int]]=[[] for _ in range(n)]
        for (a,b) in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        # Traverse
        # BFS
        visited=[False]*n
        numComponents=0
        for i in range(n):
            if visited[i]:
                continue
            # i is in new component
            numComponents+=1
            queue=deque([i])
            queueDistinct=set([i])
            while queue:
                curr=queue.popleft()
                queueDistinct.remove(curr)
                if visited[curr]:
                    continue
                visited[curr]=True
                for neighbor in neighbors[curr]:
                    if neighbor in queueDistinct:
                        continue
                    queue.append(neighbor)
                    queueDistinct.add(neighbor)
        return numComponents