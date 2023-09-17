class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        opt = [[None for x in range(len(word1))] for y in range(len(word2))]
        self.minDistanceRec(word1, word2, opt)
        return opt[len(word1)][len(word2)]
    
    def minDistanceRec(self, word1: str, word2: str, opt):
        if opt[len(word1)][len(word2)] is not None:
            return opt[len(word1)][len(word2)]
        if len(word1) == 0:
            opt[len(word1)][len(word2)] = len(word2)
        elif len(word2) == 0:
            opt[len(word1)][len(word2)] = len(word1)
        elif word1[-1] == word2[-1]:
            opt[len(word1)][len(word2)] = self.minDistanceRec(word1[:-1], word2[:-1], opt)
        else:
            minimum = min(self.minDistanceRec(word1, word2[:-1], opt), 
                          self.minDistanceRec(word1[:-1], word2, opt), 
                          self.minDistanceRec(word1[:-1], word2[:-1], opt))
            opt[len(word1)][len(word2)] = 1 + minimum
        return opt[len(word1)][len(word2)]
