"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OriginaltoCopy = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            OriginaltoCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = OriginaltoCopy[cur]
            copy.next = OriginaltoCopy[cur.next]
            copy.random = OriginaltoCopy[cur.random]
            cur = cur.next
            
        return OriginaltoCopy[head]


"""
DFS Like Graph keep track of visited
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}
        
        def dfs(node):
            if node == None:
                return None
            
            if node in visited:
                return visited[node]
            
            copy = Node(node.val, None, None)
            
            visited[node] = copy
            
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            
            return copy
        
        return dfs(head)