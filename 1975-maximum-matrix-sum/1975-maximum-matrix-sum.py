class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        minimum = float('inf')
        count = 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] < 0:
                    count +=1
                absolute = abs(matrix[i][j])
                res += absolute
                minimum = min(minimum, absolute)
        if count % 2:
            return res - minimum*2
        return res