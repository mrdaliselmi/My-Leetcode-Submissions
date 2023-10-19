class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        s_stack = []
        for i in s:
            if i =='#':
                if len(s_stack):
                    s_stack.pop()
            else:
                s_stack.append(i)
        s = ''.join(s_stack)
        n = len(t)
        t_stack = []
        for i in t:
            if i =='#':
                if len(t_stack):
                    t_stack.pop()
            else:
                t_stack.append(i)
        t = ''.join(t_stack)
        return s==t