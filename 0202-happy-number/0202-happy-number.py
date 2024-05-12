class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sumOfSquares(num):
            res = 0
            while (num%10 != num):
                res += (num%10)**2
                num //= 10
            return res + num**2
        # ----- MAFFS -----
        # while (n != 1 and n != 4):
        #     n = sumOfSquares(n)
        # if n == 1:
        #     return True
        # return False
        # ----- HashMap ----
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sumOfSquares(n)
        return n == 1