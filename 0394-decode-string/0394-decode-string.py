class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ']':
                    stack.append(s[i])
            else:
                ans = ""
                while stack[-1] != '[':
                    ans = stack.pop() + ans
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                     k = stack.pop() + k
                k = int(k)
                stack.append(k * ans)
            i+=1
        return "".join(stack)