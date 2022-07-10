class Solution:
    def median(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 != n2:
            return "not same length"
        m1 = 0
        m2 = 0
        # Edge case

        if n1 < 2:
            return (nums1[0]+ nums2[0]) / 2 if n1 == 1 else -1
        
        # Base case
        elif n1 == 2:
            return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) // 2
        
        else:
            m1 = self.getMedian(nums1)
            m2 = self.getMedian(nums2)
            # final median
            if m1 == m2: return m1
            elif m1 < m2:
                if n1%2 == 0:
                    return self.median(nums1[n1//2:], nums2[:n2//2])
                else:
                    return self.median(nums1[n1//2:], nums2[:n2//2 + 1])
            else:
                if n1%2 == 0:
                    return self.median(nums1[:n1//2], nums2[n2//2])
                else:
                    return self.median(nums1[:n1//2 + 1], nums2[n2//2:])
    
    def getMedian(self, arr):
        n = len(arr)
        if n%2 == 0:
            return (arr[n//2] + arr[n//2 - 1]) / 2
        else:
            return arr[n//2]


if __name__ == "__main__":
    # nums1 = [1, 12, 15, 26, 38]
    # nums2 = [2, 13, 17, 30, 45]

    nums1 = [1, 2, 3, 6]
    nums2 = [4, 6, 8, 10]
    s = Solution()
    ans = s.median(nums1, nums2)
    print(ans)