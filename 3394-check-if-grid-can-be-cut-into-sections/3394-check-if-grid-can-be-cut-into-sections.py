class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def check_ranges(ranges):
            ranges.sort(key=lambda x:(x[0],x[1]))
            sections = 0
            max_end = ranges[0][1]
            
            for start, end in ranges:
                if max_end <= start:
                    sections += 1
                max_end = max(max_end, end)
                
            return sections >= 2
        
        x_ranges = [[rectangle[0], rectangle[2]] for rectangle in rectangles]
        y_ranges = [[rectangle[1], rectangle[3]] for rectangle in rectangles]
        
        return check_ranges(x_ranges) or check_ranges(y_ranges)