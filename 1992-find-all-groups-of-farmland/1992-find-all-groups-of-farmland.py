class Solution(object):
    m = 0
    n = 0
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        def f(i,j):
            if i < 0 or j < 0 or i  > len(land) - 1 or j > len(land[0]) - 1:
                return 
            
            if land[i][j] == 0:
                return 
            
            land[i][j] = 0
            self.m = max(self.m,i)
            self.n = max(self.n,j)
            f(i + 1,j)
            f(i,j + 1)

        for i in range(len(land)):
            for j in range((len(land[0]))):
                if land[i][j] == 1:
                    self.m = i
                    self.n = j
                    f(i,j)
                    res.append([i,j,self.m,self.n])
        return res