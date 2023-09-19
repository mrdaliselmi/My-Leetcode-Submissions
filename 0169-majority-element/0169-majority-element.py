class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # if there's a majority element it would be in 
        # the middle of the sorted array
        return(nums[len(nums)//2])