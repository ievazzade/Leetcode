from re import A


class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nonzeros[i] = nums[i]

    def dotProduct(self, vec):
        result = 0
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result

v1 = SparseVector([2,0,0,3])
v2 = SparseVector([3,0,0,0])
ans = v1.dotProduct(v2)
print(ans)


# BINARY SEARCH

class SparseVector:
    def __init__(self, nums):
        self.nonzero = [(i, val) for i, val in enumerate(nums) if val != 0]

    def dotProduct(self, vec):

        def binarySearch(arr, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] == target:
                    return mid
                elif arr[mid][0] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        
        a, b = self.nonzero, vec.nonzero

        if len(a) > len(b):
            a, b = b, a
        
        total = 0
        j = 0

        for i, n in a:
            idx = binarySearch(b, j, len(b) - 1, i)
            if idx != -1:
                total += n * b[idx][1]
                j = idx + 1
        return total