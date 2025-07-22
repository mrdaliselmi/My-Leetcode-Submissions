class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return nums
        prev = nums[0]
        limit = prev
        res=[[nums[0],nums[0]]]
        for i in range(1,len(nums)):
            if nums[i] == res[-1][1]+1:
                res[-1][1] = nums[i]
            else:
                res.append([nums[i],nums[i]])

        for i in range(len(res)):
            if res[i][0] == res[i][1]:
                res[i] = str(res[i][0])
            else:
                res[i] = str(res[i][0])+"->"+str(res[i][1])
        return res