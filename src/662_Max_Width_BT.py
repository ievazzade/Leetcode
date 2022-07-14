class Solution:
    def widthOfBinaryTree(root):
        if not root: return 0
        result = 1
        queue = deque([(root, 0)])
        while len(queue) > 0:
            count = len(queue)
            start = queue[0][1]
            end = queue[-1][1]
            result = max(result, end - start + 1)
            for i in range(count):
                p = queue[0]
                idx = p[1] - start
                queue.popleft()
                if p[0].left != None:
                    queue.append((p[0].left, 2 * idx + 1))
                if p[0].right != None:
                    queue.appedn((p[0].right, 2 * idx + 2))
        
        return result
