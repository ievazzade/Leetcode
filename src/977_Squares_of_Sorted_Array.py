class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        l, r = 0, len(nums) - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
            res[i] = square * square
        return res