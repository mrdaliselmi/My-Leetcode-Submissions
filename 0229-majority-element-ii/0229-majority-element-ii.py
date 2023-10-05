class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        majority = len(nums)//3
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        result = []
        for key, value in d.items():
            if value>majority:
                result.append(key)
        return result