import math
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i]*nums[j]
                if product in count:
                    count[product]+=1
                else:
                    count[product]=1
        res = 0
        for key,value in count.items():
            if value>1:
                res+= 8*math.comb(value, 2)
        return res