class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        s=sum(nums)-x
        l=len(nums)
        if s<0:
            return -1
        elif s==0:
            return l
        current, left, right, m = 0,0,0,float("inf")
        while right<l:
            current+= nums[right]
            right+=1
            while current>s and left<l:
                current -= nums[left]
                left+=1
            if current==s:
                m= min(m,l-(right-left))
        if m!=float("inf"):
            return m
        return -1