class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s)<k:
            return False
        counts = collections.Counter(s)
        odd_count = 0
        for char in counts:
            if (counts[char]%2):
                odd_count+=1
        if odd_count > k:
            return False
        return True