class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n= len(prices)
        profit = 0
        for i in range(n):
            if i+1<n and prices[i+1]>prices[i]:
                    profit += prices[i+1]-prices[i]
        return profit