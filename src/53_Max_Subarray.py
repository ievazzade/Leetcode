class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        [-2,1,-3,4,-1,2,1,-5,4]
          ^
        [1,2,3, -1]
                 ^
        cur_sum = 5
        max_sum = 6
        """
        cur_sum = 0
        max_sum = nums[0]
        
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        
        return max_sum