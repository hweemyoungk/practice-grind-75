# [3/12/2024]13m out of 20m
""" 
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
 """
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Fast/slow pointers
    # What about cycle?
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Corner case
        if not head:
            return None
        
        fast = head
        slow = head
        while True:
            if not fast.next:
                return slow
            fast = fast.next
            slow = slow.next
            if not fast.next:
                return slow
            fast = fast.next
            
            # Cycle detection
            if fast == slow:
                break
        
        # Cycle detected
        slow = head
        prevFast = None
        while fast != slow:
            slow = slow.next
            prevFast = fast
            fast = fast.next
        # Now fast, slow pointers at first node of cycle
        # Break cycle and run again
        prevFast.next = None
        return self.middleNode(head)
