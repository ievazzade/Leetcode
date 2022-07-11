class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root):
        """
        [1,2,3,4,6,5,7]

        """
        result = []
        if not root:
            return result
        cache = {}
        self.minC, self.maxC = 0, 0
        
        def dfs(node, r, c):
            if not node:
                return
            
            if c in cache:
                cache[c].append([r, node.val])
            else:
                cache[c] = [[r, node.val]]
            
            self.minC = min(self.minC, c)
            self.maxC = max(self.maxC, c)

            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)
        
        dfs(root, 0, 0)
        for c in range(self.minC, self.maxC + 1):
            col = sorted(cache[c], key= lambda x: (x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)
        return result

if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(6)
    tree.right.left = Node(5)
    tree.right.right = Node(7)
    s = Solution()
    ans = s.verticalTraversal(tree)
    print(ans)