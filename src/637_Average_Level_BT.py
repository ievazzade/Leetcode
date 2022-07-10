class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        [3,9,20,null,null,15,7]
        
        [[3, 1], [29, 2], [22, 2]]
        """
        
        ans = []
        
        def helper(node, level):
            if not node:
                return
            if len(ans) >= level + 1:
                ans[level][0] += node.val
                ans[level][1] += 1
            else:
                ans.append([node.val, 1])
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        # return ans
        res = []
        for i in range(len(ans)):
            res.append(ans[i][0]/ans[i][1])
        return res

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        [3,9,20,null,null,15,7]
        
        [[3, 1], [29, 2], [22, 2]]
        """
        
        res = []
        if not root:
            return res
        queue = deque([root])
        
        while queue:
            sum_level = 0
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                sum_level += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(sum_level/length)
        
        return res