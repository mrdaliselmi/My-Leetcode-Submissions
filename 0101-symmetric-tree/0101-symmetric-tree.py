# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def testSymetry(left, right):
            if left == right == None:
                return True
            if (left == None) or (right == None):
                return False
            if (left.val == right.val):
                return testSymetry(right.left, left.right) and testSymetry(right.right, left.left)
            return False
        return testSymetry(root.left, root.right)