class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idxs = []
        for i, num in enumerate(self.nums):
            if num == target:
                idxs.append(i)
        
        return idxs[random.randint(0, len(idxs) - 1)]
                

