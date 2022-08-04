# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        [3, 4, 5, 6]
        
        """
        if not root:
            return True
        
        seen_null = False
        queue = deque([root])
        
        while len(queue) > 0:
            node = queue.popleft()
            
            if not node:
                seen_null = True
                continue
            
            if seen_null: return False
            
            queue.append(node.left)
            queue.append(node.right)
        
        return True
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])


#DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        self.count = 0
        self.max_pos = 0
        
        self.dfs(root, 1)
        return self.count == self.max_pos
    
    def dfs(self, root, position):
        if not root:
            return 
        self.count += 1
        self.max_pos = max(self.max_pos, position)
        self.dfs(root.left, 2 * position)
        self.dfs(root.right, 2 * position + 1)