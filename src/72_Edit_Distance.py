class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp = [[0] * (n + 1) for _ in range((m + 1))]
        
        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(m + 1):
            dp[i][0] = i
        

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if word1[col - 1] == word2[row - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
        print(dp)        
        return dp[m][n]