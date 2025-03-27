from collections import Counter
class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        max_count = 0
        dominant = 0
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
            if count[num]>max_count:
                max_count = count[num]
                dominant = num
        
        curr = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==dominant:
                curr+=1
                if ((curr>i+1-curr) and (max_count-curr>(n-i-1)-max_count+curr)):
                    return i
        return -1