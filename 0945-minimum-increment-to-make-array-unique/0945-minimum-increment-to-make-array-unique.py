class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prev=nums[0]
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=prev:
                count+=prev-nums[i]+1
                nums[i]+=prev-nums[i]+1
            prev=nums[i]
        return count