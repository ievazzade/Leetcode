# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        [  1, 2 ], k = 1
               l                     r
        l = 2
        """
        if not head or not head.next:
            return head
        
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        
        l = k - 1
        r = count - k

        
        count = 0
        node = head
        while node:
            if count == l:
                left = node
            if count == r:
                right = node
            node = node.next
            count += 1
            
        left.val, right.val = right.val, left.val
        return head