class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 > nums2:
            nums1, nums2 = nums2, nums1
        
        mp = {}
        for num in nums1:
            mp[num] = mp.get(num, 0) + 1
        
        ans = []
        for num in nums2:
            if num in mp and mp[num] > 0:
                ans.append(num)
                mp[num] -= 1
        
        return ans