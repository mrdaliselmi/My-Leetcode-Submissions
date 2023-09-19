class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minval=prices[0]
        maxprofit=0
        for price in prices:
            if price<minval:
                minval=price
            elif (price-minval>maxprofit):
                maxprofit=price-minval
        return maxprofit