class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        left= 0
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                res = min(res, right-left+1)
                curr -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        return int(res)