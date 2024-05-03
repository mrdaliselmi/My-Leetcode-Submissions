class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= end:
                end = i
        
        return True if end == 0 else False