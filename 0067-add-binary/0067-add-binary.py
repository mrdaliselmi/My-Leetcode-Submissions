class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = max(len(a), len(b))
        a = '0'*(m-len(a)) + a
        b = '0'*(m-len(b)) + b
        r = '0'
        res = ''
        for i in range(m-1,-1,-1):
            first = int(a[i])
            second = int(b[i])
            carry = int(r)
            res = str(int(first ^ second ^ carry)) + res
            r = str(int((first and second) or (carry and (first ^ second))))
        if r=='1':
            res = r+res
        return(res)