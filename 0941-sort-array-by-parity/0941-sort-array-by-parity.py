class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = [i for i in nums if i%2]
        even = [i for i in nums if not(i%2)]
        return even + odd