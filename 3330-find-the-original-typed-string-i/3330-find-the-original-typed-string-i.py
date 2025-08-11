class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 1
        curr = 0
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                curr+=1
            elif curr > 0:
                res+=curr
                curr = 0
        if curr > 0:
            res+=curr
        return res