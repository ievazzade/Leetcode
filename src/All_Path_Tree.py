class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self):
        res = []
        def helper(root):
            nonlocal res
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res
    
    def max_sum_path(self):
        max_sum = 0
        max_path = []

        def traverse(node, cur_sum, path):
            nonlocal max_sum
            nonlocal max_path

            if not node:
                return
            cur_sum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_path = list(path[:])
            else:
                traverse(node.left, cur_sum, path)
                traverse(node.right, cur_sum, path)
            path.pop()

        traverse(root, 0, [])
        return max_path
    
    def all_path(self):
        paths= []
        
        def traverse(node, path):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    paths.append(path[:])    
                else:
                    traverse(node.left, path)
                    traverse(node.right, path)
                path.pop()


        traverse(root, [])
        return paths

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(root.inorder())
    print(root.max_sum_path())
    print(root.all_path())
