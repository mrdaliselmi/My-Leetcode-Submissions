class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = s.lower()
        res = []
        for c in l:
            if c.isalnum():
                res.append(c)
        res = ''.join(res)
        return res[:len(res)//2] == res[-1:-(len(res)//2 + 1):-1]