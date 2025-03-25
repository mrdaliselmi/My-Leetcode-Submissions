class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')[::-1]
        res = ""
        for word in words:
            if len(word):
                res+=word+" "
        return res[:len(res)-1]