from typing import List
##########################################################
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n_h, n_n = len(haystack), len(needle)

        if needle == "": return 0

        for i in range(n_h - n_n + 1):
            for j in range(n_n):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i

        return -1

##########################################################
class Solution2:
    def strStr(self, haystack:str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

##########################################################
s = Solution2()
result = s.strStr("hello", "ll")
print(result)