class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        sorted_list = sorted(citations)

        for i,h in enumerate(sorted_list):
            if n - i <= h:
                return n - i
        return 0