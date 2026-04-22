import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        d = dict()
        distances = []
        for point in points:
            x,y = point
            distance = math.sqrt(x**2+y**2)
            if distance in d:
                d[distance].append([x,y])
            else:
                distances.append(distance)
                d[distance]= [[x,y]]
        distances.sort()
        res = []
        while len(res)<k:
            res+= d[distances[len(res)]]
        return res