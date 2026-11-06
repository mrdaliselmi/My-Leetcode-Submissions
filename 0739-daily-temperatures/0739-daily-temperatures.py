class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not len(stack):
                stack.append((i, temp))
            else:
                while len(stack) and temp > stack[-1][1]:
                    j, top = stack.pop()
                    res[j] = i-j
                stack.append((i, temp))
        
        return res

