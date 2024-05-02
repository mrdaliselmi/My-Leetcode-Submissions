class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        ans = -1
        for num in nums_set:
            if num >= 0 and -num in nums_set:
                ans = max(ans, num)
        return ans