class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0
        curr = 0
        for i in nums:
            if i==1:
                curr+=1
            else:
                curr=0
            mx = max(curr,mx)
        return mx