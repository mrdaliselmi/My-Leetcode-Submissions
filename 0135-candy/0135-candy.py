class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = 0
        candies = [1]* len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]= candies[i-1]+1
        for i in range(len(ratings)- 1,0,-1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i] + 1, candies[i - 1])
            res+=candies[i-1]
        return res + candies[len(ratings)-1]