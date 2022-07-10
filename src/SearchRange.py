class Solution:
    def searchRange(nums, target):
        n = len(nums)
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left] == target:
                pass
            else:
                left += 1
            

