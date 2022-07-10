from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,1,1,2,2,3]
        
        htable = [[]]
        maxf = 
        idx = 
        """
        hash_table={}
        
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
       
        q = []
        for key, value in hash_table.items():
            heapq.heappush(q, (-1*value, key))
        
        ans = []    
        for _ in range(k):
            top = heapq.heappop(q)
            ans.append(top[1])
        
        return ans

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    s = Solution()
    ans = s.topKFrequent(nums, 2)
    print(ans)