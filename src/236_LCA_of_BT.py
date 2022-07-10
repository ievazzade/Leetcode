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