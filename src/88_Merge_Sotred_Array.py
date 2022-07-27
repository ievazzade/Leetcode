class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        
        for i in range(m + n - 1, -1, -1):
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[i] = nums2[p2]
                    p2 -= 1
            elif p1 >= 0:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
             v
        [1,2,2,3,5,6]
           i
        [2,5,6]
         j
        """
        p1, p2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1