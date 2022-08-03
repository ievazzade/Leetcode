class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        "agbdba"
           0 1 2 3 4 5
        0  1 1 1 1 3 5
        1    1 1 1 3 3
        2      1 1 3 1
        3        1 1 1
        4          1 1
        5            1
        """
        dp = [[0] * len(s) for _ in range(len(s))]
       
        for i in range(len(s)):
            dp[i][i] = 1
            
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                    
        return dp[0][len(s)-1]