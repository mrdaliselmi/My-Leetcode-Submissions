class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx, curr=nums[0], nums[0]
        for i in range(1, len(nums)):
            if curr<0:
                    curr = nums[i]
            else:
                    curr = curr+nums[i]
            mx = max(mx, curr)
        return mx