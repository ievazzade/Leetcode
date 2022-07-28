class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        
        start = count = 0
        
        while count < n:
            current, prev = start, nums[start]
            while True:
                idx = (current + k) % n
                nums[idx], prev = prev, nums[idx]
                current = idx
                count += 1
                if current == start:
                    break
            start += 1
                
                
            
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        
        def reverse(nums, l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)