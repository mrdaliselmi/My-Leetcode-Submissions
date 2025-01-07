class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for i in range(len(words)):
            for j in range (len(words)):
                if i != j:
                    if words[j].find(words[i]) != -1:
                        ans.append(words[i])

        return ans