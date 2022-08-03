class Solution:
    def trap(self, height: List[int]) -> int:
        """
                [0,1,0,2,1,0,1,3,2,1,2,1]
        left =  [0,1,1,2,2,2,2,3,3,3,3,3]
        right = [3,3,3,3,3,3,3,3,2,2,2,1]
                [0,0,1,0,1,2,1,0,0,1,0,0]
        """
        
        if len(height) == 0:
            return 0
        ans = 0
        n = len(height)
        
        left_max = [0] * n
        left_max[0] = height[0]
        
        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        
        for i in range(1, n):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        """
                [0,1,0,2,1,0,1,3,2,1,2,1]
        left =  [0,1,1,2,2,2,2,3,3,3,3,3]
        right = [3,3,3,3,3,3,3,3,2,2,2,1]
                [0,0,1,0,1,2,1,0,0,1,0,0]
        """
        if len(height) == 0:
            return 0
        ans = 0
        l, r = 0, len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans += right_max - height[r]
                r -= 1
        return ans