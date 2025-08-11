class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        powers=[]
        i = 0
        while n:
            lsb = n & 1
            if lsb == 1:
                powers.append(2**i)
            i += 1
            n = n >> 1

        for i in range(len(powers)):
            if i > 0:
                powers[i] = powers[i-1] * powers[i]

        res = []
        for interval in queries:
            left, right = interval[0], interval[1]
            if left == 0:
                res.append((powers[right]) % (10**9 + 7))
            elif left == right:
                res.append((powers[right] // powers[left - 1])% (10**9 + 7))
            else:
                res.append((powers[right] // powers[left - 1])% (10**9 + 7))

        return res