# [3/13/2024]7m out of 20m
# 35%
""" 
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
 """
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        self.ans = []
        self.level = [root]
        while len(self.level) != 0:
            self.bfs()
        return self.ans
    
    def bfs(self):
        self.ans.append([node.val for node in self.level])
        nextLevel = []
        for node in self.level:
            if node.left != None:
                nextLevel.append(node.left)
            if node.right != None:
                nextLevel.append(node.right)
        self.level = nextLevel
        