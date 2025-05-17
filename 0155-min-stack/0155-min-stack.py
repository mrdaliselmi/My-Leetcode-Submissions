class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        min_val = self.getMin()
        if min_val == None or val < min_val:
            min_val = val
        return self.stack.append((val,min_val))
    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if len(self.stack) else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1] if len(self.stack) else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()