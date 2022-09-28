class Solution:
    def makePalindrome(self, s: str) -> bool:
        changes = 0
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                changes += 1
                if changes > 2:
                    return False
            l += 1
            r -= 1
        return True