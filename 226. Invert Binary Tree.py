# [3/11/2024]6mins
""" 
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 """
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    """ Invert leaves recursively and returns root node """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        # Recursion
        originalRight = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(originalRight)
        return root
