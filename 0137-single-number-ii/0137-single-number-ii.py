class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                sum += (num >> i) & 1
            sum %= 3
            ans |= sum << i

        return ans - 2**32 if ans >= 2**31 else ans