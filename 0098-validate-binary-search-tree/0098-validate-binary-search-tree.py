# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(root, minValue, maxValue):
            if not root:
                return True
            if not (minValue < root.val < maxValue):
                return False
            return validate(root.left, minValue, root.val) and validate(root.right, root.val, maxValue)

        return validate(root, -float('inf'), float("inf"))