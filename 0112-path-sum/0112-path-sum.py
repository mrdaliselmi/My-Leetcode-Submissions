# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def isPathSum(root, currentSum):
            if root==None:
                return False
            if root.right == root.left == None:
                return (currentSum + root.val) == targetSum
            return isPathSum(root.left, currentSum+root.val) or isPathSum(root.right, currentSum+root.val)
        if root== None:
            return False
        return isPathSum(root, 0)