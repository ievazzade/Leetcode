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



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        
        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            unique[right], unique[store_index] = unique[store_index], unique[right]
            
            return store_index
            
        def quickSelect(left, right, k_smallest):
            if left == right:
                return
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickSelect(left, pivot_index - 1, k_smallest)
            else:
                quickSelect(pivot_index + 1, right, k_smallest)
        
        n = len(unique)
        quickSelect(0, n - 1, n - k)
        
        return unique[n - k:]