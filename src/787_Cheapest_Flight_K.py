from collections import deque

class Solution:
    def findCheapestPrice(self, n, flights, src , dst, K):
        """
        0: (1, 1), (2, 5)
        1: (2, 1) 
        2: (3, 1)
        3: 
        D = [0, 1, 2, 6]
        graph = ((2,2,2),(3,2,6))
        u, stops , cost= 2, 1, 5
        """
        adj = [[] for _ in range(n)]
        D = [float('inf') for _ in range(n)]
        D[0] = 0

        for u,v,w in flights:
            adj[u].append((v,w))
        
        graph = deque()
        graph.append((src, 0, 0))

        while graph:
            u, stops, cost = graph.popleft()
            if stops >= K + 1: continue
            for v,w in adj[u]:
                if cost + w < D[v]:
                    D[v] = cost + w
                    graph.append((v, stops + 1, cost+w))
        if D[dst] == float('inf'):
            return -1
        else:
            return D[dst]
    
    
    def bellmanFord(self, n, flights, src , dst, K):
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        for i in range(K+1):
            temp_price = prices.copy()
        
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + w < temp_price[v]:
                    temp_price[v] = prices[u] + w
            prices = temp_price
        
        return -1 if prices[dst] == float('inf') else prices[dst]


if __name__ == "__main__":
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    K = 1
    s = Solution()
    ans = s.findCheapestPrice(n, flights, src, dst, K)
    ans2 = s.bellmanFord(n, flights, src, dst, K)
    print(ans, ans2)
