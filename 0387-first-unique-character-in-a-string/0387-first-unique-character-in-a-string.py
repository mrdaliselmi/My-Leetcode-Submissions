class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique={}
        charset=set()
        for i in range(len(s)):
            if s[i] not in charset:
                unique[s[i]] = i
                charset.add(s[i])
            elif s[i] in unique:
                unique.pop(s[i])
        if(len(unique)>0):
            idx=list(unique.values())
            minidx=min(idx)
            return minidx
        else:
            return -1