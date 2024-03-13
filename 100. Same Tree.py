# [3/12/2024]16m out of 20m
""" 
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
 """
# Definition for a binary tree node.
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q:
            nodes1 = [p]
            nodes2 = [q]
            while not (len(nodes1) == 0 and len(nodes2) == 0):
                isSame, nodes1, nodes2 = self.bfs(nodes1, nodes2)
                if not isSame:
                    return False
            return True
        # Either is null
        return False
        
    def bfs(self, nodes1: List[TreeNode], nodes2: List[TreeNode]) -> Tuple[bool, List[TreeNode], List[TreeNode]]:
        newNodes1 = []
        newNodes2 = []
        for n1, n2 in zip(nodes1, nodes2):
            if not n1 and not n2:
                # no need to append
                continue
            if n1 and n2:
                if n1.val != n2.val:
                    return (False, [], [])
                newNodes1.extend([n1.left, n1.right])
                newNodes2.extend([n2.left, n2.right])
                continue
            # Either is null
            return (False, [], [])
        return (True, newNodes1, newNodes2)