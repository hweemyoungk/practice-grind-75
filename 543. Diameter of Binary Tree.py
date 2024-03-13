# [3/12/2024]Time up: 35m out of 30m
""" 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
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
    # Recursive
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None or (root.left == None and root.right == None):
            return 0
        
        self.maxDiameter = 0
        self.getDepth(root)
        return self.maxDiameter
        
    
    def getDepth(self, root: Optional[TreeNode]) -> int:
        if root == None or (root.left == None and root.right == None):
            return 0
        
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        depth = 1 + max(leftDepth, rightDepth)
        
        if root.left != None and root.right != None:
            self.maxDiameter = max(self.maxDiameter, 2 + leftDepth + rightDepth)
        elif root.left != None:
            self.maxDiameter = max(self.maxDiameter, 1 + leftDepth)
        elif root.right != None:
            self.maxDiameter = max(self.maxDiameter, 1 + rightDepth)
        
        return depth


