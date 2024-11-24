class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        res = 0
        while right > left:
            res = max(res,(right-left)*min(height[right], height[left]))
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
        return res