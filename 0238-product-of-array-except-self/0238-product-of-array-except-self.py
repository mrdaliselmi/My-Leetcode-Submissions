class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1]
        suffix = [1]
        for i in range(len(nums)-1):
            prefix.append(nums[i]*prefix[i])
            suffix.append(nums[len(nums)-1-i]*suffix[i])
        suffix = suffix[::-1]
        return [prefix[i]*suffix[i] for i in range(len(nums))]