# [3/15/2024]21m out of 25m
# 84%
""" 
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.
 """
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pStack = deque()
        self.search(root, p, pStack)
        qStack = deque()
        self.search(root, q, qStack)
        commonAncestor = None
        for i in range(min(len(pStack), len(qStack))):
            pNode = pStack.popleft()
            qNode = qStack.popleft()
            if pNode == qNode:
                commonAncestor = pNode
                continue
            break
        return commonAncestor
    
    def search(self, root: Optional[TreeNode], target: TreeNode, stack: deque[TreeNode]) -> bool:
        if root == None:
            return False
        stack.append(root)
        if root.val == target.val:
            return True
        if self.search(root.left, target, stack):
            return True
        if self.search(root.right, target, stack):
            return True
        stack.pop()
        return False
