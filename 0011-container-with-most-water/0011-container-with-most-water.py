class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            surface = min(height[left], height[right]) * (right - left)
            res = max(res, surface)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return res