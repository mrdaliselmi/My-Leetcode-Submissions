class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        second = nums[0]
        while True:
            first = nums[first]
            second = nums[nums[second]]
            if first == second:
                break
        first = nums[0]
        while first!=second:
            first = nums[first]
            second = nums[second]
        return first
        
        
