# [3/18/2024]Time up
# 45%/91%
""" 
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
 """
from collections import deque
from typing import Dict, List, Optional, Tuple


class Solution:
    # Topological sort
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        if n==2:
            return [0,1]
        # Draw graph
        nodes: List[Node] = [Node(i) for i in range(n)]
        for edge in edges:
            node0=nodes[edge[0]]
            node1=nodes[edge[1]]
            node0.neighbors.append(node1)
            node1.neighbors.append(node0)
        
        remaining=n
        currNodes = [node for node in nodes if len(node.neighbors)==1]
        while currNodes:
            if remaining==2:
                return [node.val for node in currNodes]
            nextNodes=[]
            for curr in currNodes:
                remaining-=1
                neighbor = curr.neighbors[0]
                # curr.neighbors.clear()
                neighbor.neighbors.remove(curr)
                l = len(neighbor.neighbors)
                if l==1:
                    nextNodes.append(neighbor)
                elif l==0:
                    return [neighbor.val]
            currNodes=nextNodes
        

class Node:
    def __init__(self, val: int) -> None:
        self.val=val
        self.neighbors: List[Node] = []
