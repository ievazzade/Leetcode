from typing import Optional
# Definition for singly-linked list.
from curses.ascii import SO


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
                  0   1   2   3   4
        head = [  1 <- 2 <-  3 <-  4,  5]
                                   p   cur
                 con tail
        left = 1 
        right = 3

                  
        1. traverse LList till l
            * keep track of previous
        2. reverse till r
        3. prev.next = r
        4. l.next = n
        
        """
        if not head or not head.next:
            return head
        
        cur, prev = head, None
        
        while left > 1 :
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1
        
        con, tail = prev, cur
        
        while right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1
        
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        
        return head
        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    ans = s.reverseBetween(head, 2, 4)
    while ans:
        print(ans.val, end= ' ')
        ans= ans.next