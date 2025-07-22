class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum, max_sum = 0, 0
        current_set = set()
        i, j = 0, 0

        while i < len(nums) and j < len(nums):
            if nums[j] not in current_set:
                current_set.add(nums[j])
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
                j+=1
            else:
                current_set.remove(nums[i])
                current_sum -= nums[i]
                i+=1
        return max_sum