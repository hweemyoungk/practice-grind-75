# [3/14/2024]Time up
# 23%/22%
""" 
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
 """
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # stack = []
        # return self.dfs(root, stack)
        return self.dfsMinMax(root.left, None, root.val) and self.dfsMinMax(root.right, root.val, None)
        
    
    def dfsMinMax(self, root: Optional[TreeNode], lower: Optional[int], upper: Optional[int]) -> bool:
        if root == None:
            return True
        # for (node, isRight) in stack:
        # Compare upper for left, lower for right
        if (upper != None and root.val>=upper) \
            or (lower != None and root.val<=lower):
            return False
        # Left
        if not self.dfsMinMax(root.left, lower, min(upper, root.val) if upper != None else root.val):
            return False
        # Right
        if not self.dfsMinMax(root.right, max(lower, root.val) if lower != None else root.val, upper):
            return False
        return True
    
    def dfs(self, root: Optional[TreeNode], stack: List[Tuple[TreeNode, bool]]) -> bool:
        if root == None:
            return True
        for (node, isRight) in stack:
            if (not isRight and root.val>=node.val) or (isRight and root.val<=node.val):
                return False
        stack.append((root, False))
        if not self.dfs(root.left, stack):
            return False
        stack.pop()
        stack.append((root, True))
        if not self.dfs(root.right, stack):
            return False
        stack.pop()
        return True
            