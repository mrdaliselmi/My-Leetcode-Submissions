class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res, cur = set(), {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            res |= cur
        return len(res)