from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque()
        visited = set()
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))
                else:
                    mat[i][j]= float('inf')
        
        while len(queue):
            i,j, distance = queue.popleft()
            if mat[i][j]>distance:
                mat[i][j]=distance
            neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            for x,y in neighbors:
                if x>=0 and x<m and y>=0 and y<n:
                    if (x,y) not in visited:
                        newDistance= min(1+distance, mat[x][y]) if mat[x][y]==float('inf') else 1+distance
                        mat[x][y]=newDistance
                        queue.append((x,y,newDistance))
            visited.add((i,j))
        return mat
                    