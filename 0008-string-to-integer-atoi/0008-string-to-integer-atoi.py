class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        t = list(range(10))
        t = [str(i) for i in t]
        t = set(t)
        result=""
        start = 0
        if len(s) and s[0] in ["-", "+"]:
            result += s[0]
            start = 1
        for i in range(start,len(s)):
            if s[i] in t:
                result += s[i]
            else:
                break
        if result == "" or result == "-" or result == "+":
            return 0
        result = int(result)
        return min(max(result, -2**31), 2**31-1)