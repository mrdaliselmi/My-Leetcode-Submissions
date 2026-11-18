class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cmin, cmax = 1, 1
        for i in range(len(nums)):
            temp = nums[i]*cmax
            cmax = max(nums[i] * cmin, nums[i]*cmax, nums[i])
            cmin = min(nums[i] * cmin, temp, nums[i])
            res = max(res,cmax)
        return res