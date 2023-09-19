class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x<0 else 0
        num = (str(x)[sign::])[::-1]
        num = float(num) * ((-1)**sign)
        if (num<-2**31 or num>2**31-1):
            return 0
        return int(num)
