class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = str(bin(n))[2:]
        num = '0'*(32-len(num)) + num
        res = 0
        for i in range(len(num)):
            res += (2**i) * int(num[i])
        return res