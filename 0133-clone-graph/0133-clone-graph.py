"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.lookup = {}

        def clone(node):
            if node in self.lookup:
                return self.lookup[node]
            if node:
                new = Node(node.val)
                self.lookup[node]=new
                for neighbor in node.neighbors:
                    if not(len(new.neighbors)):
                        new.neighbors = []
                    new.neighbors.append(clone(neighbor))
                return new
        
        return clone(node)
