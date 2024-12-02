class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(" ")
        for i in range(len(words)):
            if len(words[i])>=len(searchWord):
                j = 0
                for char in searchWord:
                    if char == words[i][j]:
                        j+=1
                    else:
                        break
                if j == len(searchWord):
                    return i+1
        return -1
        
            