# inspiring solution:https://leetcode.com/problems/shortest-word-distance-iii/discuss/67095/Short-Java-solution-10-lines-O(n)-modified-from-Shortest-Word-Distance-I
class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = -1
        i2 = -1
        rst = len(words)
        for i, word in enumerate(words):
            if word1 == word2 and word == word1:
                if i1 < 0: i1 = i
                elif i2 < 0: i2 = i
                else: i1, i2 = i2, i
            if word1 != word2 and word in [word1, word2]:
                if word == word1: i1 = i
                else: i2 = i
            if i1 >= 0 and i2 >= 0: rst = min(rst, abs(i1-i2))
        return rst

if __name__ == "__main__":
    sol = Solution()
    print sol.shortestWordDistance(["a", "b", "c", "a", "b", "a"], "a", "a")
