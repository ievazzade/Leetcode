from typing import List

############################################################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        shortest_string = min([len(x) for x in strs])

        for char in range(shortest_string):
            pass