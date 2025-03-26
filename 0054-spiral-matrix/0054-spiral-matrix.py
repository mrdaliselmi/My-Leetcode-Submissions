class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        max_up, max_left, max_down, max_right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        while max_up <= max_down and max_left <= max_right:
            for i in range(max_left, max_right + 1):
                res.append(matrix[max_up][i])
            max_up += 1
            for i in range(max_up, max_down + 1):
                res.append(matrix[i][max_right])
            max_right -= 1
            if max_up <= max_down:
                for i in range(max_right, max_left - 1, -1):
                    res.append(matrix[max_down][i])
                max_down -= 1
            if max_left <= max_right:
                for i in range(max_down, max_up - 1, -1):
                    res.append(matrix[i][max_left])
                max_left += 1
        return res