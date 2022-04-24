from typing import Optional
##################################################
# Defenition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

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
        if slow.next is not None:
            slow.next = slow.next.next
        return head