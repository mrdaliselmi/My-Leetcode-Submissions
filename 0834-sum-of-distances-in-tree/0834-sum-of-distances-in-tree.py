class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
            
        output = [0]*n
        count = [1]*n
        self.root=0
        def dfs(curr, parent, depth):
            result = 1
            for child in graph[curr]:
                if child != parent:
                    result += dfs(child, curr, depth+1)
                    self.root += depth+1
            count[curr]=result
            return result
        dfs(0,-1,0)

        def dfs2(curr, parent, p_res):
            output[curr]=p_res
            for child in graph[curr]:
                if child != parent:
                    dfs2(child, curr,p_res+(n-count[child])-count[child])
        dfs2(0,-1,self.root)
        
        return output
# O(n^2) TLE
#   graph = defaultdict(list)
#         for s, t in edges:
#            graph[s].append(t)
#            graph[t].append(s)
#
#         def traverse(i):
#             visited = set([i])
#             q = deque([(i,0)])
#             output = 0
#             while q:
#                 curr, dis = q.popleft()
#                 for nx in graph[curr]:
#                     if nx not in visited:
#                         visited.add(nx)
#                         q.append((nx,dis+1))
#                         output += dis+1
#             return output
        
#         return [traverse(i) for i in range(n)]