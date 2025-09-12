class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                ways = 0
                if obstacleGrid[i][j]:
                    continue
                if i+1<m and j+1<n:
                    right = dp[i][j+1]
                    down = dp[i+1][j]
                    ways+= right+down
                elif i+1<m:
                    down = dp[i+1][j]
                    ways+= down
                elif j+1<n:
                    right = dp[i][j+1]
                    ways+= right
                else:
                    ways = 1
                dp[i][j] = ways
        return dp[0][0]