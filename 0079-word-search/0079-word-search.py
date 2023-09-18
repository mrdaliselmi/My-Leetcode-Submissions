import numpy as np
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def DFS(i, j, k):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or (board[i][j] != word[k]):
                return False
            if (k == len(word) - 1):
                return True
            tmp, board[i][j] = board[i][j], '1'
            res = DFS(i+1, j, k+1) or DFS(i-1, j, k+1) or DFS(i, j+1, k+1) or DFS(i, j-1, k+1)
            board[i][j] = tmp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if DFS(i, j, 0):
                    return True
        return False