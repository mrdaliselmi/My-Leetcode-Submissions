class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==3:
            return 2
        if n==2:
            return 1
        threes = n // 3
        twos = (n % 3) // 2
        ones = (n % 3) % 2
        # print(threes,twos,ones)
        if ones:
            if twos:
                twos-=1
                threes+=1
            else:
                twos+=2
                threes-=1
            ones = 0
        # print(threes,twos,ones)
        return (2**twos)*(3**threes)