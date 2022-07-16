"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            temp = Node(insertVal)
            temp.next = temp
            return temp
        
        prev, cur = head, head.next
        toInsert = False
        
        while True:
            if prev.val <= insertVal <= cur.val:
                toInsert = True
            
            elif prev.val > cur.val:
                if prev.val <= insertVal or insertVal <= cur.val:
                    toInsert = True
                
            if toInsert:
                prev.next = Node(insertVal, cur)
                return head
            
            prev = cur
            cur = cur.next
            
            if prev == head:
                toInsert = True