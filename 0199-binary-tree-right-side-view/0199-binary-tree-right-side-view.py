# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while len(queue):
            neigh=[]
            rightmost=None
            for node in queue:
                if node.left:
                    neigh.append(node.left)
                if node.right:
                    neigh.append(node.right)
                rightmost=node.val
            res.append(rightmost)
            queue=neigh
        return res

            
