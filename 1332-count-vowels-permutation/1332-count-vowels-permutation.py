class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[],[1,1,1,1,1]]
        a,e,i,o,u=0,1,2,3,4
        modulo=10**9+7
        for j in range(2,n+1):
            dp.append([0,0,0,0,0])
            dp[j][a]=(dp[j-1][u]+dp[j-1][i]+dp[j-1][e]) % modulo
            dp[j][e]=(dp[j-1][a]+dp[j-1][i]) % modulo
            dp[j][i]=(dp[j-1][e]+dp[j-1][o]) % modulo
            dp[j][o]=(dp[j-1][i]) % modulo
            dp[j][u]=(dp[j-1][o]+dp[j-1][i]) % modulo
        return sum(dp[n]) % modulo