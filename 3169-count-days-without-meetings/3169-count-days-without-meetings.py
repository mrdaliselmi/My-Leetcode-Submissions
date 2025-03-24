class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort(key=lambda x:x[0])
        merged = [meetings[0]]
        for i in range(1,len(meetings)):
            if meetings[i][0]<=merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], meetings[i][1])
            else:
                merged.append(meetings[i])
        count=0
        for interval in merged:
            count+=interval[1]-interval[0]+1
        return days-count
        