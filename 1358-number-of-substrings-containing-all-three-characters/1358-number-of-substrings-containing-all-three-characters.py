from collections import Counter
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        start = 0

        for end in range(len(s)):
            count[s[end]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - end
                count[s[start]] -= 1
                start += 1

        return res
