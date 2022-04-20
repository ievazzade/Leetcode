from typing import List

class Solution:
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


s = Solution()
result = s.strStr("hello", "ll")
print(result)