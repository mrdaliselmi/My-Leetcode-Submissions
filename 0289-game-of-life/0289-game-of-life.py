class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def count_neighbors(y, x):
            count = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue
                    y1, x1 = y + dy, x + dx
                    if 0 <= y1 < m and 0 <= x1 < n and abs(board[y1][x1]) == 1:
                        count += 1
            return count
        for i in range(m):
            for j in range(n):
                neighbors = count_neighbors(i, j)
                if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0