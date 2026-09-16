class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        nonZeroProduct = 1
        zeroCount = 0
        for num in nums:
            if num !=0:
                product *= num
                nonZeroProduct *= num
            else:
                product =0
                zeroCount += 1
        res = []
        for num in nums:
                if num !=0:
                    res.append(product//num)
                elif zeroCount>1:
                    res.append(0)
                else:
                    res.append(nonZeroProduct)
        return res 