class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[self.keys.index(key)]=value
        return self

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        return self.values[self.keys.index(key)]

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.keys:
            return -1
        i = self.keys.index(key)
        self.keys.pop(i)
        self.values.pop(i)
        return self


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)