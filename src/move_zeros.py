from typing import List
class Solution:
    def move_zeros(self, nums: List=[int]):
        n = len(nums)
        j = 0
        for num in nums:
            if (num!=0):
                nums[j]=num
                j += 1
        for x in range(j,len(nums)):
            nums[x]=0
        print(nums)
        
s = Solution()
s.move_zeros([0,2,0,1,4])
# [2,1,4,0,0]
