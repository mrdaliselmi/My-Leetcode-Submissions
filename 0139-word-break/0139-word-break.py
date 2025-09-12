class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        maxi = max(map(len, wordDict)) if wordDict else 0

        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for l in range(1, min(i, maxi) + 1):
                if not dp[i - l]:
                    continue
                if s[i - l:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]