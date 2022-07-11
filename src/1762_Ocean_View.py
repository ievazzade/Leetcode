class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_length = 0
        res = []
        for i in reversed(range(len(heights))):
            if heights[i] > max_length:
                res.append(i)
                max_length = max(heights[i], max_length)
        
        return res[::-1]

class Solution:
    def findBuildings(heights):
        ans = []
        for i in range(len(heights)):
            while ans and heights[ans[i]] <= heights[i]:
                ans.pop()
            ans.append(i)
        return ans