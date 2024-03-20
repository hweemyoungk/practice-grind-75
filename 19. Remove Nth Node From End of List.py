# [3/20/2024]Time up
# 75%/45%
""" 
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
 """

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        iCurr=1
        targetPrev=None
        while True:
            if iCurr==n+1:
                targetPrev=head
            if curr.next!=None:
                # Move next
                curr=curr.next
                iCurr+=1
                if targetPrev!=None:
                    targetPrev=targetPrev.next
                continue
            # curr is tail
            if targetPrev==None:
                # iCurr is number of nodes
                if iCurr<n:
                    # Nothing to remove
                    return head
                # iCurr==n
                # Remove head
                head=head.next
                return head
            targetPrev.next=targetPrev.next.next
            return head
            
