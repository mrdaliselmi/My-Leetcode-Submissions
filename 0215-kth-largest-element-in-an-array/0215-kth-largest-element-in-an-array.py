import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)