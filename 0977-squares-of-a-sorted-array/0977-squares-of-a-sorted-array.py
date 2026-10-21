class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums[0] >= 0:
            return [num**2 for num in nums]
        if nums[-1] < 0:
            return [num**2 for num in nums][::-1]
        first_positive = 0
        for i in range(len(nums)):
            if nums[i]>= 0:
                first_positive = i
                break
        
        left, right = first_positive -1, first_positive
        res = []
        while left>=0 and right<len(nums):
            if abs(nums[left])<abs(nums[right]):
                res.append(nums[left]**2)
                left-=1
            else:
                res.append(nums[right]**2)
                right+=1
        if left >= 0:
            while left>=0:
                res.append(nums[left]**2)
                left-=1
        if right<len(nums):
            while right<len(nums):
                res.append(nums[right]**2)
                right+=1
        return res