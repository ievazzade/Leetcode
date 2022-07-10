from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 1

        while (i < len(A) and A[i] > A[i-1]):
            i += 1
        
        if (i==1 or i == len(A)):
            return False
        
        while (i < len(A) and A[i] < A[i-1]):
            i += 1
        
        return i == len(A)

s = Solution()
val = s.validMountainArray([1,2,3,4,5,3,1])
print(val)