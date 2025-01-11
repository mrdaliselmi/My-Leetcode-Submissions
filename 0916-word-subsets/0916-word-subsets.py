class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        counts = collections.Counter()
        for word in words2:
            count = collections.Counter(word)
            for char in count:
                counts[char] = max(count[char], counts[char])
        ans = []
        for word in words1:
            occ = collections.Counter(word)
            isUniversal = True
            for char in counts:
                if not(char in occ):
                    isUniversal = False
                    break
                elif occ[char]<counts[char]:
                    isUniversal = False
                    break
            if isUniversal:
                ans.append(word)
        return ans