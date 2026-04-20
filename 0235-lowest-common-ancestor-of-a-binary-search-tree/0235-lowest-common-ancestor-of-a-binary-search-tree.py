# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def traverse(root, p, q):
            if (p.val<=root.val<=q.val) or (q.val<=root.val<=p.val):
                return root
            elif (root.val > q.val) and (root.val > p.val):
                return traverse(root.left, p, q)
            elif (root.val < q.val) and (root.val < p.val):
                return traverse(root.right, p, q)
        return traverse(root, p, q)