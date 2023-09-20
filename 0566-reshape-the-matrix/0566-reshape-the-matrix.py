import numpy as np
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if ((len(mat)*len(mat[0]))==r*c):
            return np.reshape(mat,(r,c))
        return mat