# [3/12/2024]29m out of 30m
# Not optimal solution
# 5%/79%
""" 
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
 """
from collections import deque
from typing import Dict, List

class Node:
    def __init__(self, val: int) -> None:
        self.val=val
        self.neighbors: List['Node']=[]

class Solution:
    # Topologically sortable
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:
            return True
        # 2<=n
        # Draw graph
        nodes:Dict[int,Node]={}
        for edge in edges:
            i=edge[0]
            j=edge[1]
            if i not in nodes:
                nodes[i]=Node(i)
            if j not in nodes:
                nodes[j]=Node(j)
            nodes[i].neighbors.append(nodes[j])
            nodes[j].neighbors.append(nodes[i])
        # Get indegree==1
        queue=deque([node for node in nodes.values() if len(node.neighbors)==1])
        nDone=0
        while queue:
            nDone+=1
            curr=queue.popleft()
            if len(curr.neighbors)==0:
                break
            next=curr.neighbors[0]
            next.neighbors.remove(curr)
            if len(next.neighbors)==1:
                queue.append(next)
        return nDone==n