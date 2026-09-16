class Trie(object):
    def __init__(self):
        self.dict = {}
        self.root = self.dict

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        for c in word:
            if c not in self.dict:
                self.dict[c] = {}
            self.dict = self.dict[c]
        self.dict[1] = 1
        self.dict = self.root
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for c in word:
            if c in self.dict:
                self.dict = self.dict[c]
            else:
                self.dict = self.root
                return False
        res = 1 in self.dict
        self.dict = self.root
        return res
        
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for c in prefix:
            if c in self.dict:
                self.dict = self.dict[c]
            else:
                self.dict = self.root
                return False
        self.dict = self.root
        return True