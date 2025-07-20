class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit = (left>>i) & 1
            if bit == 0:
                continue
            
            remainder = left % (1<<(i+1))
            diff = (1<<(i+1)) - remainder
            if right - left < diff:
                res |= (1<<i)
        
        return res