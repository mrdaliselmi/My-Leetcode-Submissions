class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        nums[:] = sorted(list(s))
        return len(nums)