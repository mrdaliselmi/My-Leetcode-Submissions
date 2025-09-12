class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                res = grid[i][j]
                minimum = 0
                if i+1<m and j+1<n:
                    right = dp[i][j+1]
                    down = dp[i+1][j]
                    minimum = min(right, down)
                elif i+1<m:
                    down = dp[i+1][j]
                    minimum = down
                elif j+1<n:
                    right = dp[i][j+1]
                    minimum = right
                dp[i][j] = res+minimum
        return dp[0][0]