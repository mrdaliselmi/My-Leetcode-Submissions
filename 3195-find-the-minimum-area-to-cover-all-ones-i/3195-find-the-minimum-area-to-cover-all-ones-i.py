class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        uppermost = m
        leftmost = n
        rightmost = 0
        bottommost = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i < uppermost:
                        uppermost = i
                    if j > rightmost:
                        rightmost = j
                    if i > bottommost:
                        bottommost = i
                    if j < leftmost:
                        leftmost = j
        area = (bottommost - uppermost +1) * (rightmost-leftmost+1)
        return area