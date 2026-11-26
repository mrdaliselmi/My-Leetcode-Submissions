class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = 0
        ones = 0
        lookup = dict()
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones+=1
            else:
                zeros+=1
            diff = ones-zeros
            if diff == 0:
                res = max(res, i+1)
            else:
                if diff not in lookup:
                    lookup[diff] = i
                else:
                    res = max(res, i-lookup[diff])
        return res