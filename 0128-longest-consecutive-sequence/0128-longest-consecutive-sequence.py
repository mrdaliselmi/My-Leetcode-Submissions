class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        for i in s:
            if not(i-1 in s):
                curr = i
                count = 1
                while curr+1 in s:
                    count+=1
                    curr+=1
                res=max(res,count)
        return res