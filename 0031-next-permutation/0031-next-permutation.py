class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot < 0:
            nums.reverse()
            return

        successor = len(nums) - 1
        while nums[successor] <= nums[pivot]:
            successor -= 1

        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        nums[pivot + 1:] = reversed(nums[pivot + 1:])