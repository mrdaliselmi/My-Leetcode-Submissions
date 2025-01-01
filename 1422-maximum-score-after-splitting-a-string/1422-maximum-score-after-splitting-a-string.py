class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeros = 0
        ones = s.count("1")
        res = 0 
        for c in s:
            if c == "1":
                ones -= 1
            else:
                zeros += 1
            res = max(res, zeros + ones)
        return res
