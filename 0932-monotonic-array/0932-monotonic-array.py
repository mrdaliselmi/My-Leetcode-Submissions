class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        monotony = ''
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if monotony == '+':
                    return False
                monotony = '-'
            elif nums[i]<nums[i+1]:
                if monotony == '-':
                    return False
                monotony = '+'
        return True


        