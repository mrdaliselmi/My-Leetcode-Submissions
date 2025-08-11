class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort(reverse=True)
        res = nums[0]
        for i in range(1,len(nums)):
            if res+nums[i]>res:
                res+=nums[i]
            else:
                break
        return res