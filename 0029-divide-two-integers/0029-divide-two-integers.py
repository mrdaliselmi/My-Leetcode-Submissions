class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        result = 0
        if abs(dividend) < abs(divisor):
            return 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 1:
            result = dividend if sign==1 else -dividend
            return min(max(-2**31, result), 2**31 - 1)
        while dividend >= divisor:
            add = 1
            sub = divisor
            while dividend >= sub:
                # print("dividend", dividend, "sub", sub, "add", add)
                dividend -= sub
                result += add
                sub += sub
                add += add
        result = result if sign==1 else -result
        return min(max(-2**31, result), 2**31 - 1)
        