class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        charset=set(ransomNote)
        #map of every letter in the note and number of occurences
        ransom={a:ransomNote.count(a) for a in charset}
        charset=set(magazine)
        #map of every letter in the magazine and number of occurences
        mag={a:magazine.count(a) for a in charset}
        for a,i in ransom.items():
            if (a in mag):
                if not(mag[a]>=i):
                    return False
            else:
                return False
        return True