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
