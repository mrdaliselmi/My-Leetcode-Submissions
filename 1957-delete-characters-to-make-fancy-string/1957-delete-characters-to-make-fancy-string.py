class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s)<3:
        #     return s
        curr = 1
        i = 1
        res = s[0]
        while i < len(s):
            if s[i]==s[i-1]:
                curr+=1
            else:
                curr = 1
            if curr == 3:
                curr = 2
            else:
                res+=s[i]
            i+=1
        return res