class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0]*(rowIndex+1)
        result[0]=1
        for i in range(1,(rowIndex+1)):
            c = result[:]
            for j in range(1,i+1):
                c[j]=result[j]+result[j-1]
            result=c[:]
        return result
                