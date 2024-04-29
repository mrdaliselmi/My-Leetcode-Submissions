class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for x in nums:
            res ^= x
        return bin(res ^ k).count('1')