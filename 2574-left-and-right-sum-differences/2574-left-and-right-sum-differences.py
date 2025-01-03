class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        current = 0
        ans = []
        for i in range(len(nums)):
            leftSum = current
            current += nums[i]
            rightSum = total - current
            ans.append(abs(leftSum - rightSum))
        return ans