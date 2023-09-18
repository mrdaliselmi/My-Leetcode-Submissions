class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        RESULTS = [0]*38
        RESULTS[1],RESULTS[2] = 1,1
        def recursion(n):
            if n<3:
                return RESULTS[n]
            else:
                if RESULTS[n]:
                    return RESULTS[n]
                else:
                    sol = recursion(n-1)+recursion(n-2)+recursion(n-3)
                    RESULTS[n]=sol
                    return sol
        return recursion(n)