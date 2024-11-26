class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        weak = set()
        for edge in edges:
            if not(edge[1] in weak):
                weak.add(edge[1])
        found = False
        res = -1
        for i in range(n):
            if not(i in weak):
                if found:
                    res = -1
                    break
                else:
                    res=i
                    found=True
        return res