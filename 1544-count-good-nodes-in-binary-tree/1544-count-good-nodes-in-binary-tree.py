# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def countgood(root,mx):
            if (root==None):
                return 0
            else:
                if root.val>=mx:
                    mx=root.val
                    return 1+countgood(root.left,mx)+countgood(root.right,mx)
                else:
                    return countgood(root.left,mx)+countgood(root.right,mx)
        result=0
        if root:
            result=countgood(root,root.val)
        return result

        