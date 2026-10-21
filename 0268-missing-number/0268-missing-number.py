class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ideal = ((n+1)*n)//2
        total = sum(nums)
        return ideal - total