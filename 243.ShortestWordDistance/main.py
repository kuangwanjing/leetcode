class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """  
        """
        # solution 1: tracking the positions of all words and calculate the shortest distance
        pos = {}
        for i, word in enumerate(words):
            if not word in pos: pos[word] = []
            pos[word].append(i)
        rst = len(words)
        for p1 in pos[word1]:
            for p2 in pos[word2]:
                rst = min(abs(p1-p2), rst)
        return rst
        """
        # solution 2: image that the position of word1 is fixed, then the farther element in 
        # the array has farther distance from word1. Therefore, by traversing the array and 
        # tracking the most recent position of the two words, the result is constantly replaced 
        # by the shorter distance.
        i1 = -1
        i2 = -1
        rst = len(words)
        for i, word in enumerate(words):
            if word == word1: i1 = i
            elif word == word2: i2 = i
            if i1 >= 0 and i2 >= 0: rst = min(rst, abs(i1-i2))
        return rst
