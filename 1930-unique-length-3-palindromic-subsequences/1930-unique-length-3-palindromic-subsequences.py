class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = collections.Counter(s)
        left = set()
        ans = set()
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            for j in range(26):
                char = chr(ord('a')+j)
                if (char in left) and (char in right):
                    ans.add((s[i], char))
            left.add(s[i])
        return len(ans)