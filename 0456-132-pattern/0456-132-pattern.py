class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)>2:
            l = []
            k = float('-inf')
            for num in reversed(nums):
                if num < k:
                    return True
                while l and l[-1] < num:
                    k = l.pop()
                l.append(num)
        return False