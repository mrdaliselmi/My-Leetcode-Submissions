class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return len(nums)
        index = 0
        for i in nums:
            if index < 2 or i != nums[index - 2]:
                nums[index] = i
                index += 1
        return index