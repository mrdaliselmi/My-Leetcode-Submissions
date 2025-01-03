class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        current = 0
        maximum = (2**maximumBit)-1
        n = len(nums)
        answer = [0]*n
        for i in range(len(nums)):
            current^=nums[i]
            print(current)
            answer[n-i-1] = current ^ maximum
        return answer