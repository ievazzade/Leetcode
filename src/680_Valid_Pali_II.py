class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                str1 = s[l:r]
                str2 = s[l+1:r+1]
                return str1 == str1[::-1] or str2 == str2[::-1]
            l += 1
            r -= 1
        
        return True