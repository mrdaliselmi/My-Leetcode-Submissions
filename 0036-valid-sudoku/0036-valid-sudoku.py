import numpy as np
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check(l):
            l=[i for i in l if i!="."]
            if (len(l)!=len(set(l))):
                return False
            return True
        
        # checking rows
        for row in board:
            if not(check(row)):
                return False
            
        #cheking cols
        board=((np.array(board)).transpose()).tolist()
        for col in board:
            if not(check(col)):
                return False
            
        #cheking squares
        for i in range(9):
            square = []
            r=3*(i%3-1)
            c=3*(i//3)
            for row in range(r,r+3):
                for col in range(c,c+3):
                    square+=board[row][col]
            if not(check(square)):
                return False
        return True