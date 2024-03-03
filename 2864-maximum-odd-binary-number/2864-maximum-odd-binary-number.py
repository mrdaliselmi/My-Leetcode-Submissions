class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = sorted(s, reverse=True)
        l.append(l.pop(0))
        return "".join(l)