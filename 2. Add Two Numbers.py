# [3/19/2024]10m out of 25m(40%)
# 73%/91%
""" 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 """
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, Tuple


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        emptyNode=ListNode(0)
        head=None
        prev=None
        carry=0
        while l1!=None or l2!=None or carry!=0:
            if l1==None:
                l1=emptyNode
            if l2==None:
                l2=emptyNode
            curr,carry=self.addTwoNodes(l1,l2,carry)
            if head==None:
                head=curr
            if prev!=None:
                prev.next=curr
            prev=curr
            l1=l1.next
            l2=l2.next
        
        return head
        
    def addTwoNodes(self, l1: ListNode, l2: ListNode, carry: int) -> Tuple[ListNode, int]:
        add=l1.val+l2.val+carry
        return (ListNode(add%10), add//10)

