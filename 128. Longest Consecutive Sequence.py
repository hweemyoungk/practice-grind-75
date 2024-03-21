# [3/21/2024]Time up
# Can be much simpler
# 38%/5%
""" 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
 """
from typing import Dict, List, Optional

class Graph:
    def __init__(self, solution: 'Solution', edge1: 'Node', edge2: 'Node', size: int) -> None:
        self.edges:List[Node]=[edge1, edge2]
        self.size=size
        solution.updateAns(size)

class Node:
    def __init__(self, solution: 'Solution', val: int, graph: Optional[Graph]=None) -> None:
        self.val=val
        self.graph:Graph=Graph(solution, self, self, 1) if graph==None else graph
        self.prev:Optional[Node]=None
        self.next:Optional[Node]=None

class Solution:
    def updateAns(self, newSize: int):
        self.ans=max(self.ans,newSize)

    def linkGraphs(self, i:int,j:int) -> Graph:
        # Link prev
        self.hashmap[j].prev=self.hashmap[i]
        self.hashmap[i].next=self.hashmap[j]
        currGraph=self.hashmap[j].graph
        currEdges=currGraph.edges
        currEdges.remove(self.hashmap[j])
        targetGraph = self.hashmap[i].graph
        targetEdges=targetGraph.edges
        targetEdges.remove(self.hashmap[i])
        newSize = targetGraph.size+currGraph.size
        newGraph = Graph(self, targetEdges[0], currEdges[0], newSize)
        for edge in newGraph.edges:
            edge.graph=newGraph
        return newGraph
    
    def longestConsecutive(self, nums: List[int]) -> int:
        self.ans=0
        self.hashmap:Dict[int,Node]={}
        for curr in nums:
            if curr in self.hashmap:
                continue
            self.hashmap[curr]=Node(self, curr)
            # Merge graph
            if curr-1 in self.hashmap:
                self.linkGraphs(curr-1, curr)
            if curr+1 in self.hashmap:
                self.linkGraphs(curr, curr+1)
        return self.ans