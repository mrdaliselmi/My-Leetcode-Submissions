class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write_index = 0
        for value in nums:
            if value != 0:
                nums[write_index] = value
                write_index += 1

        nums[write_index:] = [0] * (len(nums) - write_index)
        return nums