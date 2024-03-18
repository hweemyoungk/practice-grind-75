# [3/16/2024]13m out of 20m
# 69%/93%
""" 
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 """
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # BFS
        return self.bfs(root)
    
    def bfs(self, root: TreeNode) -> List[int]:
        ans=[]
        nodes=[root]
        while nodes:
            rightMost=False
            nextNodes=[]
            for node in nodes:
                if rightMost==False:
                    rightMost=True
                    ans.append(node.val)
                if node.right != None:
                    nextNodes.append(node.right)
                if node.left != None:
                    nextNodes.append(node.left)
            nodes = nextNodes
        return ans