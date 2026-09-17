class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        res = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
        while len(queue):
            neighbors = []
            for cell in queue:
                x,y = cell
                if x+1 < m and grid[x+1][y] == 1:
                        neighbors.append((x+1,y))
                        grid[x+1][y] = 2
                if x-1 >= 0 and grid[x-1][y] == 1:
                        neighbors.append((x-1,y))
                        grid[x-1][y] = 2
                if y+1 < n and grid[x][y+1] == 1:
                        neighbors.append((x,y+1))
                        grid[x][y+1] = 2
                if y-1 >= 0 and grid[x][y-1] == 1:
                        neighbors.append((x,y-1))
                        grid[x][y-1] = 2
            queue = neighbors
            if len(neighbors):
                res+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return res