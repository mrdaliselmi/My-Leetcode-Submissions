from collections import deque 
class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        queue = deque(['c','b','a'])
        result = []
        while(len(queue)):
            curr = queue.pop()
            if len(curr)==n:
                result.append(curr)
                continue
            one = curr
            two = curr
            if curr[-1]=='a':
                one+='b'
                two+='c'
            elif curr[-1]=='b':
                one+='a'
                two+='c'
            elif curr[-1]=='c':
                one+='a'
                two+='b'
            queue.appendleft(one)
            queue.appendleft(two)
        if len(result)<k:
            return ""
        return result[k-1]