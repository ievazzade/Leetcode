class Solution:
    def medianOfTwo(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        m1 = m2 = -1
        if ((n1 + n2) % 2 == 1):
            for count in range((n1 + n2) // 2 + 1):
                if (i != n1 and j != n2):    
                    if nums1[i] > nums2[j]:
                        m1 = nums2[j]
                        j += 1
                    else:
                        m1 = nums1[i]
                        i += 1
                elif (i<n1):
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            return m1         
        else:
            for count in range((n1 + n2) // 2 + 1):
                m2 = m1
                if i != n1 and j != n2:
                    if nums1[i] > nums2[j]:
                        m1 = nums2[j]
                        j += 1
                    else:
                        m1 = nums1[i]
                        i += 1
                elif i < n1:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            return (m1 + m2) / 2 

if __name__ == "__main__":
    nums1 = [1,2,3,4]
    nums2 = [5,6,7,8]
    s = Solution()
    ans = s.medianOfTwo(nums1, nums2)
    print(ans)