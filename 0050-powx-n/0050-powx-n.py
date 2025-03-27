class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n < 0):
            n = -n
            x = 1 / x
        power = 1
        while(n != 0):
            if((n & 1) != 0):
                power *= x
            x *= x
            n = n >> 1
        return power