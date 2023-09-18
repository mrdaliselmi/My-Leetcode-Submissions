from operator import add
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = list()
        if numRows == 0: return result
        result.append([1])
        if numRows == 1: return result
        for i in range(1, numRows):
            new = map(add, (result[i-1] + [0]), ([0] + result[i-1]))
            result.append(new)
    
        return result