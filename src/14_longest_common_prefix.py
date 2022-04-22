from typing import List

############################################################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i>len(strs[j])-1 or strs[0][i] != strs[j][i]:
                    return result
            result += strs[0][i]
        return result

s = Solution()
result = s.longestCommonPrefix(["flower","flow","flowie"])
print(result)

            