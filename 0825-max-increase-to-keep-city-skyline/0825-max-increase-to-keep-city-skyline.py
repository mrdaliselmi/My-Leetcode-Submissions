class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def max_row(grid, i):
            return max(grid[i])
        def max_column(grid, j):
            return max([grid[i][j] for i in range(len(grid))])
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += min(max_row(grid, i), max_column(grid, j))-grid[i][j]
        return result