# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(root, curr, total):
            if not root:
                return

            curr.append(root.val)
            total+=root.val
            if not root.left and not root.right and total==targetSum:
                res.append(curr)
                return
            dfs(root.left, curr[:], total)
            dfs(root.right, curr[:], total)
        
        dfs(root, [], 0)
        return res