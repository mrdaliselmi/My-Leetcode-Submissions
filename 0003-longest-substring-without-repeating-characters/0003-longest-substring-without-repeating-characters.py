class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        count = 0
        mx = 0
        for i in range(len(s)):
            if s[i] in d:
                n = d[s[i]]
                count = i - n
                for k,v in d.items():
                    if v <= n:
                        del d[k]
            else:
                count+=1
            d[s[i]]=i
            mx = max(mx,count)
        return mx