class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_index = 0
        for i in range(1, len(nums)):
            if nums[i]<=nums[min_index]:
                min_index = i
        i=1
        while i<len(nums):
            if nums[(min_index+i)%len(nums)]<nums[(min_index+i-1)%len(nums)]:
                return False
            i+=1
        return True