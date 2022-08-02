class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        a b c d e
        
        a c e
        
        func(0,0):
            option1 = func(1, 0)        
            option2 = 1 + func(1,1)
            
               [f(0,0),  f(1,0)]
        option1 f(1,0)    f(2,0)
        option2 1+f(1,1)
        """
        
        @lru_cache(maxsize = None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            option1 = memo_solve(p1 + 1, p2)
            
            first_occur  = text2.find(text1[p1], p2)
            option2 = 0
            if first_occur != -1:
                option2 = 1 + memo_solve(p1+1, first_occur + 1)
            
            return max(option1, option2)
        
        return memo_solve(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize = None)
        def memoLCS(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            if text1[p1] == text2[p2]:
                return 1 + memoLCS(p1 + 1, p2 + 1)
            
            else:
                return max(memoLCS(p1 + 1, p2), memoLCS(p1, p2 + 1))
        
        return memoLCS(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dp[row][col] = dp[row + 1][col + 1] + 1
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        
        return dp[0][0]