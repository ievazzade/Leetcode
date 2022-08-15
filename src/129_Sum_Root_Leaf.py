# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]
        
        while stack:
            node, cur_number = stack.pop()
            if node:
                cur_number = cur_number * 10 + node.val
                if node.left is None and node.right is None:
                    root_to_leaf += cur_number
                else:
                    stack.append((node.left, cur_number))
                    stack.append((node.right, cur_number))
        
        return root_to_leaf