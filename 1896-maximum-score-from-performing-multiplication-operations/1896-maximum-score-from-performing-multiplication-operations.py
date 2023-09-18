class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n = len(multipliers)
        m = len(nums)
        ahead = [0 for i in range(n+1)]
        cur = [0 for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            for i in range(ind,-1,-1):
                l = (nums[i]*multipliers[ind])+ahead[i+1]
                r = (nums[m-1-(ind-i)]*multipliers[ind])+ahead[i]
                cur[i] = max(l,r)
            ahead = cur[:]
        return ahead[0]