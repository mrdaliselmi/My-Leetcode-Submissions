class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = {}

        def dfs(target, index):
            if target == 0:
                return True
            if (target, index) in dp:
                return dp[(target, index)]
            if index >=len(nums):
                return False
            if target < 0:
                return False
            dp[(target, index)] = dfs(target, index+1) or dfs(target-nums[index], index+1)
            return dp[(target, index)]

        dfs(target, 0)
        return dp[(target, 0)]
            
            