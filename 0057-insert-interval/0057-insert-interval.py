class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not(len(intervals)):
            return [newInterval]
        start = newInterval[0]
        end = newInterval[1]
        result = []
        for i in range(len(intervals)):
            if intervals[i][0] > end:
                result.append([start, end])
                return result + intervals[i:]
            elif intervals[i][1] < start:
                result.append(intervals[i])
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
        result.append([start, end])
        return result