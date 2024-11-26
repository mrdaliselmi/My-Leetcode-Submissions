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
        res = []
        for i in range(n):
            if not(i in weak):
                res.append(i)
        return -1 if len(res) != 1 else res[0]