class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows

        while up < down:
            pt = (up + down) // 2
            if matrix[pt][-1] < target:
                up = pt + 1
            else:
                down = pt

        if up == rows:
            return False
        
        s=set(matrix[up])
        if target in s:
            return True
        return False