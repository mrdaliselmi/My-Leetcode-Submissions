class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(i, j, remaining, visited):
            if board[i][j] != remaining[0]:
                return False

            if len(remaining) == 1:
                return True

            visited.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < m
                    and 0 <= nj < n
                    and (ni, nj) not in visited
                    and dfs(ni, nj, remaining[1:], visited)
                ):
                    return True

            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word, set()):
                    return True

        return False