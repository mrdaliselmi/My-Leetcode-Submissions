class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        n1 = len(str1)
        n2 = len(str2)
        i = 0
        j = 0
        while i < n1 and j < n2:
            if (ord(str2[j]) - ord(str1[i]) + 26) % 26 <= 1:
                j += 1
            i += 1
        return j == n2