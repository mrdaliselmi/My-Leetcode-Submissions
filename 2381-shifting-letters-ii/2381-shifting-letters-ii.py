class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        newShifts = [0] * len(s)
        for shift in shifts:
            for i in range(shift[0], shift[1]+1):
                newShifts[i] += 1 if shift[2]==1 else -1
        ans = ""
        for i, shift in enumerate(newShifts):
            char = chr((((ord(s[i]) + shift) - ord('a')) % 26) + ord('a'))
            ans+=char
        return ans