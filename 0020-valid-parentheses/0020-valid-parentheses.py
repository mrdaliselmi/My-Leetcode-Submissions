class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        brackets={'[':']','(':')','{':'}'}
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack):
                    if brackets[stack[-1]]==c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack):
            return False
        else:
            return True