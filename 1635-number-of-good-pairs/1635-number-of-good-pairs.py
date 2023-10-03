from itertools import combinations
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = 0
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                (dic[nums[i]]).append(i)
            else:
                dic[nums[i]]=[i]
        for _,value in dic.items():
            pairs+=len(list(combinations(value,2)))
        return pairs