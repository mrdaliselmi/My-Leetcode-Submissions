from collections import deque

class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        n, m = len(grid), len(grid[0])
        
        def neighbors(i, j):
            for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= ni < n and 0 <= nj < m:
                    yield ni, nj
        
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)
        
        visited = [[False] * m for _ in range(n)]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited[0][0] = True
        points = 0
        
        for idx, q in queries_sorted:
            while heap and heap[0][0] < q:
                val, i, j = heapq.heappop(heap)
                points += 1
                for ni, nj in neighbors(i, j):
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(heap, (grid[ni][nj], ni, nj))
            res[idx] = points
            
        return res