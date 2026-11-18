class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lookup = [(sorted(s), i) for i, s in enumerate(strs)]
        lookup = sorted(lookup, key=lambda x: x[0])
        res = []
        curr = []
        prev = -1
        for s, i in lookup:
            if not len(curr):
                curr.append(strs[i])
                prev = s
            else:
                if s == prev:
                    curr.append(strs[i])
                else:
                    res.append(curr)
                    curr = [strs[i]]
                    prev = s
        if len(curr):
            res.append(curr)
        return res