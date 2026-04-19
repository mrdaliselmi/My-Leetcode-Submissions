class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m=len(image)
        n=len(image[0])
        visited = set()
        stack = [(sr,sc)]
        initial = image[sr][sc]

        if initial == color:
            return image
        
        while len(stack):
            i,j = stack.pop()
            neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for neighbor in neighbors:
                if ((0<=neighbor[0]<m) and (0<=neighbor[1]<n) and (neighbor not in visited)) and image[neighbor[0]][neighbor[1]]==initial:
                    stack.append(neighbor)
            image[i][j] = color
            visited.add((i,j))
        return image