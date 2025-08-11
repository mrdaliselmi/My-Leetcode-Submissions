class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        for i in range(1, len(nums)):
            res = max(res,abs(nums[i]-nums[i-1]))
        res = max(res, abs(nums[0]-nums[-1]))
        return res