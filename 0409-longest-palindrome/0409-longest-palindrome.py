from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = Counter(s)
        odd = False
        res = 0
        for key, value in d.items():
            if (value % 2 == 0):
                res+=value
            else:
                res+=value-1
                odd = True
        return res+1 if odd else res