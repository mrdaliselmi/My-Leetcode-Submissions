class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(p)> len(s):
            return res
        p_occ = Counter(p)
        occ = Counter(s[0:len(p)])
        for i in range(len(s)-len(p)+1):
            if i > 0:
                occ[s[i-1]] -= 1
                if occ[s[i-1]] == 0:
                    del occ[s[i-1]]
                occ[s[i+len(p)-1]] += 1
            if occ == p_occ:
                res.append(i)
        return res