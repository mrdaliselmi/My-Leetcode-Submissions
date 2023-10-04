class MyHashMap(object):

    size = ((2**17)-1)
    def __init__(self):
        self.keys = [False]*MyHashMap.size
        self.values = [None]*MyHashMap.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        i = key % MyHashMap.size
        if not(self.keys[i]):
            self.keys[i]=True
        self.values[i]=value
        return self

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        i = key % MyHashMap.size
        if self.keys[i]:
            return self.values[i]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % MyHashMap.size
        self.keys[i]=False
        return self


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)