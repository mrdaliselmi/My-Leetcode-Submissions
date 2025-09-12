class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = -1
        for i in range(m):
            for j in range(n):
                up = dp[i][j+1]
                left = dp[i+1][j]
                up_left = dp[i][j]
                val = matrix[i][j]
                mini = min(up, left, up_left)
                if val == "1":
                    dp[i+1][j+1] = 1 + mini
                else:
                    dp[i+1][j+1]= 0
                res = max(res, dp[i+1][j+1])
        return res**2