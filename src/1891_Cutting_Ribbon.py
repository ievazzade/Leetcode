class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        """
        [9,7,5]
        
        l = 6
        r = 9
        
        mid = 5
        """
        start = 1
        end = max(ribbons)
        
        while start <= end:
            mid = start + (end - start) // 2
            res = 0
            for ribbon in ribbons:
                res += ribbon//mid
            
            if res >= k:
                start = mid + 1
            else:
                end = mid - 1
        
        return end