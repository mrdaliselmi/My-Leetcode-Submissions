from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        nums = sorted(set(nums))
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            skip = dp(i + 1)
            take = nums[i] * count[nums[i]]
            if i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                take += dp(i + 2)
            else:
                take += dp(i + 1)

            memo[i] = max(skip, take)
            return memo[i]

        return dp(0)
