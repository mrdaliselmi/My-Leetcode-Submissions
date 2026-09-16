class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None
        self.minStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if self.min == None:
            self.minStack.append(value)
            self.min = value
        else:
            self.minStack.append(min(value, self.min))
            self.min = min(self.min, value)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
        self.min = self.minStack[-1] if len(self.minStack) else None
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()