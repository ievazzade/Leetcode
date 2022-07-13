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



class Solution:
    def isValidPalindrome(self, s, k):
        cache = {}
        res = self.helper(s, cache, 0, len(s) - 1, k)
        return res
    
    def helper(self, s, cache, start, end, k):
        if (start, end, k) in cache:
            return cache[(start, end, k)]
        while start < end:
            if s[start] == s[end]:
                cache[(start, end, k)] = self.helper(s, cache, start+1, end-1)
            else:
                if not k:
                   cache[(start, end, k)] == False
                else:
                    