# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSame(root, sub):
            if root is None and sub is None:
                return True
            if root is None or sub is None:
                return False
            if root.val == sub.val:
                return isSame(root.left, sub.left) and isSame(root.right, sub.right)
            else:
                return False

        def checkSubtrees(root):
            if not root:
                return False
            return (
                isSame(root, subRoot)
                or checkSubtrees(root.left)
                or checkSubtrees(root.right)
            )
        return checkSubtrees(root)