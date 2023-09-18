class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charset=set(s)
        a={a:s.count(a) for a in charset}
        charset=set(t)
        b={a:t.count(a) for a in charset}
        return a==b