from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            if a[0]==b[0]:
                c = a+b
                d = b+a
                return int(c)-int(d)
            else:
                if a > b:
                    return 1
                else:
                    return -1
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        res = ''.join(nums).lstrip('0')
        if res == '':
            res = '0'
        return res