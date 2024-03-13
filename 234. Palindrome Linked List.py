# [3/12/2024]Time up: 30m out of 20m
# 150%
""" 
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
 """
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Get length
        totalNodes = 1
        curr = head
        while curr.next:
            totalNodes+=1
            curr = curr.next
        
        # Reverse half
        prev = head
        curr = head.next
        next = head.next.next
        
        head.next = None

        mid = totalNodes // 2
        i=0
        while i < mid-1:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
            i+=1
        
        # Even nodes
        if totalNodes % 2 == 0:
            # Backwards from prev
            # Forwards from curr
            while prev != None or curr != None:
                if prev.val != curr.val:
                    return False
                prev = prev.next
                curr = curr.next
            return True
        
        # Odd nodes
        # Backwards from prev
        # Forwards from next
        while prev != None or next != None:
            if prev.val != next.val:
                return False
            prev = prev.next
            next = next.next
        return True
            