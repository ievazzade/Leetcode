class Solution:
    def lowestCommonAncestor(root, p, q):
        def recurse_tree(curr_node):
            if not curr_node:
                return False
            
            left = recurse_tree(curr_node.left)
            right = recurse_tree(curr_node.right)

            mid = curr_node == p or curr_node == q

            if mid + left + right >= 2:
                self.ans = curr_node
            
            return mid or left or right
        
        recurse_tree(root)
        return self.ans

# https://www.youtube.com/watch?v=py3R23aAPCA&t=924s
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p,q)
        
        if left == None: return right
        if right == None: return left
        
        return root