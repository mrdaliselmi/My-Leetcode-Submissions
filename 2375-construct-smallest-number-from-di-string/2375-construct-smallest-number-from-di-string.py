class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        arr = [i for i in range(1, len(pattern) + 2)]
        i = 0
        while i < len(pattern):
            if pattern[i] == 'I':
                i += 1
            else:
                start = i
                while i < len(pattern) and pattern[i] == 'D':
                    i += 1
                arr[start:i+1] = arr[start:i+1][::-1]
        return ''.join(map(str, arr))
