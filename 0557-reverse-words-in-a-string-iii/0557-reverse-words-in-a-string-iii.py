class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = [i[::-1] for i in s.split()]
        return ' '.join(l)
        