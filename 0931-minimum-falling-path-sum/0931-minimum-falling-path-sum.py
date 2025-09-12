class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        res = float('inf')
        for i in range(n-1,-1,-1):
            if i+1<n:
                for j in range(n):
                    mini = matrix[i+1][j]
                    if j<n-1:
                        mini = min(mini, matrix[i+1][j+1])
                    if j>0:
                        mini = min(mini, matrix[i+1][j-1])
                    matrix[i][j]+=mini
                    if i==0:
                        res = min(res, matrix[i][j])
                
        return min(res, matrix[0][0])