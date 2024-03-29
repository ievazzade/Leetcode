# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pFound = False
        self.qFound = False
        ans = self.LCA(root, p, q)
        return ans if (self.pFound and self.qFound) else None
    
    def LCA(self, root, p, q):
        if not root:
            return None

        left = self.LCA(root.left, p, q)
        right = self.LCA(root.right, p, q)

        if root == p:
            self.pFound = True
            return root
        
        if root == q:
            self.qFound = True
            return root

        if left == None: return right
        if right == None: return left

        return root
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound = False
        qFound = False
        
        def dfs(node):
            nonlocal pFound, qFound
            
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)            
            
            if node == p:
                pFound = True
                return node
            if node == q:
                qFound = True
                return node
            
            if left == None: return right
            if right == None: return left
            
            return node
        
        ans = dfs(root)
        
        return ans if (pFound and qFound) else None
