class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        monotony = ''
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if monotony == '+':
                    return False
                monotony = '-'
            elif nums[i]<nums[i+1]:
                if monotony == '-':
                    return False
                monotony = '+'
        return True


        