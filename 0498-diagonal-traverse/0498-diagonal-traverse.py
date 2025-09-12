class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        upward = True
        i, j = 0, 0
        result = []
        while i<m and j<n:
            while (0<=i<m) and (0<=j<n):
                end = (i,j)
                result.append(mat[i][j])
                if upward:
                    i-=1
                    j+=1
                else:
                    i+=1
                    j-=1
            upward = not(upward)
            i,j = end[0], end[1]
            if upward:
                if j == 0 and i<m-1:
                    i+=1
                elif i==m-1:
                    j+=1
            else:
                if i == 0 and j<n-1:
                    j+=1
                elif j==n-1:
                    i+=1
        return result