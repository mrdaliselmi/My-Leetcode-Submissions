from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        window = {c:0 for c in need}
        have = 0
        l, r = 0, 0
        res = ""
        length = float('inf')
        while l <= r and r<len(s):
            if s[r] in need:
                window[s[r]] += 1
                if window[s[r]] <= need[s[r]]:
                    have += 1
                if window[s[r]] == need[s[r]]:
                    if have == len(t):
                        current = r - l + 1
                        if current < length:
                            res = s[l:r+1]
                            length = current
                        while have == len(t):
                            current = r - l + 1
                            
                            if current < length:
                                res = s[l:r + 1]
                                length = current
                                
                            if s[l] in need:
                                window[s[l]] -= 1
                                if window[s[l]] < need[s[l]]:
                                    have -= 1
                                    
                            l += 1
            r+=1
        return res