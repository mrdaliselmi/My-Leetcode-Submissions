class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[1])
        res = 0
        last_shot = float('-inf')

        for point in points:
            if last_shot < point[0]:
                res += 1
                last_shot = point[1]
        return res