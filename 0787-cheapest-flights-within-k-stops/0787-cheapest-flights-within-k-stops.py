import heapq

class Solution(object):
    def __init__(self):
        self.best_cost = {}
    
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = {}
        for u, v, w in flights:
            if u in graph:
                graph[u][v] = w
            else:
                graph[u] = {v: w}
        heap = [(0, src, k + 1)]
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > 0:
                for neighbor, price in graph.get(node, {}).items():
                    best = self.best_cost.get((neighbor, stops - 1), float('inf'))
                    if cost + price < best:
                        heapq.heappush(heap, (cost + price, neighbor, stops - 1))
                        self.best_cost[(neighbor, stops - 1)] = cost + price
        
        return -1