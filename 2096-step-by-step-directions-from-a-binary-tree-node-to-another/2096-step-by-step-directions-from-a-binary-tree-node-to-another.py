# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.parent = {}
        self.height = {}
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        firstPath = []
        secondPath = []
        
        lca = self.findLCA(root, startValue, destValue)
        self.construct(lca, firstPath, startValue)
        self.construct(lca, secondPath, destValue)
        
        firstPath.reverse()
        secondPath.reverse()

        return 'U' * len(firstPath) + ''.join(secondPath)
        
    def dfs(self, p, root, h):
        if not root:
            return
        self.dfs(root, root.left, h + 1)
        self.dfs(root, root.right, h + 1)
        self.parent[root.val] = p
        self.height[root.val] = h
    
    def findLCA(self, root, u, v):
        self.dfs(None, root, 0)
        while u != v:
            if self.parent[u] == self.parent[v]:
                return self.parent[u]
            if self.height[u] > self.height[v]:
                if self.parent[u].val == v:
                    return self.parent[u]
                u = self.parent[u].val
            else:
                if self.parent[v].val == u:
                    return self.parent[v]
                v = self.parent[v].val
        
        return None
    
    def construct(self, root, s, val):
        if not root:
            return False
        if root.val == val:
            return True
        
        left = self.construct(root.left, s, val)
        right = self.construct(root.right, s, val)
        
        if left:
            s.append('L')
        elif right:
            s.append('R')
        
        return left or right