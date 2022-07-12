from functools import lru_cache


class Solution:
    def isValidPalindrome(self, s, k):
        if s == s[::-1]:
            return True
        
        @lru_cache(None)
        def helper(s, l, r, k):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if k != 0:
                        return helper(s, l+1, r, k-1) or helper(s, l, r-1, k-1)
                    else:
                        return False
            
            return True
        
        return helper(s, 0, len(s) - 1, k)