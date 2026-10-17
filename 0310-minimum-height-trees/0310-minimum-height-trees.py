class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n < 3:
            return list(range(n))

        neighbors = [set() for _ in range(n)]
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        leaves = [i for i in range(n) if len(neighbors[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves