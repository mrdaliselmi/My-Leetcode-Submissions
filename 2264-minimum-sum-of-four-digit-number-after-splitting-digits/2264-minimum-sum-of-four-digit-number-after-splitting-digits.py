class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = map(int, list(str(num)))
        digits.sort()
        nums=["",""]
        i=0
        while len(digits):
            nums[i]+= str(digits.pop(0))
            i = (i+1)%2
        return int(nums[1])+int(nums[0])