class TimeMap(object):

    def __init__(self):
        self.map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.map:
            self.map[key] = [[], []]

        timestamps, values = self.map[key]
        timestamps.append(timestamp)
        values.append(value)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.map:
            return ""

        timestamps, values = self.map[key]
        left = 0
        right = len(timestamps) - 1
        best_index = -1

        while left <= right:
            middle = (left + right) // 2

            if timestamps[middle] <= timestamp:
                best_index = middle
                left = middle + 1
            else:
                right = middle - 1

        if best_index == -1:
            return ""

        return values[best_index]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)