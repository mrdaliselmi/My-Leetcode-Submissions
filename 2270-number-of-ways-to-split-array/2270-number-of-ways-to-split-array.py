class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        current = 0
        ans = 0
        for i in range(len(nums)-1):
            current+=nums[i]
            if current>=total-current:
                ans+=1
        return ans