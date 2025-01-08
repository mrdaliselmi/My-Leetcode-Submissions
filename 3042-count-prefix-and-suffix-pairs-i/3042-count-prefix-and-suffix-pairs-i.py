class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(str1, str2):
            return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
        ans = 0
        for i in range(1,len(words)):
            for j in range(i):
                if isPrefixAndSuffix(words[j], words[i]):
                    ans+=1
        return ans