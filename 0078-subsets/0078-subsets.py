class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(start, current):
            res.append(current[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])
                dfs(i + 1, current)
                current.pop()

        dfs(0, [])
        return res


        