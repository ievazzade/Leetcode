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