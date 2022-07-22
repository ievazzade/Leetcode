"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        first, last = None, None
        
        def dfs(node):
            nonlocal first, last
            
            if not node:
                return
            
            if node.left:
                dfs(node.left)
            
            if not first:
                first = node
            else:
                last.right = node
                node.left = last                
            
            last = node
            
            if node.right:
                dfs(node.right)
        if not root:
            return None
        
        dfs(root)
        
        first.left = last
        last.right = first
        
        return first