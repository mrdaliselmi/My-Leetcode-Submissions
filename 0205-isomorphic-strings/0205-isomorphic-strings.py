class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t):
            d = {}
            tset = set()
            for i in range(len(s)):
                if not(s[i] in d):
                    if t[i] in tset:
                        return False
                    d[s[i]]=t[i]
                    tset.add(t[i])
            s = [d[key] for key in s]
            s = ''.join(s)
            if s==t:
                return True
        return False