class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        longest = 0
        area = 0
        for dimension in dimensions:
            diagonal = math.sqrt(dimension[0]**2+dimension[1]**2)
            if diagonal>longest:
                longest = diagonal
                area = dimension[0]*dimension[1]
            elif diagonal == longest:
                area = max(area, dimension[0]*dimension[1])
        return area