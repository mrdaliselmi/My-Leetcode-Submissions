class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(boxGrid), len(boxGrid[0])
        res = [['.'] * m for _ in range(n)]

        for i in range(m):
            e = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    e = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][e] = '#'
                    e -= 1

        for i in range(m):
            for j in range(n):
                res[j][m - i - 1] = boxGrid[i][j]

        return res