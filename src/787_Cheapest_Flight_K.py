class Solution:
    def findCheapestPrice(self, n, flights, src , dst, K):
        prices = [float('inf')] * n
        prices[src] = 0
        
        for i in range(K + 1):
            tmpPrices = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float('inf') else -1


class Solution:
    def findCheapestPrice(self, n, flights, src , dst, K):
        adj = {u: [] for _ in range(n)}
        for f in flights:
            adj[f[0]].append((f[1], f[2]))

        q = []
        q.append((0, src, K + 1))
        
        while len(q) > 0:
            top = heapq.heqpop(q)
            price, cur, stop  = top
            if dst == cur: return price
            if stop > 0:
                for v in adj[cur]:
                    heapq.heappush(q, (price + v[1], v[0], stop - 1))

        return -1