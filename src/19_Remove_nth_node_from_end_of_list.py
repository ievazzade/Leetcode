from typing import Optional
##################################################
# Defenition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
##################################################
# One pass algorithm (Two Pointer Technique)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head 
        fast = head
        for i in range(n):
            if fast.next is None:
                head  = head.next
                return head
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
##################################################
# Two pass algorithm (Two Pointer Technique)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        new_head = dummy_head = head
        while head:
            size += 1
            head =  head.next
        stop = size - n
        if stop == 0: return new_head.next
        for i in range(stop-1):
            dummy_head = dummy_head.next
        dummy_head.next = dummy_head.next.next
        return new_head   
