# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        [3,9,20,null,null,15,7]
        
        {0:[3], -1: [9], 1: [20]}
        """
        ans = {}
        res = []
        if not root:
            return ans
        
        queue = [[0, root]]
        
        while queue:
            length = len(queue)
            for i in range(length):
                level, node = queue.pop(0)
                if level not in ans:
                    ans[level] = [node.val]
                else:
                    ans[level].append(node.val)
                if node.left:
                    queue.append([level - 1, node.left])
                if node.right:
                    queue.append([level + 1, node.right])
        
        list_key = sorted(ans)
        for key in list_key:
            res.append(ans[key])
        return res