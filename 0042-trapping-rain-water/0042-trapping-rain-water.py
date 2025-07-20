class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        results = [max(0, min(max_left[i], max_right[i])-height[i]) for i in range(len(height))]

        return sum(results)
