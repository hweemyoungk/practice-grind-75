# [3/12/2024]8m out of 15m
""" 
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
 """
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 1
        
        # return 2 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return self.getDepth(root)
    
    def getDepth(self, root: TreeNode) -> int:
        leftDepth = 0 if not root.left else self.getDepth(root.left)
        rightDepth = 0 if not root.right else self.getDepth(root.right)
        return 1 + max(leftDepth, rightDepth)
