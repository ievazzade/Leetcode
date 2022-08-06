class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        [10, 6, 8, 5, 11, 9]
    ans [3,  1, 2, 1, 1, 0]
        
        visible = 2
        stack = [11,  ]
        """
        ans = [0] * len(heights)
        stack = []
        
        for i in range(len(heights) -1, -1, -1):
            height = heights[i]
            visible = 0
            
            while stack and height > stack[-1]:
                visible += 1
                stack.pop()
            
            if stack:
                visible += 1
            
            ans[i] = visible
            stack.append(height)
                
        
        return ans


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        [10,6,8,5,11,9]
            ^     ^
        max_h = 8
        visible = 1  
        """
        ans = []
        for i in range(len(heights)):
            max_h = 0
            visible = 0
            for j in range(i + 1, len(heights)):
                if heights[j] > heights[i]:
                    visible += 1
                    break
                if heights[j] > max_h:
                    visible += 1
                    max_h = heights[j]
            ans.append(visible)
        
        return ans