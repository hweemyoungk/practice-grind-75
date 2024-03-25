# [3/25/2024]Time up
# Not optimal
# 8%/60%
""" 
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
 """
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        # Top-down merge sort
        mid=self.getMid(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left,right)
    
    def merge(self, sorted1: Optional[ListNode], sorted2: Optional[ListNode]):
        dummyHead=ListNode()
        curr=dummyHead
        while not (sorted1==None and sorted2==None):
            if sorted1==None:
                curr.next=sorted2
                curr=curr.next
                sorted2=sorted2.next
                continue
            if sorted2==None:
                curr.next=sorted1
                curr=curr.next
                sorted1=sorted1.next
                continue
            if sorted1.val<sorted2.val:
                curr.next=sorted1
                curr=curr.next
                sorted1=sorted1.next
                continue
            curr.next=sorted2
            curr=curr.next
            sorted2=sorted2.next
        return dummyHead.next
    
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead=ListNode()
        dummyHead.next=head
        prevSlow=dummyHead
        slow=head
        fast=head
        while fast!=None:
            fast=fast.next
            if fast==None:
                break
            slow=slow.next
            prevSlow=prevSlow.next
            fast=fast.next
        prevSlow.next=None
        return slow