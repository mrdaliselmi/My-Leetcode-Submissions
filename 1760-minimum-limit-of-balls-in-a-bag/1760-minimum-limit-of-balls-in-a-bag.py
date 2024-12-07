class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        l, r = 1, max(nums)
        res = r

        while l <= r:
            mid = (l + r) // 2
            op = 0
            
            for n in nums:
                op += (n - 1) // mid
                if op > maxOperations:
                    break
            
            if op > maxOperations:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res