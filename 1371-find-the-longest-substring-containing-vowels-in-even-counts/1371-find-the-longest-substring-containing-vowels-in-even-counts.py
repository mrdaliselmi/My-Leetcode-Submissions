class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapy= [-2]*32
        mapy[0]=-1
        mask=0
        max_count=0
        for i in range(len(s)):
            if s[i] == 'a':
                mask ^=1
            if s[i] == 'e':
                mask ^=2
            if s[i] == 'i':
                mask ^=4
            if s[i] == 'o':
                mask ^=8
            if s[i] == 'u':
                mask ^=16
            
            prev=mapy[mask]
            if mapy[mask]==-2:
                mapy[mask]=i
            else:
                max_count= max(max_count, i-prev)
        return max_count