# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.mx=0
        def maxPath(root):
            if not(root):
                return 0
            left = maxPath(root.left)
            right = maxPath(root.right)
            self.mx = max(self.mx, left+right)
            return 1+max(left, right)
        maxPath(root)
        return self.mx