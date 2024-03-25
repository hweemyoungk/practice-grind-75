# [3/24/2024]Time up
# Not optimal solution (Use BST property)
# 27%/9%
""" 
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
All Nodes will have unique values.
 """
# Definition for a binary tree node.
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # 1. During inorder traversal find p and next to p
        # 2. return next to p if its value >p.val, otherwise null
        self.p=p
        isBreak, i, arr =self.inorder(root)
        if isBreak:
            return self.ans
        if i==None:
            # p not found
            return None
        if i==len(arr)-1:
            return None
        if arr[i].val<=arr[i+1].val:
            return None
        return arr[i+1]
    
    def inorder(self, root: Optional[TreeNode]) -> Tuple[bool, Optional[int], List[TreeNode]]:
        if root==None:
            return (False, None, [])
        isBreak, i, arrLeft = self.inorder(root.left)
        if isBreak:
            return (True, None, None)
        if i!=None:
            # Found in left
            if i==len(arrLeft)-1:
                self.ans=root if root.val>self.p.val else None
            else:
                self.ans=arrLeft[i+1] if arrLeft[i+1].val>self.p.val else None
            return (True, None, None)
        isBreak, i, arrRight = self.inorder(root.right)
        if isBreak:
            return (True, None, None)
        if i!=None:
            # Found in right
            if i==len(arrRight)-1:
                return (False, len(arrLeft)+len(arrRight), arrLeft + [root] + arrRight)
            else:
                self.ans=arrRight[i+1] if arrRight[i+1].val>self.p.val else None
                return (True, None, None)
        if root==self.p:
            if len(arrRight)!=0:
                self.ans=arrRight[0] if arrRight[0].val>self.p.val else None
                return (True, None, None)
            else:
                return (False, len(arrLeft), arrLeft + [root] + arrRight)
        return (False, None, arrLeft + [root] + arrRight)
