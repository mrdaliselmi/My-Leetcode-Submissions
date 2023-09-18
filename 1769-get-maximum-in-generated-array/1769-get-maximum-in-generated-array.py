class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[0]*(n+1)
        if n==0:
            return 0
        else:
            nums[1]=1
            for i in range(2,n+1):
                if i&1:
                    nums[i]=nums[i//2]+nums[(i//2)+1]
                else:
                    nums[i]=nums[i//2]
            return max(nums)