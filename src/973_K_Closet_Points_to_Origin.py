class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        [[3,3],[5,-1],[-2,4]]
        
        {18:0,  20:2, 26:1}
        """

        ans = []
        def distance(x, y):
            return x**2 + y**2
        
        mp = {i:distance(x, y) for i, [x, y] in enumerate(points)}
        mp_new = dict(sorted(mp.items(), key=lambda x: x[1]))
        for key , value in mp_new.items():
            ans.append(points[key])
            if len(ans) == k:
                break
        
        return ans

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = self.squared_distance)
        
        return points[:k]
    
    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2

# Max Heap
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if k == len(points):
            return points
        
        def sqr_distance(point):
            return point[0]**2 + point[1]**2
       
        heap = [(-sqr_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        
        for i in range(k, len(points)):
            dist = - sqr_distance(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))
        
        return [points[i] for (_, i) in heap]

# Binary Search
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [self.euclidean_distance(point) for point in points]
        
        remaining = [i for i in range(len(points))]
        
        low, high = 0, max(distances)
        
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                remining = closer
                high = mid
            else:
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low= mid
            
        return [points[i] for i in closest]
        
        
    
    def split_distances(self, remaining, distances, mid):
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
            
        return [closer, farther]
    
    
    def euclidean_distance(self, point):
        return (point[0] ** 2 + point[1] ** 2)