class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(' ')
        if len(pattern)==len(s):
            d = {}
            sset = set()
            for i in range(len(s)):
                if not(pattern[i] in d):
                    if s[i] in sset:
                        return False
                    d[pattern[i]]=s[i]
                    sset.add(s[i])
            pattern = [d[key] for key in pattern]
            pattern = ' '.join(pattern)
            s = ' '.join(s)
            if pattern==s:
                return True
        return False