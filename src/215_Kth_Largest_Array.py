# Sorting the array
# O(nlogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# Heap of size K
#O(nlogk)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [3,2,1,5,6,4]
         
        """
        heap = [nums[i] for i in range(k)]
        heapq.heapify(heap)
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        
        return heap[0]

# QuickSelect
# Average O(n); Worst O(n^2)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [3,2,1,4,6,5]
                 l r
                 i
               p         
         pivot = 
        [1,2,3,4,5,6]
        """
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
        
        return quickSelect(0, len(nums) - 1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
         0,1,2,3,4,5
        [3,2,1,5,6,4]
        """
        k = len(nums) - k
        def partition(nums, l, r):
            pivot, p = nums[r], l
            while l < r:
                if nums[l] < pivot:
                    nums[l], nums[p] = nums[p], nums[l]
                    p += 1
                    
                l += 1
            nums[r], nums[p]  = nums[p], nums[r]
            return p
        
        l,  r = 0, len(nums) - 1        
        
        while l <= r:
            pi = partition(nums, l, r)
            if pi == k:
                return nums[pi]
            elif pi < k:
                l = pi + 1
            else:
                r = pi - 1
                