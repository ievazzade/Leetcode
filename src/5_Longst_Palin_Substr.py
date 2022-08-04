class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_length = 0
        
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_length < r - l + 1:
                    res = s[l:r + 1]
                    max_length = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_length < r - l + 1:
                    res = s[l:r + 1]
                    max_length = r - l + 1
                
                l -= 1
                r += 1
            
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(res):
                res = temp
                
        return res
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]