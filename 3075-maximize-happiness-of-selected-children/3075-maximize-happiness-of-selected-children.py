class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        res=0
        for i in range(k):
            child=happiness.pop()
            res+=max(0, child-i)
        return res