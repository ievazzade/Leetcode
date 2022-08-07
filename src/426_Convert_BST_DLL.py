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
        """
        prev = 2
        node = 3
        stack = [4]
        """
        
        if not root:
            return None
        
        dummy = (0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right