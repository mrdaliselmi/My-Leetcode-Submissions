class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        current = 0
        maximum = (1 << maximumBit) - 1
        n = len(nums)
        answer = []
        for num in nums:
            current ^= num
            answer.append(current ^ maximum)
        return answer[::-1]