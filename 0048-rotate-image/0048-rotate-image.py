class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in matrix:
            for i in range(n//2):
                aux = row[i]
                row[i] = row[n-1-i]
                row[n-1-i] = aux
        for i in range(n):
            mx = n
            k = 1+i
            for j in range(n):
                if k <= mx:
                    aux = matrix[i][j]
                    matrix[i][j] = matrix[i+n-k][j+n-k]
                    matrix[i+n-k][j+n-k] = aux
                    k+=1
                else:
                    break