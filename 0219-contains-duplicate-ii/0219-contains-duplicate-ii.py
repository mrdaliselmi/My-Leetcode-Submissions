class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for index, value in enumerate(nums):
            if value in d:
                if abs(d[value]-index) <=k:
                    return True
            d[value]=index
        return False