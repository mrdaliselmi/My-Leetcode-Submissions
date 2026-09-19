class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs (curr, ignore, nums):
            if len(ignore)==len(nums):
                res.append(curr[:])
                return
            
            for i, num in enumerate(nums):
                if i not in ignore:
                    curr.append(num)
                    ignore.add(i)
                    dfs(curr, ignore, nums)
                    curr.pop()
                    ignore.remove(i)
                
        dfs([], set(), nums)
        return res