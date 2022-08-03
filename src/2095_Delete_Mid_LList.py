# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
                     v
        [1,3,4,7,1,2]
             ^
                 v
        [1,2,3,4,5]
           ^
           
        [1, 2]
        
        """
        if not head or not head.next:
            return None
        
        prev = None
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        
        return head