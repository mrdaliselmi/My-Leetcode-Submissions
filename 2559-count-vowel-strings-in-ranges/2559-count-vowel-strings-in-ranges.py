class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counts = [0]*len(words)
        counts[0] = 1 if (words[0][0] in vowels) and (words[0][-1] in vowels) else 0
        res = []
        for i in range(1, len(words)):
            if (words[i][0] in vowels) and (words[i][-1] in vowels):
                counts[i] = counts[i-1] + 1
            else:
                counts[i] = counts[i-1]

        for query in queries:
            l, r = query
            if l == 0:
                res.append(counts[r])
            else:
                res.append(counts[r] - counts[l-1])
        return res