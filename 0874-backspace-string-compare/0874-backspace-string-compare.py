class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        new_s = ""
        for i in range(n):
            if s[i]=='#':
                new_s = "" if len(new_s)==0 else new_s[:-1]
            else:
                new_s+=s[i]
        n = len(t)
        new_t = ""
        for i in range(n):
            if t[i]=='#':
                new_t = "" if len(new_t)==0 else new_t[:-1]
            else:
                new_t+=t[i]
        if new_s==new_t:
            return True
        return False
        