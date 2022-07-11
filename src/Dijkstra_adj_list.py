from dis import dis
from queue import PriorityQueue
class Solution:
    def dijkstra(self, n, graph):
        """
        graph: [[u,v,w]]
        """
        adj_list = [[] for _ in range(n)]
        for i in range(len(graph)):
            u, v, w = graph[i]
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        D = [float('inf') for _ in range(n)]
        D[0] = 0
        visited = [False] * n
        
        pq = PriorityQueue()
        pq.put((0,0)) # (dist, node)

        while not pq.empty():
            (dist, u) = pq.get()
            visited[u] = True

            for v in adj_list[u]:
                if visited[v[0]] == False:
                    old_cost = D[v[0]]
                    new_cost = D[u] + v[1]
                    if new_cost < old_cost:
                        pq.put((new_cost, v[0]))
                        D[v[0]] = new_cost
        
        return D



if __name__ == "__main__":
    s = Solution()
    graph = [(0, 1, 4), (0, 6, 7), (1, 6, 11), (1, 7, 20), (1, 2, 9), (2, 3, 6), (2, 4, 2), (3, 4, 10), (3, 5, 5), (4, 5, 15), (4, 7, 1), (4, 8, 5), (5, 8, 12), (6, 7, 1), (7, 8, 3)]
    ans = s.dijkstra(9, graph)
    print(ans)