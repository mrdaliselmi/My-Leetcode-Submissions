class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m,n= len(grid), len(grid[0])
        visited = [[0]*len(grid[0]) for i in range(len(grid))]
        islands = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1") and (visited [i][j] == 0):
                    islands +=1
                    queue = [(i,j)]
                    while len(queue):
                        x,y = queue.pop()
                        visited[x][y] = 1
                        if x+1 < m:
                            if grid[x+1][y] == "1" and visited[x+1][y] == 0:
                                queue.append((x+1,y))
                        if x-1 >= 0:
                            if grid[x-1][y] == "1" and visited[x-1][y] == 0:
                                queue.append((x-1,y))
                        if y+1 < n:
                            if grid[x][y+1] == "1" and visited[x][y+1] == 0:
                                queue.append((x,y+1))
                        if y-1 >= 0:
                            if grid[x][y-1] == "1" and visited[x][y-1] == 0:
                                queue.append((x,y-1))
        return islands
                        