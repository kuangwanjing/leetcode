class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pos = {}
        for i, word in enumerate(words):
            if not word in self.pos: self.pos[word] = []
            self.pos[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(abs(i1-i2) for i1 in self.pos[word1] for i2 in self.pos[word2])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
