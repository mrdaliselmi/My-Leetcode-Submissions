class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        flat = [num for row in grid for num in row]
        mod = flat[0] % x
        for num in flat:
            if not(num % x == mod):
                return -1
        flat.sort()
        mid = flat[len(flat) // 2]
        res = 0
        for num in flat:
            res += abs(mid - num) // x
        return res