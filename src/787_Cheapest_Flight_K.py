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