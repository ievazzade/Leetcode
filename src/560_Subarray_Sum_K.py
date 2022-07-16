class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [1,  -1,  1,  1,  1,  1] k = 3
        
        sum = 4 
        diff = 4-3 = 1 
        res = 0 + 2 + 2
        
        mp = {0:2, 1:3, 2:1}
        """
        res = 0
        cur_sum = 0
        mp = {0:1}
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            
            res += mp.get(diff, 0)
            
            mp[cur_sum] = 1 + mp.get(cur_sum, 0)
            
        return res